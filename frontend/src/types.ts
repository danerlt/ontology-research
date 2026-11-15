export interface Ontology {
  id: string;
  api_name: string;
  display_name: string;
  description: string;
  revision: number;
  object_type_count: number;
  link_type_count: number;
}

export interface PropertyDefinition {
  id: string;
  api_name: string;
  display_name: string;
  data_type: string;
  required: boolean;
  editable: boolean;
  unique_value: boolean;
  sensitive?: boolean;
  options: Record<string, unknown>;
}

export interface ObjectType {
  id: string;
  ontology_id: string;
  api_name: string;
  display_name: string;
  plural_display_name: string;
  description: string;
  primary_key_property: string;
  title_key_property: string;
  aliases: string[];
  groups: string[];
  icon: string;
  icon_color: string;
  properties: PropertyDefinition[];
}

export interface LinkType {
  id: string;
  api_name: string;
  display_name: string;
  description: string;
  source_type_id: string;
  target_type_id: string;
  source_cardinality: "one" | "many";
  target_cardinality: "one" | "many";
}

export interface DerivedPathStep {
  link_api_name: string;
  direction: "outgoing" | "incoming";
}

export interface DerivedPropertyDefinition {
  object_type_api_name: string;
  api_name: string;
  display_name: string;
  description: string;
  data_type: string;
  path: DerivedPathStep[];
  terminal_property_api_name: string;
  aggregation: "count" | "sum" | "average" | "minimum" | "maximum" | "collect_list" | "collect_set" | null;
}

export interface OntologyCanvasNodeResource {
  id: string;
  type: "objectType" | "sourceSystem" | "action";
  data: Record<string, any>;
}

export interface OntologyCanvasEdgeResource {
  id: string;
  source: string;
  target: string;
  type: "ontologyLink" | "sourceMapping" | "actionAssociation";
  data: Record<string, any>;
}

export interface OntologyCanvasResponse {
  ontology: Pick<Ontology, "id" | "api_name" | "display_name" | "revision">;
  branch: { id: string; name: string; status: string } | null;
  nodes: OntologyCanvasNodeResource[];
  edges: OntologyCanvasEdgeResource[];
}

export interface DerivedPropertyPreview {
  object_id: string;
  api_name: string;
  value: unknown;
  result_type: string;
  aggregation: string | null;
  matched_count: number;
  path_object_count: number;
  ignored_null_count: number;
  trace: Array<Record<string, unknown>>;
  warnings: string[];
}

export interface ObjectRecord {
  id: string;
  object_type_api_name: string;
  object_type_display_name: string;
  primary_key_value: string;
  properties: Record<string, unknown>;
  version: number;
  created_at: string;
  updated_at: string;
  links: Array<Record<string, unknown>>;
}

export interface ActionDefinition {
  id: string;
  api_name: string;
  display_name: string;
  description: string;
  object_type_api_name: string;
  allowed_properties: string[];
  parameters_schema: Record<string, {
    required?: boolean;
    type?: string;
    enum?: unknown[];
    minimum?: number;
    maximum?: number;
    min_length?: number;
    max_length?: number;
    pattern?: string;
  }>;
  submission_criteria?: Record<string, unknown>;
  enabled: boolean;
}

export interface ActionPreview {
  action_api_name: string;
  object_id: string;
  current_version: number;
  next_version: number;
  property_changes: Array<{
    property: string;
    before: unknown;
    after: unknown;
    sensitive: boolean;
  }>;
}

export interface Proposal {
  id: string;
  ontology_id: string;
  title: string;
  description: string;
  branch_id?: string | null;
  base_revision: number;
  changes: Array<Record<string, unknown>>;
  status: string;
  resource_reviews?: Array<{
    id: string;
    resource_key: string;
    status: string;
    reviewer_id: string | null;
    comment: string;
  }>;
  created_at: string;
}

export interface OntologyBranch {
  id: string;
  ontology_id: string;
  author_id: string;
  name: string;
  description: string;
  base_revision: number;
  snapshot: {
    revision?: number;
    object_types: Array<{
      api_name: string;
      display_name: string;
      plural_display_name?: string;
      description?: string;
      primary_key_property: string;
      title_key_property?: string;
      aliases?: string[];
      groups?: string[];
      icon?: string;
      icon_color?: string;
      properties: Array<{
        api_name: string;
        display_name: string;
        data_type: string;
        required: boolean;
        editable: boolean;
        unique_value: boolean;
        sensitive: boolean;
        options?: Record<string, unknown>;
      }>;
    }>;
    link_types: Array<{
      api_name: string;
      display_name: string;
      description?: string;
      source_type_api_name: string;
      target_type_api_name: string;
      source_cardinality?: "one" | "many";
      target_cardinality?: "one" | "many";
    }>;
    actions?: Array<{
      api_name: string;
      display_name: string;
      description?: string;
      object_type_api_name: string;
      allowed_properties: string[];
      parameters_schema: Record<string, Record<string, unknown>>;
      submission_criteria: Record<string, unknown>;
      enabled: boolean;
    }>;
  };
  changes: Array<Record<string, unknown>>;
  validation: {
    errors: Array<{ path: string; message: string }>;
    warnings: Array<{ path: string; message: string }>;
    valid: boolean;
  };
  status: "active" | "proposed" | "merged" | "closed";
  created_at: string;
  updated_at: string;
}

export interface AgentDefinition {
  id: string;
  api_name: string;
  display_name: string;
  description: string;
  allowed_tools: string[];
  allowed_actions: string[];
  enabled: boolean;
  draft_config: AgentConfiguration;
  latest_version_number: number | null;
}

export interface AgentInputDefinition {
  name: string;
  display_name: string;
  type: "string" | "number" | "integer" | "boolean";
  required: boolean;
  sensitive: boolean;
}

export interface AgentVariableDefinition {
  name: string;
  expression: string;
}

export interface AgentConfiguration {
  model_provider: string;
  model_name: string;
  system_prompt: string;
  initial_user_message: string;
  inputs: AgentInputDefinition[];
  precomputed_variables: AgentVariableDefinition[];
  allowed_tools: string[];
  allowed_actions: string[];
  session_completion: {
    mode: "stays_open" | "ends_after_first_valid_output";
    output_schema: Record<string, unknown>;
  };
}

export interface AgentVersion {
  id: string;
  agent_id: string;
  version_number: number;
  config: AgentConfiguration;
  created_by: string | null;
  published_at: string;
}

export interface AgentSession {
  id: string;
  agent_id: string;
  agent_version_id: string;
  version_number: number;
  status: "active" | "closed" | "cancelled";
  inputs: Record<string, unknown>;
  origin_resource: string;
  created_at: string;
  closed_at: string | null;
}
