#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Speech Recognition"""

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
import subprocess
from subprocess import STDOUT, PIPE

try:
    import pandas
except ImportError:
    exit("This script requires the Pandas module\n \
            Install with: sudo pip install pandas")

try:
    from past.builtins import execfile
except ImportError:
    exit("This script requires the Future module\n \
            Install with: sudo pip install future")

try:
    import speech_recognition as sr
except ImportError:
    exit("This script requires the Speech Recognition module\n \
            Install with: sudo pip install SpeechRecognition")

# Read File with Commands
colnames = ['order', 'file']
data = pandas.read_csv('commands.csv', names=colnames, header=0)
orders = data.order.tolist()
cmddict = dict(zip(data.order, data.file))

# Load Voice Recognition
recognizer = sr.Recognizer()

# Find Microphone
sr.Microphone.list_microphone_names()
mic = sr.Microphone(device_index=0)

# Choose Voice (Change mpg123 by your command line mp3 player)
mp3player = 'mpg123'

# Created with gTTS
# tts = gTTS(text='Dime que necesitas', lang='es')
# tts.save("dime.mp3")
messagefile = 'dime.mp3'

try:
    proc = subprocess.Popen(
        mp3player + ' %s' % messagefile,
        shell=True,
        executable="/bin/bash",
        stdin=None,
        stdout=PIPE,
        stderr=STDOUT)
    proc.wait()
except OSError:
    print('Error running voice, please be sure you have mpg123 installed')

with mic as source:
    # Slow option:
    # recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.listen(source)

# English Option:
# speechout = recognizer.recognize_google(audio).capitalize()
try:
    speechout = recognizer.recognize_google(
        audio, language='es-ES').capitalize()
except sr.UnknownValueError:
    print("Could not understand audio")
    speechout = None
except sr.RequestError as e:
    print("Could not request results from Speech Recognition service; {0}".
          format(e))
    speechout = None

if speechout in orders:
    execfile(cmddict.get(speechout))
else:
    print("I din't recognize the command")
    print("You said %s" % speechout)
