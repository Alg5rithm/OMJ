def solution(record):
    answer = []
    userInfo = {}
    for item in record:
        record_list = item.split()
        if record_list[0] == "Enter":
            userInfo[record_list[1]] = record_list[2]
        elif record_list[0] == "Change":
            userInfo[record_list[1]] = record_list[2]
    for item in record:
        record_list = item.split()
        if record_list[0] == "Enter":
            answer.append(userInfo[record_list[1]] + "님이 들어왔습니다.")
        elif record_list[0] == "Leave":
            answer.append(userInfo[record_list[1]] + "님이 나갔습니다.")

    return answer


data = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo",
        "Change uid4567 Ryan"]
print(solution(data))
