def solution(year):
    year = year
    century = 100

    if year % century:
        return (year // 100) + 1
    else:
        return year // 100
