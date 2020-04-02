<template>
  <div>
    <title-bar :title-stack="titleStack"/>
    <hero-bar>
      Planeación por áreas
      <router-link slot="right" to="/" class="button">
        Inicio
      </router-link>
    </hero-bar>
    <section class="section is-main-section">
      <card-component title="Planeación por áreas" icon="ballot">
        <p>aqui poner un mapa de un centro comercial para asignar con poligonos las áreas de trabajo de drones</p>
      </card-component>
      <card-component title="Mi flota" icon="ballot-outline">
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
import TitleBar from '@/components/TitleBar'
import CardComponent from '@/components/CardComponent'
import HeroBar from '@/components/HeroBar'
export default {
  name: 'AreaPlanning',
  components: { HeroBar, CardComponent, TitleBar },
  data () {
    return {
      isLoading: false,
      form: {
        name: null,
        email: null,
        phone: null,
        department: null,
        subject: null,
        question: null
      },
      customElementsForm: {
        checkbox: [],
        radio: null,
        switch: true,
        file: null
      },
      departments: [
        'Business Development',
        'Marketing',
        'Sales'
      ]
    }
  },
  computed: {
    titleStack () {
      return [
        'Admin',
        'Planeacion por área'
      ]
    }
  },
  methods: {
    submit () {

    }
  }
}
</script>
