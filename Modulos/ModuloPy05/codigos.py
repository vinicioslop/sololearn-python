# What is the output of this code?
try:
    variable = 10
    print(10 / 2)
except ZeroDivisionError:
    print("Error")

print("Finished")

# What is the output of this code?
try:
    meaning = 42
    print(meaning / 0)
    print("the meaning of life")
except (ValueError, TypeError):
    print("ValueError or TypeError occurred")
except ZeroDivisionError:
    print("Divided by zero")

# What is the output of this code?
try:
    print(1)
except:
    print(2)
finally:
    print(3)

# Which errors occur during the execution of this code?
try:
    print(1 / 0)
except ZeroDivisionError:
    raise ValueError

try:
    num = 5 / 0
except:
    print("An error occurred")
    raise

# What is the highest number printed by this code?
print(0)
assert "h" != "w"
print(1)
assert False
print(2)
assert True
print(3)

# How many characters would be in each line printed by this code, if one character is one byte?
file = open("filename.txt", "r")
for i in range(21):
    print(file.read(4))
file.close()

# If the file test.txt has 7 lines of content, what will the following expression return?
len(open("test.txt").readlines())
