import sys

q = []

n = int(sys.stdin.readline())
for i in range(n):
    str = sys.stdin.readline().split()
    com = str[0]
    if com == 'push':
        q.append(str[1])
    elif com == 'pop':
        if (len(q)):
            print(q[0])
            del q[0]
        else:
            print(-1)
    elif com == 'size':
        print(len(q))
    elif com == 'empty':
        if (len(q)):
            print(0)
        else:
            print(1)
    elif com == 'front':
        if (len(q)):
            print(q[0])
        else:
            print(-1)
    elif com == 'back':
        if (len(q)):
            ln = len(q)
            print(q[ln-1])
        else:
            print(-1)