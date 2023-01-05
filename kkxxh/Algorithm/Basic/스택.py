'''
선입선출 구조 또는 후입 선출 구조
입구와 출구가 동일한 형태
'''

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)#최하단 원소부터 출력
print(stack[::-1])#최상단 원소부터 출력