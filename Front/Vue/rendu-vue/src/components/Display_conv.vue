<template>
  <div id="bandeau">
    <v-row>
      <v-col col="8">
        <p>Texte généré automatiquement par une machine.</p>
      </v-col>
      <v-col cols="4">
        <Login v-if="userStatus == false" @updateStatus="updateStatus"></Login>
        <SignUp
          v-if="userStatus == false"
          @updateStatus="updateStatus"
        ></SignUp>
        <Logout
          v-if="userStatus == true"
          @updateStatus="updateStatus"
          @click="this.userStatus = false"
        ></Logout>
      </v-col>
    </v-row>
  </div>

  <div id="messages">
    <v-row>
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
    </v-row>
  </div>
</template>

<script>
import Login from "@/components/Login.vue";
import SignUp from "@/components/SignUp.vue";
import Logout from "@/components/Logout.vue";
export default {
  components: {
    Login,
    SignUp,
    Logout,
  },

  data() {
    return {
      messages: [],
      connecte: true,
      userStatus: false,
      selectedConv: null,
    };
  },

  props: ["messages_enbas", "selectedConvo"],
  methods: {
    updateStatus(status) {
      this.userStatus = status;
      // METTRE EMIT ICI
    },
    async getMessages(selectedConvo) {
      await fetch(`/api/messages?id=${selectedConvo}`).then(
        function (response) {
          response.json().then(
            function (data) {
              if (data.status == "success") {
                this.messages = data.messages;
              } else {
                return;
              }
            }.bind(this)
          );
        }.bind(this)
      );
    },
  },

  beforeMount() {
    fetch("/api/status").then(
      function (response) {
        response.json().then(
          function (data) {
            if (data.status == "success") {
              this.userStatus = true;
            } else {
              this.userStatus = false;
            }
          }.bind(this)
        );
      }.bind(this)
    );
  },
  // METTRE EMIT ICI
};
</script>

<style scoped>
#conversation {
  width: 100%;
  height: 95%;
  bottom: 0px;
  position: fixed;
  overflow-y: scroll;
  background-color: brown;
}
#bandeau {
  position: fixed;
  height: 5%;
  width: 100%;
  background-color: bisque;
}
.masquer {
  display: none;
}

.message {
  padding: 5px;
}

.bouton_enregistrement {
  margin: 5px;
}

p {
  background-color: rgb(147, 153, 153);
}
</style>
