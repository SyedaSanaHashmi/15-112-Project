import scipy.fftpack as fourier
import scipy.signal as signal
import scipy.io.wavfile as wavfile
import numpy as np
import Tkinter as tk
import tkFileDialog
import pygame

#hard coded filename because start screen was causing problems with main function
filename='piano tutorial full.wav'


sr,audio=wavfile.read(filename)
frames=[]
for i in range(7*(len(audio)/sr)):
    start=i*6300
    end=start+6300
    audioFft=fourier.fft(audio[start:end])
    power=np.abs(audioFft)[:3150]
    frames.append(power)   
freqs=fourier.fftfreq(6300, d=1/float(sr))[:3150]
frames=np.asarray(frames)
for i in range(len(frames)):
    highest=frames[i][np.argmax(frames[i])]
    lowest=frames[i][np.argmin(frames[i])]
    threshold=(highest-lowest)/2
    if threshold<1000000:
        threshold=1000000
    frames[i]=np.where(frames[i]>=threshold,frames[i],False)

peakfreqs=[]
for i in range(len(frames)):
    peakfreqs.append([i,signal.find_peaks(frames[i])[0],np.real(freqs[signal.find_peaks(frames[i])[0]])])









keys1={32.7032:1,34.6478:2,36.7081:3,38.8909:4,41.2034:5,43.6535:6,46.2493:7,48.9994:8,51.9131:9,55.0000:10,58.2705:11,61.7354:12}
keys2={65.4064:13,69.2957:14,73.4162:15,77.7817:16,82.4069:17,87.3071:18,92.4986:19,97.9989:20,103.826:21,110.000:22,116.541:23,123.471:24}
keys3={130.813:25,138.591:26,146.832:27,155.563:28,164.814:29,174.614:30,184.997:31,195.998:32,207.652:33,220.000:34,233.082:35,246.942:36}
keys4={261.626:37,277.183:38,293.665:39,311.127:40,329.628:41,349.228:42,369.994:43,391.995:44,415.305:45,440.000:46,466.164:47,493.883:48}
keys5={523.251:49,554.365:50,587.330:51,622.254:52,659.255:53,698.456:54,739.989:55,783.991:56,830.609:57,880.000:58,932.328:59,987.767:60}
keys6={1046.50:61,1108.73:62,1174.66:63,1244.51:64,1318.51:65,1396.91:66,1479.98:67,1567.98:68,1661.22:69,1760.00:70,1864.66:71,1975.53:72}

##keys1={32.7032:'C1',34.6478:'C#1',36.7081:'D1',38.8909:'D#1',41.2034:'E1',43.6535:'F1',46.2493:'F#1',48.9994:'G1',51.9131:'G#1',55.0000:'A1',58.2705:'A#1',61.7354:'B1'}
##keys2={65.4064:'C2',69.2957:'C#2',73.4162:'D2',77.7817:'D#2',82.4069:'E2',87.3071:'F2',92.4986:'F#2',97.9989:'G2',103.826:'G#2',110.000:'A2',116.541:'A#2',123.471:'B2'}
##keys3={130.813:'C3',138.591:'C#3',146.832:'D3',155.563:'D#3',164.814:'E3',174.614:'F3',184.997:'F#3',195.998:'G3',207.652:'G#3',220.000:'A3',233.082:'A#3',246.942:'B3'}
##keys4={261.626:'C4',277.183:'C#4',293.665:'D4',311.127:'D#4',329.628:'E4',349.228:'F4',369.994:'F#4',391.995:'G4',415.305:'G#4',440.000:'A4',466.164:'A#4',493.883:'B4'}
##keys5={523.251:'C5',554.365:'C#5',587.330:'D5',622.254:'D#5',659.255:'E5',698.456:'F5',739.989:'F#5',783.991:'G5',830.609:'G#5',880.000:'A5',932.328:'A#5',987.767:'B5'}
##keys6={1046.50:'C6',1108.73:'C#6',1174.66:'D6',1244.51:'D#6',1318.51:'E6',1396.91:'F6',1479.98:'F#6',1567.98:'G6',1661.22:'G#6',1760.00:'A6',1864.66:'A#6',1975.53:'B6'}

#harmonic removing mechanism was uspposed to go here
##for l in peakfreqs:
##    if l[2]!=[]:
##        for f in range(1:len(l[2])):
##            if float(l[2][f])/l[2][f-1]<=l[2][f])/l[2][f-1]+0.1 and float(l[2][f])/l[2][f-1]>=l[2][f])/l[2][f-1]-0.1:
##                if frames[l]
        


keyslist=[]
for k in range(len(peakfreqs)):
    sublist=[]
    for j in peakfreqs[k][2]:
        if j<62.5:
            sublist.append(keys1.get(min(keys1, key=lambda x:abs(x-j))))
        elif j<126.5:
            sublist.append(keys2.get(min(keys2, key=lambda x:abs(x-j))))
        elif j<254:
            sublist.append(keys3.get(min(keys3, key=lambda x:abs(x-j))))
        elif j<508.5:
            sublist.append(keys4.get(min(keys4, key=lambda x:abs(x-j))))
        elif j<1017.5:
            sublist.append(keys5.get(min(keys5, key=lambda x:abs(x-j))))
        elif j<2034:
            sublist.append(keys6.get(min(keys6, key=lambda x:abs(x-j))))
    keyslist.append(sublist)


            




parent=tk.Tk()
parent.geometry(str(parent.winfo_screenwidth())+'x'+str(parent.winfo_screenheight()))
parent.resizable(False,False)
parent.configure(background='gray9')
        



class pyanoGUI:
    def __init__(self,parent,keyslist,filename):
        self.keyslist=keyslist
        self.parent=parent
        self.start=0
        self.end=14
        self.width=self.parent.winfo_screenwidth()
        self.keywidth=self.width/72
        self.keyscanvas=tk.Canvas(self.parent,bg='gray9',width=self.width,height=775)
        self.keyscanvas.pack()
        self.img=tk.PhotoImage(file="resizedpiano.gif")
        self.pianolbl=tk.Label(self.parent,image=self.img)
        self.pianolbl.pack_propagate(0)
        self.pianolbl.pack()
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        self.keyscanvas.after(142,self.move)
        

        
    def move(self):
        self.keyscanvas.delete(tk.ALL)
        y=0
        for i in self.keyslist[self.end:self.start:-1]:
            for j in i:
                self.keyscanvas.create_rectangle(j*self.keywidth+7,y,(j+1)*self.keywidth+7,y+55,fill='green')
            y+=55   
        self.start+=1
        self.end+=1
        self.keyscanvas.after(142,self.move)

gui=pyanoGUI(parent,keyslist,filename)
parent.mainloop() 

  
        

