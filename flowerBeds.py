'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

array = [0,1,0,1,1,1] n=2

[1,0,0,1] n = 1


1. scope = come up with unique examples
'''

def planted(array, n):
  # edge case
    if i == 0:
        if array[i] == 0 and array[i +1] == 0:
      	    n -= 1
  
  # general case
    for i in range(1, len(array) - 2):  
        if array[i-1] == 0 and array[i] == 0 and array[i+1] == 0:
            n -= 1
    
  # edge case
    if i == len(array) - 1:
        if array[i-1] == 0 and array[i-2] == 0:
            n -=1
    
    if n == 0:
      return True
    return False