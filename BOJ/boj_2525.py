
currentClock = list(map(int, input().split())) # 현재시각
num = int(input())

currentClock[1] = currentClock[1] + num
while currentClock[1] >= 60:
    currentClock[1] = currentClock[1] - 60
    currentClock[0] += 1

while currentClock[0] >= 24:
    currentClock[0] = currentClock[0] - 24


print(currentClock[0], currentClock[1])