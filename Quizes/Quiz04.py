# PERGUNTA 01
# Fill in the blanks to define a function that takes two numbers
# as arguments and returns the smaller one.
def min(x, y):
    if x <= y:
        return x
    else:
        return y

# PERGUNTA 02
# Rearrange the code to define a function that calculates the sum
# of all numbers from 0 to its argument.
def sum(x):
    res = 0
    for i in range(x):
        res += i
    return res

# PERGUNTA 03
# How would you refer to the randint function if it was imported like
# this?
# from random import randint as rnd_int

# (ERRADA) randint
# (ERRADA) random.rnd_int
# (CERTA)  rnd_int

# PERGUNTA 04
# What is the highest number output by this code?
def print_nums(x):
  for i in range(x):
    print(i)
    return

print_nums(10) # RETORNARIA 0

# PERGUNTA 05
# What is the output of this code?
def func(x):
  res = 0
  for i in range(x):
     res += i
  return res

print(func(4)) # RETORNA 6