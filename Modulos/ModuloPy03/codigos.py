# What is the output of this code?
print(8.7 <= 8.70)

# What is the output of this code?
spam = 7
if spam > 5:
    print("five")
if spam > 8:
    print("eight")

# What is the output of this code?
num = 7
if num > 3:
    print("3")
    if num < 5:
        print("5")
        if num == 7:
            print("7")

# What is the result of this code?
if 1 + 1 == 2:
    if 2 * 2 == 8:
        print("if")
    else:
        print("else")

# What is the result of this code?
if (1 == 1) and (2 + 2 > 3):
    print("true")
else:
    print("false")

# What is the result of this code?
if not True:
    print("1")
elif not (1 + 1 == 3):
    print("2")
else:
    print("3")

# What is the result of this code?
if 1 + 1 * 3 == 6:
    print("Yes")
else:
    print("No")

# What is the result of this code?
x = 4
y = 2
if not 1 + 1 == y or x == 4 and 7 == 8:
    print("Yes")
elif x > y:
    print("No")

# What is the result of this code?
nums = [5, 4, 3, 2, 1]
print(nums[1])

# How many items are in this list?
[2, ]

# Which line of code will cause an error?
num = [5, 4, 3, [2], 1]
print(num[0])
print(num[3][0])
# print(num[5])

# What is the result of this code?
nums = [1, 2, 3, 4, 5]
nums[3] = nums[1]
print(nums[3])

nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)

# What is the result of this code?
nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5
if 4 in nums:
    print(nums[3])
else:
    print(nums[4])

# What is the result of this code?
words = ["hello"]
words.append("world")
print(words[1])

# What is the result of this code?
letters = ["a", "b", "c"]
letters.append("d")
print(len(letters))

# What is the result of this code?
nums = [9, 8, 7, 6, 5]
nums.append(4)
nums.insert(2, 11)
print(len(nums))
