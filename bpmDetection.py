import numpy as np
from scipy import signal as sig
import pywt
import miscellaneous as mis

# Follows the steps in the algorithm described in "Audio Analysis using the Discrete Wavelet Transform"
# By George Tzanetakis and 2 other people
# Begins with atttempt at downsampling in main through the ProcessFrequency class
def detectBpm(signal, frameRate, cA=[], cDsum=[], level=4):
    maxDec = 2 ** (level-1)
    min = (frameRate/maxDec) * float(60)/220
    max = (frameRate/maxDec) * float(60)/40

    for i in range(level):
        cD = []

        # Discrete Wavelet Transformation

        if i == 0:
            # No idea what db4 is, but db1 doesn't work for large wav file so there you go
            [cA, cD] = pywt.dwt(signal, 'db4')
            cD_minlen = len(cD) / maxDec + 1
            cDsum = np.zeros(cD_minlen);
        else:
            [cA, cD] = pywt.dwt(cA, 'db4')

        # Low pass filtering signal

        cD = sig.lfilter([0.01], [1 - 0.99], cD)

        # For later reconstruction

        cD = abs(cD[::(2 ** (level - i - 1))])
        cD -= np.mean(cD)

        # Combine signals for Auto Correlation
        cDsum = cD[:cD_minlen] + cDsum

    # Prep for auto correlation
    # Filter cA

    cA = sig.lfilter([0.01], [1 - 0.99], cA)
    cA = abs(cA)
    cA -= np.mean(cA)
    cDsum += cA[:cD_minlen]

    # Auto Correlation starts here

    correlation = np.correlate(cDsum, cDsum, 'full')

    midpoint = len(correlation)/2
    centerCorrelation = correlation[midpoint:]
    peak = mis.detectPeak(centerCorrelation[int(min):int(max)])

    adjustedPeak = peak[0] + min
    bpm = float(60) / adjustedPeak*(frameRate/maxDec)

    return bpm