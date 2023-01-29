<template>
  <v-app>
    <nav>
      <div id="info_user">
        <Info_user></Info_user>
      </div>
      <div id="histo_conv">
        <Histo_conv
          @convoId="selectConvo"
          v-bind:userStatus="userStatus"
        ></Histo_conv>
      </div>
    </nav>
    <main>
      <div id="display_conv">
        <Display_conv
          v-bind:messages_enbas="messages_enbas"
          v-bind:selectedConvo="selectedConvo"
          @userStatus="updUserStatus"
        >
        </Display_conv>
      </div>
      <div id="sai_message">
        <Sai_message
          @message_saisi="gestion_remonter_messages"
          v-bind:selectedConvo="selectedConvo"
        >
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
      messages_enbas: null,
      selectedConvo: null,
      userStatus: null,
    };
  },

  methods: {
    gestion_remonter_messages(messages) {
      this.messages_enbas = messages;
    },
    selectConvo(id) {
      this.selectedConvo = id;
    },
    updUserStatus(id) {
      this.userStatus = id;
    },
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
  background-color: rgb(217, 165, 179);
  border: solid 1px;
}
#histo_conv {
  height: 80%;
  background-color: rgb(217, 165, 179);
  border: solid 1px;
}
#display_conv {
  position: fixed;
  height: 90%;
  width: 100%;
  background-color: rgb(121, 167, 211);
}
#sai_message {
  padding-left: 15px;
  width: 100%;
  height: 10%;
  position: fixed;
  bottom: 0px;
  background-color: rgba(24, 104, 174);
}
body {
  padding: 50px;
}
</style>