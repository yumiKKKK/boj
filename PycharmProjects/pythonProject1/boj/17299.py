n=int(input())
a=list(map(int, input().split()))
#등장횟수
F=[]
for i in a:
    F.append(a.count(i))
#오등큰수
ngf=[]
for i in range(n-1):
    k=i
    for j in range(i+1, n):
        if F[j]>F[k]:
            k=j
            print(a[k], end=" ")
            break
    if k==i:
        print(-1, end=" ")









