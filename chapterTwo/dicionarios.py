# its another fundamental data structure in python, its a collection of key value pairs, its also called associative array or hash map in other programming languages, its a mutable data type, it can be changed after its creation, it is unordered, it does not maintain the order of the elements, it is indexed by keys, it can be created using curly braces {} or the dict() constructor.

empty_dict = {}

empty_dict2 = dict()

grades = {'gabriel': 10, 'Nicoly':10}

gabriel_grades = grades['gabriel']

#if the key does not exist, it will raise a KeyError
try:
    maria_grades = grades['maria']
except KeyError: print('Maria is not in the grades dictionary')

#instead of raising a KeyError, you can use the 'in' method

gabriel_has_grades = 'gabriel' in grades
maria_has_grades = 'maria' in grades

# in python, we have other form to access the value of a key, using the 'get' method, this method will return None if the key does not exist, instead of raising a KeyError

gabriel_grades = grades.get('gabriel')
maria_grades = grades.get('maria')
no_one_grades = grades.get('no_one')

# we can add pairs of key value using ''[]'' operator
grades['maria'] = 10

num_of_students = len(grades)

# we see something in the first chapter, the dictionary represent structured data

person = {"Gabriel": {"City": "Sao Paulo", "Age": 23}, "Nicoly": {"City": "Sao Paulo", "Age": 24}}