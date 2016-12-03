from numpy import argmax, mean, diff
from matplotlib.mlab import find
from scipy.signal import fftconvolve

# Calculate position of a sample maxima given nearby samples
# Use quadratic interpolation
def findMaxima(vector, index):

    # Input type: vector, index of said vector

    curVector = vector[index]  # Current vector
    preVector = vector[index - 1]  # Element 1 index before input vector
    postVector = vector[index + 1]  # Element 1 index after input vector

    # Process Output as coordinates

    posX = 1/2. * (preVector - postVector) / (preVector - 2 * curVector + postVector) + index
    posY = curVector - 1/4. * (preVector - postVector) * (posX - index)

    # Return position of the vertex of the parabola that goes through x and its neighbors

    return posX, posY


# Calculate frequency with auto-correlation
# Note: Does not work for musical instruments, according to the internet
def extractFrequency_autocor(signal, frameRate):

    # Calculate auto-correlation, discount negative lags

    # Remove DC offset to get rid of potential "triangular trend"

    signal -= mean(signal)

    # Convolve signal and signal[::1] using built in fast Fourier

    cor = fftconvolve(signal, signal[::-1], 'full')  # Output size 'full', output the full convolution of inputs
    cor = cor[len(cor)/2:]

    # Detect first Minima

    start = find(diff(cor) > 0)[0]

    # Detect peak after first Minima
    # Unreliable for long signals (huge file)

    peak = argmax(cor[start:]) + start  # Peak might occur between samples
    interpole = findMaxima(cor, peak)[0]

    # Result frequency in Hz

    result = frameRate/interpole

    return result

def freq_from_crossings(signal, fs):
    # Find all indices right before a rising-edge zero crossing
    indices = find((signal[1:] >= 0) & (signal[:-1] < 0))

    # More accurate, using linear interpolation to find intersample zero-crossings
    crossings = [i - signal[i] / (signal[i+1] - signal[i]) for i in indices]

    # Some other interpolation based on neighboring points might be better.
    # Spline, cubic, whatever

    return fs / mean(diff(crossings))