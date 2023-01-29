<template>
  <div id="bandeau">
    <v-row>
      <v-col col="8">
        <p>Texte généré automatiquement par une machine.</p>
      </v-col>
      <v-col cols="4">
        <Login v-if="userLog == false"></Login>
        <SignUp v-if="userLog == false"></SignUp>
        <Logout v-if="userLog == true"></Logout>
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
      userLog: false,
      message: "",
      connecte: true,
    };
  },
  props: ["messages_enbas"],
  methods: {
    changer_affichage() {
      const bouton_connexion = document.getElementById("bouton_connexion");
      const bouton_inscription = document.getElementById("bouton_inscription");
      const bouton_deconnexion = document.getElementById("bouton_deconnexion");

      if (this.connecte) {
        bouton_connexion.style.display = "none";
        bouton_inscription.style.display = "none";
        bouton_deconnexion.style.display = "flex";
      } else {
        bouton_connexion.style.display = "inline";
        bouton_inscription.style.display = "inline";
        bouton_deconnexion.style.display = "none";
      }
    },
    connexion() {
      this.connecte = true;
      this.changer_affichage();
    },
    deconnexion() {
      this.connecte = false;
      this.changer_affichage();
    },
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
