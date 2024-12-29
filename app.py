from flask import Flask, request, jsonify, render_template
from flask_sockets import Sockets
import faster_whisper
from tts.tts_handler import generate_tts  # Importer la fonction TTS corrigée
import logging

app = Flask(__name__)
sockets = Sockets(app)

# Initialize STT model
stt_model = faster_whisper.WhisperModel("base")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tts', methods=['POST'])
def text_to_speech():
    try:
        # Récupérer les données de la requête
        data = request.json
        text = data.get("text", "")
        gender = data.get("gender", "male")
        speed = int(data.get("speed", 150))

        # Appeler la fonction TTS
        audio_path = generate_tts(text, gender, speed)

        return jsonify({"audio_url": audio_path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@sockets.route('/stt')
def speech_to_text(ws):
    print("WebSocket connection established.")
    while not ws.closed:
        try:
            message = ws.receive()
            if message:
                print(f"Message received: {message}")
                ws.send(f"Processed: {message}")  # Echo the message back
        except Exception as e:
            print(f"WebSocket error: {e}")
            break
    print("WebSocket connection closed.")


if __name__ == "__main__":
    import eventlet
    from eventlet import wsgi
    eventlet.monkey_patch()
    wsgi.server(eventlet.listen(("127.0.0.1", 5050)), app)
