def solution(array, commands):
    answer = []
    for item in commands:
        commands_list = item
        array_list = array[commands_list[0] - 1:commands_list[1]]
        array_list.sort()
        answer.append(array_list[commands_list[2] - 1])
    return answer
