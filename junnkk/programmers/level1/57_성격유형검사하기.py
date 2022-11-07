def solution(survey, choices):
    personality = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}

    for i, s in enumerate(survey):
        if s == "RT":
            if choices[i] < 4:
                personality['R'] += 4-choices[i]
            else:
                personality['T'] += choices[i] - 4
        elif s == "TR":
            if choices[i] < 4:
                personality['T'] += 4-choices[i]
            else:
                personality['R'] += choices[i] - 4
        elif s == "FC":
            if choices[i] < 4:
                personality['F'] += 4-choices[i]
            else:
                personality['C'] += choices[i] - 4
        elif s == "CF":
            if choices[i] < 4:
                personality['C'] += 4-choices[i]
            else:
                personality['F'] += choices[i] - 4
        elif s == "MJ":
            if choices[i] < 4:
                personality['M'] += 4-choices[i]
            else:
                personality['J'] += choices[i] - 4
        elif s == "JM":
            if choices[i] < 4:
                personality['J'] += 4-choices[i]
            else:
                personality['M'] += choices[i] - 4
        elif s == "AN":
            if choices[i] < 4:
                personality['A'] += 4-choices[i]
            else:
                personality['N'] += choices[i] - 4
        elif s == "NA":
            if choices[i] < 4:
                personality['N'] += 4-choices[i]
            else:
                personality['A'] += choices[i] - 4

    answer = ''
    if personality['R'] >= personality['T']:
        answer += 'R'
    else:
        answer += 'T'
    if personality['C'] >= personality['F']:
        answer += 'C'
    else:
        answer += 'F'
    if personality['J'] >= personality['M']:
        answer += 'J'
    else:
        answer += 'M'
    if personality['A'] >= personality['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer
