N = int(input())
array = []
for i in range(N):
  i = int(input())
  array.append(i)

array.sort(reverse = True)

for i in range(len(array)):
  print(array[i])