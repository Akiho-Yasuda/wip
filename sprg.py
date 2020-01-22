import speech_recognition as sr
from datetime import datetime
import time


filename = datetime.now().strftime('%Y%m%d_%H:%M:%S')
txt =filename +".txt"

with open(txt, 'w') as f: #txtファイルの新規作成
    f.write(filename + "\n") #最初の一行目にはfilenameを記載する

r = sr.Recognizer()
mic = sr.Microphone()

t_end = time.time() + 10 #10秒間
while time.time() < t_end:
    print("Say something ...")

    with mic as source:
        r.adjust_for_ambient_noise(source) #雑音対策
        audio = r.listen(source)

    print ("Now to recognize it...")

    try:
        print(r.recognize_google(audio, language='en-US'))

        with open(txt,'a') as f: #ファイルの末尾に追記していく
            f.write("\n" + r.recognize_google(audio, language='en-US'))

    # 以下は認識できなかったときに止まらないように。
    except sr.UnknownValueError:
        print("could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
