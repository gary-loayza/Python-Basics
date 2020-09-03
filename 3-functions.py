##############################
# Docstrings
##############################

def square(num):
    """
    THIS IS A DOCSTRING
    CAN GO MULITPLE LINES.
    THIS FUNCTION SQUARES A NUMBER.
    """
    return num**2

print(square(3))


##############################
# The Map Function
##############################
def times2(var):
    return var*2

seq = [1,2,3,4,5]

map_seq = map(times2, seq)
print(list(map_seq))


##############################
# Lambda Expressions
# (Anonymous Functions)
##############################

# This is the same function as times2
lambda var:var *2

# This map defines its own function to be applied to 'seq'
lambda_version = list(map(lambda num: num*3,seq))
print(lambda_version)


##############################
# Filter Functions
##############################

# This filter will remove any odd numbers from 'seq'
my_filter = filter(lambda num: num%2 == 0, seq)
# my_filter has to be cast to list to print
print(list(my_filter))


##############################
# Methods
##############################

s = 'Hello my name is Red'
s.lower()       # This method makes everything lowercase
s.split()       # This method splits each word separated by whitespace
print(s.split())

tweet = 'Go Sports! #SportsFan'
tweet.split('#')    # This will split the string where it finds a "hashtag"
print(tweet.split('#'))

tweet.split('#')[1]     # This will return hastag used, "SportsFan"
print(tweet.split('#')[1])


##############################
# Some other useful Methods
##############################
d = { 'k1': 1, 'k2': 2}

d.keys()        # Returns the keys in the dictionary
print(d.keys())


list123 = [1,2,3]
list123.pop()       # Removes and returns last item in list
list123.pop(0)      # Removes and returns FIRST item in list

# To check something is inside a list
'x' in [1,2,3]      # This returns False
'x' in ['x','y','z']    # This returns True


##############################
# Tuple Unpacking
##############################
x = [(1,2),(3,4),(5,6)]     # x contains a list of tuples

for item in x:
    print(item)

# Tuple unpacking allows this form
for (a,b) in x:
    print(a)
