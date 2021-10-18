N = int(input())
array = []
for i in range(N):
  a,b = input().split()
  a = int(a)
  array.append((a,b))

result = (sorted(array,key = lambda x : x[0]))

for i in result:
  print(i[0],i[1])