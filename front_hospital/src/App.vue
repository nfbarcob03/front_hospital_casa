<template>
  <b-container>
    <b-row class="text-center">
      <b-col md="3" class="py-3">
        <div id="app" class="app">
          <div class="header">
            <h1>Hospital en casa</h1>
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
              <button class="nav-link" v-if="is_auth">
                Inicio
              </button>
              <button class="nav-link" v-if="is_auth">
                Pacientes
              </button>
              <button class="nav-link" v-if="is_auth">
                Cerrar Sesión
              </button>
              <button
                class="nav-link"
                v-if="!is_auth"
                v-on:click="loadLogIn"
              >
                Iniciar Sesión
              </button>
              <button
                class="nav-link"
                v-if="!is_auth"
                v-on:click="loadSignUp"
              >
                Registrarse
              </button>
            </nav>
          </div>
          <div class="main-component">
            <router-view
              v-on:completedLogIn="completedLogIn"
              v-on:completedSignUp="completedSignUp"
            >
            </router-view>
          </div>

          <div class="footer">
            <h2>Misión TIC 2022</h2>
          </div>
        </div>
      </b-col>
    </b-row>
  </b-container>
</template>
<script>
export default {
  name: "App",
  data: function () {
    return {
      is_auth: false,
    };
  },
  components: {},
  methods: {
    verifyAuth: function () {
      if (this.is_auth == false) this.$router.push({ name: "logIn" });
    },
    loadLogIn: function () {
      this.$router.push({ name: "logIn" });
    },
    loadSignUp: function () {
      this.$router.push({ name: "crearPaciente" });
    },
    completedLogIn: function (data) {},
    completedSignUp: function (data) {},
  },
  created: function () {
    this.verifyAuth();
  },
};
</script>

<style>
body {
  margin: 0 0 0 0;
}
.header {
  margin: 0%;
  padding: 0;
  width: 100%;
  height: 10vh;
  min-height: 100px;
  background-color: #283747;
  color: #e5e7e9;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.header h1 {
  width: 20%;
  text-align: center;
}
.header nav {
  height: 100%;
  width: 20%;
  display: flex;
  justify-content: space-around;
  align-items: center;
  font-size: 20px;
}
.header nav button {
  color: #e5e7e9;
  background: #283747;
  border: 1px solid #e5e7e9;
  border-radius: 5px;
  padding: 10px 20px;
}
.header nav button:hover {
  color: #283747;
  background: #e5e7e9;
  border: 1px solid #e5e7e9;
}
.main-component {
  height: 75vh;
  margin: 0%;
  padding: 0%;
  background: #fdfefe;
}
.footer {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 10vh;
  min-height: 100px;
  background-color: #283747;
  color: #e5e7e9;
}
.footer h2 {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
