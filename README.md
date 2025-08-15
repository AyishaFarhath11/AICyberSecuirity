# AI-Enhanced Cybersecurity Threat Detector 🔐

An **advanced network traffic and system log analyzer** leveraging **transformer-based machine learning models** to detect anomalies and predict potential cybersecurity threats **proactively**.

This project combines **AI-driven analysis**, **real-time visualization**, and a **robust backend API** to provide an end-to-end solution for identifying suspicious activities before they become critical breaches.

---

## ✨ Key Features

- **AI-Powered Anomaly Detection**  
  Utilizes **transformer models** to analyze network traffic and system logs, identifying unusual patterns and predicting potential threats.

- **Real-Time Visualization Dashboard**  
  Built with **React.js**, using libraries like **D3.js** or **Chart.js** to display:
  - Network activity trends
  - Threat detection alerts
  - Anomaly severity levels
  - Historical incident logs

- **Backend Intelligence with Flask**  
  - Handles data ingestion and preprocessing  
  - Manages analysis requests from the frontend  
  - Stores logs and threat reports in a **PostgreSQL** database

- **Comprehensive Data Pipeline**  
  - Supports datasets such as **UNSW-NB15** and **CICIDS2017**  
  - Includes preprocessing: normalization, feature engineering, and labeling  
  - Model evaluation metrics: **Precision**, **Recall**, **F1-score**, **ROC-AUC**

---

## 🛠 Tech Stack

**Frontend:**
- React.js
- D3.js / Chart.js for visualizations
- TailwindCSS 

**Backend:**
- Flask (Python)
- Transformer models (PyTorch / TensorFlow)


**ML & Data Science:**
- Transformers for anomaly detection
- Pandas, NumPy, Scikit-learn for preprocessing
- Matplotlib / Seaborn for offline data visualization

---

## 🚀 How It Works

1. **Data Ingestion** – Network traffic and system logs are collected from datasets or real-time feeds.
2. **Preprocessing** – Features are normalized, engineered, and labeled for analysis.
3. **AI Analysis** – Transformer model processes the data to identify anomalies and predict potential threats.
4. **Visualization** – Results are displayed on a React.js dashboard with real-time updates.
5. **Storage & Logging** – All events are stored in a PostgreSQL database for auditing and future analysis.

---

## 📊 Example Use Cases

- Detecting **DDoS attacks** from unusual traffic patterns.
- Identifying **brute-force login attempts** in system logs.
- Monitoring **internal network anomalies** for insider threats.
- Providing **proactive security alerts** before a breach occurs.

---

