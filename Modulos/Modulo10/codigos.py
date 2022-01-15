# import this
def function(named_arg, *args):
    print(named_arg)
    print(args)


function(1, 2, 3, 4, 5)


def my_func(x, y=7, *args, **kwargs):
    print(kwargs)


my_func(2, 3, 4, 5, 6, a=7, b=8)

a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)

# What is the output of this code?
a, b, c, d, *e, f, g = range(20)
print(len(e))

try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)

try:
    print(1/0)
except ZeroDivisionError:
    print(4)
else:
    print(5)
