def solution(babbling):

    count = 0

    for b in babbling:
        if 'ayaaya' not in b and 'yeye' not in b and 'woowoo' not in b and 'mama' not in b:
            b = b.replace('aya', '1')
            b = b.replace('ye', '2')
            b = b.replace('woo', '3')
            b = b.replace('ma', '4')
            if b.isdigit():
                count += 1

    return count
