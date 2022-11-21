s = input()

alpha = []
digit = 0
for i in s:
    if i.isalpha():
        alpha.append(i)
    elif i.isdigit():
        digit += int(i)

s = ''.join(sorted(alpha)) + str(digit)

print(s)
