import sys
n, m = map(int, input().split())
Lans = [int(sys.stdin.readline().strip()) for i in range(n)]

start=1
end=max(Lans)
result=0

def binary_lan(array, target, start, end):
    global result
    if start > end:
        return None
    
    while start <= end:
        count=0
        mid = ((start + end) // 2)
        
        for i in array:
            if i >= mid:
                count += (i//mid)
        
        if count < target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result

print(binary_lan(Lans, m, start, end))