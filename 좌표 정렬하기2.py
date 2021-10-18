N = int(input())
array = []
for i in range(N):
  a,b = map(int,input().split())
  array.append((a,b))
result = sorted(array,key = lambda x : (x[1],x[0]))

for i in result:
  print(i[0],i[1])