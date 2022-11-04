'''
선택 정렬 : 가장 작은 것을 선택해서 제일 앞으로 보내기
min  # 가장 작은 것을 반복적으로 선택하기 위함 , 우선적으로 아주 큰 값 초기화
index # 가장 작은 원소가 있는 위치
temp # 임시 저장
'''

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i #가장 작은 원소의 인덱스
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i],array[min_index] = array[min_index],array[i] #swap

'''
array = [1, 10, 4, 6, 8, 3, 2, 5, 9, 7 ]

for i in range(10):
    # 탐색하면서 가장 작은 값을 선택하는 과정
    min = 99999
    for j in range(i,10):
        if min > array[j] :
            min = array[j]
            index = j # 가장 작은 값의 인덱스를 저장
    #swap
    tmp = array[i]
    array[i] = array[index]
    array[index] = tmp

print(array)

'''

'''
비교 연산을 10 + 9 + 8 + 7 + 6+ ... + 2만큼 함
=> N( N+1)/2
시간 복잡도 => O(N*N)
        
'''

