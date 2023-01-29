<template>
  <v-form
    ref="form"
    @submit.prevent="envoyer_message"
    v-model="valid"
    lazy-validation
    color="red"
  >
    <v-row>
      <v-col col="9">
        <v-text-field
          id="champ_saisi"
          clearable
          label="Saisissez votre message"
          variant="underlined"
          v-model="message_saisi"
          :rules="nameRules"
          required
        ></v-text-field>
      </v-col>
      <v-col cols="3">
        <v-btn variant="tonal" @click="envoyer_message">
          <v-icon>mdi-send</v-icon>
          Envoyer
        </v-btn>
      </v-col>
    </v-row>
  </v-form>
</template>

<script>
export default {
  data() {
    return {
      message_saisi: "",
      nameRules: [
        (v) => !!v || "Message obligatoire",
        (v) => (v && v.length >= 3) || "Veuillez saisir au moins 3 caractères",
      ],
      dico: [],
    };
  },
  props: ["id_conv"],
  methods: {
    envoyer_message() {
      this.$refs.form.validate().then((data) => {
        if (data.valid) {
          fetch("/api/messages", {
            method: "POST",
            body: JSON.stringify({
              id_conv: this.id_conv,
              text: this.message_saisi,
            }),
            headers: { "Content-Type": "text/plain" },
          }).then((response) =>
            response.json().then((data) => console.log(data))
          );
        }

        const champ_saisi = document.getElementById("champ_saisi");

        champ_saisi.value = "";
        this.remonter_messages();
        this.message_saisi = "";
      });
    },
    remonter_messages() {
      this.$emit("remonter_messages", this.message_saisi);
    },
  },
};
</script>
