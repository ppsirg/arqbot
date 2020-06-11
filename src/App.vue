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
const NavBar = () => import(/* webpackChunkName: "navbarmain" */ '@/components/NavBar')
const AsideMenu = () => import(/* webpackChunkName: "asidemenu" */ '@/components/AsideMenu')
const FooterBar = () => import(/* webpackChunkName: "footerbar" */ '@/components/FooterBar')

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
            label: 'Planeación',
            icon: 'table'
          },
          {
            to: '/monitor',
            label: 'En progreso',
            icon: 'square-edit-outline'
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
