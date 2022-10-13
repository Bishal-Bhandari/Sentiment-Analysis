import speech_recognition as sr
from pydub import AudioSegment

filename = "Resources/Myname.wav"

# convert file format
# wav_fileformat = r"Resources\file1.wav"

# Recognition process
recognition = sr.Recognizer()

# Access file
with sr.AudioFile(filename) as source:
    # Audio to memory
    audio_data = recognition.record(source)
    # Audio to text
    text = recognition.recognize_google(audio_data)
    print(text)
