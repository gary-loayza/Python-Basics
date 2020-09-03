################################################################################
# What is 7 to the power of 4
################################################################################
7**4


################################################################################
# Split this string
#
## s = "Hi there Sam!"
#
# into a list
################################################################################
s = "Hi there Sam!"
s.split()


################################################################################
# Given the variables:
#
### planet = "Earth"
### diameter = 12742
#
# Use .format() to print the following string:
### The diameter of Earth is 12742 kilometers.
################################################################################
planet = "Earth"
diameter = 12742
print('The diameter of {} is {} kilometers'.format(planet,diameter))


################################################################################
# Given the nested list, use indexing to grab the word "hello"
### lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
################################################################################
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
lst[3][1][2][0]


################################################################################
# Given this nest dictionary grab the word "hello".
################################################################################
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
d['k1'][3]['tricky'][3]['target'][3]


################################################################################
# What is the main difference between a tuple and a list?
################################################################################
#### Answer: A tuple is immutable, a list is mutable.


################################################################################
# Create a function that grabs the email website domain
# from a string in the form:
### user@domain.com
################################################################################
def domainGet(email):
    return email.split('@')[1]

domainGet('user@domain.com')      # Returns "domain.com"


################################################################################
# Create a basic function that returns True if the word 'dog' is contained in
# the input string. Don't worry about edge cases like a punctuation being
# attached to the word dog, but do account for capitalization.
################################################################################
def findDog(s):
    return 'dog' in s.lower().split()

findDog('Is there a dog here?')     # Returns True


################################################################################
# Create a function that counts the number of times the word "dog" occurs in
# a string. Again, ignore edge cases.
################################################################################
def findDog(s):
    x = s.lower().split()
    # x is now an array of words in lower case
    y = list(filter(lambda word: word=='dog', x))
    return len(y)

findDog('It is a dog eat dog world, dog')       # Returns 3


################################################################################
# Use lambda expressions and the filter() function to filter out words from
# a list that don't start with the letter 's'. For example:
#
### seq = ['soup', 'dog', 'salad', 'cat', 'great']
#
# should be filtered down to:
#
### ['soup', 'salad']
################################################################################
seq = ['soup', 'dog', 'salad', 'cat', 'great']
result = list(filter(lambda word: word[0]=='s', seq))



################################################################################
# Final Problem: You are driving a little too fast and a police officer stops
# you. Write a function to return one of 3 possible results:
# "No ticket" if your speed is 60 or less,
# "Small ticket" if your speed is between 61 and 80 inclusive,
# or "Big Ticket" if your speed is 81 or more.
# If it is your birthday(boolean), your speed can be 5 higher in all cases.
################################################################################
def caught_speeding(speed, is_birthday):
    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed

    if speeding > 80:
        return 'Big Ticket'
    elif speeding > 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'


print(caught_speeding(81, True))        # Returns "Small Ticket"
print(caught_speeding(81, False))       # Returns "Big Ticket"
