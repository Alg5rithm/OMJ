n = int(input())

for i in range(n):
    data = int(input())
    result = 0
    for j in range(data):
        if (j + 1) % 2 == 0:
            result = result - (j + 1)
        else:
            result = result + (j + 1)

    s = '#{0} {1}'.format(i + 1, result)
    print(s)
