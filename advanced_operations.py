# Task 1
# Implement a function to create a new list using list comprehension that contains squares 
# of numbers from 1 to n, where n is a parameter. Analyze the time and space complexity of this operation.


# I know this is not list comprehension as the task required but I didnt know how to do it with list comprehension. I still included
# it but I definitely researched the lc way and then put it together below.

# The time complexity of this would be 'O(n)' or linear since the time it takes to complete grows equally with the size of the input.
# This function uses a for loop which I beleive we mentioned was usually indicative of linear time complexity. The larger the 
# number, the more time this function will take to execute. The math portion I I think we mentioned was quick, so its the for loop
# that gives this funtion the time complexity.

def first_task(num):
    squares_list = []
    for index in range(1,num+1):
        squares_list.append(index ** 2)
    return squares_list
print(first_task(7))

# List comprehension way

# so with list comprehension I understand it to go right to left. the range is created, the for loop is executed for every number in
# that range. What the for loop is applying to every number in the range is the squaring (index ** 2). 
def lc_task(new_num):
    return [index ** 2 for index in range(1, new_num+1)]
print(lc_task(9))

# Task 2
# Implement a function to merge two pre-sorted lists into a single sorted list. Analyze the time complexity of this operation.


# This was my first attempt and as you can see  stopped after the print statement realizing I was adding an entire list into a list
# list1 = [1,2,3,4,5]
# list2 = [3,4,5,6,7]

# def merger(a,b):
#     merged = []
#     merged.append(a)
#     for num in b:
#         merged.append(num)
#     print(merged)
# print(merger(list1,list2))

# Second attempt
# This one I think works just fine, at least with the example lists. I didnt try it with letters but sorted() should work the same
# Time complexity on this one is (or should be) O(n log n). Concatanating the list is easy and fast. The time complexity comes 
# from the sorting. Its taking every element of the 'combine' list and arranging it from smallest to largest causing many shifts in the
# list
list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]

def merger(a,b):
    combine = a + b
    merged = sorted(combine)
    return merged

print(merger(list1,list2))
