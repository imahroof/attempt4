import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from './store/auth'

import Home from './pages/Home.vue'
import Login from './pages/Login.vue'
import Register from './pages/Register.vue'
import Dashboard from './pages/Dashboard.vue'
import Training from './pages/Training.vue'
import About from './pages/About.vue'
import Ransomware from './pages/Ransomware.vue'
import SoftwareUpdates from './pages/SoftwareUpdates.vue'
import Passwords from './pages/Passwords.vue'
import TFASimulator from './pages/TFASimulator.vue'
import Phishing from './pages/Phishing.vue'
import VPNSimulator from './pages/VPNSimulator.vue'
import SocialEngin from './pages/SocialEngin.vue'
import QuickLinks from './pages/QuickLinks.vue'
import ROCU from './pages/ROCU.vue'





const routes = [

  { path: '/', redirect: '/home' },
  { path: '/home', component: Home },
  { path: '/about', component: About },
  { path: '/training', component: Training },
  { path: '/login', component: Login },
  { path: '/register', component: Register },



  { 
    path: '/dashboard',
    name: 'dashboard',
    component: Dashboard,
    beforeEnter: (to, from, next) => {
      const authStore = useAuthStore()
      if (!authStore.isAuthenticated) {
        next('/login') // Redirect if not authenticated
      } else {
        next()
      }
    }
  },
  { 
    path: '/ransomware',
    name: 'ransomware',
    component: Ransomware,
    beforeEnter: (to, from, next) => {
      const authStore = useAuthStore()
      if (!authStore.isAuthenticated) {
        next('/login') 
      } else {
        next()
      }
    }
  },

  { 
    path: '/SoftwareUpdates',
    name: 'SoftwareUpdates',
    component: SoftwareUpdates,
    beforeEnter: (to, from, next) => {
      const authStore = useAuthStore()
      if (!authStore.isAuthenticated) {
        next('/login') 
      } else {
        next()
      }
    }
  },

  { 
    path: '/passwords',
    name: 'passwords',
    component: Passwords,
    beforeEnter: (to, from, next) => {
      const authStore = useAuthStore()
      if (!authStore.isAuthenticated) {
        next('/login')
      } else {
        next()
      }
    }
  },

  { 
    path: '/TFASimulator',
    name: 'TFASimulator',
    component: TFASimulator,
    beforeEnter: (to, from, next) => {
      const authStore = useAuthStore()
      if (!authStore.isAuthenticated) {
        next('/login') 
      } else {
        next()
      }
    }
  },

  { 
    path: '/Phishing',
    name: 'Phishing',
    component: Phishing,
    beforeEnter: (to, from, next) => {
      const authStore = useAuthStore()
      if (!authStore.isAuthenticated) {
        next('/login') 
      } else {
        next()
      }
    }
  },

  { 
    path: '/vpnsimulator',
    name: 'vpnsimulator',
    component: VPNSimulator,
    beforeEnter: (to, from, next) => {
      const authStore = useAuthStore()
      if (!authStore.isAuthenticated) {
        next('/login') 
      } else {
        next()
      }
    }
  },

  { 
    path: '/socialengin',
    name: 'socialengin',
    component: SocialEngin,
    beforeEnter: (to, from, next) => {
      const authStore = useAuthStore()
      if (!authStore.isAuthenticated) {
        next('/login') 
      } else {
        next()
      }
    }
  },

  { 
    path: '/quicklinks',
    name: 'quicklinks',
    component: QuickLinks,
    beforeEnter: (to, from, next) => {
      const authStore = useAuthStore()
      if (!authStore.isAuthenticated) {
        next('/login') 
      } else {
        next()
      }
    }
  },

  { 
    path: '/rocu',
    name: 'rocu',
    component: ROCU,
    beforeEnter: (to, from, next) => {
      const authStore = useAuthStore()
      if (!authStore.isAuthenticated) {
        next('/login') 
      } else {
        next()
      }
    }
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
