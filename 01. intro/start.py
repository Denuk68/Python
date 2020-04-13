# a = 10 # int
# print(a,type (a))

# a = 10.6 # Float
# print(a,type (a))

# a = True # bool
# print(a,type (a))

# a = 'Bil' # string
# print(a,type (a))


# name = input('Your name: ')
# age = int(input('Your age: '))
# print(name, type(name))
# print(age, type(age))


# a = int(input('Number 1: '))
# b = int(input('Number 2: '))

# sum = a + b
# mult = a * b
# dev = a / b
# min = a - b

# print('Result = ', sum)
# print('Result = ', mult)
# print('Result = ', dev)
# print('Result = ', min)


# a = int(input('Number 1: '))
# b = int(input('Number 2: '))

# if a > b:
#     print("a > b")
# elif a < b:
#     print('a < b')
# else:
#     print('a = b')


# a = int(input('Number 1: '))
# b = int(input('Number 2: '))
# c = int(input('Number 2: '))

# if a > b and  a > c:
#     print('first if')
# if a > b or b > c:
#     print("elif")


# a = int(input('Kilometrs: '))
# b = a * 1000

# print('Result :', b)


# a = int(input('Gruvni: '))

# USD = 28.2
# EUR = 31.1
# RUB = 0.35

# ResUsd = print(a * USD)
# ResEur = print(a * EUR)
# ResRub = print(a * RUB)


# a = int(input('Vutrata Paluva/100km: '))
# b = int(input('Price 1l: '))
# c = int(input('Distance: '))

# res = print('Cash', c / a * b)


# import random
# a = random.randrange(0, 2)
# b = random.randrange(0, 2)
# c = random.randrange(0, 2)
# print(a,b,c)
# if a == b == c:
#  print('All equal')






# # Цикл While



# import random
# i = 0
# counter = 0

# while i < 7:
#     i += 1
#     temp = random.randint(-10, 30)
#     if temp > 10:
#         counter += 1
#         print(temp)
# print('More then =>', counter)






# exit = False
# a = int(input('Number 1 : '))
# b = int(input('Number 2 : '))

# sum = a + b
# min = a - b
# mult = a * b
# dev = a / b

# while not exit:
#     choice = int(input('1. Add\n2. Min\n3. Mult\n4. Dev\n0. Exit'))
#     if choice == 1:
#         print('a + b =' , sum)
#     elif choice == 2:
#         print('a - b =', min)
#     elif choice == 3:
#         print('a * b =', mult)
#     elif choice == 4:
#         print('a / b =', dev)
#     elif choice == 0:
#         exit = True





# # Цикл for

# tmp = 10
# i = 0

# for i in range(1, tmp): #range це метод
#     print(i)



# import random

# number = 8
# counter = 0

# for i in range(1, number):
#     temp = random.randint(-10, 30)    
#     if temp > 10:
#         counter += 1
#     print(temp)

# print('More then =>', counter)


