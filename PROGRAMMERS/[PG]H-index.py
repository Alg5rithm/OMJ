def solution(citations):
    citations.sort(reverse=True)
    count, index = 0, 0
    while citations[index] > count:
        index += 1
        count += 1
        if index == len(citations):
            break

    return count


data_list = [10, 10, 10, 10, 10]
print(solution(data_list))
