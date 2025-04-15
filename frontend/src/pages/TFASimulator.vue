<template>
  <Navbar />
  <div class="page-container">

    <!-- Two Factor Authentication DEMO -->
    <div class="otp-container">
      <h1>Live 2FA Demo</h1>
      <input v-model="username" placeholder="Username" />
      <input v-model="password" type="password" placeholder="Password" />
      
      <button class="toggle-otp-button" @click="toggleOTPVisibility">{{ otpVisible ? 'Hide OTP' : 'Show OTP' }}</button>
      
      <div v-if="otpVisible">
        <p>Your OTP Code:</p>
        <div class="otp">{{ otp || "------" }}</div>
        <button class="generate-otp-button" @click="generateOTP">Generate OTP</button>
        <input v-model="enteredOTP" placeholder="Enter OTP" />
        <button class="verify-otp-button" @click="verifyOTP">Verify OTP</button>
        <p v-if="message" :class="{ 'error': !isCorrect, 'success': isCorrect }">{{ message }}</p>
      </div>
      
      <button class="back-button" @click="goBack">Back</button>
    </div>

    <!-- Educational Content -->
    <div class="text-container">
      <h1>Two Factor Authentication</h1>
      <ul>
        <li>Should be used on all your accounts!</li>
        <li>Adds a layer of protection for your account</li>
        <li>Prevents unauthorised access EVEN IF your password is comprimised</li>
        <li>Most major services support 2FA</li>
        <li>Can act as an alert system, alerting you when someone is trying to gain access</li>
        <li>Adds peace of mind, can save you from a lot of stress</li>
      </ul>

      <h2>Applications that offer 2FA</h2>
      <ul>
        <li>Major services that offer 2FA include:</li>
        <li>Google</li>
        <li>Microsoft</li>
        <li>Social Media platforms</li>
        <li>Email clients</li>
        <li>E - commerce platforms</li>
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
      username: '',
      password: '',
      otp: '',
      enteredOTP: '',
      message: '',
      isCorrect: false,
      otpVisible: true, 
      recentAttacks: []
    };
  },
  methods: {
    //generate a random OTP, just for demo purposes
    generateOTP() {
      const digits = Array.from({ length: 6 }, () => Math.floor(Math.random() * 10));
      this.otp = digits.join('-');
      this.enteredOTP = '';
      this.message = '';
    },
    //username and password DOES NOT matter, matching of codes does, 
    verifyOTP() {
      if (this.enteredOTP === this.otp.replace(/-/g, '')) { //does not need dashes in between codes
        this.isCorrect = true;
        this.message = 'Login successful!';
      } else {
        this.isCorrect = false;
        this.message = 'Invalid OTP. Please try again.';
      }
    },
    toggleOTPVisibility() {
      this.otpVisible = !this.otpVisible;
    },
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

.otp-container {
  flex: 1;
  max-width: 45%;
  background-color: #fff;
  padding: 25px;
  border-radius: 8px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
  overflow-y: auto;
  height: 680px; /* Adjust the height to your needs */
}

h1 {
  font-size: 1.8rem;
  margin-bottom: 20px;
  color: #2c3e50;
}

.otp-box {
  text-align: center;
  margin-bottom: 30px;
}

input {
  width: 95%;
  padding: 10px;
  margin-top: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
}

button {
  color: white;
  border: none;
  padding: 10px;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 10px;
  width: 100%;
  font-size: 16px;
}

button.toggle-otp-button {
  background: #007bff;
}

button.generate-otp-button {
  background: #ffc107;
}

button.verify-otp-button {
  background: #28a745;
}

button.back-button {
  background: #626d77;
  width: 30%;
  margin-top: 20px;
}

button:hover {
  opacity: 0.9;
}

button.toggle-otp-button:hover {
  background: #0056b3;
}

button.generate-otp-button:hover {
  background: #218838;
}

button.verify-otp-button:hover {
  background: #e0a800;
}

button.back-button:hover {
  background: #5a6268;
}

.otp {
  font-size: 24px;
  color: black;
  font-weight: bold;
  background: #eee;
  padding: 10px;
  border-radius: 5px;
  margin-bottom: 15px;
}

.error {
  color: red;
  font-weight: bold;
}

.success {
  color: green;
  font-weight: bold;
}

/* Text Container */
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

/* Media Queries */
@media (max-width: 768px) {
  .page-container {
    flex-direction: column;
  }

  .otp-container,
  .text-container {
    max-width: 100%;
  }
}
</style>
