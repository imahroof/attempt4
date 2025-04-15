<template>
  <Navbar />
  <div class="main-container">
    
    <!-- VPN DEMO -->
    <div class="vpn-container">
      <label class="toggle-switch">
        <span>VPN Off</span>
        <input type="checkbox" v-model="vpnEnabled" />
        <div class="slider"></div>
        <span>VPN On</span>
      </label>

      <h2>Your Network Traffic</h2>
      
      <ul class="data-list">
        <li v-for="(packet, index) in displayedData" :key="index">
          {{ packet }}
        </li>
      </ul>
    </div>

    <!-- Educational Content -->
    <div class="text-container">
      <h1>Public Wifi</h1>
      <ul>
        <li>Public wifi is widely available and easy to connect to, but it's risky.</li>
        <li>All traffic is unencrypted and public, meaning it can be intercepted.</li>
        <li>Anyone on the same network could be spying on your activity.</li>
        <li>If connected to a public network, avoid sharing sensitive information or making transactions.</li>
        <li>Man-in-the-Middle (MITM) attacks are a potential threat.</li>
        <li>Your mobile data connection is safer than public wifi.</li>
      </ul>

      <h2>What Is a VPN?</h2>
      <ul>
        <li>A VPN (Virtual Private Network) encrypts your internet traffic, ensuring your privacy.</li>
        <li>It hides your identity and encrypts all data sent from your device.</li>
        <li>Especially useful when connected to public wifi networks, like in coffee shops.</li>
        <li>All data sent is unreadable to anyone trying to spy on it.</li>
        <li>There are many VPN options available, some of them are even free.</li>
        <li>Other benefits of a VPN include access to geo-blocked content.</li>
      </ul>
    </div>

  </div>
</template>

<script>
import Navbar from '../components/Navbar.vue';

export default {
  components: {
    Navbar
  },
  data() {
    return {
      vpnEnabled: false, // VPN ON OR OFF
      rawData: [
        "Username: gmoore47",
        "Password: qwerty987!",
        "Credit Card: 5522-3333-4444-5555",
        "Email: garymoore@outlook.com",
        "Search Query: How to set up a secure server",
        "WiFi SSID: CoffeeShop_Open_WiFi",
        "IP Address: 10.0.0.25",
        "Messages: See you at 7 PM!",
        "App Usage: Instagram - 30 minutes today",
        "Recent Purchases: Wireless Headphones, Travel Backpack"
      ]
    };
  },
  computed: {
    displayedData() {
      return this.vpnEnabled ? this.encryptData() : this.rawData;
    }
  },
  methods: {
    encryptData() {
      return this.rawData.map(data => this.scrambleText(data));
    },
    scrambleText(text) {
      // Shift each character by 3 values just for educational purposes to demonstrate encryption
      return text
        .split('')
        .map(char => String.fromCharCode(char.charCodeAt(0) + 3)) 
        .join('');
    }
  }
};
</script>

<style scoped>
.main-container {
  display: flex;
  justify-content: space-between;
  padding: 40px;
  max-width: 1400px;
  margin: 0 auto;
  gap: 30px;
  flex-wrap: wrap;
}

.vpn-container {
  flex: 1;
  max-width: 45%;
  background-color: #fff;
  padding: 25px;
  border-radius: 8px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}

.toggle-switch {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  margin-bottom: 16px;
  cursor: pointer;
  color: black;
}

.toggle-switch input {
  display: none;
}

.slider {
  width: 40px;
  height: 20px;
  background: gray;
  border-radius: 10px;
  position: relative;
  transition: 0.3s;
}

.slider::before {
  content: "";
  width: 18px;
  height: 18px;
  background: white;
  border-radius: 50%;
  position: absolute;
  top: 1px;
  left: 2px;
  transition: 0.3s;
}

.toggle-switch input:checked + .slider {
  background: #10b981;
}

.toggle-switch input:checked + .slider::before {
  transform: translateX(20px);
}

.data-list {
  list-style: none;
  padding: 0;
  color: black;
}

.data-list li {
  padding: 8px;
  border-bottom: 1px solid #ddd;
  color: black;
}

.text-container {
  flex: 1;
  max-width: 45%;
  background-color: #fff;
  padding: 25px;
  border-radius: 8px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}

.text-container h1 {
  font-size: 2.2rem;
  margin-bottom: 20px;
  color: #2c3e50;
}

.text-container h2 {
  font-size: 1.6rem;
  margin-top: 30px;
  color: #34495e;
}

.text-container p,
.text-container li {
  font-size: 1.1rem;
  margin-bottom: 10px;
  line-height: 1.6;
  color: #000;
  font-family: 'Arial', sans-serif;
}

@media (max-width: 768px) {
  .main-container {
    flex-direction: column;
  }

  .vpn-container,
  .text-container {
    max-width: 100%;
  }
}
</style>
