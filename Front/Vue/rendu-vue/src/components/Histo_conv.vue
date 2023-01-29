<template>
  <div id="history">
    <v-list>
      <h3>Conversations</h3>
      <v-list-item v-for="(convo, id) in this.convos" :key="id" :title="convo" @click="selectConvo(id) ">
        <v-list-item-action >
              <v-btn  variant="tonal" text color="error" @click="suppr_conv(id)">Supprimer</v-btn>
            </v-list-item-action>
      </v-list-item>
    </v-list>
  </div>
  <div id="conv_management_button">
    <div class="conv_management" @click="this.changer_affichage">
      <v-btn variant="tonal"> Créer </v-btn>
    </div>
  </div>
  <div id="conv_management_sai" class="masquer">
    <v-form ref="form" v-model="valid" lazy-validation>
      <v-text-field
        clearable
        @keydown.enter="validate"
        @update:focused="charger_conv"
        @click:input="charger_conv"
        label="Nom de la conversation"
        name="name"
        variant="underlined"
        v-model="nom_conv"
        :rules="nameRules"
        required
      ></v-text-field>
    </v-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showText: true,
      nom_conv: "",
      nameRules: [
        (v) => !!v || "Nom obligatoire",
        (v) => (v && v.length >= 3) || "Veuillez saisir au moins 3 caractères",
      ],
      convos: [],
    };
  },

  props:["userStatus"],
  watch: {
    selectedConvo() {
      this.getMessages();
    },
    userStatus() {
      this.charger_conv();
    }
  },

  methods: {
    async validate(event) {
      event.preventDefault();
      const { valid } = await this.$refs.form.validate();

      if (valid) {
        this.creer_conv();
      };
      this.charger_conv()
    },

    creer_conv() {
      this.changer_affichage();
      fetch("/api/conversations", {
        method: "POST",
        headers: {
          "Content-Type": "application/json;charset=utf-8",
        },
        body: JSON.stringify({
          name: this.nom_conv,
        }),
      }).then((response) => response.json().then((data) => console.log(data)));
    },

    async charger_conv() {
      await fetch("/api/conversations").then(
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

    async suppr_conv(id) {
      await fetch(`api/del+conversations/${id}`, {
          method: "DELETE"
        });
      try {
        this.charger_conv();
      } catch (error) {
        console.error(error);
      }
    },

    selectConvo(id){
      this.$emit("convoId", id)
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
