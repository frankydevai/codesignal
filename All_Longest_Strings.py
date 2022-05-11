def solution(er):
    d = []

    for i in er:
        d.append(i)
    for i in range(len(d)):
        l = min(d, key=len)
        if l != max(d, key=len):
            d.remove(l)
    return d
