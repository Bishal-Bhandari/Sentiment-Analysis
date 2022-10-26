import speech_recognition as sr
import LiveInput
import BERT

# Recognition process
recognition = sr.Recognizer()
# using BERT model
bertObj = BERT.BertAnalysis


def audioTotext():
    # Access file
    src_file = "Resources/Recording.wav"
    # Access file
    with sr.AudioFile(src_file) as source:
        # Audio to memory
        src_file_data = recognition.record(source)
        # Audio to text
        audio_to_text = recognition.recognize_google(src_file_data)
        score_bert = bertObj.bert_analysis(audio_to_text)
        print(audio_to_text + '\n Analysied score:' + score_bert)


def LiveVoice():
    # class and object
    LiveObj = LiveInput.LiveAudio()
    live_audio_data = LiveObj.TakeAudio()
    # feeding data to recognition process
    audio_to_text = recognition.recognize_google(live_audio_data)
    score_bert = bertObj.bert_analysis(audio_to_text)
    print(audio_to_text + '\n Analysied score:' + score_bert)


print('\x1b[6;30;42m' + 'WELCOME' + '\x1b[0m')
user_val = int(input('\x1b[1;31;40m' + "Please select an input.\n Press 1 for audio file.\n Press 2 for live voice "
                                       "input.   " + '\x1b[0m'))
if user_val == 1:
    audioTotext()
elif user_val == 2:
    LiveVoice()
else:
    print("Please press 1 or 2 as an option.")
