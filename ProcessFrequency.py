import audioop
import os
import wave
from numpy import mean, diff
from matplotlib.mlab import find

# Estimate frequency using zeroes crossing
def estimateFrequency_zeroCross(signal, frameRate):

    # Find all indices before a rising-edge zero crossing

    indices = find((signal[1:] >= 0) & (signal[:-1] < 0))

    # Use linear interpolation to find zero-crossings inbetween samples, more accurate

    crosses = [i - signal[i] / (signal[i+1] - signal[i]) for i in indices]

    return frameRate/mean(diff(crosses))

# Downsampling to 3Hz, if can't downsample then ignore
def downsample(src, dst, inFreq, outFreq=3, inChannel=1, outChannel=1):

    # Prepare new file to write

    write = wave.open(dst, 'w')

    read = wave.open(src, 'r')
    frames = read.getnframes()
    signal = read.readframes(frames)

    write.setparams((outChannel, read.getsampwidth(), outFreq, 1, 'NONE', 'Uncompressed'))

    # Convert from inFreq to outFreq, 2 is width of output

    try:
        convert = audioop.ratecv(signal, 2, inChannel, inFreq, outFreq, None)
    except:
        write.close()
        os.remove(dst)
        print "Can't downsample!!! Using original file"

        # If false then whatever, fuck the downsampling
        return

    try:
        write.writeframes(convert)
    except:
        write.close()
        os.remove(dst)
        print "Can't write file!!!"

        # If false then whatever, fuck the downsampling
        return

    write.close()