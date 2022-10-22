def solution(s, n):
    answer = ''

    for i in s:
        # 공백인 경우
        if i == ' ':
            answer += ' '
        # 대문자인 경우
        elif 65 <= ord(i) <= 90:
            if ord(i)+n <= 90:
                answer += chr(ord(i)+n)
            else:
                answer += chr(ord(i)+n-90+65-1)
        # 소문자인 경우
        else:
            if ord(i)+n <= 122:
                answer += chr(ord(i)+n)
            else:
                answer += chr(ord(i)+n-122+97-1)

    # print(ord('A'))
    # print(ord('Z'))
    # print(ord('a'))
    # print(ord('z'))
    return answer
