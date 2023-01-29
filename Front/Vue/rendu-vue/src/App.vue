<template>
  <v-app>
    <nav>
      <div id="info_user">
        <Info_user></Info_user>
      </div>
      <div id="histo_conv">
        <Histo_conv></Histo_conv>
      </div>
    </nav>
    <main>
      <div id="display_conv">
        <Display_conv v-bind:messages_enbas="messages_enbas" v-bind:userStatus="userStatus"> </Display_conv>
      </div>
      <div id="sai_message">
        <Sai_message @remonter_messages="gestion_remonter_messages">
        </Sai_message>
      </div>
    </main>
  </v-app>
</template>

<script>
import Info_user from "@/components/Info_user.vue";
import Histo_conv from "@/components/Histo_conv.vue";
import Sai_message from "@/components/Sai_message.vue";
import Display_conv from "@/components/Display_conv.vue";

export default {
  components: {
    Info_user,
    Histo_conv,
    Sai_message,
    Display_conv,
  },
  data() {
    return {
      messages_enbas: "",
      userStatus: false,
    };
  },
  methods: {
    gestion_remonter_messages(messages) {
      this.messages_enbas = messages;
    },
    getStatus() {
      fetch("/api/status").then(
        function (response) {
          if (response.status != 201) {
            this.fetchError = response.status;
          } else {
            response.json().then(
              function (data) {
                this.fetchResponse = data;
                if (this.fetchResponse.status == "success") {
                  this.userStatus = true;
                } else {
                  this.userStatus = false;
                }
              }.bind(this)
            );
          }
        }.bind(this)
      );
    },
  },
  beforeMount() {
    this.getStatus();
  },
};
</script>

<style scoped>
nav {
  position: fixed;
  height: 100%;
  background-color: aqua;
  width: 15%;
}

main {
  background-color: red;
  position: fixed;
  height: 100%;
  width: 85%;
  right: 0px;
}

#info_user {
  height: 20%;
  background-color: lightblue;
}

#histo_conv {
  height: 80%;
  background-color: yellow;
}

#display_conv {
  position: fixed;
  height: 90%;
  width: 100%;
  background-color: blue;
}

#sai_message {
  padding-left: 15px;

  width: 100%;
  height: 10%;
  position: fixed;
  bottom: 0px;
  background-color: blueviolet;
}

body {
  padding: 50px;
}
</style>
