<template>
  <div class="quiz-container">
    <Navbar />
    <h1>Phishing Email Quiz</h1>

    <!-- Email template -->
    <div v-if="currentEmail" class="email-container">
      <p><strong>From:</strong> {{ currentEmail.sender }} </p>
      <p><strong>To:</strong> {{ currentEmail.receiver }}</p>
      <p><strong>Subject:</strong> {{ currentEmail.subject }}</p>
      <p><strong>Email:</strong></p>
      <p>{{ currentEmail.text }}</p>

      <!-- Phishing or not phishing buttons -->
      <div class="options">
        <button @click="checkAnswer(true)" class="phishing-button">Phishing</button>
        <button @click="checkAnswer(false)" class="notphishing-button">Not Phishing</button>
      </div>

      <!-- Answer -->
      <p v-if="answerGiven">
        <span :class="isPhishing ? 'correct' : 'incorrect'">
          {{ isPhishing ? 'Correct!' : 'Incorrect!' }}
        </span>
      </p>

      <!-- Next Email -->
      <div v-if="answerGiven">
        <button @click="nextEmail" class="next-email-button">Next Email</button>
      </div>
    </div>
    <div v-else>
      <p>Loading quiz...</p>
    </div>
  </div>
</template>

<script>
import Navbar from '../components/Navbar.vue';

export default {
  components: {
    Navbar,
  },

  data() {
    return {
      // Array of emails, can be added to in the future. 
      emails: [
        { 
          sender: "CustomerService@Amazon.com",
          receiver: "rocuuser@ROCU.com",
          subject: "MYSTERY BOX: Claim your mystery box today",
          text: "CLAIM NOW: Your mystery box today. Hurry up before its too late, you may never get this chance again! Click here to redeem: http://Amazion.io/mysterybox23423",
          isPhishing: true
        },
        { 
          sender: "noreply@booking.org",
          receiver: "rocuuser@ROCU.com",
          subject: "Confirm your booking!",
          text: "Reminder: Your booking will expire if you do not log in and reserve it! Log in here to reserve your booking: http://booking.org/confirm123",
          isPhishing: true
        },
        { 
          sender: "n499783To@pansam.net",
          receiver: "rocuuser@ROCU.com",
          subject: "Phone Number added",
          text: "Hi, We've added your phone number ending in 65 to your account, as you asked. Your phone number will be used if you forget your password and for important account messages. Verify your number here to confirm: http://netflix.com/confirmnumberphone89797. Your friends at Netflix",
          isPhishing: true
        },
        {
          sender: "noreply@communcation.paypal.com",
          receiver: "rocuuser@ROCU.com",
          subject: "Welcome to PayPal",
          text: "You've just opened a PayPal account and are set to begin paying with PayPal around the world and sending money to friends.",
          isPhishing: false
        },
        { 
          sender: "TSApp@UB3R.ik",
          receiver: "rocuuser@ROCU.com",
          subject: "Free Ride",
          text: "We are excited to inform you that you have won a complimentary ride with us! To redeem your free ride, simply click on the link below and fill in your details: http://UB3R.com/CLa1M",
          isPhishing: true
        },
        {
          sender: "info@instagram.com",
          receiver: "rocuuser@ROCU.com",
          subject: "Recent Login",
          text: "Hi rocuuser, there was a login attempt at this geographic location: Birmingham. If this was you, you can ignore this. If this wasn't you, please reset your password.",
          isPhishing: false
        }
      ],
      currentEmailIndex: 0, 
      answerGiven: false, 
      isPhishing: false 
    };
  },

  computed: {
    // show email on screen
    currentEmail() {
      return this.emails[this.currentEmailIndex];
    }
  },

  methods: {
    // Checks if correct
    checkAnswer(answer) {
      this.answerGiven = true; 
      this.isPhishing = answer === this.currentEmail.isPhishing; 
    },

    // load the next email
    nextEmail() {
      this.answerGiven = false; 
      if (this.currentEmailIndex < this.emails.length - 1) {
        this.currentEmailIndex++;
      } else {
        alert("Congratulations! You've completed the quiz."); 
        this.currentEmailIndex = 0; 
      }
    }
  }
};
</script>

<style scoped>
.quiz-container {
  text-align: center;
  font-size: 1.2em;
  padding: 20px;
  background-color: white;
  color: black;
}

h1 {
  font-size: 2rem;
}

.email-container {
  padding: 20px;
  border: 1px solid #ccc;
  margin-bottom: 20px;
  background-color: #f9f9f9;
}

.email-container p {
  margin: 10px 0;
}

.options button {
  margin: 10px;
  padding: 10px 20px;
  font-size: 1rem;
  margin-top: 20px;
  cursor: pointer;
}

.correct {
  color: green;
}

.incorrect {
  color: red;
}

button {
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 1rem;
  margin-top: 90px;
  width: 50%;
}

button:hover {
  background-color: #45a049;
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.phishing-button {
  background-color: #d9534f;
}

.notphishing-button {
  background-color: #5cb85c;
}

.next-email-button {
  background-color: #5bc0de;
}
</style>
