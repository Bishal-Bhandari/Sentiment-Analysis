import speech_recognition as sr
import LiveInput

# Recognition process
recognition = sr.Recognizer()


def audioTotext():
    # Access file
    src_file = "Resources/Recording.wav"
    # Access file
    with sr.AudioFile(src_file) as source:
        # Audio to memory
        src_file_data = recognition.record(source)
        # Audio to text
        audio_to_text = recognition.recognize_google(src_file_data)
        print(audio_to_text)


def LiveVoice():
    # class and object
    LiveObj = LiveInput.LiveAudio()
    live_audio_data = LiveObj.TakeAudio()
    # feeding data to recognition process
    audio_to_text = recognition.recognize_google(live_audio_data)
    print(audio_to_text)


print("WELCOME")
user_val = int(input("Please select an input.\n Press 1 for audio file.\n Press 2 for live voice input."))
if user_val == 1:
    audioTotext()
elif user_val == 2:
    LiveVoice()
else:
    print("Please press 1 or 2 as an option.")
