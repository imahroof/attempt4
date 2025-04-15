<template>
  <div class="navbar">
  <div class="navbar-left">
    <span>ThreatAware</span> 
  </div>
  <nav class="navbar-right">
    <ul class="nav-links">
        <li><button @click="sendHome" class="nav-button">Home</button></li>
        <li><button @click="sendAbout" class="nav-button">About</button></li>
        <li><button @click="sendTraining" class="nav-button">Training</button></li>
        <li><button @click="sendLogin" class="nav-button">Login</button></li>
        <li><button @click="sendRegister" class="nav-button">Register</button></li>
    </ul>
    </nav>
  </div> 

</template>

<script>

export default {
  name: "Navbar",
  methods: {
    sendHome() {
      this.$router.push("/home");
    },
    sendAbout() {
      this.$router.push("/about");
    },
    sendTraining() {
      this.$router.push("/training");
    },
    sendLogin() {
      this.$router.push("/login");
    },
    sendRegister() {
      this.$router.push("/register");
    },
  },
};

</script>



<style>

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

.nav-button:hover {
  background-color: #cecece;  
  border-radius: 5px;
}

.nav-button {
  color: black;
  background-color: white;
  text-decoration: none;
  font-size: 16px;  
  padding: 8px 12px;
  font-weight: bold;
  border: none;
  cursor: pointer;
}

</style>

