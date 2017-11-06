import sys
f = open('result_plb.txt', 'r')

for line in f:
    txt = line.strip()
    if txt == '':
        sys.stdout.write('\n\n')
        sys.stdout.flush()
    sys.stdout.write( txt + ',')
    sys.stdout.flush()
f.close()