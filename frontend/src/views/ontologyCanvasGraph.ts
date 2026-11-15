import { MarkerType, Position } from "@xyflow/vue";
import type { Edge, Node } from "@xyflow/vue";
import type { OntologyCanvasResponse } from "../types";

export type OntologyCanvasNode = Node<Record<string, unknown>, string>;
export type OntologyCanvasEdge = Edge<Record<string, unknown>, string>;

export interface CanvasLayout {
  nodes: Record<string, { x: number; y: number }>;
  viewport?: { x: number; y: number; zoom: number };
}

function defaultPositions(canvas: OntologyCanvasResponse): Record<string, { x: number; y: number }> {
  const objectNodes = canvas.nodes.filter((node) => node.type === "objectType");
  const objectIds = new Set(objectNodes.map((node) => node.id));
  const depth = new Map<string, number>();
  const incomingCount = new Map<string, number>();
  for (const node of objectNodes) incomingCount.set(node.id, 0);
  for (const edge of canvas.edges.filter((item) => item.type === "ontologyLink")) {
    if (objectIds.has(edge.source) && objectIds.has(edge.target)) incomingCount.set(edge.target, (incomingCount.get(edge.target) ?? 0) + 1);
  }
  const queue = objectNodes.filter((node) => incomingCount.get(node.id) === 0).map((node) => node.id);
  for (const id of queue) depth.set(id, 0);
  for (let cursor = 0; cursor < queue.length; cursor += 1) {
    const source = queue[cursor];
    for (const edge of canvas.edges.filter((item) => item.type === "ontologyLink" && item.source === source)) {
      if (!depth.has(edge.target)) {
        depth.set(edge.target, (depth.get(source) ?? 0) + 1);
        queue.push(edge.target);
      }
    }
  }
  for (const node of objectNodes) if (!depth.has(node.id)) depth.set(node.id, 0);

  const positions: Record<string, { x: number; y: number }> = {};
  const rankRows = new Map<number, number>();
  for (const node of objectNodes) {
    const rank = depth.get(node.id) ?? 0;
    const row = rankRows.get(rank) ?? 0;
    positions[node.id] = { x: 80 + rank * 350, y: 86 + row * 250 };
    rankRows.set(rank, row + 1);
  }
  const nodeById = new Map(objectNodes.map((node) => [node.id, node]));
  const sourceRows = new Map<string, number>();
  const actionRows = new Map<string, number>();
  for (const node of canvas.nodes) {
    if (node.type === "sourceSystem") {
      const mapping = canvas.edges.find((edge) => edge.type === "sourceMapping" && edge.source === node.id);
      const target = mapping ? positions[mapping.target] : undefined;
      const row = target ? (sourceRows.get(mapping!.target) ?? 0) : 0;
      if (mapping && target) sourceRows.set(mapping.target, row + 1);
      positions[node.id] = { x: Math.max(30, (target?.x ?? 80) - 285), y: (target?.y ?? 86) + row * 135 + 22 };
    } else if (node.type === "action") {
      const related = canvas.edges.find((edge) => edge.type === "actionAssociation" && edge.target === node.id);
      const target = related ? positions[related.source] : undefined;
      const row = target ? (actionRows.get(related!.source) ?? 0) : 0;
      if (related && target) actionRows.set(related.source, row + 1);
      positions[node.id] = { x: (target?.x ?? 80) + 290, y: (target?.y ?? 86) + row * 135 + 35 };
    }
  }
  for (const id of Object.keys(positions)) {
    if (!nodeById.has(id) && !canvas.nodes.some((node) => node.id === id)) delete positions[id];
  }
  return positions;
}

export function mapCanvasToFlow(
  canvas: OntologyCanvasResponse,
  layout?: CanvasLayout,
  highlightedLinkApis: string[] = [],
): { nodes: OntologyCanvasNode[]; edges: OntologyCanvasEdge[] } {
  const positions = { ...defaultPositions(canvas), ...(layout?.nodes ?? {}) };
  const highlighted = new Set(highlightedLinkApis);
  const nodes = canvas.nodes.map((resource) => ({
    id: resource.id,
    type: resource.type,
    position: positions[resource.id] ?? { x: 80, y: 86 },
    sourcePosition: Position.Right,
    targetPosition: Position.Left,
    data: resource.data,
  }));
  const edges = canvas.edges.map((resource) => {
    const isLink = resource.type === "ontologyLink";
    const isHighlighted = isLink && highlighted.has(String(resource.data.api_name));
    const cardinality = `${resource.data.source_cardinality ?? "many"} → ${resource.data.target_cardinality ?? "many"}`;
    return {
      id: resource.id,
      source: resource.source,
      target: resource.target,
      type: "smoothstep",
      label: isLink ? `${resource.data.display_name} · ${cardinality}` : resource.type === "sourceMapping" ? `字段映射 · ${resource.data.mapped_property_count ?? 0}` : "可触发",
      markerEnd: isLink ? MarkerType.ArrowClosed : undefined,
      animated: Boolean(isHighlighted),
      class: `ontology-canvas-edge ontology-canvas-edge--${resource.type}${isHighlighted ? " is-highlighted" : ""}`,
      style: {
        stroke: isHighlighted ? "#8A6BC1" : resource.type === "sourceMapping" ? "#5D86A8" : resource.type === "actionAssociation" ? "#C3894C" : "#78918A",
        strokeWidth: isHighlighted ? 2.5 : 1.6,
        strokeDasharray: resource.type === "ontologyLink" ? undefined : "5 4",
      },
      labelStyle: { fill: isHighlighted ? "#684F98" : "#657772", fontSize: 11, fontWeight: 600 },
      data: { ...resource.data, canvas_type: resource.type, highlighted: isHighlighted },
    };
  });
  return { nodes, edges };
}

export function canvasLayoutKey(projectId: string, ontologyId: string, branchId: string): string {
  return `ontology-canvas:${projectId}:${ontologyId}:${branchId || "main"}`;
}
