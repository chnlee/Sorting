N = int(input())
array = []
for i in range(N):
  number = int(input())
  array.append(number)

for i in range(len(array)):
  min_index = i
  for j in range(i+1,len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i]

for i in range(len(array)):
  print(array[i])