# pass_gen.py
import string
import secrets
import espeak
import numpy as np
import wave
import pyaudio
import matplotlib.pyplot as plt
from datetime import datetime
import glob
import paramiko
import scp
import os

def select_file():
    list_of_files = glob.glob('/Users/akiho/wip/*.wav') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file


def send_wav(filename):
    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname='ccz00.sfc.keio.ac.jp', port=22, username='s18779ay', password='akibon2727')
        with scp.SCPClient(ssh.get_transport()) as scp2:
            scp2.put(filename, '/home/s18779ay/public_html/googlehome')
            # scp.get('/upload/to/remote/directory/')

# def pass_gen(size=5):
#    chars = string.digits
#    # 記号を含める場合
#    # chars += '%&$#()'
#    return ''.join(secrets.choice(chars) for x in range(size))

chars = string.digits
pas = ''.join(secrets.choice(chars) for x in range(5))

# pas = pass_gen(5)

f=open('pas.txt', 'w+')
f.write(pas)
f.close()

print(pas)

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

def speak():
    es = espeak.ESpeak()
    # es.say(pas)
    filename = datetime.now().strftime('%Y%m%d_%H:%M:%S')
    wav = filename +".wav"
    es.save(pas, wav)

if __name__ == "__main__":
    speak()
    latest_file = select_file()
    send_wav(latest_file)
