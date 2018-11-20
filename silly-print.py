import sys
# I wish I could import money
import time

symbol = "#"
repeat = 1
duration = 1000
length = 10
if (len(sys.argv) > 1):
    symbol = sys.argv[1]
if (len(sys.argv) > 2):
    repeat = int(sys.argv[2])
if (len(sys.argv) > 3):
    duration = int(sys.argv[3])
if (len(sys.argv) > 4):
    length = int(sys.argv[4])
if (len(sys.argv) > 1 and sys.argv[1] =='HELP'):
  print("python silly-print.py [symbol-to-print] [how-many-on-a-line] [duration] [steps]")
  sys.exit()
print("sup "+ symbol);

def goSilly(str, repeat, duration):
    line = ""
    while repeat > 0:
        line += str
        repeat -= 1
    mark = 0
    add = True
    while duration > 0:
        print(line)
        time.sleep(0.01)
        sys.stdout.flush()
        if add:
            line = " " + line
            mark += 1
        else:
            line = line[1:]
            mark -= 1
        if mark == length:
            add = False
        if mark == 0:
            add = True
        duration -= 1
    return

goSilly(symbol, repeat, duration)
