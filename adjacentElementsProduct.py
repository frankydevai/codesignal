def solution(inputArray):
    a = []
    for i in range(len(inputArray) - 1):

       a.append(inputArray[i] * inputArray[i + 1])
    return(max(a))
