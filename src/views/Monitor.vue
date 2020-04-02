<template>
  <div>
    <title-bar :title-stack="titleStack"/>
    <hero-bar>
      Misiones en progreso
      <router-link slot="right" to="/" class="button">
        Inicio
      </router-link>
    </hero-bar>
    <section class="section is-main-section">
      <card-component title="Misiones en progreso">
        <p>ver si es necesario</p>
      </card-component>
    </section>
  </div>
</template>

<script>
import CardComponent from '@/components/CardComponent'
import TitleBar from '@/components/TitleBar'
import HeroBar from '@/components/HeroBar'
export default {
  name: 'Profile',
  components: { HeroBar, TitleBar, CardComponent },
  computed: {
    titleStack () {
      return [
        'Admin',
        'Monitor'
      ]
    }
  }
}
</script>
