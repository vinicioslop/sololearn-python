# QUESTÃO 01
# How is a property created?
# a - (ERRADA) Making a class a subclass of property
# b - (CERTA)  Using the property decorator 
# c - (ERRADA) Using the classmethod decorator

# QUESTÃO 02
# What is the difference between a class method and a static method?
# a - (CERTA)  Class methods are passed the calling class, static methods
#     aren't
# b - (ERRADA) Class methods are faster
# C - (ERRADA) Class methods are inherited, static methods aren't

# QUESTÃO 03
# What are the usual parameter names for the calling instance and the
# calling class?
# a - (CERTA)  self and cls
# b - (ERRADA) slf and cls
# c - (ERRADA) self and class

# QUESTÃO 04
# What method is called just before an object is instantiated?
# a - (CERTA)  __init__
# b - (ERRADA) __del__
# c - (ERRADA) __create__

# QUESTÃO 05
# Fill in the blanks to make the egg attribute strongly private and access it from outside of the class.
# class Test:
#   __egg = 7
# 
# t = Test()
# print(t._Test__egg)

# QUESTÃO 06
# What is the automatic process by which unnecessary objects are deleted to free memory?
# a - (CERTA)  Garbage collection
# b - (ERRADA) Rubbish deletion
# c - (ERRADA) Bit-trash exfoliation

# QUESTÃO 07
# Fill in the blanks to make a setter for the property name.
# class Person:
#   def __init__(self, name):
#     self._name = names
#
#   @property
#   def name(self):
#     return self._name
#
#   @name.setter
#   def name(self, value):
#     self._name = value