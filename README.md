## Sign Language Recognition System

## 📌 Overview
This project is a **real-time sign language recognition system** that utilizes **deep learning and OpenCV** to interpret hand gestures. A **Convolutional Neural Network (CNN)** is employed to classify gestures, which are then converted into speech using **Google Text-to-Speech (gTTS)**. The system is capable of recognizing American Sign Language (ASL) gestures via a webcam and providing real-time audio feedback.

## 🚀 Features
- Load and train the system with an ASL dataset.
- Utilizes a pre-trained CNN model for hand gesture recognition.
- Processes live webcam input for real-time sign detection.
- Converts recognized gestures into speech using gTTS.
- User-friendly interface built with Tkinter.

## 🛠️ Technologies Used
- **Programming Language:** Python (Tkinter, OpenCV, NumPy, Keras, gTTS, playsound)
- **Machine Learning:** Deep learning with CNN for gesture classification
- **Computer Vision:** Background subtraction and image processing

## 📂 Project Structure
```
├── model/                      # Stores trained model files
│   ├── model.json              # CNN model architecture
│   ├── model_weights.h5        # CNN model weights
│   ├── X.txt.npy, Y.txt.npy    # Dataset features and labels
├── play/                       # Stores generated speech files
├── main.py                     # Main script for GUI & recognition
├── README.md                   # Project documentation
```

## 🔧 Installation
### 1️⃣ Prerequisites
Ensure that **Python 3.x** is installed along with the required dependencies:

```sh
pip install numpy opencv-python keras tensorflow gtts playsound tkinter imutils
```

### 2️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/sign-language-recognition.git
cd sign-language-recognition
```

### 3️⃣ Run the Application
```sh
python main.py
```

## 📸 How It Works
1. **Upload Dataset** – Import ASL gesture images for training.
2. **Train CNN Model** – Trains a deep learning model using the dataset.
3. **Start Webcam** – Captures and processes hand gestures in real time.
4. **Predict Gesture** – Identifies the sign language gesture.
5. **Convert to Speech** – Converts recognized signs into spoken output.

## 🎯 Future Enhancements
- Enhance accuracy by adopting advanced deep learning architectures.
- Expand support to include additional sign languages.
- Integrate **MediaPipe Hands** for improved hand tracking.
- Develop a mobile-compatible version of the application.

## 🏆 Contributors
- **Your Name** - [GitHub](https://github.com/Teja1282)

## 📜 License
This project is licensed under the MIT License.

