total=1
for i in range(3):
    a=int(input())
    total*=a

total_list=list(map(int, str(total)))
print(total_list)

for i in range(10):
    print(total_list.count(i))