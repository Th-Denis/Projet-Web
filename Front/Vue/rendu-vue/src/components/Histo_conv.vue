<template>
  <div id="history">
    <h3>Conversations</h3>
    <div class="conversations" v-for="(convo, id) in convos" v-bind:id="id">
      {{ convo }}
    </div>
  </div>
  <div id="conv_management_button">
    <div class="conv_management">
      <v-btn variant="tonal" @click="changer_affichage"> Créer </v-btn>
    </div>
    <div class="conv_management">
      <v-btn variant="tonal" @click="charger_conv()"> Supprimer </v-btn>
    </div>
  </div>
  <div id="conv_management_sai" class="masquer">
    <form @submit="charger_conv()">
      <v-text-field
        clearable
        @keydown.enter="creer_conv"
        label="Nom de la conversation"
        name="name"
        variant="underlined"
        v-model="nom_conv_saisi"
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

      fetch("/api/conversations", {
        method: "POST",
        headers: {
          "Content-Type": "application/json;charset=utf-8",
        },
        body: JSON.stringify({
          name: this.nom_conv_saisi,
        }),
      }).then((response) => response.json().then((data) => console.log(data)));
      this.charger_conv();
    },

    charger_conv() {
      fetch("/api/conversations").then(
        function (response) {
          response.json().then(
            function (data) {
              if (data.status == "success") {
                this.convos = data.conversations;
              } else {
                return;
              }
            }.bind(this)
          );
        }.bind(this)
      );
    },

    changer_affichage() {
      const div_bouton = document.getElementById("conv_management_button");
      const div_saisie = document.getElementById("conv_management_sai");

      div_bouton.classList.toggle("masquer");
      div_saisie.classList.toggle("masquer");
    },
  },

  beforeMount() {
    fetch("/api/status").then(
      function (response) {
        response.json().then(
          function (data) {
            if (data.status == "success") {
              fetch("/api/conversations").then(
                function (response) {
                  response.json().then(
                    function (data) {
                      if (data.status == "success") {
                        this.convos = data.conversations;
                      } else {
                        return;
                      }
                    }.bind(this)
                  );
                }.bind(this)
              );
            } else {
              this.convos = JSON.stringify({});
            }
          }.bind(this)
        );
      }.bind(this)
    );
  },
};
</script>

<style scoped>
h3 {
  color: wheat;
}

.btn_management {
  width: 100%;
}
.conv_management {
  height: 5%;
}
.conversations {
  color: aqua;
}

.masquer {
  display: none;
}
#history {
  overflow-y: scroll;
  height: 90%;
  background-color: black;
}

#conv_management_sai {
  padding: 5px;
}

#sai_nom_conv {
  display: none;
}
</style>
