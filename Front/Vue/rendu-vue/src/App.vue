<template>
  <SignUp></SignUp>
  <Login></Login>
  <Logout></Logout>
</template>

<script>
import Login from "@/components/Login.vue";
import SignUp from "@/components/SignUp.vue";
import Logout from "@/components/Logout.vue";
export default {
  components: {
    Login,
    SignUp,
    Logout,
  },
};
</script>
