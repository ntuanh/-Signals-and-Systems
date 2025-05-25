import numpy as np

# input in here

y = [1 , -3 , 2]
y_condition = [1 , -1/3 , -4/9]

y = np.array(y)
n = len(y)
Compute_Y = np.zeros((n , n))

# assign
for i in range(len(y_condition)):
  Compute_Y[i: , i] = y_condition[i]

y = y.reshape((1 ,-1))
Compute_Y = np.transpose(y)*Compute_Y

Compute_Z = []
for i in range(n - 1):
  sum = 0
  for j in range( 1 , n - i  , 1):
    sum += Compute_Y[j + i][j]
  Compute_Z.append(sum)

Compute_Z = np.array(Compute_Z)

print(f"Y(Z) * {Compute_Y[: ,0]}")
for i in range(n -1):
  print(f"Z^{i*-1} : {Compute_Z[i]}")
