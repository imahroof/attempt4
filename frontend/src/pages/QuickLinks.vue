<template>
    <div class="container">

          <!-- Quick links for ROCU officer  -->

      <h1 class="header">Cyber Security Resources</h1>
      <div class="card-container">
        <div v-for="(link, index) in links" :key="index" class="card">
          <a :href="link.url" target="_blank" class="card-link">
            <h2 class="card-title">{{ link.title }}</h2>
          </a>
          <p class="card-description">{{ link.description }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  //Links
  const links = [
    { title: "ROCU", description: "Regional Organised Crime Unit – Local cybercrime reporting and support.", url: "https://www.ncsc.gov.uk/information/regional-organised-crime-units-rocus" },
    { title: "West Midlands Cyber Resilience Centre", description: "Helping businesses become more cyber resilient in the West Midlands.", url: "https://www.wmcrc.co.uk/" },
    { title: "Action Fraud", description: "Report cybercrime and fraud in the UK.", url: "https://www.actionfraud.police.uk/" },
    { title: "Phishing Report (NCSC)", description: "Report phishing emails to the UK's NCSC.", url: "https://www.ncsc.gov.uk/section/about-this-website/report-scam-website" },
    { title: "National Cyber Security Centre (NCSC)", description: "Official UK government cybersecurity guidance and support.", url: "https://www.ncsc.gov.uk/" },
    { title: "Cyber Aware (NCSC)", description: "Advice on protecting yourself and businesses from cyber threats.", url: "https://www.ncsc.gov.uk/cyberaware/home" },
    { title: "Cyber Essentials", description: "Government-backed certification to protect against cyber threats.", url: "https://www.ncsc.gov.uk/cyberessentials/overview" },
    { title: "FCA Scam Reporting", description: "Report financial scams to the Financial Conduct Authority.", url: "https://www.fca.org.uk/consumers/report-scam-unauthorised-firm" },
    { title: "ICO – Information Commissioner's Office", description: "Report data breaches and learn about GDPR.", url: "https://ico.org.uk/" },
    { title: "Cyber Security Information Sharing Partnership (CiSP)", description: "A platform for businesses to share cyber threat intelligence.", url: "https://www.ncsc.gov.uk/section/keep-up-to-date/cisp" },
    { title: "Police CyberAlarm", description: "A free tool from UK police to help businesses identify and monitor cyber threats.", url: "https://www.cyberalarm.police.uk/" },
    { title: "CyberFirst (NCSC)", description: "Cyber security learning programs and career opportunities for young people.", url: "https://www.ncsc.gov.uk/section/education-skills/cyberfirst" },
    { title: "Take Five to Stop Fraud", description: "A national campaign offering practical advice to help prevent financial fraud.", url: "https://www.takefive-stopfraud.org.uk/" }
  ];
  </script>
  
  <style scoped>
  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    background-color: #f5f5f5;
    min-height: 110vh;
    width: 1300px;
  }
  
  .header {
    font-size: 2rem;
    font-weight: bold;
    color: #1e3a8a;
    margin-bottom: 60px;
    margin-top: 100px;
    text-align: center;
  }
  
  .card-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 20px;
    max-width: 1200px;
    width: 100%;
  }
  
  .card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
  }
  
  .card:hover {
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
  }
  
  .card-link {
    text-decoration: none;
  }
  
  .card-title {
    font-size: 1.1rem;
    color: #1e40af;
    font-weight: 600;
    text-align: center;
  }
  
  .card-title:hover {
    text-decoration: underline;
    color: #2563eb;
  }
  
  .card-description {
    font-size: 0.9rem;
    color: #555555;
    margin-top: 10px;
    text-align: center;
  }
  </style>
  