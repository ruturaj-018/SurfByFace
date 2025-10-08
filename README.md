# 🎮 SurfByFace

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5+-green.svg?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Latest-orange.svg?style=for-the-badge&logo=google&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

### 🚀 *Control Subway Surfers with Your Face!*

*No hands, no controllers — just your head movements and facial gestures*

[🎮 Play Online](https://subwaysurf.io/subway-surfers-buenos-aires) • [📹 Watch Demo](#-live-demo) • [⚡ Quick Start](#-installation)

---

</div>

## 🔥 Introduction

**SurfByFace** is an innovative face-controlled gaming system that transforms your webcam into a motion controller! Using cutting-edge computer vision and facial landmark detection, you can play Subway Surfers hands-free by simply moving your head and making facial gestures.

🎯 **Perfect for:**
- Accessibility gaming solutions
- Tech demonstrations and hackathons
- Fun experiments with computer vision
- Breaking the traditional gaming paradigm

---

## 🧠 How It Works

SurfByFace uses a sophisticated pipeline of computer vision technologies to translate your face movements into game controls:

```
📷 Webcam Feed → 🤖 MediaPipe Face Detection → 📊 Landmark Analysis 
→ 🎮 Gesture Recognition → ⌨️ Keyboard Simulation → 🏃 Game Control
```

**Control Mapping:**
- 👈 **Move Left**: Tilt your head to the left
- 👉 **Move Right**: Tilt your head to the right  
- ⬆️ **Jump**: Raise your eyebrows or tilt head up
- ⬇️ **Roll/Duck**: Tilt your head down

The system processes facial landmarks in real-time at **30+ FPS**, ensuring smooth and responsive gameplay!

---

## ⚙️ Tech Stack

<div align="center">

| Technology | Purpose |
|------------|---------|
| 🐍 **Python 3.8+** | Core programming language |
| 👁️ **OpenCV** | Real-time video processing |
| 🎯 **MediaPipe** | Face mesh detection & tracking |
| ⌨️ **PyAutoGUI** | Keyboard event simulation |

</div>

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- Webcam (built-in or external)
- Modern browser for playing Subway Surfers

### Setup Instructions

1️⃣ **Clone the repository**
```bash
git clone https://github.com/ruturaj-018/SurfByFace.git
cd SurfByFace
```

2️⃣ **Install dependencies**
```bash
pip install opencv-python mediapipe pyautogui numpy
```

Or use a requirements file if available:
```bash
pip install -r requirements.txt
```

3️⃣ **Verify installation**
```bash
python face.py --test
```

---

## 🎮 Usage

### Quick Start Guide

1. **Open Subway Surfers** in your browser:
   
   <div align="center">
   
   [![Play Now](https://img.shields.io/badge/🎮_PLAY_SUBWAY_SURFERS-ONLINE-ff69b4?style=for-the-badge&labelColor=000000)](https://subwaysurf.io/subway-surfers-buenos-aires)
   
   </div>

2. **Run the face detection script**:
   ```bash
   python face.py
   ```

3. **Position yourself** in front of your webcam with good lighting

4. **Start playing!** The system will automatically detect your face and begin tracking movements

### Tips for Best Performance

✅ **DO:**
- Ensure proper lighting on your face
- Position yourself 1-2 feet from the webcam
- Make clear, deliberate head movements
- Calibrate by testing movements before gameplay

❌ **DON'T:**
- Play in low-light conditions
- Make overly subtle gestures
- Cover your face with hands or objects
- Have multiple faces in the frame

---

## 🎥 Live Demo

<div align="center">

### Watch SurfByFace in Action! 🎬

https://github.com/ruturaj-018/SurfByFace/assets/screen-recording.mp4

*Experience hands-free gaming powered by computer vision*

</div>

> **Note:** The demo video showcases real-time face tracking and gesture recognition controlling Subway Surfers gameplay. Watch how natural head movements translate into precise game controls!

---

## 🌐 Play Subway Surfers Online

Ready to try it yourself? Launch the game and start your hands-free adventure:

<div align="center">

### 🏃‍♂️ [**CLICK HERE TO PLAY SUBWAY SURFERS**](https://subwaysurf.io/subway-surfers-buenos-aires) 🏃‍♂️

*Buenos Aires Edition - Optimized for Face Control*

</div>

---

## 🛠️ Advanced Configuration

### Sensitivity Adjustments

Modify the `face.py` script to adjust gesture sensitivity:

```python
# Adjust these thresholds for custom sensitivity
HEAD_TILT_THRESHOLD = 15  # degrees
EYEBROW_RAISE_THRESHOLD = 0.02  # normalized units
```

### Debug Mode

Enable visual feedback for landmark detection:
```bash
python face.py --debug
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| 🚫 Face not detected | Improve lighting, remove glasses/masks |
| ⚡ Laggy response | Close other applications, check CPU usage |
| 🎮 Controls not working | Ensure game window is focused |
| 📷 Webcam not found | Check permissions, try different camera index |

---

## 🚀 Future Enhancements

- [ ] Multi-face support for multiplayer
- [ ] Custom gesture mapping interface
- [ ] Integration with other web games
- [ ] Mobile device support via app
- [ ] Machine learning for personalized calibration
- [ ] Voice command integration

---

## 🧑‍💻 Author

**Ruturaj**

[![GitHub](https://img.shields.io/badge/GitHub-ruturaj--018-black?style=flat-square&logo=github)](https://github.com/ruturaj-018)

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🌟 Show Your Support

If you found this project interesting or useful, please consider:

- ⭐ **Starring** this repository
- 🍴 **Forking** for your own experiments  
- 🐛 **Reporting** bugs or suggesting features
- 📢 **Sharing** with the community

---

<div align="center">

### 💡 *Innovation meets accessibility in gaming*
---

**🎮Game over? Nah, just a new level.🚀**

</div>
