def solution(scoville, K):
    counter = 0
    scoville.sort()
    while True:
        if scoville[0] < K:
            newScoville = scoville[0] + (scoville[1] * 2)
            del scoville[0]
            del scoville[0]
            scoville.append(newScoville)
            counter += 1
            scoville.sort()
        else:
            break
    return counter


scoville_list = [1, 2, 3, 9, 10, 12]
print(solution(scoville_list, 7))

## 효율성 꽝
