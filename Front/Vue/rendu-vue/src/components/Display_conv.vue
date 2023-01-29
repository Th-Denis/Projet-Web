<template>
  <div id="bandeau">
    <v-row>
      <v-col col="8">
        <p>Texte généré automatiquement par une machine.</p>
      </v-col>
      <v-col cols="4">
        <Login v-if="userStatus == false" @updateStatus="updateStatus"></Login>
        <SignUp v-if="userStatus == false" @updateStatus="updateStatus"></SignUp>
        <Logout v-if="userStatus == true" @updateStatus="updateStatus"></Logout>
      </v-col>
    </v-row>
  </div>
  <div id="conversation">
    <div class="message" v-for="item in items">
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
    };
  },
  props: ["messages_enbas"],
  methods: {
    updateStatus(status) {
      this.userStatus=status;
    }
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
