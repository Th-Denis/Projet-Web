<template>
  <div>
    <div v-for="message in conversation" :key="message.id">
      {{ message.text }}
    </div>
  </div>
</template>

<script>
export default {
  props: {
    conversation: {
      type: Array,
      required: true,
    },
  },
};
</script>
