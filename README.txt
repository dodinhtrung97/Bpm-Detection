Numerical Method Project - Beat Detection
Group: Sky 5780182
	   Sunny 5780642

To run -> python main.py

Expected user input -> .wav file with directory [root/music/<file name>]
Return -> Values of estimated bpm and frequency

Coded in Pycharm, backend error (for graph drawing) might not occur in other debugger

All wav file with stereo channels are to be converted into mono.
The base algorithm follows the basic steps in detecting bpm described in "Audio Analysis using the Discrete Wavelet Transform" by George Tzanetakis, George Essl, and Perry Cook

Takes very long for a large Wav file so it's better you don't even try.