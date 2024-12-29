import faster_whisper

stt_model = faster_whisper.WhisperModel("base")

def transcribe_audio(audio_chunk):
    result = stt_model.transcribe(audio_chunk)
    return result["text"]
