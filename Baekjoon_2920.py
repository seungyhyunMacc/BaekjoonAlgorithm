compare= list(map(int, input().split()))

if(compare==sorted(compare, reverse=False)):
    print('ascending')
elif(compare==sorted(compare, reverse=True)):
    print('descending')
else:
    print('mixed')
    