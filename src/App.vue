<template>
  <div id="app">
    <nav-bar/>
    <aside-menu :menu="menu"/>
    <router-view/>
    <footer-bar/>
  </div>
</template>

<script>
// @ is an alias to /src
import NavBar from '@/components/NavBar'
import AsideMenu from '@/components/AsideMenu'
import FooterBar from '@/components/FooterBar'

export default {
  name: 'home',
  components: {
    FooterBar,
    AsideMenu,
    NavBar
  },
  computed: {
    menu () {
      return [
        'General',
        [
          {
            to: '/',
            icon: 'desktop-mac',
            label: 'Panel'
          }
        ],
        'Misiones',
        [
          {
            to: '/route-planning',
            label: 'Planeación ruta',
            icon: 'table'
          },
          {
            to: '/area-planning',
            label: 'Planeacion sector',
            icon: 'account-circle'
          },
          {
            to: '/monitor',
            label: 'En progreso',
            icon: 'square-edit-outline'
          }
        ],
        'Capa Normalización',
        [
          {
            to: '/normalized-data',
            label: 'Estructura de datos',
            icon: 'credit-card'
          },
          {
            to: '/about-us',
            label: 'Sobre Nosotros',
            icon: 'help'
          }
        ]
      ]
    }
  },
  created () {
    this.$store.commit('user', {
      avatar: '/data-sources/avatars/annie-spratt-121576-unsplash.jpg'
    })
  }
}
</script>
