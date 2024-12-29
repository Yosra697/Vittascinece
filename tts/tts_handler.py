import pyttsx3
print("pyttsx3 importé avec succès !")

def generate_tts(text, gender="male", speed=150):
    # Initialiser le moteur TTS
    engine = pyttsx3.init()

    # Récupérer les voix disponibles
    voices = engine.getProperty('voices')
    if gender == "male":
        engine.setProperty('voice', voices[0].id)  # Voix masculine
    elif gender == "female":
        engine.setProperty('voice', voices[1].id)  # Voix féminine

    # Régler la vitesse de la voix
    engine.setProperty('rate', speed)

    # Générer le fichier audio
    audio_path = "static/output_audio.mp3"
    engine.save_to_file(text, audio_path)
    engine.runAndWait()

    return audio_path


def generate_ttsFR(text, gender="male", speed=150):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Get available voices
    voices = engine.getProperty('voices')

    # Find a French voice
    french_voice = None
    for voice in voices:
        if "fr" in voice.languages:  # Look for French language in voice
            french_voice = voice.id
            break

    if not french_voice:
        raise RuntimeError("No French voice found on this system. Please install one.")

    # Set the French voice
    engine.setProperty('voice', french_voice)

    # Set the speech rate
    engine.setProperty('rate', speed)

    # Generate the audio file
    audio_path = "static/output_audio.mp3"
    engine.save_to_file(text, audio_path)
    engine.runAndWait()

    return audio_path