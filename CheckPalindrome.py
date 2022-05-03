def solution(inputString):
    string = inputString

    if string[::-1] == string:
        return True
    else:
        return False
