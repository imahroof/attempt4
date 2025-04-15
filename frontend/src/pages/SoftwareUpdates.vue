<template>
  <Navbar />
  <div class="main-container">

    <!-- Live CVE Data -->
    <div class="api-container">
      <h2 class="api-title">Live CVE Vulnerabilities</h2>
      
      <ul v-if="cveList.length" class="cve-list">
        <li v-for="(cve, index) in cveList" :key="index" class="cve-item">
          <h3 class="cve-title">{{ cve.id }}</h3>
          <p class="cve-description">{{ getCveDescription(cve) }}</p>
          <p class="cve-date"><strong>Published:</strong> {{ formatDate(cve.published) }}</p>
          <p class="cve-date"><strong>Last Modified:</strong> {{ formatDate(cve.lastModified) }}</p>
          <a
            :href="`https://nvd.nist.gov/vuln/detail/${cve.id}`"
            target="_blank"
            class="cve-link"
          >View Full Details</a>
        </li>
      </ul>

      <p v-else>No current CVE vulnerabilities found.</p>
    </div>

    <!-- Educational Content -->
    <div class="text-container">
      <h1>What Are CVEs?</h1>
      <ul>
        <li>CVEs (Common Vulnerabilities & Exposures) are unique identifiers for known security vulnerabilities</li>
        <li>Standardising CVEs helps different tools and databases refer to the same issue</li>
        <li>Cybercriminals often exploit known CVEs to breach systems.</li>
        <li>ALL updates will provide the vulnerablities in software and what is being patched</li>
        <li>Staying updated and patching your systems is key to protecting against these threats.</li>
      </ul>

      <h2>Software Updates</h2>
      <ul>
        <li>Subscribe to CVE feeds and vulnerability alerts.</li>
        <li>Regular updates help fix known security holes.</li>
        <li>Keep backups in place before major software updates.</li>
        <li>Apply security patches promptly to reduce risk.</li>
        <li>Technical teams should update all systems and nodes on a server</li>
      </ul>
    </div>

  </div>
</template>

<script>
import Navbar from "../components/Navbar.vue";
import axios from "axios";

export default {
  components: {
    Navbar
  },
  data() {
    return {
      cveList: []
    };
  },
  async mounted() {
    await this.fetchCveData();
  },
  methods: {
    // Fetch CVE data 
    async fetchCveData() {
      try {
        const response = await axios.get("http://localhost:8000/api/fetch-cves/");
        this.cveList = response.data.vulnerabilities.map(item => item.cve) || [];
      } catch (error) {
        console.error("Failed to fetch CVE data:", error);
        this.cveList = [];
      }
    },

    // retrieve description otherwise show none
    getCveDescription(cve) {
      const description = cve.descriptions.find(desc => desc.lang === 'en');
      return description ? description.value : "No description available.";
    },

    // Format date strings into a readable format
    formatDate(dateString) {
      if (!dateString) return "Unknown";
      const date = new Date(dateString);
      return date.toLocaleString();
    }
  }
};
</script>

<style scoped>
.main-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: flex-start;
  padding: 40px;
  margin: 0 auto;
  max-width: 1400px;
  min-height: 80vh;
  background-color: #f9f9f9;
  border-radius: 12px;
  gap: 30px;
}

.api-container {
  flex: 1;
  max-width: 45%;
  background-color: #fff;
  padding: 25px;
  border-radius: 8px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
  height: 680px;
  overflow-y: auto;
}

.api-title {
  font-size: 1.8rem;
  margin-bottom: 20px;
  color: #c0392b;
}

.cve-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.cve-item {
  padding: 15px;
  margin-bottom: 15px;
  background-color: #fef6f6;
  border-left: 5px solid #c0392b;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  text-align: left;
}

.cve-title {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 5px;
  color: #c0392b;
}

.cve-description {
  font-size: 14px;
  color: #333;
}

.cve-date {
  font-size: 12px;
  color: #777;
}

.cve-link {
  display: inline-block;
  margin-top: 8px;
  font-size: 14px;
  color: #c0392b;
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

.text-container li {
  font-size: 1.1rem;
  line-height: 1.6;
  color: #000;
  font-family: 'Arial', sans-serif;
  margin-bottom: 10px;
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
