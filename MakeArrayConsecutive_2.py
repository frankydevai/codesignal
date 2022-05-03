def solution(statues):
    add = 0
    for i in range(min(statues), max(statues)):
        if i not in  statues:
            add += 1
    return add