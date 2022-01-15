# We need to create a number formatting system for
# a contacts database.
# Create a program that will take the phone number
# as input, and if the number starts with "00",
# replace them with "+".
# The number should be printed after formatting.

# Sample Input
# 0014860098

# Sample Output
# +14860098

# Notice that here you shouldn't convert the input
# string to integer, because you will work with symbols.

# your code goes here
import re

pattern = r"00"

number = input()

if re.match(pattern, number):
    number = re.sub(pattern, "+", number)

print(number)
