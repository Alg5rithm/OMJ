import re


def solution(str1, str2):
    # 대/소문자 통일
    str1 = str1.upper()
    str2 = str2.upper()

    # 공백, 숫자, 특수문자 제외
    str1_str = list(filter(bool, re.split('[^A-Z]', str1)))
    str2_str = list(filter(bool, re.split('[^A-Z]', str2)))

    str1_list = []
    str2_list = []

    # 리스트형태로 저장
    for item in str1_str:
        for j in range(0, len(item) - 1):
            str1_list.append(item[j:j + 2])
    for item in str2_str:
        for j in range(0, len(item) - 1):
            str2_list.append(item[j:j + 2])

    # 리스트가 빈 경우
    if len(str1_list) == 0 and len(str2_list) == 0:
        answer = 65536
    else:
        a_temp = str1_list.copy()
        a_result = str1_list.copy()

        for i in str2_list:
            if i not in a_temp:
                a_result.append(i)
            else:
                a_temp.remove(i)

        result = []

        for i in str2_list:
            if i in str1_list:
                str1_list.remove(i)
                result.append(i)

        answer = int((len(result) / len(a_result)) * 65536)

    return answer

str1 = "A+C"
str2 = "DEF"
print(solution(str1, str2))
