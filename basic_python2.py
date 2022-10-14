
'''
DRY is better than WET
'''

import math

def ugly_square(number):
    '''Returning the square of a certain number
    '''
    return number * number

def normal_square(num):
    '''Returning the square of a number using the library math
    '''
    return num**2

def cartesian_to_polar(x, y):
    '''Transforming bidimensional cartesian variables into polars
    '''
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return r, theta

print(ugly_square(2.))
print(normal_square(4.))
print(cartesian_to_polar(3., 7.5))