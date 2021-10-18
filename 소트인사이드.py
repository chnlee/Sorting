array = input()
_list = []
for i in range(len(array)):
  _list.append(int(array[i]))

_list.sort(reverse=True)

for j in range(len(_list)):
  print(_list[j],end="")