<template>
  <Navbar />
  <div class="main-container">

     <!-- Have i been pwned api -->

    <div class="password-check-container">
      <h2>Check Password Against Have I Been Pwned</h2>
      <input v-model="passwordToCheck" placeholder="Enter password to check" />
      <button @click="checkPassword">Check Password</button>
      <p v-if="pwnedStatus !== null" :class="statusClass">{{ pwnedStatus }}</p>
      <p v-if="breachCount" class="analogy">{{ analogy }}</p>

      <h2>Random Password Generator</h2>
      <button @click="generatePassword" class="generate-btn">Generate Password</button>
      <p v-if="password" class="generated-password">Generated Password: {{ password }}</p>
    </div>

    <!-- Educational content -->


    <div class="text-container">
      <h1>Passwords</h1>
      <ul>
        <li>Password strength is the difference between becoming a target or remaining a safe individual</li>
        <li>Easy and generic passwords can easily be hacked or even guessed</li>
        <li>AI is throttling the rate at which passwords can be figured out</li>
        <li>Password requirements that you are used to are not safe</li>
        <li>Hackers compare hashes with rainbow tables and find a match for your password</li>
      </ul>

      <h2>Three Random Words</h2>
      <ul>
        <li>Old password requirements are not safe anymore</li>
        <li>It is not hard to break these passwords</li>
        <li>Government guidance is to use three random words</li>
        <li>Statistically harder to crack than standard passwords</li>
        <li>But still easy to remember your password!</li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import sha1 from "sha1";
import Navbar from "../components/Navbar.vue";

export default {
  components: { Navbar },
  data() {
    return {
      passwordToCheck: "",
      pwnedStatus: null,
      statusClass: "",
      breachCount: null,
      analogy: "",
      password: ""
    };
  },
  methods: {
    async checkPassword() {
      if (!this.passwordToCheck) {
        this.pwnedStatus = "Please enter a password to check.";
        this.statusClass = "";
        return;
      }
      
      //hash the password, seperate prefix and suffixes
      const hashedPassword = sha1(this.passwordToCheck);
      const prefix = hashedPassword.substring(0, 5);
      const suffix = hashedPassword.substring(5);

      //check against api

      try {
        const response = await axios.get(`https://api.pwnedpasswords.com/range/${prefix}`);
        const hashes = response.data.split("\r\n");
        const match = hashes.find((hash) => hash.toLowerCase().startsWith(suffix.toLowerCase()));

        if (match) {
          this.breachCount = parseInt(match.split(":")[1]);
          this.pwnedStatus = `This password has been pwned ${this.breachCount} times.`;
          this.statusClass = "pwned";
          this.setAnalogy();
        } else {
          this.pwnedStatus = "This password has not been pwned.";
          this.statusClass = "not-pwned";
          this.analogy = "";
        }
      } catch (error) {
        console.error("Error checking password:", error);
        this.pwnedStatus = "Error checking password.";
        this.statusClass = "";
        this.analogy = "";
      }
    },

    //Generaate a random password with three words
    async generatePassword() {
      try {
        const words = await this.fetchRandomWords(3);
        this.password = words.map((word) => this.capitalizeWord(word)).join("");
      } catch (error) {
        console.error("Error fetching random words:", error);
      }
    },

    //Generate 3 random words to demonstrate in HIBP API
    async fetchRandomWords(number) {
      try {
        const response = await axios.get(`https://random-word-api.herokuapp.com/word?number=${number}`);
        return response.data;
      } catch (error) {
        console.error("Error fetching random words:", error);
        throw error;
      }
    },

    //Easy to read for the audience is the words are capitalised
    capitalizeWord(word) {
      return word.charAt(0).toUpperCase() + word.slice(1);
    },

    //Analogys for shock element of the delievery

    setAnalogy() {
      if (this.breachCount <= 10) {
        this.analogy = "Your password is relatively safe.";
      } else if (this.breachCount <= 50) {
        this.analogy = "Your password could be cracked faster than you can say 'oops'.";
      } else if (this.breachCount <= 100) {
        this.analogy = "This password has been pwned more times than most passwords. It’s a target!";
      } else if (this.breachCount <= 500) {
        this.analogy = "This password is a hacker's dream. It could be cracked in a heartbeat.";
      } else if (this.breachCount <= 1000) {
        this.analogy = "This password is practically a public secret. Better change it ASAP!";
      } else {
        this.analogy = "This password is like a broken lock!";
      }
    }
  }
};
</script>

<style>
.main-container {
  display: flex;
  justify-content: space-between;
  padding: 40px;
  margin: 0 auto;
  max-width: 1400px;
  min-height: 80vh;
  background-color: #f9f9f9;
  border-radius: 12px;
  gap: 30px;
}

.password-check-container,
.text-container {
  flex: 1;
  max-width: 45%;
  background-color: #fff;
  padding: 25px;
  border-radius: 8px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}

h2, h1 {
  font-size: 1.8rem;
  margin-bottom: 40px;
  color: #333;
}

button {
  padding: 12px 25px;
  font-size: 1.2em;
  cursor: pointer;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  transition: background-color 0.3s ease;
  width: 100%;
  margin-top: 20px;
}

button:hover {
  background-color: #0056b3;
}

input {
  padding: 12px;
  font-size: 1em;
  margin-top: 20px;
  width: 100%;
  border-radius: 5px;
  border: 1px solid #ddd;
  box-sizing: border-box;
}

input:focus {
  outline: none;
  border-color: #007bff;
}

.pwned {
  color: #d9534f;
}

.not-pwned {
  color: #28a745;
}

.generated-password {
  color: #28a745;
  font-size: 1.2em;
}

.generate-btn {
  width: auto;
  padding: 12px 25px;
  font-size: 1.2em;
  margin-top: 20px;
  background-color: #28a745;
  border-radius: 5px;
}

.generate-btn:hover {
  background-color: #218838;
}

.text-container li {
  font-size: 1.1rem;
  line-height: 1.6;
  color: #000;
  font-family: 'Arial', sans-serif;
  margin-bottom: 10px;
}

@media (max-width: 768px) {
  .main-container {
    flex-direction: column;
  }

  .password-check-container,
  .text-container {
    max-width: 100%;
  }
}
</style>
