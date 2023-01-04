# 베스트앨범

# 딕셔너리 다루는 방법 익숙해지기
# 딕셔너리를 이용하여 sort하는 방법 

def solution(genres, plays):
    answer = []
    d = dict()
    genre_total = {}

    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in d:
            d[genre] = [(i, play)]
            genre_total[genre] = play
        else:
            d[genre] += [(i, play)]
            genre_total[genre] += play

    genre_total = sorted(
        genre_total, key=lambda x: genre_total[x], reverse=True)

    for g in genre_total:
        temp = sorted(d[g], key=lambda x: x[1], reverse=True)
        answer.append(temp[0][0])
        if len(d[g]) > 1:
            answer.append(temp[1][0])

    return answer


# 참고

def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer

