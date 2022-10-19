y,m,d=map(int,input().split())
y1,m1,d1=map(int,input().split())
sum=0
if m<m1: sum=y1-y
elif m==m1 and d<=d1: sum=y1-y
else: sum=y1-y-1
print(sum)
print(y1-y+1)
print(y1-y)