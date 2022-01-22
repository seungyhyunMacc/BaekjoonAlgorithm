a, b = map(int, input().split())
compare=[]
compare.append((int(str(a)[::-1])))
compare.append((int(str(b)[::-1])))
print(max(compare))