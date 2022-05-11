def solution(n):
    lst = []
    for i in str(n):
        lst.append(int(i))
    lst_1 = []
    for i in range(len(lst) // 2):
        lst_1.append(lst[int(i)])
    print(lst_1)
    lst2 = []
    for i in range(len(lst) // 2, len(lst)):
        lst2.append(lst[int(i)])
    print(lst2)
    if sum(lst_1) == sum(lst2):
        return True
    else:
        return False

