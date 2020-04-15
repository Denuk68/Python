# Інкапсуляція(Робити дані приватними) , Наслідування , Поліморфізм = ООП

# __  два андерскора перед назвою робить  метод або властивості приватними
# метод завжди має приймати self першим параметром
# def __init__ - конструктор
# def __del__ - деструктор

# getter - ним віддаємо значення яке знаходиться в класі(Можемо доступитись до приватного поля завдяки публічному методу)
# @property = це доступ до нашої властивості, тобто ми кажем що це getter.
# setter змінює нашу властивість.

# Антотація @property(getter) і setter ======>  (Можна присвоювати анотацію тоді коли це потрібно)


class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

        print("Constructor Working...")

    def __del__(self):
        print("Desctructor working...")

    def person_info(self):
        print(self.__name, " <-> ", self.__age, " years old")

    # getter
    @property
    def name(self):
        return self.__name

    # getter
    @property
    def age(self):
        return self.__age

    # setter
    @age.setter
    def age(self, new_age):
        if self.__age == new_age:
            print("The same age")
        else:
            self.__age = new_age

    # setter
    @name.setter
    def name(self, new_name):
        if self.name == new_name:
            print("The same name")
        else:
            self.__name = new_name


bill = Person("Billy", 56)
# bill.person_info()


# print("Bill age before => ", bill.name)
# print("Bill age before => ", bill.age)
# bill.name = "John"
# bill.age = 58
# print("Bill age after => ", bill.name)
# print("Bill age after => ", bill.age)





stive = Person("Stiven", 26)
# # stive.person_info()

adam = Person('Adam', 34)
eva = Person('Eva', 27)
tina = Person('Tina', 29)
sara = Person('Adam', 39)

person_list = []
person_list.append(bill)
person_list.append(stive)
person_list.append(adam)
person_list.append(eva)
person_list.append(tina)
person_list.append(sara)

for person in person_list:
    # item.person_info()
    print(person.name, '=', person.age)
    person.age += 1

# print("===========================")

# for person in person_list:
#     # person.person_info()
#     print(person.name, " = ", person.age)
