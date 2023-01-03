# 전화번호 목록

def solution(phone_book):
    answer = True
    
    phone_book.sort()
    
    for i in range(0,len(phone_book)-1):
        if len(phone_book[i])>len(phone_book[i+1]):
            continue
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break
        if answer == False:
            break
        
    return answer
