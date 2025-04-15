<template>
  <Navbar />
  <div class="about-page">
    <h1>About Us</h1>
    
    <section class="about-section">
      <h2>Our Mission</h2>
      <p>At ThreatSecure, we’re here to help ROCU officers deliver impactful training using engaging demos and hands-on resources. Our goal is to support law enforcement in providing practical cybersecurity training that truly makes a difference. We know that protecting against cyber threats can be challenging, which is why our platform offers everything ROCU officers need to teach real-world security practices. With ThreatSecure, we make training easier, more effective, and ready to tackle today’s digital risks.</p>
    </section>

    <section class="about-section">
      <h2>Who We Are</h2>
      <p>We’re a team of passionate security experts, developers, and seasoned officers dedicated to creating practical educational tools for ROCU officers. Our mission is to provide a straightforward platform that gives officers everything they need to teach employees how to stay safe online. With our firsthand experience of the challenges in cybersecurity, we’re here to make sure you have all the right information to protect yourself in the digital world.</p>    </section>

    <section class="about-section">
      <h2>What We Offer</h2>
      <p>ThreatAware offers a range of tools designed to suuport officers:</p>
      <ul>
        <li>Password Guidance: Educational demos about password security</li>
        <li>Data Breaches: A guide through data breaches, what happens and where data ends up</li>
        <li>Phishing: The powerful tool hackers use to trick individuals into revealing sensitive information</li>
        <li>CVEs: Software vulnerabilities and what they mean for individuals.</li>
      </ul>

      <p>Contact our team to find out more</p>

    </section>

    <section class="about-section">
      <h2>Our Commitment</h2>
      <p>We’re dedicated to constantly improving our platform and staying ahead of new security threats. Your safety is our top priority, and we’re always working to provide you with the best protection training.</p>    </section>

    <section class="about-section">
      <h2>Contact Us</h2>
      <p>If you have any questions, feedback, or need assistance, please don't hesitate to reach out to us. We are here to help you stay secure.</p>
      <p>Email: support@mysecure.com</p>
      <p>Phone: 0121 604 3728</p>
    </section>
  </div>
</template>

<script>
import Navbar from "../components/Navbar.vue";

export default {
  components: {
    Navbar,
  },
  name: "AboutUsPage",
};
</script>

<style scoped>
.about-page {
  width: 1200px;
  margin: 0 auto;
  padding: 20px;
  background: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

h1 {
  text-align: center;
  color: #333;
  margin-bottom: 30px;
}

.about-section {
  background: white;
  padding: 15px;
  margin-bottom: 15px;
  border-radius: 6px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

h2 {
  color: #0066cc;
}

p {
  color: #555;
  line-height: 1.6;
}

ul {
  color: #555;
  line-height: 1.6;
  padding-left: 20px;
}

ul li {
  margin-bottom: 10px;
}
</style>
