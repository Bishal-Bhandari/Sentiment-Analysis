import speech_recognition as sr

filename = "Resources/Myname.m4a"

# Recognition process
recognition = sr.Recognizer()

# Access file
with sr.AudioFile(filename) as source:
    # Audio to memory
    audio_data = recognition.record(source)
    # Audio to text
    text = recognition.recognize_google(audio_data)
    print(text)
