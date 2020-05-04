import mysql.connector
if __name__ == "__main__":
    db_manager


class db_manager:

    def __init__(self, host, user, passwd):
        self.__db = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd
        )
        self.__cursor = self.__db.cursor()
        self.__cursor.execute("CREATE DATABASE IF NOT EXISTS pythonlogin")
        self.__cursor.execute("USE pythonlogin")
        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), email VARCHAR(255), password VARCHAR(255))")

    def menu(self):
        exit = False
        while not exit:
            choice = int(input(
                "1. Register\n2. Login\n3. Edit\n4. Delete\n5. Show all users\n6. Search by username\n7. Search by email\n0. Exit\n====>> "))
            if choice == 1:
                answer = self.__register()
                print(answer)
            elif choice == 2:
                login = self.__login()
                print(login)
            elif choice == 4:
                delete = self.__delete()
                print(delete)
            elif choice == 0:
                exit = True
                print("Bye!")
            else:
                print("Wrong choise")


    def __register(self):
        username = input("Enter username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        re_password = input("Retype password: ")

        if password != re_password:
            return "Password dont match"

        self.__cursor.execute(
            "SELECT * FROM users WHERE username='" + username + "'")
        result = self.__cursor.fetchone()
        if result != None:
            return "User exists"
        else:
            sql = "INSERT INTO users (username, email, password) VALUES (%s, %s,%s)"
            val = (username, email, password)
            self.__cursor.execute(sql, val)
            self.__db.commit()
            return "User created"


    def __delete(self):
        username = input("Enter username: ")
        self.__cursor.execute("SELECT * FROM users WHERE username='" + username + "'")
        result = self.__cursor.fetchone()

        if result != None:
            sql = "DELETE FROM users WHERE username = '" + username + "'"
            self.__cursor.execute(sql) 
            self.__db.commit() 
        else: 
            return 'No match found'


    # def  __login(self):
    #     email = input('Enter email: ')
    #     password = input('Enter password: ')
    #     self.__cursor.execute(
    #         "SELECT * FROM users WHERE username='" + email + "'AND password = '" + password +"'")
    #     result = self.__cursor.fetchone()

    #     if result != None:
    #         return 'You are login'
    #     else:
    #         return 'False email or password'
