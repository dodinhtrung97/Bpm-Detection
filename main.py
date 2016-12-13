import numpy as np
import sys
import os
import miscellaneous as mis
import bpmDetection as detectBpm
import ProcessFrequency as freq

# Use bpmDetection and loop through a window of 10s
def bpmWindow(signal, frameRate):
    signalLength = len(signal)
    sampleWindow = (10 * frameRate)  # Window of 10 sec to scan through
    firstSample = 0
    maxWindow = signalLength / sampleWindow
    allBpms = np.zeros(maxWindow)  # Have to do this for indexing

    for i in xrange(0, maxWindow):
        bpm = detectBpm.detectBpm(signal, frameRate)

        if bpm:
            allBpms[i] = bpm
            firstSample += sampleWindow

    # Pick median in list of all gathered allBpms for general bpm
    bpm = np.median(allBpms)
    return bpm

# Execute
if __name__ == '__main__':
    path, fileName = mis.takeInput()
    fileType = path.split('.')[-1]

    # Wrong type

    if fileType != "wav":
        print 'Type not supported! Exiting!'
        sys.exit(0)

    # File doesn't exist

    while not os.path.exists(path):
        print 'Cannot find file! Re-enter file name'
        path, fileName = mis.takeInput();

    # Retrieve for frequency processing

    signal, frameRate = mis.processWave(path)

    # Retrieve estimated frequency of Wav

    frequency = freq.estimateFrequency_zeroCross(signal, frameRate)

    # Downsample the frequency, write into file named "<original name>+postProc"

    out_file = fileName+"postProc.wav"
    out_path = path.rsplit('\\',1)[0] + '\\' + out_file

    post_proc_file = freq.downsample(path,out_path,frequency)

    if post_proc_file:
        signal, frameRate = mis.processWave(post_proc_file)

    print "Estimated Frequency:", freq.estimateFrequency_zeroCross(signal, frameRate)
    print "Estimated BPM:", bpmWindow(signal, frameRate)
