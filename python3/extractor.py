__author__ = "Max Margolin, margolinmax@gmail.com"
#pay no attention to this yet

# Beat tracking example
from __future__ import print_function
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

filename = "selena.mp3"
filename = "et.mp3"
filename = "hotcold.mp3"
# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
y, sr = librosa.load(filename)
claim = [30]
# 3. Run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

print('Estimated tempo: {:.2f} beats per minute'.format(tempo))




def extract(current_time, wave, sr, time_multiples):
    print(len(wave)/sr)
    current = current_time*sr
    arr = []
    for i in range(-10,10):
        start = current + sr * i * time_multiples
        finish = current + sr * (i + 1) * time_multiples
        arr.append(np.average(np.abs(wave[start:finish])))
    return arr
e = extract(claim[0], y, sr, 1)


plt.figure()
#plt.subplot(3, 1, 1)
#librosa.display.waveplot(y, sr=sr)

plt.plot(range(-10,10),e)
print (claim[0])
print(len(y)/sr)

plt.show()
