a, b = map(int, input().split())

if (b<45):
    b = b + 60 - 45
    a -=1
    if (a<0):
        a=23
else:
    b -= 45

print(a, b)