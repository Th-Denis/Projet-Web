<template>
        <v-btn variant="tonal" @click="sendLogout"> Logout </v-btn>
</template>

<script>
export default {
  methods: {
    sendLogout() {
      fetch("/api/logout").then(
        function (response) {
          if (response.status != 201) {
            this.fetchError = response.status;
          } else {
            response.json().then(
              function (data) {
                this.fetchResponse = data;
                this.$emit("updateStatus", false);
              }.bind(this)
            );
          }
        }.bind(this)
      );
    },
  },
};
</script>
