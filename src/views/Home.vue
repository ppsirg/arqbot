<template>
  <div>
    <title-bar :title-stack="titleStack"/>
    <hero-bar :has-right-visible="false">
      Panel de mision
    </hero-bar>
    <!-- login  -->
    <section class="section is-main-section" v-show="! userName">
        <b-field label="Username"
            type="is-success"
            message="This username is available">
            <b-input v-model="user.name" maxlength="30"></b-input>
        </b-field>
        <b-field label="Password">
            <b-input type="password"
                v-model="user.pass"
                password-reveal>
            </b-input>
        </b-field>
        <b-button @click="loginUser">Iniciar sesion</b-button>
    </section>
    <!-- home -->
    <section class="section is-main-section" v-show="userName">
      <h1>Bienvenido {{ userName }}</h1>
    </section>
  </div>
</template>

<script>
import { mapState } from 'vuex'
// @ is an alias to /src
const TitleBar = () => import(/* webpackChunkName: "titlebar" */ '@/components/TitleBar')
const HeroBar = () => import(/* webpackChunkName: "herobar" */ '@/components/HeroBar')

export default {
  name: 'home',
  components: {
    HeroBar,
    TitleBar
  },
  data () {
    return {
      user: {
        name: '',
        pass: ''
      }
    }
  },
  computed: {
    titleStack () {
      return [
        'Admin',
        'Dashboard'
      ]
    },
    ...mapState([
      'userName'
    ])
  },
  mounted () {
    this.$buefy.snackbar.open({
      message: 'Welcome back',
      queue: false
    })
  },
  methods: {
    loginUser: function (loginevent) {
      console.log({ loginevent })
      const dbdata = require('@/assets/db.json')
      var userDrones = []
      var emailDomain = 'user'
      dbdata.users.forEach(element => {
        if (element.user === this.user.name) {
          userDrones = element.drones
          emailDomain = element.company
        }
      })
      let userData = {
        name: this.user.name,
        email: `${this.user.name}@${emailDomain}.com`,
        drones: userDrones
      }
      this.$store.commit('user', userData)
    }
  }
}
</script>
