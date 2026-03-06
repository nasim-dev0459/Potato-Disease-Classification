# Potato Disease Classification System

An AI-powered system that identifies potato leaf diseases (Early Blight, Late Blight, or Healthy) using deep learning and provides a user-friendly interface.

## Project Overview
This project consists of:
* **AI Model**: A Convolutional Neural Network (CNN) trained with TensorFlow/Keras.
* **Backend**: A high-performance API built with FastAPI.
* **Frontend**: A modern web interface using React.js (Work in progress).

## Tech Stack
* **Language**: Python 3.11
* **Deep Learning**: TensorFlow, Keras, NumPy
* **Backend**: FastAPI, Uvicorn
* **Image Processing**: Pillow (PIL)
* **Frontend**: React.js, Axios
* **Version Control**: Git & GitHub

## Project Structure
```text
Potato_Disease_Project/
├── api/                # FastAPI backend code
│   ├── main.py         # API entry point
│   └── 1.keras         # Trained model file
├── saved_models/       # Model checkpoints
├── tarning/            # Jupyter notebooks for model training
└── frontend/           # React.js web application (To be created)
