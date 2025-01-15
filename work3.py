#Question
def remove_duplicates_and_sort(input_list):
    return sorted(set(input_list))

input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(remove_duplicates_and_sort(input_list))

#Question 2
def double_tuple(input_tuple):
    return tuple(x * 2 for x in input_tuple)

input_tuple = (1, 2, 3, 4)
print(double_tuple(input_tuple))

#Question 3

def highest_grade_student(grades):
    return max(grades, key=grades.get)

grades = {"John": 85, "Mary": 92, "Alex": 89}
print(highest_grade_student(grades))

#Question 4

def find_intersection(set1, set2):
    return set1 & set2

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(find_intersection(set1, set2))

#Question 5

def combine_frozen_sets(frozen_sets):
    result = frozenset().union(*frozen_sets)
    return result

frozen_set1 = frozenset([1, 2, 3])
frozen_set2 = frozenset([3, 4, 5])
frozen_sets = [frozen_set1, frozen_set2]
print(combine_frozen_sets(frozen_sets))

#Question 6

from collections import ChainMap

def merge_dicts(dict1, dict2):
    merged = ChainMap(dict1, dict2)
    return dict(merged)

dict1 = {"name": "John", "age": 25}
dict2 = {"city": "New York", "country": "USA"}
print(merge_dicts(dict1, dict2))

#Question 7

from collections import deque

def manipulate_deque(dq):
    dq.append(4)        
    dq.appendleft(0)    
    dq.pop()            
    dq.popleft()        
    return dq

dq = deque([1, 2, 3])
print(manipulate_deque(dq))
