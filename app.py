from flask import Flask, render_template, request, send_from_directory
import os
import wave
import time
from google import genai
from google.genai import types

app = Flask(__name__)

from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


client = genai.Client(api_key=GEMINI_API_KEY)

VOICE_OPTIONS = [
    "Zephyr", "Puck", "Charon", "Kore", "Fenrir", "Leda", "Orus", "Aoede",
    "Autonoe", "Enceladus", "Lapetus", "Umbriel", "Algieba", "Despina",
    "Erinome", "Algenib", "Rasalgethi", "Laomedeia", "Achernar", "Alnilam",
    "Schedar", "Gacrux", "Achird", "Sulafat"
]

def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        voice_name = request.form["voice"]

        response = client.models.generate_content(
            model="gemini-2.5-flash-preview-tts",
            contents=text,
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO"],
                speech_config=types.SpeechConfig(
                    voice_config=types.VoiceConfig(
                        prebuilt_voice_config=types.PrebuiltVoiceConfig(
                            voice_name=voice_name,
                        )
                    )
                ),
            )
        )

        data = response.candidates[0].content.parts[0].inline_data.data
        out_filename = "out.wav"
        out_path = os.path.join("static", out_filename)
        wave_file(out_path, data)

        timestamp = int(time.time())
        return render_template(
            "index.html",
            audio_file=out_filename,
            text=text,
            voice=voice_name,
            voices=VOICE_OPTIONS,
            ts=timestamp
        )

    return render_template("index.html", audio_file=None, voices=VOICE_OPTIONS, voice="Kore")

@app.route("/download/<filename>")
def download(filename):
    return send_from_directory("static", filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
