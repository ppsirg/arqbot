<template>
  <div>
    <title-bar :title-stack="titleStack"/>
    <hero-bar>
      Misiones en progreso
    </hero-bar>
    <section class="section is-main-section">
      <card-component v-for="dr in userDrones" :key="dr" :title="'Dron ' + dr">
        <img v-bind:src="videoStreamerURL + dr" :alt="dr">
      </card-component>
    </section>
  </div>
</template>

<script>
import { mapState } from 'vuex'
// @ is an alias to /src
const TitleBar = () => import(/* webpackChunkName: "titlebar" */ '@/components/TitleBar')
const HeroBar = () => import(/* webpackChunkName: "herobar" */ '@/components/HeroBar')
const CardComponent = () => import(/* webpackChunkName: "cardcomponent" */ '@/components/CardComponent')
const sts = require('@/assets/db.json')
export default {
  name: 'Profile',
  components: { HeroBar, TitleBar, CardComponent },
  data: function () {
    return {
      videoStreamerURL: `${sts.video_streamer_server}/stream/`
    }
  },
  computed: {
    titleStack () {
      return [
        'Admin',
        'Monitor'
      ]
    },
    ...mapState([
      'userDrones'
    ])
  }
}
</script>
