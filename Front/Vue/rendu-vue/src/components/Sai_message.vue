<template>
  <v-form ref="form" v-model="valid" lazy-validation color="red">
    <v-row>
      <v-col col="9">
        <v-text-field
          id="champ_saisi"
          clearable
          label="Saisissez votre message"
          variant="underlined"
          v-model="message_saisi"
          :counter="3"
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
      artiste_saisi:"Bad bunny",
      nameRules: [
        (v) => !!v || "Message obligatoire",
        (v) => (v && v.length >= 3) || "Veuillez saisir au moins 3 caractères",
      ],
      dico: []
    };
  },
  methods: {
    envoyer_message() {
      this.$refs.form.validate().then((data) => {
        /*
        if (data.valid) {
          console.log(this.message_saisi);
          fetch("http://127.0.0.1:5000/messages", {
            method: "POST",
            body: this.message_saisi,
            headers: { "Content-Type": "text/plain" },
          }).then((response) =>
            response.json().then((data) => console.log(data))
          );
        }
        */
        if (data.valid) {
          const url =
            "https://itunes.apple.com/search?term=" +
            this.artiste_saisi.replace(" ", "+") +
            "&media=music&limit=10";
          fetch(url)
            .then((response) => response.json())
            .then((data) => {
              data.results.forEach((music) => {
                this.dico.push({
                  titre: music.trackName,
                  url_img: music.artworkUrl100,
                  extrait_musique: music.previewUrl,

                });
              });
            });
        }

        const champ_saisi = document.getElementById("champ_saisi");

        champ_saisi.value = "";
        this.message_saisi = "";
        this.remonter_messages();
      });
    },
    remonter_messages(){
      this.$emit('remonter_messages',this.dico);
    }
  },
};
</script>
