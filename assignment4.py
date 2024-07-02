# Task 2

# Implement a function to find the intersection of two dictionaries, 
# i.e., keys common to both dictionaries along with their values. Analyze the time complexity of this operation.

dict_1 = {
'pie': 'apple',
'ice_cream': 'moose tracks',
'cobbler': 'peach',
'cake': None
}

dict_2 = {
'dinner': 'turkey',
'ice_cream': 'vanilla',
'appetizer': 'soup',
'cobbler': 'peach'
}

def solution(adic, bdic):
    intersection = {}
    for key in adic: #O(n) Linear
        if key in bdic: #O(1) Constant
            if adic[key] == bdic[key]: #O(1) Constant
                intersection[key] = adic[key] #O(1) Constant

    return intersection

print(solution(dict_1, dict_2))

#O(n) Linear is the Time and complexity