# 🌦 Weather Forecast & Alert Application

##  Project Overview

The Weather Forecast & Alert Application is a Python-based industry-oriented project that fetches real-time weather forecast data using a public weather API and generates weather alerts based on temperature, humidity, and rain conditions.

The project helps users monitor weather conditions for different cities and provides alerts for:

* High temperature
* Rain possibility
* High humidity
* Weather changes

This project demonstrates:

* API Integration
* Data Processing
* Weather Forecast Analysis
* Alert Systems
* CSV Report Generation
* Data Visualization
* Dashboard Development
* FastAPI Backend Development


# Industry Relevance

This project is useful in industries such as:

* Logistics
* Agriculture
* Travel
* Public Safety
* Event Planning
* Energy Sector

Companies use similar systems for:

* Route planning
* Weather risk management
* Outdoor event scheduling
* Irrigation planning
* Heatwave monitoring

---

# Features

1.Real-time weather forecast

2. City-wise weather search

3. Rain alerts

4. High temperature alerts

5. Humidity alerts

6. CSV weather report generation

7. Temperature visualization charts

8. Streamlit dashboard

9. FastAPI backend

10. Professional project structure


# 🛠 Tech Stack

## Programming Language

* Python 3.14.4

## Libraries Used

* requests
* pandas
* matplotlib
* streamlit
* fastapi
* uvicorn
* python-dotenv

## API Used

* OpenWeatherMap API

---

#  Project Structure

```bash
Weather-Forecast-Alert-Application/
│
├── data/
├── images/
├── reports/
├── src/
│   └── api/
│       └── app.py
│
├── main.py
├── streamlit_app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
```

---

# ⚙ Installation Guide

## Step 1 — Clone Repository

```bash
git clone https://github.com/manasa476/Weather-Forecast-Alert-Application.git
```

## Step 2 — Open Project Folder

```bash
cd Weather-Forecast-Alert-Application
```

## Step 3 — Create Virtual Environment

### Windows

```bash
python -m venv venv
```

## Step 4 — Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

## Step 5 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 API Setup

## Create .env File

```env
API_KEY=your_openweathermap_api_key
```

⚠ Never upload your real `.env` file to GitHub.

Use `.env.example` instead.

---

# ▶ How To Run Project

## Run Main Weather Application

```bash
python main.py
```

Example:

```bash
Enter City Name: Mumbai
```

---

# 📊 Run Streamlit Dashboard

```bash
streamlit run streamlit_app.py
```

Dashboard URL:

```bash
http://localhost:8501
```

---

# ⚡ Run FastAPI Backend

```bash
python -m uvicorn src.api.app:app --reload
```

API URL:

```bash
http://127.0.0.1:8000
```

Swagger Documentation:

```bash
http://127.0.0.1:8000/docs
```

---

# 📈 Project Workflow

```text
User Enters City
        ↓
Weather API Request
        ↓
JSON Weather Data
        ↓
Data Processing
        ↓
Forecast Analysis
        ↓
Alert Generation
        ↓
CSV Report Creation
        ↓
Chart Visualization
        ↓
Dashboard Display
```

---

# 📷 Screenshots To Add

Add screenshots for:

* Project Folder Structure
* Terminal Output
* Weather Forecast Output
* Alerts
* CSV Report
* Temperature Chart
* Streamlit Dashboard
* FastAPI Swagger Docs
* GitHub Repository

---

# 📄 Sample Output

```text
===== WEATHER FORECAST =====

Temperature: 29°C
Humidity: 75%
Weather: Clouds
Rain: 0 mm

===== ALERTS =====

No Alerts
```

---

# 📊 Generated Outputs

## Reports Folder

```bash
Mumbai_weather_report.csv
```

## Images Folder

```bash
Mumbai_chart.png
```


✅ Upload:

* .env.example
* source code
* screenshots
* reports

---

# Learning Outcomes

Through this project I learned:

* REST API Integration
* JSON Data Handling
* Python Automation
* Error Handling
* Data Visualization
* Dashboard Development
* Backend API Development
* CSV Report Generation
* GitHub Project Management

---

# 💼 Resume Value

This project is useful for roles such as:

* Python Developer
* Software Developer
* API Integration Engineer
* Data Analyst
* AI/ML Engineer
* Backend Developer

---

# 🎤 Interview Questions

## 1. Explain your project.

I built a Python-based Weather Forecast & Alert Application that fetches real-time weather data using APIs, processes forecast information, generates alerts for rain, humidity, and temperature conditions, and displays the output using charts and dashboards.

---

## 2. Which API did you use?

I used the OpenWeatherMap API to fetch weather forecast data.

---

## 3. What libraries were used?

requests, pandas, matplotlib, streamlit, fastapi, uvicorn, and python-dotenv.

---

## 4. What is JSON?

JSON is a lightweight data format used by APIs to transfer structured data.

---

## 5. How does the alert system work?

The system compares weather conditions with predefined thresholds and generates alerts if conditions exceed safe limits.

---

#  Future Improvements

* SMS Alerts
* Email Notifications
* AQI Integration
* Live Weather Maps
* Multi-city Tracking
* Mobile Application
* AI-based Weather Prediction

---

#  Author

Manasa Hiremath

GitHub: https://github.com/manasa476/Weather-Forecast-Alert-Application

LinkedIn: www.linkedin.com/in/manasa-hiremath-22548a332



---

# ⭐ Conclusion

This project demonstrates practical implementation of:

* Python Programming
* API Integration
* Weather Forecast Analysis
* Dashboard Development
* Alert Automation
* Data Visualization
* Backend API Development

making it a strong proof-of-work project for GitHub, internships, and software development interviews.
