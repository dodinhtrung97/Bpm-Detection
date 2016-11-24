from matplotlib import pyplot as plt
from scipy.io.wavfile import read
import numpy as np
import wave
import os
import sys

# Backend fix, changed to type TkAgg, might not occur in other debugger

plt.switch_backend('TkAgg')

# OverflowError fix, increased fixed chunksize

plt.rcParams['agg.path.chunksize'] = 10000


# Take user input in the form of .wav
# File folder is root/music/<file>
def takeInput():
    currentDir = os.path.dirname(__file__)
    subDir = 'music'  # Sub folder in root
    fileName = raw_input('Enter wav file: ')
    fileType = fileName.split('.')[-1]

    wholePath = os.path.join(currentDir, subDir, fileName)

    # Wrong type

    if fileType != "wav":
        print 'Type not supported'
        sys.exit(0)

    # File doesn't exist

    elif not os.path.exists(wholePath):
        print 'Cannot find file'
        sys.exit(0)

    return wholePath


# Check for wav's channel type
# getnchannels() returns 2 if stereo, 1 if mono
def isStereo(file):
    return file.getnchannels() == 2


# Convert stereo wav file to mono by manipulating 2 dimensional array
# Stereo wav yields 2 channel in the form of [[left right], [left right] ....]
def stereoToMono(audioArray):
    monoResult = (audioArray[:, 0]/2) + (audioArray[:, 1]/2)  # (array[:,0]+array[:,1])/2 yields wrong result

    return np.array(monoResult, 'Int16')  # Return in dtype='int16'


# Plot wave for x-axis = time, y-axis = wave signal
# Return wave length for main processing
def processWave(path):
    file = wave.open(path, 'r')  # Processed wave, read-only mode

    # If Stereo, convert to mono, function somewhere up

    if isStereo(file):
        frameRate, x = read(path)  # Yields <Frame Rate, Audio Data>
        signal = stereoToMono(x)

    # If mono, do simple wave read

    else:
        frameRate = file.getframerate()  # Get frame rate for time axis (x-axis)
        signal = np.fromstring(file.readframes(-1), 'Int16')

    wavTime = np.linspace(0, len(signal)/frameRate, len(signal))  # Math stuff, nothing to see here

    plt.figure()
    plt.xlabel('Time (s)')
    plt.ylabel('Wavelength (fuck knows)')
    plt.plot(wavTime, signal)
    plt.show()

    return signal


# Execution steps, to be moved to its own file later
def execute():
    path = takeInput()
    processWave(path)


x = np.linspace(0,5,500)

def step(x):
    return 0.0 if x%3>(3./2) else 1.0

def integrate_ai(x, i, L):
    xs = np.linspace(0, L, 100)
    h = xs[1] - xs[0]
    first = ((step(xs[0])*math.cos(i*math.pi*xs[0]/float(L)))/2.0)*h
    last = ((step(xs[-1])*math.cos(i*math.pi*xs[-1]/float(L)))/2.0)*h
    int_sum = 0
    for j in xs[1:-1]:
        int_sum += (step(j)*math.cos(i*math.pi*j/float(L))) * h
    return (int_sum + first + last) / float(L)

def integrate_bi(x, i, L):
    xs = np.linspace(0, L, 100)
    h = xs[1] - xs[0]
    first = ((step(xs[0])*math.sin(i*math.pi*xs[0]/float(L)))/2.0)*h
    last = ((step(xs[-1])*math.sin(i*math.pi*xs[-1]/float(L)))/2.0)*h
    int_sum = 0
    for j in xs[1:-1]:
        int_sum += (step(j)*math.sin(i*math.pi*j/float(L))) * h
    return (int_sum + first + last) / float(L)

def f(x, n, L=1.5):
    s = 0
    for i in range(n+1):
        if i == 0:
            s += integrate_ai(x, i, L)/2.0
        else:
            s += (integrate_ai(x, i, L)*cos(i*math.pi*(x/float(L)))) + (integrate_bi(x, i, L)*sin(i*math.pi*(x/float(L))))
    return s

y = [step(xx) for xx in x]
fy = np.array([f(xx, 3) for xx in x])

plt.plot(x,y,label='step')
plt.plot(x,fy)
plt.grid()
plt.legend()

