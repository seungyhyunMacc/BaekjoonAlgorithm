from posixpath import split


s=input()
s=s.upper()
compare=list(set(s))

max=0

for i in compare:
    b=s.count(i)
    if b>max:
        max=b
        answer=i
    elif b==max:
        answer='?'
print(answer)
