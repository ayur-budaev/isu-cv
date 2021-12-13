import numpy as np
from sys import argv

if argv[1] is None:
  exit(-1)

filename = argv[1]

with open(filename, 'r') as f:
  nominal_width = float(f.readline())

if nominal_width == 0:
  print('No objects')
  exit(0)

matrix = np.loadtxt(filename, skiprows=2)
min_x, min_y, max_x, max_y = matrix[0].shape[0], matrix[0].shape[0], 0, 0

for y in range(matrix.shape[0]):
  for x in range(matrix.shape[1]):
      
    if matrix[y, x] == 1:
      if x < min_x:
        min_x = x
        
      if y < min_y:
        min_y = y
        
      if x > max_x:
        max_x = x
        
      if y > max_y:
        max_y = y

obj_size = max_x - min_x + 1, max_y - min_y + 1

print('Nominal Image Size: ', matrix.shape[1] * nominal_width / obj_size[0])