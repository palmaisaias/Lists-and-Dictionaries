# Task 1

# Implement a function to merge two dictionaries, preserving the values of common keys from the second dictionary. 
# Analyze the time complexity of this operation.

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

# The time it takes to combine the dictionaries is relative to their length so this would be O(n). Also, the value from the duplicate
# key in the second dictionary simply replaces the value of the key in the first dictionary. Now, the printing portion does depend on the
# length of the dictionaries as well since it would take longer the longer the list of key value pairs, not sure if it would make it a lesser
# time efficiency ranking

def combine_dict(a,b):
    a.update(b)
    print(a)
print(combine_dict(dict_1,dict_2))

# Task 2

# Implement a function to find the intersection of two dictionaries, i.e., keys common to both dictionaries along with their values.
# Analyze the time complexity of this operation.

dessert_1 = {
'pie': 'apple',
'ice_cream': 'moose tracks',
'cobbler': 'peach',
'cake': None
}

dessert_2 = {
'dinner': 'turkey',
'ice_cream': 'vanilla',
'appetizer': 'soup',
'cobbler': 'peach'
}

# The function takes each key value pair in the first dictionary and comares it to each key value pair in the second one. This would
# make it O(n) or linear time complexity because the longer the first dictionary the longer this function will take to execute.

def cross (a,b):
    intersection = {}
    for key, value in a.items():
        if key in b and b[key] == value:
            intersection[key] = value
    return intersection
print(cross(dessert_1,dessert_2))