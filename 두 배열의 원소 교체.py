N, K = map(int,input().split())

sum = 0
#이조건을 기억할 것.
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort(reverse = True)

for i in range(K):
  if A[i] < B[i]:
    A[i], B[i] = B[i], A[i]
  else:
    break

for i in range(len(A)):
  sum += A[i]

print(sum)
