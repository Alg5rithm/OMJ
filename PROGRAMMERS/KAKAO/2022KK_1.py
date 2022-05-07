dic = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0, }


def solution(survey, choices):
    answer = ''
    for i in range(len(survey)):
        if choices[i] == 4:
            continue
        elif choices[i] < 4:
            question = survey[i][0:1]
            if choices[i] == 1:
                dic[question] += 3
            elif choices[i] == 2:
                dic[question] += 2
            else:
                dic[question] += 1
        else:
            question = survey[i][1:2]
            if choices[i] == 5:
                dic[question] += 1
            elif choices[i] == 6:
                dic[question] += 2
            else:
                dic[question] += 3

    if dic['R'] >= dic['T']:
        answer += 'R'
    else:
        answer += 'T'
    if dic['C'] >= dic['F']:
        answer += 'C'
    else:
        answer += 'F'
    if dic['J'] >= dic['M']:
        answer += 'J'
    else:
        answer += 'M'
    if dic['A'] >= dic['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer
