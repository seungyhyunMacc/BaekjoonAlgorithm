a=int(input())

number=0
answer=0
answer_list=''

for i in range(a):
    result=list(input())
    for j in result:
        if(j=='O'):
            number +=1
            answer +=number
        else:
            number=0
    answer_list+=str(answer)
    if i != a-1:
        answer_list+='\n'
    number=0
    answer=0
    

print(answer_list)