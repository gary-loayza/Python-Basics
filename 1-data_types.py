##############################
# Strings
##############################

num = 26
name = 'Gary'

print('My name is {one} and I am {two} years old.'.format(one=name,two=num))


##############################
# Sequence
##############################

s = 'abcdefghijk'
# Select everything beyond 'f'
f = s[6:]
print('LN 18: ' + f)
# Select everything before 'd'
d = s[:3]
print('LN 21: ' + d)
# Select everything between 'd' and 'j'
g = s[4:9]
print('LN 24: ' + g)

##############################
# Lists
##############################
my_list = ['a','b','c','d','e']

my_list.append('f')
print(my_list)

nest = [1,2,3,[4,5,['target']]]
# Select the target
n = nest[3][2][0]
print('LN 37: ' + n)


##############################
# Dictionaries
##############################
d = {'key': 'value', 'color': 'green', 'age': 26}
print('LN 44: ' + d['key'])
print(d['age'])

d_nested = {'k1': {'innerkey': [1,2,3]}}
# Select number 2
print(d_nested['k1']['innerkey'][1])


##############################
# Tuples
##############################
t = (1,2,3)
# Change 1 to 'NEW'
## t[0] = 'NEW'
# This gives us an error because tuples are immutable. Compare this to a list.
print(t)


##############################
# Sets
##############################
my_set = {1,1,2,1,1,2,2,3,3,1,3,2}
print(my_set)
# A set is defined by unique elements,
# thus my set ends up as {1,2,3}

make_set = set([1,1,1,1,2,2,2,2,5,5,5,5,6,6,6,6])
print(make_set)

# Add to a set
new_set = {1,2,3}
new_set.add(5)
print(new_set)
