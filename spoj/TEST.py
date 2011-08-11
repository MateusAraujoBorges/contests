import sys

while True:
    line = sys.stdin.readline()
    val = int(line)
    if(val == 42):
        break
    else:
        print val
