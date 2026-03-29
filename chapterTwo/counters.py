#Counters are a type of collection in Python that allows you to count the occurrences of elements in a list or other iterable. They are part of the collections module and can be used to easily count the frequency of items.

from collections import Counter

c = Counter([0,1,2,0,3,2])
print(c)

#'document' is an example of a list of words

word_count = Counter(document)

# we can use the most_common method to get the most common elements in the counter, it returns a list of tuples with the element and its count
for word, count in word_count.most_common(10):
    print(word, count)