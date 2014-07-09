import wave
import struct
#w = wave.open('silence.wav')
w = wave.open('codingiscool.wav')
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
slice_size = 1000
avg = 0
scale = 0.01
slice_num = 0
fh = open('results.csv','w')

for frame in range(frames):
    count += 1
    a = w.readframes(1)
    val = struct.unpack('<h',a)
    int_val =  int(val[0])
    int_val = abs(int_val)
    avg += int_val
    if count > slice_size:
        size = int((avg/count)*scale)
	print("%04d %s" % (size,'*'*size))
	fh.write("%d,%d\n" % (slice_num,size))
	slice_num+=1
	avg = 0
	count = 0
fh.close()
print("finished, made %d slices" % slice_num) 
