<template>
  <v-list-item v-for="(message, id) in messages" :key="id">
    <v-list-item-content>
      <v-list-item-title v-if="id % 2 === 0">
        {{ message }}
      </v-list-item-title>
      <v-list-item-title class="text-right" v-else>
        {{ message }}
      </v-list-item-title>
    </v-list-item-content>
  </v-list-item>
</template>

<script>
export default {
  props: {
    conversation: {
      required: true,
    },
  },
};
</script>
