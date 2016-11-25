from math import *

# Test case

<<<<<<< HEAD
Testnum = 8
=======
Testnum = 32
>>>>>>> 7d1e89b7392624e97650e934cf96e5ec01396da0
result = [sin(k) for k in xrange(Testnum)]

# Pre-processed output

for i in xrange(Testnum):
    print result[i]


# Create spectrogram analyser
# Based on Haar wavelet transform algorithm
# Considerably faster than FFT atm
def discreteHaarWaveletTransform(x):
    inputLength = len(x)

    # Simple append doesn't work

    output = [0.0]*inputLength

    length = inputLength >> 1

    # Loop unless meets break condition
    # No real deadline

    while True:
        for i in xrange(0, length):
<<<<<<< HEAD
            sum = x[i*2] + x[i*2 + 1]
            difference = x[i*2] - x[i*2 + 1]
            output[i] = sum
            output[length+i] = difference
=======
            sum = x[i * 2] + x[i * 2 + 1]
            difference = x[i * 2] - x[i * 2 + 1]
            output[i] = sum
            output[length + i] = difference
>>>>>>> 7d1e89b7392624e97650e934cf96e5ec01396da0

        # Break condition

        if length == 1:
            return output

        # Swap arrays to do next iteration
        # arraycopy(output, 0, x, 0, length << 1)
        # Shift index to left

        x = output[:length << 1]

        # Shift to right

        length >>= 1


res = discreteHaarWaveletTransform(result)

# Post-processed output

for i in xrange(Testnum):
    print res[i]
