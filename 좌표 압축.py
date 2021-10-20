import sys

N = int(sys.stdin.readline())
array = list(map(int,sys.stdin.readline().split()))
sort_arr = sorted(set(array))
# enumerate -> 번호와 value를 각각 따로 매기는 것
arr = {i:v for v,i in enumerate(sort_arr)}
for i in array:
  print(f'{arr[i]}')