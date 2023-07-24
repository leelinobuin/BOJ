T = int(input())
for j in range (T):
  a, b = input().split()
  a = int(a)
  b = list(b)
  for i in range (len(b)):
    print(a*b[i], end='')
  print()