import numpy as np
from math import sqrt

def find_highest_point(matrix):
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

  return min_x, min_y

with open('img1.txt', 'r') as f:
  nominal_width1 = float(f.readline())

with open('img2.txt', 'r') as f:
  nominal_width2 = float(f.readline())

if nominal_width1 == 0 or nominal_width2 == 0 or nominal_width1 != nominal_width2:
  print('No objects')
  exit(0)

matrix1 = np.loadtxt('img1.txt', skiprows=2)
matrix2 = np.loadtxt('img2.txt', skiprows=2)

x1, y1 = find_highest_point(matrix1)
x2, y2 = find_highest_point(matrix2)

print('Image offset:', sqrt((x1-x2)**2+(y1-y2)**2))