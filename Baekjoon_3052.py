numbers=[]
for i in range(10):
    a=int(input())    
    numbers.append(a%42)

print(len(set(numbers)))