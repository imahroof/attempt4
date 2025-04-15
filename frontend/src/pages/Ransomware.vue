<template>
  <Navbar />
  <div class="page-container">

    <!-- API Data Container (Left) -->
    <div class="api-container">
      <h2 class="api-title">Recent Ransomware Attacks LIVE</h2>
      <ul v-if="recentAttacks.length" class="attack-list">
        <li v-for="(attack, index) in recentAttacks" :key="index" class="attack-item">
          <p><strong>{{ attack.post_title }}</strong> - {{ formatDate(attack.discovered) }}</p>
          <p><strong>Attacking Group:</strong> {{ attack.group_name || "Unknown" }}</p>
          <p v-if="attack.description">{{ attack.description }}</p>
          <a v-if="attack.link" :href="attack.link.startsWith('http') ? attack.link : `https://www.ransomlook.io/recent`" target="_blank">View More</a>
        </li>
      </ul>
      <p v-else>No recent attacks found.</p>
    </div>

    <!-- Text Container (Right) -->
    <div class="text-container">
      <h1>Ransomware</h1>
      <ul>
        <li>The leading threats in businesses</li>
        <li>In 2023, ransomware attacks resulted in data encryption in 70% of cases, 59% of organizations reported being hit, and 67% of those organizations paid their ransom using insurance</li>
        <li>Data is never guaranteed...</li>
        <li>Hackers use backdoors, default passwords, crack simple passwords</li>
        <li>DO NOT PAY THE RANSOM, negotiating with hackers is dangerous</li>
        <li>Systems will need to be replaced/wiped</li>
      </ul>

      <h2>Data Leak</h2>
      <ul>
        <li>Hackers will order a ransom to be paid</li>
        <li>A Proof of Life document will be shown</li>
        <li>Law enforcement should be notified as well as the ICO</li>
        <li>If not notified, a fine could be issued</li>
        <li>Do not engage with hackers</li>
        <li>Data is leaked and posted onto the dark web</li>
      </ul>
    </div>

  </div>
</template>

<script>
import Navbar from '../components/Navbar.vue';
import axios from 'axios';

export default {
  components: {
    Navbar
  },
  data() {
    return {
      recentAttacks: []
    };
  },
  async mounted() {
    //update with the most recent attacks
    await this.fetchRecentAttacks();
  },
  methods: {
    //RansomLook API
    async fetchRecentAttacks() {
      try {
        const response = await axios.get("http://localhost:8000/api/fetch-ransomware-attacks/");
        this.recentAttacks = response.data || [];
      } catch (error) {
        console.error('Error fetching recent attacks:', error);
        this.recentAttacks = [];
      }
    },
    //Date formated to be readable for the audience
    formatDate(dateString) {
      if (!dateString) return "Unknown";
      const date = new Date(dateString);
      return date.toLocaleString();
    }
  }
};
</script>

<style>
.page-container {
  display: flex;
  justify-content: space-between;
  padding: 40px;
  width: 100%;
  max-width: 1400px;
  background-color: #f9f9f9;
  min-height: 80vh;
  align-items: flex-start;
  border-radius: 12px;
  margin: 0 auto;
  gap: 30px;
  flex-wrap: wrap;
}

.api-container {
  flex: 1;
  max-width: 45%;
  background-color: #fff;
  padding: 25px;
  border-radius: 8px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
  overflow-y: auto;
  height: 680px; 
}

.api-title {
  font-size: 1.8rem;
  margin-bottom: 20px;
  color: #d63031;
}

.attack-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.attack-item {
  background-color: #ffe6e6;
  padding: 15px;
  border-radius: 8px;
  margin-bottom: 15px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.attack-item a {
  color: #d63031;
  text-decoration: underline;
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
  .page-container {
    flex-direction: column;
  }

  .api-container,
  .text-container {
    max-width: 100%;
  }
}
</style>
