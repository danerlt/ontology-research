import { describe, expect, it } from "vitest";
import { canvasLayoutKey, mapCanvasToFlow, mergeCanvasEdgeUpdates, mergeCanvasNodeUpdates } from "./ontologyCanvasGraph";
import type { OntologyCanvasResponse } from "../types";

const canvas: OntologyCanvasResponse = {
  ontology: { id: "ontology-a", api_name: "commerce", display_name: "交易本体", revision: 3 },
  branch: null,
  nodes: [
    { id: "object_type:customer", type: "objectType", data: { display_name: "客户" } },
    { id: "object_type:order", type: "objectType", data: { display_name: "订单" } },
    { id: "source_system:warehouse", type: "sourceSystem", data: { name: "交易仓库" } },
    { id: "action:close_order", type: "action", data: { display_name: "关闭订单" } },
  ],
  edges: [
    { id: "link:customer_orders", source: "object_type:customer", target: "object_type:order", type: "ontologyLink", data: { api_name: "customer_orders", display_name: "客户订单", source_cardinality: "many", target_cardinality: "one" } },
    { id: "mapping:order", source: "source_system:warehouse", target: "object_type:order", type: "sourceMapping", data: { mapped_property_count: 4 } },
    { id: "action_on:close_order", source: "object_type:order", target: "action:close_order", type: "actionAssociation", data: { api_name: "close_order" } },
  ],
};

describe("本体画布资源映射", () => {
  it("把服务端真实节点和关系映射为流程图节点与有向边", () => {
    const graph = mapCanvasToFlow(canvas);

    expect(graph.nodes.map((node) => node.id)).toEqual(canvas.nodes.map((node) => node.id));
    expect(graph.edges.map((edge) => [edge.source, edge.target])).toEqual(canvas.edges.map((edge) => [edge.source, edge.target]));
    expect(graph.edges[0]?.label).toContain("many → one");
    expect(graph.nodes.find((node) => node.id === "object_type:order")!.position.x).toBeGreaterThan(graph.nodes.find((node) => node.id === "object_type:customer")!.position.x);
  });

  it("按项目、本体和分支隔离布局保存键", () => {
    expect(canvasLayoutKey("p1", "o1", "main")).not.toBe(canvasLayoutKey("p2", "o1", "main"));
    expect(canvasLayoutKey("p1", "o1", "branch-1")).not.toBe(canvasLayoutKey("p1", "o1", "branch-2"));
  });

  it("选择派生属性路径时只强调定义中的真实链接", () => {
    const graph = mapCanvasToFlow(canvas, undefined, ["customer_orders"]);

    expect(graph.edges[0]?.data?.highlighted).toBe(true);
    expect(graph.edges[1]?.data?.highlighted).toBe(false);
  });

  it("忽略 Vue Flow 回写的未变化节点快照", () => {
    const nodes = mapCanvasToFlow(canvas).nodes;
    const echoedNodes = nodes.map((node) => ({
      ...node,
      selected: false,
      dragging: false,
      data: { ...node.data, showDerived: true },
    }));

    expect(mergeCanvasNodeUpdates(nodes, echoedNodes)).toBe(nodes);
  });

  it("保存移动后的节点坐标并保留未变化节点", () => {
    const nodes = mapCanvasToFlow(canvas).nodes;
    const movedNodes = nodes.map((node, index) => index === 0 ? { ...node, position: { x: 210, y: 50 } } : node);
    const updatedNodes = mergeCanvasNodeUpdates(nodes, movedNodes);

    expect(updatedNodes[0]?.position).toEqual({ x: 210, y: 50 });
    expect(updatedNodes[1]).toBe(nodes[1]);
  });

  it("忽略 Vue Flow 回写的未变化边快照", () => {
    const edges = mapCanvasToFlow(canvas).edges;
    const echoedEdges = edges.map((edge) => ({ ...edge, selected: false }));

    expect(mergeCanvasEdgeUpdates(edges, echoedEdges)).toBe(edges);
  });
});
