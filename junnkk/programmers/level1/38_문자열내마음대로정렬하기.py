
def solution(strings, n):
    strings.sort()
    
    temp = {}
    
    for string in strings:
        temp[string] =string[n]
    
    temp = sorted(temp ,key=lambda x:temp[x])
    
    return temp

# 딕셔너리 정렬 방법 검색함.