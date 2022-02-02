import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
numbers=[]
compared=[]
answers=[]
count = 0
impossible=True

for i in range(n):
    a = int(sys.stdin.readline().rstrip())

    while count < a:
        count += 1
        compared.append(count)
        answers.append('+')
    
    if compared[-1] == a:
        compared.pop()
        answers.append('-')
    else:
        impossible=False
        

if impossible == False:
    print('NO')
else:
    print("\n".join(answers))   ## join함수 \n으로 구분


