s=list(input().strip().split(' '))

if '' in s:
    print(len(s)-1)
else:
    print(len(s))