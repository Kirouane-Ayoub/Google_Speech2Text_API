
from google.cloud import speech 
client = speech.SpeechClient.from_service_account_file("app/key.json")


def run(file_name , language='en-US') : 
    with open(file_name , 'rb') as f :
        mp3_data = f.read()
        audio_file = speech.RecognitionAudio(content=mp3_data)


    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        enable_automatic_punctuation=True,
        audio_channel_count=2,
        language_code="en-US")

    response = client.recognize(request={"config": config, "audio": audio_file})
    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))
    
run(file_name="audio.mp3")


