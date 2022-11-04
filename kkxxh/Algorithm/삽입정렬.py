'''
삽입 정렬: 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입
1) 첫번째 데이터가 정렬되었다고 가정
2) 다음 데이터가 첫번째 데이터보다 작으면 첫번째 데이터의 왼쪽에 위치, 아니면 오른쪽에 위치
3) 다음 데이터가 바로 왼쪽 데이터보다 크면 내버려두기
'''

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i,0,-1): #인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j-1]: #한 칸씩 왼쪽으로 이동
            array[j],array[j-1] = array[j-1],array[j] #swap
        else : #자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break
print(array)

'''
시간 복잡도 -> O(N*N) #반복문 두번 중첩
현재 리스트의 데이터가 거의 정렬되어 있는 상태(최선의 경우) 라면 매우 빠르게 동작 => 시간복잡도 O(N)

'''