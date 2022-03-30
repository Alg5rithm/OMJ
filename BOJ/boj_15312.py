import sys

dic = {
    'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 3, 'F': 3, 'G': 2, 'H': 3, 'I': 3, 'J': 2, 'K': 2,
    'L': 1, 'M': 2, 'N': 2, 'O': 1, 'P': 2, 'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1, 'V': 1,
    'W': 1, 'X': 2, 'Y': 2, 'Z': 1
}

A = sys.stdin.readline()
B = sys.stdin.readline()
initial = list()

for i in range(len(A) - 1):
    initial.append(dic[A[i]])
    initial.append(dic[B[i]])

answer = initial.copy()

while len(answer) > 2:
    count = 0
    answer.clear()
    while count < len(initial) - 1:
        answer.append((initial[count] + initial[count + 1]) % 10)
        count += 1
    initial = answer.copy()

answer_str = ''
for i in answer:
    answer_str += str(i)

print(answer_str)
