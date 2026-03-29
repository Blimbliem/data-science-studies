# Default dict is a subclass of the built-in dict class. It is a dictionary that provides a default value for a key that does not exist. It is useful when you want to avoid KeyError when accessing a key that does not exist in the dictionary. The default value is specified by a function that is passed as an argument to the defaultdict constructor.


# 'document' is an example 

words_count = {}
for word in document:
    if word in words_count:
        words_count[word] += 1
    else: words_count[word] = 1

words_counts = {}
for word in document:
    try:
        words_counts[word]+=1
    except KeyError:
        words_counts[word] = 1

words_count2 = {}
for word in document: 
    previous_count = words_count2.get(word,0)
    words_count2[word] = previous_count + 1

# we can use the defaultdict to simplify the code above

# first we need to import the defaultdict class from the collections module

from collections import defaultdict

words_count3 = defaultdict(int) # int() will return 0 as the default value for any key that does not exist in the dictionary

words_count3[word] += 1 

# some useful functions

dd_list = defaultdict(list) # list() will return an empty list as the default value for any key that does not exist in the dictionary

dd_list[2].append(1)
print(dd_list)

dd_dict = defaultdict(dict) # dict() will return an empty dictionary as the default value for any key that does not exist in the dictionary

dd_dict["Gabriel"]["City"] = "Sao Paulo"

dd_pair = defaultdict(lambda: [0,0])

dd_pair[2,1] = 1 
