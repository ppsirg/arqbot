<template>
  <div>
    <title-bar :title-stack="titleStack"/>
    <hero-bar :has-right-visible="false">
      Sobre nosotros
    </hero-bar>
    <section class="section is-main-section">

      <card-component title="Estudiantes" @header-icon-click="fillChartData" icon="finance" header-icon="reload">
        <p>Para el curso de arquitectura de software de la Universidad Pontificia Javeriana Cali.</p>
        <ul>
            <li>Ing Cristian Maldonado</li>
            <li>Ing Diana Muñoz</li>
            <li>Ing Pedro Rivera</li>
        </ul>
      </card-component>
    </section>
  </div>
</template>

<script>
// @ is an alias to /src
import TitleBar from '@/components/TitleBar'
import HeroBar from '@/components/HeroBar'
import CardComponent from '@/components/CardComponent'
export default {
  name: 'aboutus',
  components: {
    CardComponent,
    HeroBar,
    TitleBar
  },
  computed: {
    titleStack () {
      return [
        'Admin',
        'sobre nosotros'
      ]
    }
  }
}
</script>
