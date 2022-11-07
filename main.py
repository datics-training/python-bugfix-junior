'''
I am trying to filter out empty arrays from an array. In other words, I want to transform something that looks like this: 
["a", "b", [], [], [1, 2, 3]] to look like ["a", "b", [1, 2, 3]]. 
My code is the function 'remove_empty_arrays' as given below.

However, it seems that I've run into a problem, with an error message of object of type 'int' has no len(). Fix my code so that all tests pass.

What I want:
remove_empty_arrays([1, 2, [], 4]) ➞ [1, 2, 4]
'''

def remove_empty_arrays(arr):
  return [x for x in arr if len(x) != 0]


remove_empty_arrays([1, 2, [], 4])

