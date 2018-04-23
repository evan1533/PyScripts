
import pyaudio
import numpy as np
import time
from threading import Thread

def myfunc(pyAud, freq):
    volume = 0.5     # range [0.0, 1.0]
    fs = 44100       # sampling rate, Hz, must be integer
    duration = 3.0   # in seconds, may be float
    # generate samples, note conversion to float32 array
    samples = (np.sin(2*np.pi*np.arange(fs*duration)*freq/fs)).astype(np.float32)

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = pyAud.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)
    stream.write(0.5*samp);
    stream.stop_stream()
    stream.close()

p = pyaudio.PyAudio()
t = Thread(target=myfunc, args=(p,261.63))
t2 = Thread(target=myfunc, args=(p,329.63))
t.start()
t2.start()


p.terminate()
