import math

class vector2d:
 def __init__(self, x, y):
  self.x = x
  self.y = y
 
 def print_coordinates(self):
  print(f'{self.vector2d(self.x, self.y)}') #REVISAR ESTO Y ACLARARME
 
 def module(self):
  return math.sqrt(self.x**2 + self.y**2)

if __name__ == '__main__':
 v = vector2d(1., 1.)
 print(v)
 v.print_coordinates()
 print(f'The module of the vector v is {v.module():.7f}')
 print(f'The value of pi is approximately {math.pi:.9f}.')