numbers= list(map(int, input().split()))
sum=0

for i in numbers:
    sum = sum + (i*i)
print(sum%10)