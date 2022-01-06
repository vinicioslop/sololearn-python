# 1 - What is the result of this code?
nums = {1, 2, 3, 4, 5, 6}
# & PEGA OS VALORES EXISTENTES NOS 2 SETS, LOGO A LISTA S4ERÁ {1, 2, 3}
nums = {0, 1, 2, 3} & nums
# RETIRA TODOS OS VALORES MENORES QUE 1, LOGO NUMS TERÁ (2, 3)
nums = filter(lambda x: x > 1, nums)
# TRANSFORMA EM UMA LISTA E PEGA A QUANTIDADE DE VALORES QUE EXISTEM NELE
# EXIBINDO 2, JÁ QUE EXISTEM 2 VALORES
print(len(list(nums)))
# R: 2

# 2 - What is the result of this code?
def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y-1)

print(power(2, 3))
# R: 8

# 3 - Fill in the blanks to calculate the expression x*(x+1)
# using an anonymous function and call it for the number 6.
a = (lambda x: x * (x + 1)) (6)
print(a)

# 4 - Fill in the blanks to leave only even numbers in the list.
nums = [1, 2, 8, 3, 7]
res = list(filter(lambda x: x%2==0, nums))
print(res)

# 5 - Drag and drop from the options below to print only the items
# in the set "a" that are not in the set "b".
print(a - b)