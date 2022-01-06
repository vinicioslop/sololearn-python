ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])

# bad_dict = {
# 	[1, 2, 3]: "one two three",
# }

squares = {1: 1, 2: 4, 3: "error", 4: 16, }
squares[8] = 64
squares[3] = 9
print(squares)

nums = {
    1: "one",
    2: "two",
    3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

pairs = {1: "apple",
         "orange": [2, 3, 4],
         True: False,
         None: "True",
         }

print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])
print(squares[7:])

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])

# a list comprehension
cubes = [i**3 for i in range(5)]

print(cubes)

evens = [i**2 for i in range(10) if i ** 2 % 2 == 0]

print(evens)
