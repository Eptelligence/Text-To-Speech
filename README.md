<img width="1149" height="402" alt="image" src="https://github.com/user-attachments/assets/f57ea9a8-5947-4272-83f5-997bdecbafd3" />



# 🎙️ Text-to-Speech (TTS) Web App

> A minimal Flask-based web app that converts user-written text into spoken audio using Gemini's TTS API — designed with speed, clarity, and elegance in mind.

---

## 🌟 About the Project

This project reflects my passion for working with **Flask**, a lightweight and powerful Python web framework.
Although this application might look simple at first glance, it brings together:

- Dynamic web UI interaction
- Secure API integration with environment variables
- Audio generation and playback via modern browser features
- A clean deployment pipeline using **Render**

🚀 Live demo:
🔗 [https://tts-text-to-speech.onrender.com/](https://tts-text-to-speech.onrender.com/)

---

## 💡 Features

- 📝 Write any Persian sentence and convert it into voice
- 🎧 Choose from 20+ different AI voice tones
- 🔒 Secure use of Google Gemini API via `.env`
- 📁 WAV audio file generation and download
- 🌐 Fully deployed on [Render](https://render.com/)

---

## 🛠️ Tech Stack

- **Python** (3.x)
- **Flask**
- **Google Gemini TTS API**
- **HTML/CSS** with minimal RTL-friendly design
- **Render** for free cloud deployment
- **dotenv** for secret management

---

## ⚙️ Setup Instructions

> You'll need a valid [Google Gemini API key](https://makersuite.google.com/app) to run this app.

```bash
# 1. Clone the repo
git clone https://github.com/Eptelligence/Text-To-Speech
cd Text-To-Speech

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create a .env file and add your Gemini API key
echo "GEMINI_API_KEY=your_key_here" > .env

# 5. Run the app
python app.py
```
Then open http://localhost:5000 in your browser.


 ## 📌 Why I Built This
 
I wanted a fast, minimal, and satisfying way to interact with modern TTS systems —
and at the same time explore the elegance of Flask for building practical web tools.

This project also served as a personal exercise in:

Clean API integration
Secure key handling
Real-world deployment of Flask apps


## 📷 Screenshot
<img width="1919" height="907" alt="image" src="https://github.com/user-attachments/assets/95a75c3b-b779-4b0b-9448-4156970f03a4" />


## 📄 License
MIT License — Free to use and modify.


## 🤝 Let's Connect
I'm always up for collaboration or feedback!

LinkedIn: https://www.linkedin.com/in/erfan-pouretemad/

GitHub: https://github.com/Eptelligence

Website: www.Eptelligence.com
