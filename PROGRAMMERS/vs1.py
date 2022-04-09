def solution(user_times, T):
    max_value = max(user_times)
    origin_T = T
    while T < max_value:
        T += T

    for i in range(len(user_times)):
        user_times[i] = (T - user_times[i]) % origin_T

    return max(user_times)