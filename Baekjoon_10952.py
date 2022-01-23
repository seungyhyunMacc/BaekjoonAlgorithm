answer=''

while(1):
    a, b=map(int, input().split())
    if a==0 and b==0:
        answer=answer.strip('\n')
        break
    else:
        answer += str(a+b)
        answer +='\n'
        
print(answer)