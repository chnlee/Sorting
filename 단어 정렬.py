N = int(input())
array = []
for i in range(N):
  a = input()
  b = len(a)
  array.append((a,b))
array = set(array)
result = (sorted(array,key = lambda x : (x[1],x[0])))

for i in result:
  print(i[0])