class A:
    def spam(self):
        print(1)


class B(A):
    def spam(self):
        print(2)
        super().spam()


B().spam()


class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])


spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)


class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)


spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs

import random

class VagueList:
	def __init__(self, cont):
		self.cont = cont

	def __getitem__(self, index):
		return self.cont[index + random.randint(-1, 1)]

	def __len__(self):
		return random.randint(0, len(self.cont)*2)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])

class Queue:
	def __init__(self, contents):
		self._hiddenlist = list(contents)

	def push(self, value):
		self._hiddenlist.insert(0, value)

	def pop(self):
		return self._hiddenlist.pop(-1)

	def __repr__(self):
		return "Queue({})".format(self._hiddenlist)

queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)

class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height

	def calculate_area(self):
		return self.width * self.height

	@classmethod
	def new_square(cls, side_length):
		return cls(side_length, side_length)

square = Rectangle.new_square(5)
print(square.calculate_area())

class Pizza:
	def __init__(self, toppings):
		self.toppings = toppings

	@property
	def pineapple_allowed(self):
		return False

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True