'''
선입선출
'''

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)

queue.poplift()
queue.append(1)
queue.append(4)
queue.poplift()

print(queue)#먼저 들어온대로 출력
queue.reverse()#다음 출력을 위해 역순으로바꾸기
print(queue)#나중에 들어온 원소부터 출력

