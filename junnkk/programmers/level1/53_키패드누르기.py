def solution(numbers, hand):
    answer = ''

    keypad = {1: (0, 0), 2: (0, 1), 3: (0, 2),
              4: (1, 0), 5: (1, 1), 6: (1, 2),
              7: (2, 0), 8: (2, 1), 9: (2, 2),
              '*': (3, 0), 0: (3, 1), '#': (3, 2)}

    left, right = keypad['*'], keypad['#']

    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            left = keypad[num]
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
            right = keypad[num]
        else:
            left_distance = abs(left[0]-keypad[num][0]) + abs(left[1]-keypad[num][1])
            right_distance = abs(right[0]-keypad[num][0]) + abs(right[1]-keypad[num][1])

            if left_distance < right_distance:
                answer += 'L'
                left = keypad[num]
            elif left_distance > right_distance:
                answer += 'R'
                right = keypad[num]
            else:
                if hand == 'left':
                    answer += 'L'
                    left = keypad[num]
                else:
                    answer += 'R'
                    right = keypad[num]

    return answer
