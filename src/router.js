import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

Vue.use(Router)

export default new Router({
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/route-planning',
      name: 'routeplan',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "routeplan" */ './views/Route_planning.vue')
    },
    {
      path: '/area-planning',
      name: 'areaplan',
      component: () => import(/* webpackChunkName: "areaplan" */ './views/Area_planning.vue')
    },
    {
      path: '/monitor',
      name: 'monitor',
      component: () => import(/* webpackChunkName: "monitor" */ './views/Monitor.vue')
    },
    {
      path: '/normalized-data',
      name: 'normalized_data',
      component: () => import(/* webpackChunkName: "normalizeddata" */ './views/NormalizedData.vue')
    },
    {
      path: '/about-us',
      name: 'aboutus',
      component: () => import(/* webpackChunkName: "aboutus" */ './views/AboutUs.vue')
    }
  ],
  scrollBehavior (to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { x: 0, y: 0 }
    }
  }
})
