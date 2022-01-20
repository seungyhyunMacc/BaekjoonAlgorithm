input_number=input()

TotalAnswer=''
for i in range(int(input_number)):
    answer=''
    string_number, String= input().split()
    String=list(String)
    for j in String:
        answer += j*int(string_number)
    TotalAnswer +=answer
    if(i==(int(input_number)-1)):
        print(TotalAnswer)
    else:
        TotalAnswer +='\n'
        
    