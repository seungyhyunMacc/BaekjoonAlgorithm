answer=''
while(1):
    try:
        a, b=map(int, input().split())
        answer += str(a+b)
        answer+='\n'
    except:
        answer = answer.strip('\n')
        break
print(answer)