<template>
    <v-dialog v-model="dialog" persistent>
      <template v-slot:activator="{ props }">
        <v-btn variant="tonal" v-bind="props"> SignUp </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="text-h5">SignUp</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-form ref="form" v-model="valid" lazy-validation>
              <v-text-field
                v-model="email"
                :rules="emailRules"
                label="E-mail"
                placeholder="Enter your e-mail"
                required
              ></v-text-field>
              <v-text-field
                v-model="name"
                :rules="nameRules"
                label="Name"
                placeholder="Enter your name"
                required
              ></v-text-field>
              <v-text-field
                v-model="password"
                :rules="passwordRules"
                label="Password"
                placeholder="Enter your password"
                required
              ></v-text-field>
            </v-form>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue-darken-1" variant="text" @click="reset">
            Close
          </v-btn>
          <v-btn color="blue-darken-1" variant="text" @click="validate">
            SignUp
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
</template>

<script>
export default {
  data: () => ({
    dialog: false,
    valid: true,
    show1: false,
    show2: true,
    email: "",
    emailRules: [
      (v) => !!v || "E-mail is required",
      (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
    ],
    name: "",
    nameRules: [(v) => !!v || "Name is required"],
    password: "",
    passwordRules: [(v) => !!v || "Password is required"],
  }),
  methods: {
    async validate() {
      const { valid } = await this.$refs.form.validate();

      if (valid) {
        this.sendSignUp();
      }
    },
    reset() {
      this.$refs.form.reset();
      this.dialog = false;
    },
    sendSignUp() {
      fetch("/api/signup", {
        method: "POST",
        headers: {
          "Content-Type": "application/json;charset=utf-8",
        },
        body: JSON.stringify({
          email: this.email,
          name: this.name,
          password: this.password,
        }),
      }).then(
        function (response) {
          console.log(response.json());
          if (response.status != 201) {
            this.fetchError = response.status;
          } else {
            response.json().then(
              function (data) {
                this.fetchResponse = data;
                console.log(this.fetchResponse);
              }.bind(this)
            );
          }
        }.bind(this)
      );
    },
  },
};
</script>
