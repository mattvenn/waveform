import wave
import struct

# open the wav file
w = wave.open('codingiscool.wav')

# check it's mono
chans = w.getnchannels()
if chans != 1:
    print("aborting, can only handle mono")
    exit(1)

# get the number of samples in the wav file (usually 44100 per second)
frames = w.getnframes()
framerate = w.getframerate()

# ask the user how many slices (this will define the length of the necklace)
# we have to turn the string into an int
slices = int(input("how many slices? "))

# some variables we'll be using later
count = 0
slice_size = frames / slices
avg = 0
scale = 0.02
slice_num = 0

# open the results file
fh = open('results.csv', 'w')

# for each sample...
for frame in range(frames):
    count += 1
    # this is the bit that turns the sample into a number
    a = w.readframes(1)
    val = struct.unpack('<h', a)
    int_val = int(val[0])
    int_val = abs(int_val)

    # add to a running total
    avg += int_val

    # once we have enough samples
    if count >= slice_size:
        size = int(avg/count)

        # print out some details for each slice
        print("%3d %4d %s" % (slice_num, size, '*' * int(size * 0.01)))

        # this is how we write it to a file
        fh.write("%d,%d\n" % (slice_num, size))

        slice_num += 1
        avg = 0
        count = 0

# close the file
fh.close()

# print out a summary of what happened
print("found %d samples at %d samples per second" % (frames, framerate))
print("finished, made %d slices" % slice_num)
