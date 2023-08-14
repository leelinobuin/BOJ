N = int(input()) #4
l = list(map(int, input().split())) # 1 3 5 7
s = 0
def isprime(x): # 5
  
    if x <= 1: 
      return False
    for i in range(2, x): # 2345
      if x % i == 0:
        return False
    return True
for i in range (N):  # 0123
  if (isprime(l[i]) == True):
    s += 1  
print(s)
