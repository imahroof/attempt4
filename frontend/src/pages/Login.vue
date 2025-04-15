<template>
  <Navbar />
  <div>
    <!-- Login Container -->
    <div class="login-container">
      <img src="/images/security-shield.png" alt="Security Shield" class="login-image" />
      <h1>Login</h1>
      <form @submit.prevent="login" class="login-form">
        <div class="input-group">
          <label for="email" class="input-label">Email:</label>
          <input v-model="email" id="email" type="email" required @input="resetError" class="input-field" />
        </div>
        <div class="input-group">
          <label for="password" class="input-label">Master Password:</label>
          <input v-model="password" id="password" type="password" required @input="resetError" class="input-field" />
        </div>
        <button type="submit" class="submit-btn">Login</button>
      </form>
      <button @click="goToRegister" class="register-btn">Register</button>
      <p v-if="error" class="error-message">{{ error }}</p>
    </div>
  </div>
</template>

<script>
import Navbar from "../components/Navbar.vue";
import { useAuthStore } from "../store/auth";

export default {
  components: {
    Navbar,
  },
  setup() {
    const authStore = useAuthStore();
    return { authStore };
  },
  data() {
    return {
      email: "",
      password: "",
      error: "",
    };
  },
  methods: {
    async login() {
      //if login failed, not registred, push to register
      await this.authStore.login(this.email, this.password, this.$router);
      if (!this.authStore.isAuthenticated) {
        this.error = "Login failed. Please check your credentials.";
      }
    },
    resetError() {
      this.error = "";
    },
    goToRegister() {
      this.$router.push("/register"); 
    },
  },
};
</script>

<style scoped>

/* To make space for the navbar at the top of the page */
.login-container {
  max-width: 400px;
  margin: 80px auto 0; /* Added top margin to offset the navbar height */
  padding: 50px;
  background-color: #f4f4f9;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.login-image {
  width: 150px; /* Adjust the size as needed */
  height: auto;
  margin-bottom: 20px; /* Space between image and heading */
  display: block;
  margin-left: auto;
  margin-right: auto;
}

h1 {
  font-size: 2rem;
  color: #333;
  margin-bottom: 20px;
}

.login-form {
  display: flex;
  flex-direction: column;
}

.input-group {
  margin-bottom: 15px;
}

.input-label {
  display: block;
  font-size: 1rem;
  color: #555;
  margin-bottom: 5px;
}

.input-field {
  width: 100%;
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

.input-field:focus {
  border-color: #0066cc;
  outline: none;
}

.submit-btn {
  padding: 12px;
  font-size: 1rem;
  background-color: #0066cc;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.submit-btn:hover {
  background-color: #005bb5;
}

.register-btn {
  padding: 12px;
  font-size: 1rem;
  background-color: #28a745; /* Green */
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
  width: 100%;
  margin-top: 10px;
}

.register-btn:hover {
  background-color: #218838; /* Darker green */
}

.error-message {
  margin-top: 10px;
  color: #d9534f;
  font-size: 0.9rem;
}
</style>
