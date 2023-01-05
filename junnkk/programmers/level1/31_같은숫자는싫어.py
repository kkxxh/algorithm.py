def solution(arr):
    answer = [arr[0]]

    for a in arr:
        if answer[-1] != a:
            answer.append(a)

    return answer

    # 실패 코드 1 -> set은 중복된 원소를 제거하지만 값에 순서가 없다
    # return list(set(arr))
