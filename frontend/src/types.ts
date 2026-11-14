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
  description: string;
  primary_key_property: string;
  properties: PropertyDefinition[];
}

export interface LinkType {
  id: string;
  api_name: string;
  display_name: string;
  description: string;
  source_type_id: string;
  target_type_id: string;
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
  parameters_schema: Record<string, { required?: boolean }>;
  enabled: boolean;
}

export interface Proposal {
  id: string;
  ontology_id: string;
  title: string;
  description: string;
  base_revision: number;
  changes: Array<Record<string, unknown>>;
  status: string;
  created_at: string;
}

export interface AgentDefinition {
  id: string;
  api_name: string;
  display_name: string;
  description: string;
  allowed_tools: string[];
  allowed_actions: string[];
  enabled: boolean;
}
