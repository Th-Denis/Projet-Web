<template>
  <div id="history">
    <h3>Conversations</h3>
    <div class="conversations" v-for="item in items" v-bind:id="item">
      {{ item }}
    </div>
  </div>
  <div id="conv_management_button">
    <div class="conv_management">
      <v-btn variant="tonal" @click="changer_affichage"> Créer </v-btn>
    </div>
    <div class="conv_management">
      <v-btn variant="tonal"> Supprimer </v-btn>
    </div>
  </div>
  <div id="conv_management_sai" class="masquer">
    <form action="http://127.0.0.1:5000/conversations" method="post">
      <v-text-field
        clearable
        @keydown.enter="creer_conv"
        label="Nom de la conversation"
        name="name"
        variant="underlined"
        v-model="nom_conv_saisi"
        :counter="3"
        :rules="nameRules"
        required
      ></v-text-field>
    </form>
  </div>
</template>
<script>
export default {
  data() {
    return {
      showText: true,
      items: ["item 1", "item 2", "item 3"],
      nom_conv_saisi: "",
      nameRules: [
        (v) => !!v || "Nom obligatoire",
        (v) => (v && v.length >= 3) || "Veuillez saisir au moins 3 caractères",
      ],
    };
  },
  methods: {
    creer_conv(event) {
      event.preventDefault();
      this.changer_affichage();

      fetch("http://127.0.0.1:5000/conversations", {
        method: "POST",
        body: this.message_saisi,
        headers: { "Content-Type": "text/plain" },
      }).then((response) => response.json().then((data) => console.log(data)));
    },

    changer_affichage() {
      const div_bouton = document.getElementById("conv_management_button");
      const div_saisie = document.getElementById("conv_management_sai");

      div_bouton.classList.toggle("masquer");
      div_saisie.classList.toggle("masquer");
    },
  },
};
</script>

<style scoped>
h3 {
  color: black;
  padding-top: 10px;
  padding-bottom: 30px;
}

.btn_management {
  width: 100%;
}
.conv_management {
  height: 20%;
  padding-top: 20px ;
}
.conversations {
  color: black;
  padding-bottom: 20px;
}

.masquer {
  display: none;
}
#history {
  overflow-y: scroll;
  height: 80%;
  background-color: rgb(217, 165, 179);
  border: solid 1px;
}

#conv_management_sai {
  padding: 5px;
}

#sai_nom_conv {
  display: none;
}
</style>
