import re as regex # used for working with regular expressions, which are a powerful tool for searching and manipulating strings. We can use the regex module to compile regular expressions, search for patterns in strings, and perform various operations on strings using regular expressions.

my_regex = regex.compile("[0-9] + " ,regex.I)

import matplotlib.pyplot as plt # used for plotting data, and creating visualizations. We can use the plt alias to access the functions and classes of the matplotlib.pyplot module.

plt.plot()

from collections import Counter,defaultdict # used for counting hashable objects, and for creating dictionaries with default values. We can use the Counter class to count the occurrences of elements in a collection, and the defaultdict class to create dictionaries that return a default value when a key is not found.
 
lookup = defaultdict(int)
my_counter = Counter()

#but in this chapter we will focus on the built-in functions and modules that are available in Python, and how to use them effectively in our code. We will also explore some of the best practices for writing clean and efficient code, and how to use the Zen of Python as a guide for writing better code.