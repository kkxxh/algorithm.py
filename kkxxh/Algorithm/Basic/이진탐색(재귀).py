
'''
이진탐색 : 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
    -> 이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정합니다.
순차탐색 : 리스트 안에 들어 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법


이진 탐색 동작 예시
step 1 - 시작점, 끝점, 중간점 = (시작점+끝점)/2 (소주점 이하 제거)
step 2 - 찾는 값과 중간값을 비교 -> 필요 없는 부분은 더 이상 확인하지 않음
step 3 - 범위 줄이기

'''
#재귀적 코드
def binary_search(array, target, start, end):
    if start>end:
        return None
    mid = (start+end) //2
    #찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    elif array[mid] >target:
        return binary_search(array,target, start, mid-1)
    else :
        return binary_search(array, target, mid+1,end)

# n(원소의 개수)과 target(찾고자 하는 값)을 입력받기
n, target = list(map(int,input().split()))
#전체 원소 입력 받기
array = list(map(int,input().split()))

#이진 탐색 수행 결과 출력
result = binary_search(array,target,0, n-1)

if result == None:
    print("원소가 존재하지 않습니다.")
else :
    print(result +1)


'''
시간 복잡도 : O(logN)
연산 횟수는 log2N에 비례
'''