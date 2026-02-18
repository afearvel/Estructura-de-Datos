A = [[5,6,13],[3,10,1],[2,11,3]]
B = [[1,2,17],[6,5,15],[3,11,12]]

c = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            c[i][j] += A[i][k] * B[k][j]

print(c)


C = [[sum(A[i][k]*B[k][j] for k in range(len(B)))
      for j in range(len(B[0]))]
      for i in range(len(A))]

print(C)
