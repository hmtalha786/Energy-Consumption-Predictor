# Energy Consumption Prediction System

A modern Machine Learning web application that predicts building energy consumption using building characteristics and environmental factors.

Built with:

* [Kaggle](https://www.kaggle.com/datasets/govindaramsriram/energy-consumption-dataset-linear-regression/data)
* [FastAPI](https://fastapi.tiangolo.com/?utm_source=chatgpt.com)
* [Streamlit](https://streamlit.io/?utm_source=chatgpt.com)
* [Scikit-learn](https://scikit-learn.org/?utm_source=chatgpt.com)
* [Pandas](https://pandas.pydata.org/?utm_source=chatgpt.com)
* [NumPy](https://numpy.org/?utm_source=chatgpt.com)

---

# ⚡ Project Overview

This project predicts energy consumption for buildings based on:

* Building Type
* Square Footage
* Number of Occupants
* Appliances Used
* Average Temperature
* Day Type (Weekday / Weekend)

The system uses a Linear Regression Machine Learning model served through a FastAPI backend and a modern Streamlit frontend.

---

# 🚀 Features

* Modern Streamlit UI
* FastAPI backend API
* Machine Learning prediction system
* Real-time prediction requests
* Data preprocessing pipeline
* Feature scaling and encoding
* Outlier removal using IQR
* Noise injection for realistic predictions
* Responsive and sleek interface
* Swagger API documentation

---

# 🧠 Machine Learning Pipeline

The model includes:

* Data Cleaning
* Noise Injection
* Outlier Removal
* Feature Scaling
* One-Hot Encoding
* Polynomial Features
* Linear Regression

---

# 📂 Project Structure

```text
Project/
│
├── app.py                     # Streamlit Frontend
├── main.py                    # FastAPI Backend
├── requirements.txt
├── README.md
├── .gitignore
│
├── model/
    └── full_analysis_code.ipynb
    └── train_energy_data.csv
    └── test_energy_data.csv
    └── train_model.py             # Model Training Script
    └── energy_model.pkl           # Trained ML Model
```

---

# 📊 Dataset Features

| Feature             | Description                         |
| ------------------- | ----------------------------------- |
| Building Type       | Residential, Commercial, Industrial |
| Square Footage      | Total area of building              |
| Number of Occupants | Number of people in building        |
| Appliances Used     | Number of electrical appliances     |
| Average Temperature | Temperature in °C                   |
| Day of Week         | Weekday or Weekend                  |
| Energy Consumption  | Target value in kWh                 |

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone YOUR_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🏋️ Train Model

Run:

```bash
python train_model.py
```

This will:

* preprocess data
* train model
* save model as:

```text
energy_model.pkl
```

---

# 🔥 Run FastAPI Backend

```bash
uvicorn main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# 🎨 Run Streamlit Frontend

Open another terminal:

```bash
streamlit run app.py
```

---

# 🧪 Example API Request

## Endpoint

```http
POST /predict
```

## JSON Body

```json
{
  "Square_Footage": 1500,
  "Number_of_Occupants": 4,
  "Appliances_Used": 8,
  "Average_Temperature": 28,
  "Building_Type": "Residential",
  "Day_of_Week": "Weekday"
}
```

---

# 📈 Example Prediction Response

```json
{
  "Predicted Energy Consumption": 542.13
}
```

---

# 🖥️ Application Architecture

```text
Streamlit Frontend
        ↓
HTTP Request
        ↓
FastAPI Backend
        ↓
Machine Learning Model
        ↓
Prediction Response
        ↓
Streamlit UI
```

---

# 📦 Requirements

Main libraries used:

```text
fastapi
uvicorn
streamlit
scikit-learn
pandas
numpy
requests
joblib
```

---

# 🛡️ Future Improvements

Possible future enhancements:

* Docker Deployment
* Cloud Deployment
* Authentication System
* Database Integration
* Prediction History
* Charts & Analytics
* Model Monitoring
* Deep Learning Models
* CI/CD Pipeline
* Dark/Light Theme Toggle

---

# 🤝 Contributing

Contributions are welcome.

Steps:

1. Fork repository
2. Create feature branch
3. Commit changes
4. Push branch
5. Open Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Developed by H M Talha using Machine Learning, FastAPI, and Streamlit.
