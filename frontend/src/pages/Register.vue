<template>

<Navbar />

  <div class="login-container">
    <img src="/images/security-shield.png" alt="Security Shield" class="login-image" />

    <!-- Register Page -->

    <h1>Register</h1>
    <form @submit.prevent="register" class="login-form">
      <div class="input-group">
        <label for="first_name" class="input-label">First Name:</label>
        <input
          v-model="first_name"
          id="first_name"
          type="text"
          required
          class="input-field"
          placeholder="Enter your first name"
        />
      </div>
      <div class="input-group">
        <label for="last_name" class="input-label">Last Name:</label>
        <input
          v-model="last_name"
          id="last_name"
          type="text"
          required
          class="input-field"
          placeholder="Enter your last name"
        />
      </div>
      <div class="input-group">
        <label for="email" class="input-label">Email:</label>
        <input
          v-model="email"
          id="email"
          type="email"
          required
          class="input-field"
          placeholder="Enter your email"
        />
      </div>
      <div class="input-group">
        <label for="password" class="input-label">Master Password:</label>
        <input
          v-model="password"
          id="password"
          type="password"
          required
          class="input-field"
          placeholder="Enter your master password"
        />
      </div>
      <button type="submit" class="submit-btn">Register</button>
    </form>
    <button @click="$router.back()" class="back-btn">Back</button>
    <p v-if="error" class="error-message">{{ error }}</p>
    <p v-if="success" class="success-message">{{ success }}</p>
  </div>
</template>

<script>
import Navbar from "../components/Navbar.vue";
import { getCSRFToken } from "../store/auth";

export default {
  components: {
    Navbar,
  },
  data() {
    return {
      first_name: "",
      last_name: "",
      email: "",
      password: "",
      error: "",
      success: "",
    };
  },
  methods: {
    async register() {
      //register user
      try {
        const response = await fetch("http://localhost:8000/api/register", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken(),
          },
          body: JSON.stringify({
            first_name: this.first_name,
            last_name: this.last_name,
            email: this.email,
            password: this.password,
          }),
          credentials: "include",
        });
        const data = await response.json();
        if (response.ok) {
          this.success = "Registration successful! Please log in.";
          setTimeout(() => {
            this.$router.push("/login");
          }, 1000);
        } else {
          this.error = data.error || "Registration failed";
        }
      } catch (err) {
        this.error = "Error occurred: " + err;
      }
    },
  },
};
</script>

<style scoped>
.navbar {
  display: flex;  
  justify-content: space-between;  
  align-items: center;
  background-color: #333; 
  padding: 10px 20px;  
}

.navbar-left {
  color: white;
  font-size: 20px;  
}

.navbar {
  display: flex;  
  justify-content: space-between;  
  align-items: center;  
  background-color: #ffffff;  
  padding: 10px 20px;  
  position: fixed;  
  top: 0;  
  left: 0;  
  right: 0;  
  z-index: 1000;  
}

.navbar-left {
  color: rgb(0, 0, 0);
  font-weight: bold;
  font-size: 24px; 
}

.navbar-right {
  display: flex;  
  
}

.nav-links {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex; 
}

.nav-links li {
  margin-left: 20px;  
}

.nav-links a {
  color: rgb(73, 73, 73);
  text-decoration: none;
  font-size: 16px;  
  padding: 8px 12px;
  font-weight: bold;

}

.nav-links a:hover {
  background-color: #cecece;  
  border-radius: 5px;
}

.login-container {
  width: 400px;
  margin: 0 auto;
  padding: 50px;
  background-color: #f4f4f9;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  text-align: center;
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
  background-color: #28a745;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.submit-btn:hover {
  background-color: #005bb5;
}

.error-message {
  margin-top: 10px;
  color: #d9534f;
  font-size: 0.9rem;
}

.success-message {
  margin-top: 10px;
  color: #28a745;
  font-size: 0.9rem;
}

.login-image {
  width: 150px; 
  height: auto;
  margin-bottom: 20px;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.back-btn {
  width: 100%;  
  padding: 12px;
  font-size: 1rem;
  background-color: #777;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
  margin-top: 10px;
}

.back-btn:hover {
  background-color: #555;
}


</style>
