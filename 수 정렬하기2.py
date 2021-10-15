import sys
sys.setrecursionlimit(10 ** 4)

N = int(input())
array = []
for i in range(N):
  a = int(input())
  array.append(a)

# def quickSort(array,start,end):
#   pivot = start
#   left = start + 1
#   right = end
#   if start >= end:
#     return
#   while left <= right:
#     while left <=end and array[left] <= array[pivot]:
#       left += 1
#     while right > start and array[right] >= array[pivot]:
#       right -= 1
#     if left >= right:
#       array[right],array[pivot] = array[pivot], array[right]
#     else:
#       array[left], array[right] = array[right], array[left]
#   quickSort(array,start,right-1)
#   quickSort(array,right+1,end)

# def quickSort(array):
#   if len(array) <= 1:
#     return array
  
#   pivot = array[0]
#   tail = array[1:]

#   left_side = [ x for x in tail if x <= pivot]
#   right_side = [ x for x in tail if x > pivot]

#   return quickSort(left_side) + [pivot] + quickSort(right_side)


# for i in quickSort(array):
#   print(i)

# quickSort(array,0,len(array)-1)

# for i in array:
#   print(i)

for i in sorted(array):
  print(i)