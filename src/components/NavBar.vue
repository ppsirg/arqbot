<template>
  <nav v-show="isNavBarVisible" id="navbar-main" class="navbar is-fixed-top">

    <div class="navbar-menu fadeIn animated faster" :class="{'is-active':isMenuNavBarActive}">
      <div class="navbar-end">

        <nav-bar-menu class="has-divider has-user-avatar">
          <user-avatar/>
          <div class="is-user-name">
            <span>{{ userName }}</span>
          </div>

          <div slot="dropdown" class="navbar-dropdown">
            <a class="navbar-item">
              <b-icon icon="account" custom-size="default"></b-icon>
              <span>My Profile</span>
            </a>
            <a class="navbar-item">
              <b-icon icon="settings" custom-size="default"></b-icon>
              <span>Settings</span>
            </a>
            <a class="navbar-item">
              <b-icon icon="email" custom-size="default"></b-icon>
              <span>Messages</span>
            </a>
            <hr class="navbar-divider">
            <a class="navbar-item">
              <b-icon icon="logout" custom-size="default"></b-icon>
              <span>Log Out</span>
            </a>
          </div>
        </nav-bar-menu>
        <a href="https://justboil.me/bulma-admin-template/one" class="navbar-item has-divider is-desktop-icon-only" title="About">
          <b-icon icon="help-circle-outline" custom-size="default"/>
          <span>About</span>
        </a>
        <a class="navbar-item is-desktop-icon-only" title="Log out" @click="logout">
          <b-icon icon="logout" custom-size="default"/>
          <span>Log out</span>
        </a>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapState } from 'vuex'
import NavBarMenu from '@/components/NavBarMenu'
import UserAvatar from '@/components/UserAvatar'

export default {
  name: 'NavBar',
  components: {
    UserAvatar,
    NavBarMenu
  },
  data () {
    return {
      isMenuNavBarActive: false
    }
  },
  computed: {
    menuNavBarToggleIcon () {
      return (this.isMenuNavBarActive) ? 'close' : 'dots-vertical'
    },
    menuToggleMobileIcon () {
      return this.isAsideMobileExpanded ? 'backburger' : 'forwardburger'
    },
    ...mapState([
      'isNavBarVisible',
      'isAsideMobileExpanded',
      'userName'
    ])
  },
  methods: {
    menuToggleMobile () {
      this.$store.commit('asideMobileStateToggle')
    },
    menuNavBarToggle () {
      this.isMenuNavBarActive = (!this.isMenuNavBarActive)
    },
    logout () {
      this.$buefy.snackbar.open({
        message: 'Log out clicked',
        queue: false
      })
    }
  }
}
</script>
