# ----------------------------------
# This script is used for learning
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
# as you can see when this script is started to write to file
# the file size remain 0 kb for some time
# because of python use buffer
# binary files are buffered in fixed-size chunks; the size of the buffer is chosen using a heuristic trying to determine the underlying device’s “block size” and falling back on io.DEFAULT_BUFFER_SIZE. On many systems, the buffer will typically be 4096 or 8192 bytes long.
# “Interactive” text files (files for which isatty() returns True) use line buffering. Other text files use the policy described above for binary files.
import time
file1 = open('sleep.txt', mode='w')
string1 = '=========='
i = 0
while True:
    file1.write(f'ssstrin {string1}++++{i}\n')
    i += 1
    time.sleep(1)