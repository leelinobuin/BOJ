N, X = map(int, input().split())
li = [*map(int, input().split())]
for i in reversed(range (N)):
  if (li[i]>=X):
    del li[i]
print(*li)