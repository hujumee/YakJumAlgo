import sys

stck = []

n = int(sys.stdin.readline())
for i in range(n):
    str = sys.stdin.readline().split()
    com = str[0]
    if com == 'push':
        stck.append(str[1])
    elif com == 'pop':
        if (len(stck)):
            si = len(stck)
            print(stck[si - 1])
            del stck[si - 1]
        else:
            print(-1)
    elif com == 'size':
        print(len(stck))
    elif com == 'empty':
        if (len(stck)):
            print(0)
        else:
            print(1)
    elif com == 'top':
        if (len(stck)):
            si = len(stck)
            print(stck[si - 1])
        else:
            print(-1)