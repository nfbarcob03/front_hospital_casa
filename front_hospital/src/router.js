import { createRouter, createWebHistory } from "vue-router";
import App from "./App.vue";

import LogIn from './components/Login.vue'
import CrearPaciente from './components/CrearPaciente.vue'

const routes = [
  {
    path: "/",
    name: "root",
    component: App,
  },
  {
    path: '/user/logIn',
    name: "logIn",
    component: LogIn
    },
    {
    path: '/user/crearPaciente',
    name: "crearPaciente",
    component: CrearPaciente
    },
];
const router = createRouter({
  history: createWebHistory(),
  routes,
});
export default router;
