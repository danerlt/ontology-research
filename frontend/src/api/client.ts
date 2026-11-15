export class ApiError extends Error {
  constructor(
    message: string,
    public readonly status: number,
  ) {
    super(message);
    this.name = "ApiError";
  }
}

export function readableError(error: unknown): string {
  if (typeof error === "object" && error !== null && "detail" in error) {
    const detail = (error as { detail?: unknown }).detail;
    if (typeof detail === "string" && detail.trim()) return detail;
    if (typeof detail === "object" && detail !== null && "message" in detail) {
      const message = (detail as { message?: unknown }).message;
      if (typeof message === "string" && message.trim()) return message;
    }
  }
  if (error instanceof ApiError && error.message) return error.message;
  return "服务暂不可用，请检查网络后重试";
}

export class ApiClient {
  private tokenProvider: () => string | null = () => null;
  private projectProvider: () => string | null = () => null;
  private unauthorizedHandler: () => void = () => undefined;

  configure(options: {
    tokenProvider: () => string | null;
    projectProvider?: () => string | null;
    onUnauthorized: () => void;
  }): void {
    this.tokenProvider = options.tokenProvider;
    this.projectProvider = options.projectProvider ?? (() => null);
    this.unauthorizedHandler = options.onUnauthorized;
  }

  async get<T>(path: string, query?: Record<string, string | number | undefined>, base = ""): Promise<T> {
    const params = new URLSearchParams();
    Object.entries(query ?? {}).forEach(([key, value]) => {
      if (value !== undefined && value !== "") params.set(key, String(value));
    });
    const suffix = params.size ? `?${params.toString()}` : "";
    return this.request<T>(`${base}${path}${suffix}`);
  }

  post<T>(path: string, body?: unknown, base = ""): Promise<T> {
    return this.request<T>(`${base}${path}`, {
      method: "POST",
      body: body === undefined ? undefined : JSON.stringify(body),
    });
  }

  put<T>(path: string, body: unknown, base = ""): Promise<T> {
    return this.request<T>(`${base}${path}`, {
      method: "PUT",
      body: JSON.stringify(body),
    });
  }

  private async request<T>(path: string, init: RequestInit = {}): Promise<T> {
    const headers = new Headers(init.headers);
    headers.set("Accept", "application/json");
    if (init.body !== undefined) headers.set("Content-Type", "application/json");
    const token = this.tokenProvider();
    const projectId = this.projectProvider();
    if (token) headers.set("Authorization", `Bearer ${token}`);
    if (projectId) headers.set("X-Project-ID", projectId);
    let response: Response;
    try {
      response = await fetch(path, { ...init, headers });
    } catch {
      throw new ApiError("服务暂不可用，请检查网络后重试", 0);
    }
    if (response.status === 401) this.unauthorizedHandler();
    const payload = response.status === 204 ? undefined : await response.json().catch(() => undefined);
    if (!response.ok) {
      throw new ApiError(readableError(payload), response.status);
    }
    return payload as T;
  }
}

export const api = new ApiClient();
