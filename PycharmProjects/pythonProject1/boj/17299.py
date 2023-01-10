from collections import Counter
from sys import stdin
n=int(stdin.readline())
a=list(map(int, stdin.readline().split()))
#등장횟수
F=Counter(a)

stack=[]
ans=[-1]*n
#오등큰수
for i in range(n):
    while(stack and F[a[stack[-1]]]<F[a[i]]):
        ans[stack.pop()]=a[i]
    stack.append(i)

print(*ans)








