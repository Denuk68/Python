# a = int(input('Please enter an hour : '))

# if a > 4 and a <= 11:
#     print('good morning')
# elif a > 11 and a <= 16:
#     print('good day')
# elif a > 16 and a <= 22:
#     print('good evening')
# elif a > 22 and a <= 24 or a >= 1 and a <= 4:
#     print('good night')
# elif a < 1 or a > 24:
#     print('Please enter an hour (1 - 24)')



# exit = False

# while not exit:
#     choice = int(input(
#         ' 1. Centimeter to Inch\n 2. Inch to Centimeter\n 3. Exit\n Your choice : '))

#     value = int(input(' Please enter value to convert : '))

#     INCH = 2.54

#     CentimeterToInch = value / INCH
#     InchToCentimeter = INCH * value
    
#     if choice == 1:
#         print(CentimeterToInch, 'Inch')
#     elif choice == 2:
#         print(InchToCentimeter, 'Centimeter')
#     elif choice == 3:
#         exit = True



# exit = False

# while not exit:
#     choice = int(input(
#         ' 1. Fahrenheit to Celsius\n 2. Celsius to Fahrenheit\n 3. Exit\n Your choice : '))
#     value = int(input(' Please enter value to convert : '))

#     TC = (value - 32) / 1.8
#     TF = value * 1.8 + 32  
    
#     if choice == 1:
#         print(value, ' degrees Fahrenheit = ', TC, ' degrees Celsius')
#     elif choice == 2:
#         print(value, ' degrees Celsius = ', TF, ' degrees Fahrenheit')
#     elif choice == 3:
#         exit = True



# i = 0
# mult = 1
# average = 0
# QUANTITY = 8

# while i < QUANTITY:
#     i += 1
#     numbers = int(input("Enter number : "))
#     mult *= numbers
#     average += numbers / QUANTITY

# print('Your mult : ', mult)
# print('Your аrithmetic mean : ', average)



# import random

# i = 0
# array = []

# while i < 7:
#     i += 1
#     temp = random.randint(-10, 30)    
#     array.append(temp)   

# print(array)

# print('Max temp = >', max( array ))
# print('Min temp = >', min( array ))