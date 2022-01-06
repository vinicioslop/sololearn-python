# Given a text as input, find and output the longest word.

# Sample Input
# this is an awesome text

# Sample Output
# awesome

# Recall the split(' ') method, which returns a list of words
# of the string.

txt = input()

#your code goes here
words = txt.split(" ")
lenght = [len(w) for w in words]

for w in words:
    if max(lenght) == len(w):
        print(w)