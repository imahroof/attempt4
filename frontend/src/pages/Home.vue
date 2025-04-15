<template>
  <div>
    <Navbar />
    <div class="home-page">
      <div class="welcome-banner">
        <img src="/images/welcome-banner.jpeg" alt="Welcome to MySecure" class="banner-image" />
        <div class="banner-text">

          <!-- Main image + title + slogan -->

          <h1 class="title">Welcome to ThreatAware</h1>
          <p class="subtitle">Building knowledge, Strengthening security.</p>
        </div>
      </div>
      <div class="content">

        <!-- Intro + login -->  

        <h2 class="who-are-we">Who are we?</h2>
        <p>At ThreatAware, we work with law enforcement to provide ROCU officers with the best tools and resources to deliver exceptional cybersecurity training to businesses. Our platform helps officers educate organisations on how to protect themselves from cyber threats, stay updated on emerging risks, and strengthen their digital security. Whether you're looking to improve training outcomes or enhance business defenses, we’ve got you covered.</p>

        <p>To request a session with your local ROCU, please contact them <a href="https://www.ncsc.gov.uk/information/regional-organised-crime-units-rocus">here</a></p>
          <div v-if="authStore.isAuthenticated">
            
            <!-- Loggedin? -->  

          <p>Hi there, {{ authStore.user?.username }}!</p>
          <p class="current-status">You are logged in. 
            <button @click="continueToDashboard" class="continue-button">Continue</button>
          </p>
          <button @click="logout" class="logout-button">Logout</button>
        </div>
        <p v-else class="not-logged-in">
          You are not logged in. <router-link to="/login" class="login-link">Login</router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import { useAuthStore } from "../store/auth.js";
import { useRouter } from "vue-router";
import Navbar from "../components/Navbar.vue";

export default {
  components: {
    Navbar,
  },
  setup() {
    const authStore = useAuthStore();
    const router = useRouter();

    return {
      authStore,
      router,
    };
  },
  methods: {
    async logout() {
      try {
        await this.authStore.logout(this.$router);
      } catch (error) {
        console.error(error);
      }
    },
    continueToDashboard() {
      this.router.push("/dashboard"); 
    },
  },
  async mounted() {
    await this.authStore.fetchUser();
  },
};
</script>

<style scoped>
.home-page {
  font-family: Arial, sans-serif;
  text-align: center;
  padding: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.content-wrapper {
  width: 90%;
  max-width: 800px;
  margin: 0 auto;
}

.welcome-banner {
  position: relative;
  width: 100%;
  overflow: hidden;
  margin-bottom: 20px;
  border: 2px solid white;
  border-radius: 8px;
}

.banner-image {
  width: 100%;
  height: auto;
  display: block;
  border-radius: 8px;
}

.banner-text {
  position: absolute;
  top: 50%;
  left: 20%;
  transform: translate(-50%, -50%);
  color: white;
  text-align: center;
  width: 90%;
  max-width: 600px;
}

.banner-text h1 {
  font-size: clamp(24px, 5vw, 36px); 
  margin: 0;
  color: white;
}

.subtitle {
  font-size: clamp(16px, 3vw, 20px);
  margin-top: 10px;
}

.content {
  width: 100%;
  background: #f9f9f9;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.who-are-we {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
  color: black; 
}

.content p {
  color: black; 
}

.not-logged-in {
  width: 100%;
  font-size: 18px;
  color: black;
  padding: 20px;
  border-radius: 8px;
}

.continue-button, .logout-button {
  padding: 10px 20px;
  font-size: 16px;
  width: 10%;
  margin: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.continue-button {
  background-color: #28a745;
  color: white;
}

.continue-button:hover {
  background-color: #218838;
}

.logout-button {
  background-color: #dc3545;
  color: white;
}

.logout-button:hover {
  background-color: #c82333;
}

.login-link {
  color: #007bff;
  text-decoration: none;
  font-weight: bold;
}

.login-link:hover {
  text-decoration: underline;
}

@media (max-width: 768px) {
  .banner-text {
    width: 100%;
    padding: 10px;
  }
  
  .content-wrapper {
    width: 95%;
  }
  
  .not-logged-in {
    font-size: 16px;
    padding: 15px;
  }
}

</style>
