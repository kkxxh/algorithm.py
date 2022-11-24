import math


def solution(arr):
    gcd = 0
    lcd = arr[0]

    for i in range(1, len(arr)):
        gcd = math.gcd(lcd, arr[i])
        lcd = lcd*arr[i]//gcd

    return lcd
