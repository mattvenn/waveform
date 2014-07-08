import wave
import struct
#w = wave.open('silence.wav')
w = wave.open('start.wav')
chans = w.getnchannels()
if chans != 1:
    print("aborting, can only handle mono")
    exit(1)
frames = w.getnframes()
#import ipdb; ipdb.set_trace()
framerate = w.getframerate()
print frames
print framerate

count = 0
slot = 10
avg = 0
for frame in range(frames):
    count += 1
    a = w.readframes(1)
    val = struct.unpack('<h',a)
    int_val =  int(val[0])
    int_val = abs(int_val)
    avg += int_val
    if count % 1000 == 0:
        print avg/count
	avg = 0
	count = 0
  
