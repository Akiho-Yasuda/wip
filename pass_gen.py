# pass_gen.py
import string
import secrets
import espeak
import numpy as np
import wave
import pyaudio
import matplotlib.pyplot as plt

def pass_gen(size=12):
   chars = string.digits
   # 記号を含める場合
   # chars += '%&$#()'

   return ''.join(secrets.choice(chars) for x in range(size))

def PlayWavFie(Filename = "400hz.wav"):
    try:
        wf = wave.open(Filename, "r")
    except FileNotFoundError: #ファイルが存在しなかった場合
        print("[Error 404] No such file or directory: " + Filename)
        return 0

    # ストリームを開く
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # 音声を再生
    chunk = 1024
    data = wf.readframes(chunk)
    while data != '':
        stream.write(data)
        data = wf.readframes(chunk)
    stream.close()
    p.terminate()

# PlayWavFie("400hz.wav")
tmp = str(pass_gen(5))
es = espeak.ESpeak()
es.save(tmp, pass.wav)
