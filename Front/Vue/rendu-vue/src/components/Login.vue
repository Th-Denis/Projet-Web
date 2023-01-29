<template>
    <v-dialog v-model="dialog" persistent>
      <template v-slot:activator="{ props }">
        <v-btn variant="tonal" v-bind="props"> Login </v-btn>
      </template>
      <v-card>
        <v-card-title>
          <span class="text-h5">Login</span>
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
            Login
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
    password: "",
    passwordRules: [(v) => !!v || "Password is required"],
  }),
  methods: {
    async validate() {
      const { valid } = await this.$refs.form.validate();

      if (valid) {
        this.sendLogin();
      }
    },
    reset() {
      this.$refs.form.reset();
      this.dialog = false;
    },
    sendLogin() {
      fetch("/api/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json;charset=utf-8",
        },
        body: JSON.stringify({
          email: this.email,
          password: this.password,
        }),
      }).then(
        function (response) {
          if (response.status != 200) {
            this.fetchError = response.status;
          } else {
            response.json().then(
              function (data) {
                this.fetchResponse = data;
                if (this.fetchResponse.status = "success"){
                  this.$emit("updateStatus", true);
                  this.dialog=false;
                }
              }.bind(this)
            );
          }
        }.bind(this)
      );
    },
  },
};
</script>
