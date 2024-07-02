# Task 1

# Implement a function to create a new list using list comprehension that contains squares of numbers from 1 to n, 
# where n is a parameter. Analyze the time and space complexity of this operation.

def solution(num):
    alist = []
    i = 1
    while i <= num:
        isquare = i * i #O(1) Constant
        alist.append(isquare) #O(1) Constant
        i += 1 #O(1) Constant
    return alist 

print(solution(10))

# Time Complexity is O(n) : Linear
# Space Complexity is O(n) : Linear

