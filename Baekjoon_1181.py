import imp


import sys

number=int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(number)]
ProcessData = set(data) 
CompleteData = list(ProcessData) 
CompleteData.sort()
CompleteData.sort(key=len)

for i in range(len(CompleteData)):
    print(CompleteData[i])
