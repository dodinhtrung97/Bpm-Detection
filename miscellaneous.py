from matplotlib import pyplot as plt
from scipy.io.wavfile import read
import numpy as np
import wave
import os


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

    wholePath = os.path.join(currentDir, subDir, fileName)

    # fileName for ProcessFrequency

    return wholePath, fileName.rsplit('.',1)[0]


# Check for wav's channel type
# getnchannels() returns 2 if stereo, 1 if mono
def isStereo(file):
    return file.getnchannels() == 2


# Convert stereo wav file to mono by manipulating 2 dimensional array
# Stereo wav yields 2 channel in the form of [[left right], [left right] ....]
def stereoToMono(audioArray):
    monoResult = (audioArray[:, 0]/2) + (audioArray[:, 1]/2)  # (array[:,0]+array[:,1])/2 yields wrong result

    return np.array(monoResult, 'float64')  # Return in dtype='float64'


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
        signal = np.fromstring(file.readframes(-1), 'float64')

    ######### Draw Graph
    # wavTime = np.linspace(0, len(signal)/frameRate, len(signal))  # Math stuff, nothing to see here
    #
    # plt.figure()
    # plt.xlabel('Time (s)')
    # plt.ylabel('Wavelength (fuck knows)')
    # plt.plot(wavTime, signal)
    # plt.show()

    return signal, frameRate

# Detect peak
def detectPeak(signal):
    max = np.amax(abs(signal))
    peak = np.where(signal == max)

    # If no max found then peak is negative

    if len(peak[0]) == 0:
        peak = np.where(signal == -max)

    return peak