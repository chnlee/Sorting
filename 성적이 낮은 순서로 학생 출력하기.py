N = int(input())
array = []
for i in range(N):
  a = input().split()
  array.append((a[0],int(a[1])))

array = sorted(array, key = lambda student: student[1])
print(array)
for student in array:
  print(student[0])