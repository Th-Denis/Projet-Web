<template>
  <div id="bandeau">
    <v-row>
      <v-col col="8">
        <p>Texte généré automatiquement par une machine.</p>
      </v-col>
      <v-col cols="4"
        ><v-btn
          id="bouton_inscription"
          class="bouton_enregistrement"
          variant="tonal"
          @click="connexion"
        >
          Inscription </v-btn
        ><v-btn
          id="bouton_connexion"
          class="bouton_enregistrement"
          variant="tonal"
          @click="connexion"
        >
          Connexion
        </v-btn>
        <v-btn
          id="bouton_deconnexion"
          class="bouton_enregistrement masquer"
          variant="tonal"
          @click="deconnexion"
        >
          Déconnexion
        </v-btn></v-col
      >
    </v-row>
  </div>
  <div id="conversation">
    <div class="message" v-for="item in items">
      {{ item }}
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showText: true,
      items: ["item 1", "item 2", "item 3"],
      message: "",
      imageUrl: "https:</exemple.fr/img.png",
      connecte: true,
    };
  },
  props: ['messages_enbas'],
  methods: {
    changer_affichage() {
      const bouton_connexion = document.getElementById("bouton_connexion");
      const bouton_inscription = document.getElementById("bouton_inscription");
      const bouton_deconnexion = document.getElementById("bouton_deconnexion");
      console.log(this.messages_enbas);
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
    connexion(){
        this.connecte = true;
        this.changer_affichage();
    },
    deconnexion(){
        this.connecte = false;
        this.changer_affichage();
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
