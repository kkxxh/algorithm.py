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




# 참고 코드 
# 문자열의 startwith() 함수

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True