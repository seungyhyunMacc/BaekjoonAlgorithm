number=int(input())

answer=''
for i in range(number):
    a, b=map(int, input().split())
    answer += str(a+b)
    if i < number-1:
        answer +='\n'
    else:
        continue
print(answer)
    