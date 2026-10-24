# 🚦 Traffic Sign Detection Using CNN

A deep learning web application that identifies traffic signs from uploaded images using a Convolutional Neural Network (CNN). The application is built with Python, TensorFlow/Keras, and Streamlit and is deployed on Render.

## 🌐 Live Demo

**Try the application:** https://traffic-sign-detection-2k6y.onrender.com

## 📌 Project Overview

Traffic sign recognition is an important application of computer vision for intelligent transportation systems and driver-assistance technologies.

This project uses a trained CNN model to classify traffic sign images into one of 43 classes. Users can upload a traffic sign image through a simple web interface and receive the predicted sign label, class ID, and model confidence score.

## ✨ Features

- Upload traffic sign images for prediction.
- Classify traffic signs into 43 categories.
- Display the predicted traffic sign name.
- Show the predicted class ID and confidence score.
- Interactive web interface built with Streamlit.
- Deployed online using Render.

## 🛠️ Technologies Used

- **Python** — Programming language
- **TensorFlow / Keras** — Deep learning and CNN model
- **NumPy** — Numerical operations
- **Pillow (PIL)** — Image processing
- **Streamlit** — Web application interface
- **Git and GitHub** — Version control and source code hosting
- **Render** — Application deployment

## 📂 Project Structure

```text
PRAICP-1002-TrafSignDetc/
├── app.py
├── traffic_sign_model.keras
├── classes.json
├── requirements.txt
├── .python-version
├── Train.csv
├── Test.csv
├── Meta.csv
├── Train/
├── Test/
└── Meta/
```

## 📊 Dataset

The project uses a traffic sign dataset containing labeled images from 43 classes.

- **Training dataset:** `Train.csv` and the associated training images.
- **Testing dataset:** `Test.csv` and the associated test images.
- **Metadata:** `Meta.csv` and the `Meta/` directory.

The model was evaluated on the official test dataset and achieved **96% test accuracy**.

## 🧠 Model

A Convolutional Neural Network (CNN) was trained to recognize traffic sign patterns from images.

The trained model is saved as `traffic_sign_model.keras`, and `classes.json` stores the class-label mapping used by the application.

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/sujal-5104/Traffic-Sign-Detection.git
cd Traffic-Sign-Detection
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
streamlit run app.py
```

The application will open in your browser, usually at `http://localhost:8501`.

## ☁️ Deployment

The application is deployed on Render.

**Live URL:** https://traffic-sign-detection-2k6y.onrender.com

The deployment uses the GitHub repository, installs the dependencies from `requirements.txt`, and starts the Streamlit application.

## 🧪 Example Prediction

The deployed application was tested successfully with the following result:

- **Predicted sign:** Speed limit (30 km/h)
- **Class ID:** 1
- **Reported confidence:** 100%

Confidence scores indicate the model's output for an image and do not guarantee that a prediction is correct.

## 🎯 Applications

- Intelligent transportation systems
- Driver-assistance systems
- Traffic sign recognition research
- Computer vision and deep learning education

## 🔮 Future Improvements

- Improve recognition of visually similar traffic signs.
- Evaluate performance across different lighting and weather conditions.
- Add webcam-based real-time traffic sign recognition.
- Improve image preprocessing and model robustness.
- Explore deployment on edge devices.

## 👨‍💻 Author

**Sujal Padhiyar**

GitHub: [sujal-5104](https://github.com/sujal-5104)

## 📄 License

This project is intended for educational and demonstration purposes. Add a license file if you plan to distribute or reuse the project under specific terms.
