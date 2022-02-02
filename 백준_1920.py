import sys
n = int(sys.stdin.readline().rstrip())
StandardLst=list(map(int, input().split()))

m = int(sys.stdin.readline().rstrip())
ComparedLst=list(map(int, input().split()))

StandardLst.sort()
def binary_search(array1, target, start, end):
    if start> end:
        return None
    while start <= end:
        mid = (start + end) // 2

        if array1[mid]==target:  ## 리턴1 을 하고 끝
            return 1
        elif array1[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in range(m):
    start=0
    end=n-1
    if binary_search(StandardLst, ComparedLst[i], start, end) == 1:
        print(1)
    else:
        print(0)

