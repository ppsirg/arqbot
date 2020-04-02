<template>
  <div>
    <title-bar :title-stack="titleStack"/>
    <hero-bar>
      Planeación por definición de ruta
      <router-link slot="right" to="/" class="button">
        Inicio
      </router-link>
    </hero-bar>
    <section class="section is-main-section">
      <card-component title="Planeación por definición de ruta">
        <p>aqui poner un mapa en el que se puedan poner los drones en sus posiciones iniciales y moviendolos
          estilo drag and drop poder definir las rutas que van a seguir durante la mision
        </p>
      </card-component>
      <card-component title="Mi Flota">
        <p>poner aqui una lista de las cosas que tiene la flota del dron e información de la mision como:</p>
        <ul>
          <li>hora inicio - hora fin</li>
          <li>drones a usar</li>
          <li>costo de uso</li>
        </ul>
      </card-component>
    </section>
  </div>

</template>

<script>
import CardComponent from '@/components/CardComponent'
import TitleBar from '@/components/TitleBar'
import HeroBar from '@/components/HeroBar'
export default {
  name: 'Tables',
  components: { HeroBar, TitleBar, CardComponent },
  computed: {
    titleStack () {
      return [
        'Admin',
        'Planeacion por ruta'
      ]
    }
  }
}
</script>
