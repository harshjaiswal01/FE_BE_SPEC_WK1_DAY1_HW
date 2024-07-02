# Task 1

# Implement a function to merge two dictionaries, preserving the values of common keys from the second dictionary. Analyze the time complexity of this operation.


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
    merged_dic = {}
    for key in adic: #O(n) Linear
        merged_dic[key]= adic[key] #O(1) Constant
    for key in bdic:
        merged_dic[key] = bdic[key]
    print(merged_dic)

solution(dict_1, dict_2)

# This is has O(n) Linear Space and Time Complexity


