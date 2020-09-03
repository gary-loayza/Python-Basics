from decorators import world, kanye, twice_with_args, fun_with_return


# The decorator "kayne" can be used to modify what is printed before a function
# runs. In this case, we call say_whee with the kanye modifications.
@kanye
def thank_you():
    print("Thanks a lot.")

thank_you()

# Before moving on. Realize that @decorator is syntactic sugar
# In the case above,
# @kanye is just an easier way of saying thank_you = kanye(thank_you)
# AFTER the definition of the thank_you function.
# See how we would implement another decorator manually.

def hello():
    print("\nHello")

hello = world(hello)
hello()


# But what happens when you try to "Kanye" a thank you speech that has arguments?
# In this case, what happens when we want to show our appreciation for Beyonce?
@kanye
def thank_name(name):
    print(f"Thank's specifically to {name}")

# Now we would normally call thank_name(), but I know this won't work.
# So I wrap it in a try block to keep things moving.
try:
    # This will not run
    thank_name("Beyonce")
except TypeError:
    # Here's what the console log actually returns in the above case
    print(70*"=")
    print("\nTypeError: wrapper() takes 0 positional arguments but 1 was given\n")

    print("The Kanye wrapper could not interrupt")
    print("Probably because it looked like you were going to thank Beyonce")
    print("\n")



# So then how do we run a function that has arguments?
# We add (*args, **kwargs) to the wrapper function in the decorator
# As with @twice_with_args
@twice_with_args
def single_people(name):
    print(f"All my single {name}")

single_people("ladies")


# Let's do more than just printing.
# Let's return a value from a function using @twice_with_args
@twice_with_args
def pokeball(pokemon):
    print("I choose you. . .")
    return pokemon

pokeball("pikachu")
# Notice how @twice_with_args only runs the function twice and decorates it.
# The value of pokemon is not returned in this decorator,
# so we don't know who was chosen.
print("pokeball('pikachu') = ? ", pokeball("pikachu"))


# Looking at the decorator "fun_with_return" we can see that the decorator will
# need to pass the returned value of pokemon outside of "wrapper" by returning
# This decorator should perform the function, include the return value,
# and decorate the output with formatting.
@fun_with_return
def pokeball_2(pokemon):
    print("I choose you. . .")
    return pokemon

pikachu = pokeball_2("pikachu")
print(pikachu)
