<template>
  <Navbar />
  <div class="page-container">

    <!-- Social Profile -->
    <div class="profile-container">
      <div class="profile-header">
        <img src="/images/pfp.jpeg" alt="Profile Picture" class="profile-pic" />
        <div class="profile-info">
          <h1 class="profile-name">{{ user.name }}</h1>
          <p class="profile-bio">{{ user.bio }}</p>
        </div>
      </div>
      <div class="profile-details">
        <p><strong>Location:</strong> {{ user.location }}</p>
        <p><strong>Interests:</strong> {{ user.interests.join(', ') }}</p>
        <p><strong>Joined:</strong> {{ user.joined }}</p>
      </div>
      <div class="profile-posts">
        <h2>Recent Posts</h2>
        <div v-for="post in user.posts" :key="post.id" class="post">
          <p>{{ post.content }}</p>
          <small>{{ post.date }}</small>
        </div>
      </div>
    </div>

    <!-- Educational Content -->
    <div class="text-container">
      <h1>Digital Footprint </h1>
      <ul>
        <li>Your DF is your online prescense, you should limit this</li>
        <li>Analyse your profiles and limit the amount of personal information </li>
        <li>Even slight hints can be constantly</li>
        <li>Social engineering is one of the top methods to gain sensitive data</li>
        <li>Intimidation should not pressure you to reveal sensitive data, always double check!</li>
        <li>What information can we find out from this profile?</li>
      </ul>

      <h2>Spear Phishing</h2>
      <ul>
        <li>Another form of phishing, used to target individuals</li>
        <li>Profession shown here, LinkedIn profile?</li>
        <li>Emails crafted specifically for him, likely to fall for them </li>
        <li>"The Weakest Link"</li>
        <li>What emails would you craft to trick this individual?</li>
        <li>Only takes one target out of hundred in a company</li>
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
      //User profile
      user: {
        name: "John Doe",
        bio: "Cybersecurity enthusiast and software developer.",
        location: "Birmingham, United Kingdom",
        interests: ["Cybersecurity", "Football", "Music", "Travel"],
        joined: "January 2023",
        posts: [
          { id: 1, content: "Happy birthday to me!", date: "March 25, 2025" },
          { id: 2, content: "Alice's first birthdays today! It's nearly mine too. I hope she has been saving her money ha", date: "February 12, 2025" },
          { id: 3, content: "The traffic in Hall Green is horrible, takes me 30 mins to get to work when it should take me 10!", date: "January 18, 2025" },
          { id: 4, content: "Exploring new cybersecurity vulnerabilities!", date: "March 15, 2025" }
        ]
      }
    };
  },
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

.profile-container {
  flex: 1;
  max-width: 45%;
  background-color: #fff;
  padding: 25px;
  border-radius: 8px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
  overflow-y: auto;
  height: 680px; 
}

.profile-header {
  display: flex;
  align-items: center;
  gap: 15px;
  padding: 15px;
  border-bottom: 2px solid #ddd;
}

.profile-pic {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  border: 4px solid #fff;
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.2);
}

.profile-info {
  flex-grow: 1;
  text-align: left;
}

.profile-name {
  margin: 0;
  font-size: 26px;
  font-weight: bold;
  color: #333;
}

.profile-bio {
  color: #555;
  font-style: italic;
}

.profile-details {
  margin-top: 15px;
  background: white;
  padding: 15px;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.profile-posts {
  margin-top: 20px;
}

.profile-posts h2 {
  color: #333;
}

.post {
  background: white;
  padding: 12px;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  margin-bottom: 10px;
}

.post p {
  margin: 0;
  font-size: 16px;
  color: #444;
}

.post small {
  display: block;
  margin-top: 5px;
  color: #888;
  font-size: 12px;
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

  .profile-container,
  .text-container {
    max-width: 100%;
  }
}
</style>
