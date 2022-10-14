import speech_recognition as sr


def audioTOtext():
    # Access file
    src = "Resources/Recording.wav"

    # Recognition process
    recognition = sr.Recognizer()

    # Access file
    with sr.AudioFile(src) as source:
        # Audio to memory
        audio_data = recognition.record(source)
        # Audio to text
        text = recognition.recognize_google(audio_data)
        print(text)


audioTOtext()