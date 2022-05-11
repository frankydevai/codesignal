def solution(s1, s2):
    list_l = list(s1)

    ls_2 = list(s2)
    count = 0
    for i in list_l:
        if i in ls_2:
            count += 1
            ls_2.remove(i)
    return count