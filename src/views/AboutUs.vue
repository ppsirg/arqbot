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
// @ is an alias to /src
const TitleBar = () => import(/* webpackChunkName: "titlebar" */ '@/components/TitleBar')
const HeroBar = () => import(/* webpackChunkName: "herobar" */ '@/components/HeroBar')
const CardComponent = () => import(/* webpackChunkName: "cardcomponent" */ '@/components/CardComponent')
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
