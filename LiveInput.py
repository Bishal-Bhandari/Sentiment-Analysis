import speech_recognition as sr


class LiveAudio:
    def TakeAudio(self):
        init_rec = sr.Recognizer()
        print("Let's speak!!")
        with sr.Microphone() as source:
            audio_data = init_rec.record(source, duration=5)
            print("Recognizing your text.............")
            # text = init_rec.recognize_google(audio_data)
            # print(text)
        return audio_data

