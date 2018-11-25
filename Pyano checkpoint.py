# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 21:15:45 2018

@author: Sana
"""

from scipy import fftpack,signal
from scipy.io import wavfile
import matplotlib.pyplot as plot
import numpy as np
import librosa
import scipy


fs,sound=wavfile.read('piano segment.wav')
ltChannel=[]
rtChannel=[]
for i in sound:
    ltChannel.append(i[0])
    rtChannel.append(i[1])
    
sound = ltChannel


fftSignal=fftpack.fft(sound)
f=np.arange(0,len(fftSignal)/2)
f=f*fs/len(fftSignal)
fftSignal=fftSignal[(len(fftSignal)/2):]

b=plot.subplot(211)
plot.plot(f, fftSignal)
b.set_xlabel('Frequency (Hz)')
b.set_ylabel('magnitude')
plot.show()


maximum=np.amax(fftSignal)
maxThreshold=maximum*0.5
maximaPoints=[]
for i in range(len(fftSignal)):
    if fftSignal[i]>=maxThreshold:
        maximaPoints.append([fftSignal[i],abs(f[i])])
print maximaPoints

KeysList=[]
zeroOne={A0:27, B0:30, C1:32, D1:36, E1:41, F1:43, G1:48, A1:55, B1:61}
Two={C2:65, D2:73, E2:82, F2=87, G2=97, A2=110, B2=123}
Three={A3:110,B3:123,C3:131,D3:147,E3:165,F3:175,G3:196}
Four={A4:220,B4: 247,C4: 262,D4: 294,E4: 330,F4: 349,G4: 392}
Five={ A5: 440,B5: 494,C5: 523,D5: 587,E5: 659,F5: 698,G5: 784}
Six={A6:880,B6: 988,C6:1047,D6: 1175,E6: 1319,F6:1397,G6: 1568}
for i in maximaPoints:
    if i<=61 and i>=27:
        for j in zeroOne:
            if i==zeroOne[j]:
                KeysList.append(j)
    elif i<=123 and i>=65:
        for j in zeroOne:
            if i==zeroOne[j]:
                KeysList.append(j)
    elif i<=196 and i>=110:
        for j in zeroOne:
            if i==zeroOne[j]:
                KeysList.append(j)
    elif i<=392 and i>=220:
        for j in zeroOne:
            if i==zeroOne[j]:
                KeysList.append(j)
    

    
    
#and so on
