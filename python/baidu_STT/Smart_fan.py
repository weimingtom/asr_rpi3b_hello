#coding:utf-8
import pyaudio
import wave
from baidu_speech_api import BaiduVoiceApi
import json
import signal
import sys
import RPi.GPIO as GPIO
import os
from aip.speech import AipSpeech

from urllib2 import Request, urlopen, URLError, HTTPError

from pixels import Pixels
import time
import vadSound

RESPEAKER_RATE = 16000
RESPEAKER_CHANNELS = 1
RESPEAKER_WIDTH = 2
CHUNK = 1024
RECORD_SECONDS = 2
#WAVE_OUTPUT_FILENAME = "output.wav"

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.output(12, GPIO.LOW)
GPIO.output(13, GPIO.LOW)

p = pyaudio.PyAudio()
stream = p.open(
            rate=RESPEAKER_RATE,
            format=p.get_format_from_width(RESPEAKER_WIDTH),
            channels=RESPEAKER_CHANNELS,
            input=True,
            start=False,)

APP_ID = '15017573'
API_KEY = 'ifutkd8oyrc7yu3NkbzYldsD'
SECRET_KEY = 'DTlVjdnuOlQ0rHqlogAhfFCFm4j4Yw15'


aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

baidu = BaiduVoiceApi(appkey=API_KEY,secretkey=SECRET_KEY)

def generator_list(list):
    for l in list:
        yield l

def record():
    stream.start_stream()
    print("* recording")
    frames = []
    for i in range(0, int(RESPEAKER_RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("* done recording")
    stream.stop_stream()
    print("start to send to baidu")
    # audio_data should be raw_data
    print("server_api data len:", len(frames) * CHUNK)
    text = baidu.server_api(generator_list(frames))
    if text:
        try:
            text = json.loads(text)
            for t in text['result']:
                print(t)
                return(t)
        except KeyError: 
            return("get nothing")
    else:
        print("get nothing")
        return("get nothing")

def record_sound():
    print("* recording")
    raw_data = vadSound.record_sound()
    print("* done recording")
    print("start to send to baidu")
    print("server_api data len:", len(raw_data))
    # audio_data should be raw_data 
    data = generator_list(raw_data)
    print("start to send to baidu 2")
    text = baidu.server_api(data)
    print("start to send to baidu 3")
    if text:
        try:
            text = json.loads(text)
            for t in text['result']:
                print(t)
                return(t)
        except KeyError: 
            return("get nothing")
    else:
        print("get nothing")
        return("get nothing")

def sigint_handler(signum, frame):
    stream.stop_stream()
    stream.close()
    p.terminate()
    print("catched interrupt signal!")
    sys.exit(0)

# 注册ctrl-c中断
signal.signal(signal.SIGINT, sigint_handler)

pixels = Pixels()
pixels.off()

while True:
    try:
        #outputtext = record()
        outputtext = record_sound()
        if (u'开风扇') in outputtext:
            GPIO.output(13, GPIO.LOW) 
            GPIO.output(12, GPIO.HIGH) 
            # os.system("sudo mpg123 turnon.mp3")
            pixels.wakeup()
            time.sleep(3)

        if (u'快一点') in outputtext:
            GPIO.output(12, GPIO.LOW)
            GPIO.output(13, GPIO.HIGH)  
            # os.system("sudo mpg123 faster.mp3")
            pixels.think()
            time.sleep(3)
                    
        if (u'慢一点') in outputtext:
            GPIO.output(13, GPIO.LOW) 
            GPIO.output(12, GPIO.HIGH)
            # os.system("sudo mpg123 lower.mp3")
            pixels.speak()
            time.sleep(3)

        if (u'关风扇') in outputtext:
            GPIO.output(12, GPIO.LOW)
            GPIO.output(13, GPIO.LOW)
            # os.system("sudo mpg123 off.mp3")
            pixels.off()
            time.sleep(3)
            
    except KeyError: 
        stream.close()
        p.terminate()
    except IOError:
        stream.close()
        p.terminate()
        p = pyaudio.PyAudio()
        stream = p.open(
            rate=RESPEAKER_RATE,
            format=p.get_format_from_width(RESPEAKER_WIDTH),
            channels=RESPEAKER_CHANNELS,
            input=True,
            start=False,)
    except KeyboardInterrupt:
        break        

pixels.off()
time.sleep(1)

