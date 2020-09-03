##############################
# For loops
##############################
x = [1,2,3,4]
out = []

# Square the numbers in array 'x' and write them into 'out'
for num in x:
    out.append(num**2)
print(out)

# Python allows the above process to be done with "List comprehension"
# List comprehension:
list_comp = [num**2 for num in x]
print(list_comp)
