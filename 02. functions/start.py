### !!!!!!!!!!!!!!!!!!Функції , оголошується через def!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



# def sum():
#      print("function sum")

# sum()


# def sum(a, b):
#     print(a + b)

# a = int(input('Enter first number : '))
# b = int(input('Enter second number : '))

# sum(a, b)


# def sum(a = 0, b = 0):
#     if a > 0:
#         return a + b # Функція має завжди щось повертати а Ретурн останнє в коді після нього нічого не працює
#     else:
#         print('test')
#         return 0


# a = int(input('Enter first number : '))
# b = int(input('Enter second number : '))

# res = sum(a, b)
# print('Resault = ', res)


# glob = 5  # Глобальна змінна

# def sum(a = 0, b = 0):
#     glob = "Gloabal vars"
#     if a > 0:
#         return a + b
#     else:
#         print('Test')
#         return 0

# a = int(input('Enter first number : '))
# b = int(input('Enter second number : '))

# res = sum(a, b)
# print('Resault = ', res)
# print(glob)


# def sum(*params): #params це масив який приймає необмежену кількість данних , "*" - spred оператор
#     res = 0
#     for i in params:
#         print(i)
#         res += i
#     return res


# result = sum(2, 5, 3)
# print("resault =>", result)





# # Задачи по функціям

# # 1. Написати функцію, яка отримує в якості параметрів два цілих числа і повертає суму чисел з діапазону між ними.

# a = int(input('Fist number : '))
# b = int(input('Second number : '))


# def find_range(a, b):
#     res = 0
#     for i in range(a + 1, b):
#         print('i = ', i)
#         res += i
#     return res


# result = find_range(a, b)
# print('Result => ', result)


# #2. Написати функцію, яка отримує відстань, яку пробіг спортсмен та час пробігу і повертає швидкість спортсмена. Відстань та час пробігу вводяться користувачем

# l = float(input("Enter length: "))
# t = float(input("Enter time: "))

# def v(l,t):
#     return l/t

# res = v(l,t)
# print("Speed is",res)













### !!!!!!!!!!!!!!!!! Cписки !!!!!!!!!!!!!!!!! Дані які можна змінити

# arr = [4, 6, 7, 8, 0, 9, 2, 4, 8, 8]
# # print(arr, 'type => ', type(arr))
# # for i in arr:
# #     print(i)
# print('========================>')
# # arr[2] = 100
# # for i in arr:
# #     print(i)

# arr.append(99)
# print('========================>')
# arr[2] = 100
# # for i in arr:
# #     print(i)

# print('========================>')
# arr.insert(2, 150)
# # for i in arr:
# #     print(i)

# arr.remove(4)
# print('========================>')
# for i in arr:
#     print(i)

# print("index => ", arr.index(0))
# print("Arr len => ", len(arr))
# print("count => ", arr.count(8))
# arr.pop()
# print("after pop => ")
# for i in arr:
#     print(i)

# print("Sort =================================>")
# arr.sort()
# for i in arr:
#     print(i)

# print("Revers =================================>")
# arr.reverse()
# for i in arr:
#     print(i)

# print('Max => ', max(arr))
# print('Min => ', min(arr))


# arr = [4, 6, 7, 5, 4, [55, 43, 32], 66, 44, "works", True]
# print(arr)
# arr[5][0] = 90
# print(arr)


# person = ['Tom', 'Bill', 'Steel', 'Adam']
# for i in person:
#     print(i)

# person.sort()
# for i in person:
#     print(i)


# # 1.  Дано список 30 елементів . Замінити всі від’ємні елементи додатніми.  Діапазон - 20 +30

# import random

# a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# for i in range(len(a)):
#         a[i] = random.randint(-20, 30)
#         print(a)
# for i in range(len(a)):
#     if a[i] < 0:
#         a[i] = -a[i]
# print(a)



# lang = ['C++', 'Python', "JS", 'C#', "Java", 'PHP', 'HTML', 'CSS']

# # prog = lang
# # print(prog)
# # prog[0] = 'Kotlin'
# # print('Prog =>', prog)
# # print('Lang =>', lang)

# # import copy
# # prog = copy.deepcopy(lang)
# # prog[0] = 'Kotlin'
# # print('Prog =>', prog)
# # print('Lang =>', lang)

# part = lang[3:8:2] # копіюєм елементи з 3-го індекса  по 8-тий індекс кожен 2-гий елемент
# print(part)








### !!!!!!!!!!!!!!!!! Кортеж(Tuple) !!!!!!!!!!!!!!!!! Дані які НЕ можна змінити

# car = ('BMW', 'Renault', "VW", "Audi")

# for i in car:
#     print(i)

# print(car[-1]) # Показує останній елемент масиву(тобто зворотній напрямок елементів)

# print(len(car))
# print('Audi count ', car.count('Audi'))

# i = 0 
# while i < len(car):
#     print(car[i])
#     i += 1



# person = ('Bill', 34)

# name, age = person

# print('Name : ', name, '\nAge: ',age)







# ### !!!!!!!!!!!!!!!!! Словники !!!!!!!!!!!!!!!!! 


# countries = {
#     'UA': 'Ukraine',
#     'US': 'USA',
#     3: 'Brasil'
# }

# print('=========Before======')
# for  key, value in countries.items():
#     print(key, '====', value)

# countries.pop('US')
# print('=========After======')

# for  key, value in countries.items():
#     print(key, '====', value)

# for  key in countries.keys():
#     print(key)

# for  value in countries.values():
#     print(value)

# print(countries[3])
# print(countries.get('US'))

# countries['IT'] = 'Italy'
# for key, value in countries.items():
#     print(key, '====', value)