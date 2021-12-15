# PERGUNTA 01
# Which number is not printed by this code?
try:
    print(1)
    print(20 / 0)
    print(2)  # NÃO É EXIBIDO NO CONSOLE
except ZeroDivisionError:
    print(3)
finally:
    print(4)

# PERGUNTA 02
# Open the file in binary write mode.
open("text.txt", "wb")

# PERGUNTA 03
# Fill in the blanks to try to open and read from a file.
# Print an error message in case of an exception.
try:
    with open("text.txt") as f:
        print(f.read())
except:
    print("Error")

# PERGUNTA 04
# What is the highest number that would be printed by this code?
try:
  print(1)
  assert 2 + 2 == 5
except AssertionError:
  print(3) # MAIOR NÚMERO EXIBIDO
except:
  print(4)