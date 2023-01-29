<template>
  <div id="bandeau">
    <v-row>
      <v-col col="8">
        <p>Texte généré automatiquement par une machine.</p>
      </v-col>
      <v-col cols="4">
        <Login v-if="userStatus == false" @updateStatus="updateStatus" class="bouton_connexion"></Login>
        <SignUp v-if="userStatus == false" @updateStatus="updateStatus" class="bouton_connexion"></SignUp>
        <Logout v-if="userStatus == true" @updateStatus="updateStatus" @click="this.userStatus=false" class="bouton_connexion"></Logout>
      </v-col>
    </v-row>
  </div>
  <div id="conversation">
    <div class="message" v-for="item in items">
      fdg 
      {{ item }}
    </div>
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
      message: "",
      connecte: true,
      userStatus: false,
    };
  },
  props: ["messages_enbas"],
  methods: {
    updateStatus(status) {
      this.userStatus = status;
    },
  },
  beforeMount() {
    fetch("/api/status").then(
        function (response) {
          response.json().then(
            function (data) {
              if (data.status=="success"){
                this.userStatus=true;
              } else {
                this.userStatus=false;
              };
            }.bind(this)
          );
        }.bind(this)
      );
    },
};
</script>

<style scoped>
#conversation {
  width: 100%;
  height: 95%;
  bottom: 0px;
  position: fixed;
  overflow-y: scroll;
  background-color: rgb(198, 215, 235);
  color: black;
}
#bandeau {
  position: fixed;
  height: 5%;
  width: 100%;
  background-color: rgb(24, 104, 174);
}

.message {
  padding: 5px;
  color: black;
}


</style>