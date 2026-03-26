# inpython strings can be represented by one ' or two " and they are the same
# the only reason to use one or the other is to avoid the need for escaping characters

single_quoted_string = 'data science'

double_quoted_string = "datascience"

#in python whe use inverted backslash \ to escape characters
tab_string = 'data\tscience'


not_tab_string = r"\t" # the r before the string means that it is a raw string and that the backslash should be treated as a literal character

print(len(not_tab_string)) # é 2

# if you want build a coment with more lines, you need to use a triple quote string

triple_quoted_string = """data
                        science
                            is 
                            nice"""
                            
# f string: f string is a string that can contain expressions that are evaluated at runtime and then formatted using the format() protocol.

name = "Gabriel"
last_name = "Blimbliem"

print(f"My name is {name} and my last name is {last_name}")