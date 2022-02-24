n = int(input())
numbers = []

for i in range(n):
    numbers.append(i+1)

while True:
    numbers.pop(0)
    if len(numbers) == 1:
        break
    numbers.append(numbers.pop(0))

print(numbers[0])
