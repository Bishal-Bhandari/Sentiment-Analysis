import speech_recognition as sr


def audioTOtext():
    # Access file
    src_file = "Resources/Recording.wav"

    # Recognition process
    recognition = sr.Recognizer()

    # Access file
    with sr.AudioFile(src_file) as source:
        # Audio to memory
        src_file_data = recognition.record(source)
        # Audio to text
        audio_to_text = recognition.recognize_google(src_file_data)
        print(audio_to_text)


audioTOtext()