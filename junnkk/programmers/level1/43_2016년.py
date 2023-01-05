import datetime

def solution(a, b):
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']

    dt1 = datetime.datetime(2016, 1, 1)

    dt2 = datetime.datetime(2016, a, b)

    return day[(dt2-dt1).days % 7]
