<template>
  <div class="signUp_user">
    <div class="container_signUp_user">
      <h2>Registrarse</h2>
      <form v-on:submit.prevent="processSignUp">
        <h2>Información usuario</h2>
        <input type="text" v-model="user.username" placeholder="Username" />
        <br />
        <input type="password" v-model="user.password" placeholder="Password" />
        <br />
        <input type="text" v-model="user.nombre" placeholder="Name" />
        <br />
        <input type="text" v-model="user.apellido" placeholder="Apellido" />
        <br />
        <input type="email" v-model="user.correo" placeholder="Email" />
        <br />
        <input type="text" v-model="user.direccion" placeholder="Direccion" />
        <br />
        <input type="text" v-model="user.telefono" placeholder="Telefono" />
        <br />

        <h2>Información paciente</h2>
        <input type="text" v-model="user.eps" placeholder="EPS" />
        <br />

        <button type="submit">Registrarse</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "SignUp",
  data: function () {
    return {
      user: {
        usuario_info: {
          username: "",
          password: "",
          nombre: "",
          apellido: "",
          correo: "",
          direccion: "",
          telefono: "",
        },
        paciente_info: {
          eps: "",
          id_registra: "",
        },
      },
    };
  },

  methods: {
    processSignUp: function () {
      axios
        .post("http://127.0.0.1:8000/registrarPaciente/", this.user, {
          headers: {},
        })
        .then((result) => {
          let dataSignUp = {
            username: this.user.username,
            token_access: result.data.access,
            token_refresh: result.data.refresh,
          };

          this.$emit("completedSignUp", dataSignUp);
        })
        .catch((error) => {
          console.log(error);

          alert("ERROR: Fallo en el registro.");
        });
    },
  },
};
</script>

<style>
.signUp_user{
margin: 0;
padding: 0%;
height: 100%;
width: 100%;
display: flex;
justify-content: center;
align-items: center;
}
.container_signUp_user {
    border

: 3px solid #283747
;

border-radius: 10px;

width: 25%;
height: 90%;
display: flex;

flex-direction: column;

justify-content: center;

align-items: center;

}
.signUp_user h2
{
color: #283747;

}
.signUp_user form
{

width: 70%;

}
.signUp_user input
{

height: 40px;
width: 100%;

box-sizing: border-box;

padding: 10px 20px;

margin: 5px 0;
border: 1px solid #283747;

}
.signUp_user button
{

width: 100%;
height: 40px;
color: #E5E7E9;
background: #283747;

border: 1px solid #E5E7E9;

border-radius: 5px;

padding: 10px 25px;

margin: 5px 0 25px 0;

}
.signUp_user button:hover
{

color: #E5E7E9;
background: crimson;
border: 1px solid #283747;
}
</style>