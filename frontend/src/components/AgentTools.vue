<script setup lang="ts">
import { computed, ref } from "vue";

const props = withDefaults(defineProps<{ allowedTools: string[]; sessionActive?: boolean }>(), { sessionActive: true });
const emit = defineEmits<{
  "call-tool": [tool: string, arguments_: Record<string, unknown>];
  "invalid-input": [message: string];
}>();
const query = ref("");
const objectId = ref("");
const actionName = ref("");
const expectedVersion = ref(1);
const actionParameters = ref('{"tier":"preferred"}');

const hasSearch = computed(() => props.allowedTools.includes("search_objects"));
const hasGetObject = computed(() => props.allowedTools.includes("get_object"));
const hasAction = computed(() => props.allowedTools.includes("execute_action"));

function callSearch() {
  emit("call-tool", "search_objects", { query: query.value });
}

function callGetObject() {
  emit("call-tool", "get_object", { object_id: objectId.value });
}

function callAction() {
  try {
    emit("call-tool", "execute_action", {
      action_api_name: actionName.value,
      object_id: objectId.value,
      expected_version: Number(expectedVersion.value),
      parameters: JSON.parse(actionParameters.value),
    });
  } catch {
    emit("invalid-input", "Action 参数必须是有效 JSON");
  }
}
</script>

<template>
  <section class="tool-list" aria-label="Agent 工具">
    <article class="tool-card">
      <div><h3>查找对象</h3><p>按名称或对象类型搜索本体数据</p></div>
      <div class="tool-controls">
        <input v-model="query" aria-label="搜索词" placeholder="输入对象名称" />
        <button data-tool="search_objects" class="button button-primary" :disabled="!hasSearch || !sessionActive" @click="callSearch">运行查询</button>
      </div>
    </article>
    <article class="tool-card">
      <div><h3>读取对象</h3><p>使用对象记录 ID 查看详情</p></div>
      <div class="tool-controls">
        <input v-model="objectId" aria-label="对象 ID" placeholder="对象 UUID" />
        <button data-tool="get_object" class="button button-primary" :disabled="!hasGetObject || !sessionActive" @click="callGetObject">读取对象</button>
      </div>
    </article>
    <article class="tool-card">
      <div><h3>执行 Action</h3><p>仅能运行 Agent 已获授权的 Action</p></div>
      <div class="action-inputs">
        <input v-model="actionName" aria-label="Action 名称" placeholder="Action API 名称" />
        <input v-model="expectedVersion" aria-label="对象版本" type="number" min="1" />
        <textarea v-model="actionParameters" aria-label="Action 参数" rows="2" />
        <button data-tool="execute_action" class="button button-primary" :disabled="!hasAction || !sessionActive" @click="callAction">执行 Action</button>
      </div>
    </article>
  </section>
</template>
