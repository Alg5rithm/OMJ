import sys

N = int(sys.stdin.readline())

for i in range(1, N + 1):
    day = sys.stdin.readline().strip()
    result = ''
    if day == 'SUN':
        print("#%d 7" %i)
    elif day == 'MON':
        print("#%d 6" %i)
    elif day == 'TUE':
        print("#%d 5" %i)
    elif day == 'WED':
        print("#%d 4" %i)
    elif day == 'THU':
        print("#%d 3" %i)
    elif day == 'FRI':
        print("#%d 2" %i)
    elif day == 'SAT':
        print("#%d 1" %i)

