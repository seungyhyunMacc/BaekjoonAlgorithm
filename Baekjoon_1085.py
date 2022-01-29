a, b, c, d=map(int, input().split())
x_y1=[]
x_y2=[]

x_y1.append(a)
x_y1.append(b)
x_y2.append(c)
x_y2.append(d)

answer=[]
for i in range(len(x_y2)):
    answer.append(x_y2[i]-x_y1[i])
    answer.append(x_y1[i]-0)

print(min(answer))
