# You need to write a function that takes multiple words as its
# argument and returns a concatenated version of those words
# separated by dashes (-).
# The function should be able to take a varying number of words
# as the argument.

# Sample Input
# this
# is
# great

# Sample Output
# this-is-great

# Recall, using *args as a function parameter enables you to pass
# an arbitrary number of arguments to that function.

from operator import indexOf


def concatenate(*args):
    full_word = ""
    cont = 0

    for word in args:
        if cont == len(args) - 1:
            full_word = full_word + word
        else:
            full_word = full_word + word + "-"

        cont += 1

    return full_word


print(concatenate("I", "love", "Python", "!"))
