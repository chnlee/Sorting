import sys

N = int(sys.stdin.readline())

count = [0] * 10001

for i in range(N):
  i = int(sys.stdin.readline())
  count[i] +=1 

for i in range(len(count)):
  for j in range(count[i]):
    print(i)
