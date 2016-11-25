from math import *

# Test case

N = 8
result = [sin(k) for k in xrange(N)]


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
            sum = x[i*2] + x[i*2 + 1]
            difference = x[i*2] - x[i*2 + 1]

            output[i] = sum
            output[length+i] = difference

            sum = x[i * 2] + x[i * 2 + 1]
            difference = x[i * 2] - x[i * 2 + 1]

            output[i] = sum
            output[length + i] = difference

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

# Pre-processed output

for j in xrange(N):
    print result[j]

print "\n"
# Post-processed output

for i in xrange(N):
    print res[i]
