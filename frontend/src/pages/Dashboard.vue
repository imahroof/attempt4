<template>
  <Navbar />

  <div class="dashboard">
    <!-- If no dashboard is selected, show the portal -->
    <div v-if="!selectedDashboard">
      
      <!-- Portal information -->
      <div class="dashboard-header">
        <h1>Your Portal</h1>
        <p>Welcome to your cybersecurity training dashboards.</p>
        <p>Here you can create and manage your upcoming deliveries to prepare impactful demos for your clients.</p>
        <p>If you encounter any issues, please contact our support team.</p>
        <p>Email: support@mysecure.com</p>
        <p>Phone: 0121 604 3728</p>

        <h2 style="margin-top: 30px;">Your Upcoming Deliveries</h2>
      </div>

      <!-- Delivery stats -->
      <div class="delivery-stats">
        <p><strong>Total Deliveries:</strong> {{ totalDeliveries }}</p>
        <p><strong>Next Delivery:</strong> 
          {{ nextDelivery ? nextDelivery.name : 'None' }} at 
          {{ nextDelivery ? new Date(nextDelivery.deliveryTime).toLocaleString() : '' }}
        </p>
      </div>

      <!-- Search bar -->
      <input 
        type="text" 
        style="margin-top: 50px;" 
        v-model="searchQuery" 
        placeholder="Search for deliveries" 
        class="search-bar" 
      />

      <button @click="showDashboardForm = true" class="add-dashboard-button">Add Dashboard</button>

      <!-- Showing completed deliveries -->
      <label class="button-checkbox">
        <input type="checkbox" v-model="showCompleted" class="button-input" />
        <span class="button-text">Show Completed Deliveries</span>
      </label>

      <!-- Dashboard List -->
      <ul class="dashboard-list">
        <li v-for="dashboard in filteredDashboards" :key="dashboard.id" class="dashboard-item">
          <span @click="selectDashboard(dashboard)" class="dashboard-name">
            {{ dashboard.name }} - {{ new Date(dashboard.deliveryTime).toLocaleDateString() }}
          </span>
          <div class="button-group">
            <!-- Open Button -->
            <button @click="selectDashboard(dashboard)" class="open-dashboard-button button">Open</button>

            <!-- Completed Button -->
            <button @click="completed(dashboard.name)" class="completed-dashboard-button button">Completed</button>

            <!-- Remove Button -->
            <button @click="removeDashboard(dashboard.id, dashboard.name)" class="remove-dashboard-button button">Remove</button>
          </div>
        </li>
      </ul>

      <button @click="logout" class="logout-button">Logout</button>
    </div>

    <!-- Selected Dashboard-->
    <div v-else>
      <div class="dashboard-header">
        <h1>{{ selectedDashboard.name }}</h1>
      </div>

      <!-- Toggle for delivery details -->
      <button @click="showDeliveryDetails = !showDeliveryDetails" class="toggle-details-button">
        {{ showDeliveryDetails ? 'Hide' : 'Show' }} Delivery Details
      </button>

      <div v-if="showDeliveryDetails" class="delivery-details">
        <p><strong>Organisation:</strong> {{ selectedDashboard.organisation }}</p>
        <p><strong>Contact Person:</strong> {{ selectedDashboard.contact }}</p>
        <p><strong>Location:</strong> {{ selectedDashboard.location }}</p>
        <p><strong>Notes:</strong> {{ selectedDashboard.notes }}</p>
        <p><strong>Date and Time:</strong> {{ selectedDashboard.deliveryTime }}</p>

        <div id="map" v-if="selectedDashboard.location" class="map-container"></div>
      </div>

      <!-- Add widget section -->
      <div class="action-buttons">
        <button @click="showWidgetMenu = !showWidgetMenu" class="add-widget-button"> Add Widget</button>
      </div>

      <div v-if="showWidgetMenu" class="widget-add-section">
        <select v-model="selectedWidget" class="widget-dropdown">
          <option disabled value="">Select a widget</option>
          <option v-for="widget in availableWidgets" :key="widget.name" :value="widget">{{ widget.name }}</option>
        </select>
        <button @click="addWidget" class="confirm-add-button">Add</button>
      </div>

      <!-- Widgets display -->
      <div class="dashboard-container">
        <div class="widgets-container">
          <div v-for="(widget, wIndex) in selectedDashboard.widgets" :key="wIndex" class="widget-card">
            <img :src="widget.image" :alt="widget.name" class="widget-image" />
            <button class="widget-button" @click="goTo(widget.route)">{{ widget.name }}</button>
            <button class="delete-widget-button" @click="deleteWidget(wIndex)">Delete</button>
          </div>
        </div>
      </div>

      <button @click="selectedDashboard = null" class="back-button">← Back to Dashboards</button>
      <button @click="logout" class="logout-button">Logout</button>
    </div>

    <!-- Modal for creating a new delivery -->
    <div v-if="showDashboardForm" class="modal">
      <div class="modal-content">
        <h2>Create New Delivery</h2>
        <input v-model="newDashboard.name" placeholder="Dashboard Name" />
        <input v-model="newDashboard.organisation" placeholder="Organisation Name" />
        <input v-model="newDashboard.contact" placeholder="Contact Person" />
        <input v-model="newDashboard.location" placeholder="Location" />
        <input v-model="newDashboard.notes" placeholder="Notes" />
        <input type="datetime-local" v-model="newDashboard.deliveryTime" />
        <button @click="saveDashboard" class="save-button">Save</button>
        <button @click="showDashboardForm = false" class="cancel-button">Cancel</button>
      </div>
    </div>
  </div>
</template>


<script>
//Imports
import Navbar from '../components/Navbar.vue';
import { useAuthStore } from '../store/auth.js';
import { getCSRFToken } from '../store/auth.js';
import axios from 'axios'; 
import L from 'leaflet';
import 'leaflet/dist/leaflet.css'; 

export default {
  components: { Navbar },
  data() {
    return {
      // Dashboard array for objects
      dashboards: [], 
      selectedDashboard: null, 
      availableWidgets: [  //All widgets + paths
        { name: "ROCU", route: "/rocu", image: "/images/ROCUlogo.png" },
        { name: "Quick Links", route: "/quicklinks", image: "/images/links.png" },
        { name: "Ransomware", route: "/ransomware", image: "/images/ransomware.png" },
        { name: "Software Updates", route: "/softwareupdates", image: "/images/softwareupdates.png" },
        { name: "Passwords", route: "/Passwords", image: "/images/passwords.png" },
        { name: "TFA Simulator", route: "/TFASimulator", image: "/images/2fa.png" },
        { name: "Phishing", route: "/Phishing", image: "/images/phishing.png" },
        { name: "Public Wifi / VPN", route: "/vpnsimulator", image: "/images/wifi.png" },
        { name: "Social Engineering", route: "/socialengin", image: "/images/profile.png" },
      ],
      selectedWidget: null, 
      showWidgetMenu: false, 
      showDashboardForm: false, 
      searchQuery: "", 
      showCompleted: false, 
      showDeliveryDetails: true,
      newDashboard: {  
        name: '',
        organisation: '',
        contact: '',
        location: '',
        notes: '',
        deliveryTime: '',
        completed: false
      },
      map: null 
    };
  },
  setup() {
    const authStore = useAuthStore(); 
    return { authStore };
  },
  computed: {
    sortedDashboards() {
      return [...this.dashboards].sort((a, b) => new Date(a.deliveryTime) - new Date(b.deliveryTime)); // Sort dashboards by delivery time
    },
    filteredDashboards() {
      return this.sortedDashboards.filter(dashboard => {
        const query = this.searchQuery.toLowerCase();

        // Check if dashboard matches search query
        const matchesSearch = (
          dashboard.name.toLowerCase().includes(query) ||
          dashboard.organisation.toLowerCase().includes(query) ||
          dashboard.contact.toLowerCase().includes(query) ||
          dashboard.location.toLowerCase().includes(query) ||
          (dashboard.notes || '').toLowerCase().includes(query)
        );

        // Only show dashboards that are completed 
        const matchesCompletion = this.showCompleted || !dashboard.completed;

        // Filter based on both criteria

        return matchesSearch && matchesCompletion;  
      });
    },
    totalDeliveries() {
      return this.dashboards.length;
    },
    nextDelivery() {
      const now = new Date();
      // Upcoming deliveries
      const upcomingDeliveries = this.dashboards.filter(dashboard => new Date(dashboard.deliveryTime) > now);

      if (upcomingDeliveries.length === 0) {
        return null; 
      }

      // Return the earliest delivery
      return upcomingDeliveries.reduce((prev, curr) => {
        return new Date(prev.deliveryTime) - now < new Date(curr.deliveryTime) - now ? prev : curr;
      });
    }
  },
  methods: {
    //Mark delivery as completed
    async completed(name) {
      try {
        const response = await axios.put(
          `http://localhost:8000/dashboardcomplete/`,
          { name, completed: true },  
          {
            headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': getCSRFToken(),
            },
            withCredentials: true, 
          }
        );

        await this.fetchDashboards();  // Refresh
      } catch (error) {
        console.error(error);
      }
    },
    async fetchDashboards() {
      try {
        if (!this.authStore.isAuthenticated) {
          console.error("User is not authenticated.");
          this.$router.push("/login");  // Redirect to login page
          return;
        }

        const response = await axios.get('http://localhost:8000/dashboardget/', {
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken(),
          },
          withCredentials: true,  
        });

        this.dashboards = response.data.map(dashboard => ({
          name: dashboard.Name,
          organisation: dashboard.Organisation,
          contact: dashboard.Contact,
          location: dashboard.Location,
          notes: dashboard.Notes,
          deliveryTime: new Date(dashboard.Date_Time),
          widgets: dashboard.Widgets,
          completed: dashboard.Completed
        }));
      } catch (error) {
        console.error(error);
      }
    },

    selectDashboard(dashboard) {
      this.selectedDashboard = dashboard;
      this.$nextTick(() => {
        this.initMap();  // Show map after dash selected
      });
    },
    // load map
    initMap() {
      this.$nextTick(() => {
        if (this.map) {
          this.map.remove(); 
        }

        if (this.selectedDashboard.location) {
          axios.get(`https://nominatim.openstreetmap.org/search?format=json&q=${this.selectedDashboard.location}`)
            .then(response => {
              if (response.data.length > 0) {
                const { lat, lon } = response.data[0];

                // Initialise Leaflet map
                this.map = L.map('map').setView([lat, lon], 13);

                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(this.map);

                // Add a marker to the map
                L.marker([lat, lon]).addTo(this.map)
                  .bindPopup(this.selectedDashboard.location)
                  .openPopup();
              } else {
                console.error("No results found for location:", this.selectedDashboard.location);
              }
            })
            .catch(
              console.error(error));
        }
      });
    },
    logout() {
      this.$router.push("/home");
      this.authStore.logout();  
    },
    //Save new dashboard
    async saveDashboard() {
      try {
        if (!this.authStore.isAuthenticated) {
          console.error("User is not authenticated.");
          this.$router.push("/login");  
          return;
        }

        const dashboardData = {
          Name: this.newDashboard.name,
          Organisation: this.newDashboard.organisation,
          Contact: this.newDashboard.contact,
          Location: this.newDashboard.location,
          Notes: this.newDashboard.notes,
          Date_Time: new Date(this.newDashboard.deliveryTime).toISOString(),
          Widgets: [],
        };

        const response = await axios.post(
          "http://localhost:8000/dashboardpost/",
          dashboardData,
          {
            headers: {
              "Content-Type": "application/json",
              "X-CSRFToken": getCSRFToken(),
            },
            withCredentials: true,
          }
        );

        this.dashboards.push(response.data);
        this.showDashboardForm = false;  
        this.newDashboard = { name: "", organisation: "", contact: "", location: "", deliveryTime: "" };

        await this.fetchDashboards(); 
      } catch (error) {
        console.error(error);
      }
    },
    //Remove a dashboard
    async removeDashboard(id, name) {
      try {
        const response = await axios.delete(`http://localhost:8000/dashboarddelete/`, {
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken(),
          },
          data: { name },
          withCredentials: true,
        });

        await this.fetchDashboards();  
      } catch (error) {
        console.error(error);
      }
    },
    //Go to the selected widget
    goTo(route) {
      this.$router.push(route);  
    },
    //Add widget to dashboard
    async addWidget() {
      if (this.selectedWidget) {
        this.selectedDashboard.widgets.push(this.selectedWidget); // Add widget to selected dashboard

        try {
          const response = await axios.put(`http://localhost:8000/dashboardaddwidget/`, {
            name: this.selectedDashboard.name,
            widgets: this.selectedDashboard.widgets,
          }, {
            headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': getCSRFToken(),
            },
            withCredentials: true,
          });

          this.selectedWidget = null;
          this.showWidgetMenu = false;  
        } catch (error) {
          console.error(error);
        }
      }
    },
    //Delete widget from dashboard
    async deleteWidget(widgetIndex) {
      const widgetToDelete = this.selectedDashboard.widgets[widgetIndex];

      try {
        const response = await axios.delete(`http://localhost:8000/dashboarddeletewidget/`, {
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken(),
          },
          data: {
            name: this.selectedDashboard.name,
            widget: widgetToDelete,
          },
          withCredentials: true,
        });

        this.selectedDashboard.widgets.splice(widgetIndex, 1);  // Remove widget from list
      } catch (error) {
        console.error(error);
      }
    }
  },
  //Changes in dashboard = refresh map
  watch: {
    showDeliveryDetails(newValue) {
      if (newValue) {
        this.$nextTick(() => {
          this.initMap();  // Refresh the map when delivery details are shown
        });
      }
    },
  },
  mounted() {
    this.fetchDashboards(); // Fetch dashboards when program starts
  }
};
</script>


<style>

.map-container {
  height: 300px;
  width: 100%;
  margin-top: 20px;
  border-radius: 10px;
  overflow: hidden;
  border: 1px solid white;
}

.dashboard-container {
  display: flex;
  justify-content: center;
  width: 100%;
}

.widgets-container {
  display: flex;
  flex-wrap: wrap;
  gap: 30px; 
  justify-content: center; 
  align-items: flex-start;
  padding: 10px;
}

.widget-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 10px;
  border: 1px solid white;
  border-radius: 8px;
  background: white;
  width: 200px;
  text-align: center;
  margin-bottom: 20px; 
}

.widget-image {
  width: 150px;
  height: auto;
  margin-bottom: 10px;
}

.widget-button {
  width: 100%;
  padding: 10px;
  border: none;
  background: blue;
  color: white;
  border-radius: 5px;
  cursor: pointer;
}

.button-card {
  display: flex;
  flex-direction: column;
  align-items: center; 
  justify-content: center; 
  width: 150px; 
  padding: 10px;
  background: white;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.big-button {
  width: 100%; 
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 14px;
  text-align: center;
}

.big-button:hover {
  background-color: #0056b3;
}

.widget-dropdown {
  color: black; 
  background-color: white; 
  border: 1px solid white;
  padding: 10px; 
  font-size: 16px; 
  margin-bottom: 20px;
}

.widget-dropdown option {
  color: black; 
  background-color: white; 
}

.toggle-details-button {
  background: #ffc107;
  width: 30%;
  color: #333;
  padding: 15px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 16px;
  margin-top: 20px;
  margin-bottom: 20px; 
}

.add-dashboard-button {
  padding: 10px 20px;
  background: #28a745;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 16px;
  margin-bottom: 20px;
  margin-top: 20px; 
}
.add-dashboard-button:hover {
  background: #218838;
}

.add-widget-button {
  background: #007bff;  
  color: white;
  padding: 15px;  
  border: none;
  border-radius: 8px;  
  cursor: pointer;
  font-size: 16px;  
  margin-top: 30px;  
  width: 30%;
  margin-bottom: 30px; 
}

.add-widget-button:hover {
  background: #0056b3;  
}

.toggle-details-button:hover {
  background: #e0a800;
}

.confirm-add-button {
  padding: 10px;
  width:30%;
  background: #28a745; 
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 16px;
  margin-top: 20px;
  margin-left: 15px;
}


h2, p{
  color: black;
}

.dashboard {
  background: #eef2f7;
  padding: 40px;
  font-family: 'Arial', sans-serif;
  min-height: 100vh;
  width:70em;
}

.dashboard-header {
  text-align: center;
  margin-bottom: 40px;
  color: #333;
}

.dashboard-list {
  display: flex;
  flex-direction: column;
  gap: 25px; 
  margin-top: 20px;
}

.dashboard-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 15px;
  background: white;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease-in-out;
  margin-bottom: 15px; 
}
.dashboard-item:hover {
  transform: translateY(-3px);
}

.dashboard-name {
  flex-grow: 1;
  font-size: 18px;
  font-weight: bold;
  cursor: pointer;
  color: #007bff;
}

.button-group {
  display: flex;
  gap: 15px; 
}

.open-dashboard-button,
.remove-dashboard-button {
  padding: 10px 15px; 
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 14px;
  transition: background 0.2s;
}

.open-dashboard-button {
  background-color: #007bff;
  color: white;
}
.open-dashboard-button:hover {
  background-color: #0056b3;
}

.remove-dashboard-button {
  background-color: #dc3545;
  color: white;
}
.remove-dashboard-button:hover {
  background-color: #c82333;
}

.logout-button {
  position: fixed;
  width: 100px;
  bottom: 20px;
  right: 20px;
  padding: 10px 20px;
  background-color: #dc3545;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 16px;
}
.logout-button:hover {
  background-color: #c82333;
}


.modal-content {
  background: white;
  padding: 40px;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  gap: 10px; 
  width: 60%;
  max-width: 700px;
  min-height: 350px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.modal-content input {
  width: 100%;  
  padding: 12px; 
  font-size: 16px; 
  border: 1px solid #ccc; 
  border-radius: 5px; 
  margin-bottom: 10px; 
}

.modal-content button {
  padding: 10px 20px;
  color: white;
  border: none;
  border-radius: 8px;
  align-items: center;
  cursor: pointer;
  font-size: 16px;
  width: 40%;
  text-align: center;
  margin-bottom: 10px; 
}

.save-button {
  background: #28a745; 
}

.cancel-button{
  background: #c82333; 
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.delete-widget-button {
  margin-top: 10px;
  padding: 8px 12px;
  background-color: #dc3545;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 14px;
}

.delete-widget-button:hover {
  background-color: #c82333; 
}

.button-checkbox {
  display: inline-block;
  cursor: pointer;
  font-family: Arial, sans-serif;
  font-size: 16px;
  color: #fff;
  background-color: #614caf;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  user-select: none;
  transition: background-color 0.3s ease;
}

.button-input {
  display: none;
}

.button-input:checked + .button-text {
  background-color: #8a8a92; 
}

.button-text {
  display: block;
  text-align: center;
  font-weight: bold;
  pointer-events: none; 
}

.button {
  padding: 10px 15px; 
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 14px;
  transition: background 0.2s;
}

.open-dashboard-button {
  background-color: rgb(0, 94, 255);
  color: white;
}

.open-dashboard-button:hover {
  background-color: #0056b3;
}

.completed-dashboard-button {
  background-color: #32c21f;
  color: white;
}

.completed-dashboard-button:hover {
  background-color: #218838;
}

.remove-dashboard-button {
  background-color: #dc3549;
  color: white;
}

.remove-dashboard-button:hover {
  background-color: #c82333;
}



</style>
