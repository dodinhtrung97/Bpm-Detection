Numerical Method Project - Beat Detection
Group: Sky 5780182
	   Sunny <ID>

Expected user input -> .wav file with directory [root/music/<file name>]
Return -> Int value bpm
Coded in Pycharm, backend error might not occur in other debugger

All wav file with stereo channels are to be converted into mono.

Main file Execute (not yet implemented) will calling plotWav for basic and whatever the main process file will be for output

Updates on plotWav file:
# Progress update 1: Problem with converting stereo to mono
# Progress update 2: Taking way too fucking long to read the fucking wav file (prolly due to file size?)
# Progress update 3: Changed looping method in stereoToMono(audioArray)
#                    running time improved, plotting not working but savefig is(backend?)
# Progress update 4: Show() works, problem was in backend, set new backend to 'TkAgg'
# Progress update 5: Fixed OverflowError on large file
# Progress update 6: Minor bug fixed, added x-y labels for aesthetic values (rofl)

NOTE: Do not write everything in 1 python file