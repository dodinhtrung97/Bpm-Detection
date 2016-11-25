from math import *

Testnum = 32
result = [sin(k) for k in xrange(Testnum)]

def discreteHaarWaveletTransform(x):
    inputLength = len(x)

    output = [0.0]*inputLength

    length = inputLength >> 1

    while True:
        for i in xrange(0, length):
            sum = x[i * 2] + x[i * 2 + 1]
            difference = x[i * 2] - x[i * 2 + 1]
            output[i] = sum
            output[length + i] = difference

        if length == 1:
            return output

        x = output[:length << 1]

        length >>= 1


res = discreteHaarWaveletTransform(result)
