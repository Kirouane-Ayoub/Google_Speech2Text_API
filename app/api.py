from fastapi import FastAPI, UploadFile, File
from google.cloud import speech_v1p1beta1 as speech

import uvicorn
app = FastAPI()
client = speech.SpeechClient.from_service_account_json("app/key.json")

@app.post("/transcribe")
async def transcribe_speech(mp3_file: UploadFile = File(...), language: str = 'en-US'):
    mp3_data = await mp3_file.read()
    audio_file = speech.RecognitionAudio(content=mp3_data)
    config = speech.RecognitionConfig(
        encoding="MP3",
        sample_rate_hertz=16000,
        language_code=language,
        speech_contexts=[{'phrases': ['installer']}]
    )
    response = client.recognize(config=config, audio=audio_file)
    transcriptions = [result.alternatives[0].transcript for result in response.results]
    return {"transcriptions": transcriptions}

if __name__ == "__main__" : 
    uvicorn.run(app , port=8080 , host="0.0.0.0" , workers=1)