# 🥔 Potato Disease Classification System using Deep Learning

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange?style=for-the-badge&logo=tensorflow" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/React-Frontend-blue?style=for-the-badge&logo=react" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
</p>

---

# 📌 Project Overview

The **Potato Disease Classification System** is an AI-powered agricultural solution developed using **Deep Learning** and **Computer Vision** technologies.

This project automatically detects and classifies potato leaf diseases from uploaded images, helping farmers and agricultural researchers identify plant diseases quickly and accurately.

The system can classify:

* 🟢 Healthy Potato Leaves
* 🟠 Early Blight Disease
* 🔴 Late Blight Disease

The project combines:

* A **CNN-based Deep Learning Model**
* A **FastAPI Backend**
* A modern **React.js Frontend**
* Image processing and prediction APIs

This solution demonstrates the practical application of Artificial Intelligence in **Smart Agriculture** and **Precision Farming**.

---

# 🎯 Objectives

* Detect potato diseases automatically from leaf images
* Reduce manual disease identification errors
* Support smart farming and agricultural automation
* Build a scalable AI-powered web application
* Provide real-world experience in AI model deployment

---

# ✨ Key Features

## 🧠 Deep Learning-Based Disease Detection

* Uses Convolutional Neural Networks (CNN)
* High accuracy image classification model
* Trained using TensorFlow/Keras

---

## 📷 Image Classification

Classifies potato leaves into:

* Healthy
* Early Blight
* Late Blight

---

## ⚡ FastAPI Backend

* High-performance REST API
* Fast image prediction response
* Easy integration with frontend and mobile apps

---

## 🌐 Modern Web Interface

* User-friendly React.js frontend
* Upload leaf images easily
* Instant prediction results

---

## 📊 Real-Time Prediction

* Upload image
* Process image
* Predict disease
* Display confidence score

---

# 🛠️ Technologies Used

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Core Programming Language |
| TensorFlow   | Deep Learning Framework   |
| Keras        | CNN Model Development     |
| FastAPI      | Backend API               |
| React.js     | Frontend Development      |
| NumPy        | Numerical Computation     |
| Pillow (PIL) | Image Processing          |
| Uvicorn      | API Server                |
| Git & GitHub | Version Control           |

---

# 📂 Project Structure

```bash
Potato-Disease-Classification/
│
├── api/
│   ├── main.py                # FastAPI Backend
│   ├── 1.keras                # Trained Deep Learning Model
│
├── saved_models/              # Model Checkpoints
│
├── training/                  # Model Training Notebooks
│
├── frontend/                  # React Frontend
│
├── README.md
├── requirements.txt
│
└── dataset/
```

---

# 📊 Dataset

The dataset used for this project is publicly available on Kaggle.

## 🔗 Dataset Link

[Potato Leaf Disease Dataset](https://www.kaggle.com/datasets/mdnasimhawlader/potato-leaf-disease-dataset)

The dataset contains:

* Healthy potato leaf images
* Early Blight infected leaf images
* Late Blight infected leaf images

---

# 🧪 Model Training

The CNN model was trained using:

* Image Augmentation
* Data Preprocessing
* TensorFlow/Keras
* Multi-class Classification Techniques

### Training Workflow

```text
Dataset Collection
        ↓
Image Preprocessing
        ↓
CNN Model Training
        ↓
Model Evaluation
        ↓
Model Saving
        ↓
API Deployment
```

---

# 🚀 Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/nasim-dev0459/Potato-Disease-Classification.git
```

---

## 2️⃣ Move Into Project Directory

```bash
cd Potato-Disease-Classification
```

---

## 3️⃣ Create Virtual Environment (Optional)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Backend Server

```bash
uvicorn api.main:app --reload
```

Server will run on:

```bash
http://127.0.0.1:8000
```

---

# 🌐 Frontend Setup

```bash
cd frontend
npm install
npm start
```

---

# 📸 Application Workflow

```text
User Uploads Potato Leaf Image
                ↓
Image Sent to FastAPI Backend
                ↓
CNN Model Processes Image
                ↓
Disease Prediction Generated
                ↓
Prediction Displayed on Frontend
```

---

# 📈 Future Improvements

* 📱 Mobile Application Integration
* ☁️ Cloud Deployment
* 🌍 Multi-Crop Disease Detection
* 📊 Disease Analytics Dashboard
* 🔔 Farmer Notification System
* 🤖 Advanced Transfer Learning Models

---

# 🎓 Academic & Research Value

This project demonstrates practical skills in:

* Deep Learning
* Computer Vision
* AI Model Deployment
* Backend API Development
* Full Stack AI Applications
* Smart Agriculture Systems

It is suitable for:

* Final Year Projects
* Research Portfolios
* Internship Applications
* Scholarship Applications
* AI/ML Portfolio Showcase

---

# 💡 Learning Outcomes

Through this project, I gained experience in:

* CNN Architecture Design
* TensorFlow & Keras
* Image Classification
* REST API Development
* Frontend & Backend Integration
* AI System Deployment

---

# 🤝 Contributing

Contributions are welcome.

If you would like to improve this project:

1. Fork the repository
2. Create a new branch
3. Commit changes
4. Submit a Pull Request

---

# 📜 License

This project is developed for:

* Educational Purposes
* Research
* Portfolio Showcase

---

# 👨‍💻 Developer

## Md Nasim Hawlader

Computer Engineering Student

### Interests

* Artificial Intelligence
* Machine Learning
* Deep Learning
* Computer Vision
* Full Stack Development

---

# ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub.
Your support motivates future AI and research projects 🚀
