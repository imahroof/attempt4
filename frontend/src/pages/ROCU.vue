<template>
  <Navbar />
  <div class="main-container">
    
    <!-- ROCU Map -->
    <div class="map-container">
      <img src="/images/ROCU.jpeg" alt="Map of ROCU regions" class="map-image" />
    </div>

    <!-- Informative ROCU content -->
    <div class="text-container">
      <h1>Regional Organised Crime Unit (ROCU)</h1>
      <ul>
        <li>ROCU is a collaborative network of 10 units across the UK.</li>
        <li>We operate regionally—supporting national efforts and enhancing local force capabilities.</li>
        <li>Three key departments: <strong>Protect</strong>, <strong>Prepare</strong>, and <strong>Pursue</strong>.</li>
        <li> Work alongside international law enforcement agencies to combat serious and organised crime.</li>
        <li>Our cyber teams respond to incidents and provide free training and awareness for organisations.</li>
      </ul>

      <h2>Why we are here</h2>
      <p>
        ROCU is here to safeguard communities and organisations from the growing threat of cyber crime and organised crime. Today we are here to help you understand the latest cyber threats, how to mitigate them, and how to respond to an attack.
      </p>
    </div>
  </div>
</template>

<script>
import Navbar from '../components/Navbar.vue';

export default {
  components: {
    Navbar
  },
  name: "MapAndTextPage",
};
</script>

<style scoped>
.main-container {
  display: flex;
  justify-content: center;
  gap: 30px;
  padding: 40px;
  width: 100%;
  max-width: 1400px;
  background-color: #f9f9f9;
  min-height: 80vh;
  align-items: center;
  flex-wrap: wrap;
  border-radius: 12px;
  margin: 0 auto;
}

.map-container {
  flex: 1;
  max-width: 45%;
  height: 510px;
  background-color: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease-in-out;
}

.map-image {
  width: 100%;
  height: auto;
  border-radius: 8px;
}

.text-container {
  flex: 1;
  max-width: 45%;
  background-color: #fff;
  padding: 25px;
  border-radius: 8px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease-in-out;
  overflow: hidden;
}

.text-container h1 {
  color: #2c3e50;
  font-size: 2.5rem;
  margin-bottom: 20px;
  font-family: 'Arial', sans-serif;
}

.text-container h2 {
  color: #34495e;
  font-size: 1.8rem;
  margin-bottom: 15px;
  font-family: 'Arial', sans-serif;
}

.text-container p {
  color: #000000;
  line-height: 1.8;
  font-size: 1.1rem;
  margin-bottom: 15px;
  font-family: 'Arial', sans-serif;
}

li {
  color: #000000;
  line-height: 1.6;
  font-size: 1.1rem;
  margin-bottom: 10px;
  font-family: 'Arial', sans-serif;
}

@media (max-width: 768px) {
  .page-container {
    flex-direction: column;
    gap: 20px;
    padding: 20px;
  }

  .map-container,
  .text-container {
    max-width: 100%;
  }
}
</style>
