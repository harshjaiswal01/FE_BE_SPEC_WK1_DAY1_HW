# Task 2

# Implement a function to merge two pre-sorted lists into a single sorted list. Analyze the time complexity of this operation.

def solution(alist, blist):
    merged_list = []
    i = 0
    j = 0

    while i < len(alist) and j < len(blist): #O(n) Linear
        if alist[i] < blist[j]: #Linear O(n)
            merged_list.append(alist[i]) #Constant O(1)
            i += 1
        else:
            merged_list.append(blist[j]) #Constant O(1)
            j += 1

    while i < len(alist): #O(n) Linear
        merged_list.append(alist[i]) #Constant O(1)
        i += 1

    while j < len(blist): #O(n) Linear
        merged_list.append(blist[j]) #constant O(1)
        j += 1
    
    return merged_list #Constant O(1)

alist = [1, 2, 3, 4,5, 6]
blist = [4, 6, 7, 8, 9,10, 11, 12, 13]

print(solution(alist, blist))

# I would say this is Linear O(n)