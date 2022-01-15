# Regular expressions

# You are playing a word game with your friends,
# and are asked for a word starting with "gl".
# Write a program that takes the word as input
# and outputs "Match" if it starts with required
# characters, and "No match" if it doesn't.

# Sample Input
# glue

# Sample Output
# Match

# The re.match function determines whether the
# regular expression matches at the beginning of
# a string.
import re
word = input()

# your code goes here
pattern = r"gl"
if re.match(pattern, word):
    print("Match")
else:
    print("No match")