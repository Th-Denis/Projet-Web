<template>
  <v-row justify="center">
        <v-btn color="primary" @click="sendLogout"> Logout </v-btn>
  </v-row>
</template>

<script>
export default {
  methods: {
    sendLogout() {
      fetch("/api/logout").then(
        function (response) {
          console.log(response.json());
          if (response.status != 201) {
            this.fetchError = response.status;
          } else {
            response.json().then(
              function (data) {
                this.fetchResponse = data;
                console.log(this.fetchResponse);
              }.bind(this)
            );
          }
        }.bind(this)
      );
    },
  },
};
</script>
