def solution(n, arr1, arr2):

    answer = []

    for i in range(n):
        bin_arr = str(int(str(bin(arr1[i])[2:]))+int(str(bin(arr2[i])[2:])))

        if len(bin_arr) < n:
            bin_arr = "0"*(n-len(bin_arr)) + bin_arr

        bin_arr = bin_arr.replace('0', ' ')
        bin_arr = bin_arr.replace('1', '#')
        bin_arr = bin_arr.replace('2', '#')

        answer.append(bin_arr)

    return answer
