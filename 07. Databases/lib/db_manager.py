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
            elif choice == 3:
                edit = self.__edit()
                print(edit)
            elif choice == 4:
                delete = self.__delete()
                print(delete)
            elif choice == 5:
                showAllUsers = self.__showAllUsers()
                print(showAllUsers)
            elif choice == 6:
                searchByUsername = self.__searchByUsername()
                print(searchByUsername)
            elif choice == 7:
                searchByEmail = self.__searchByEmail()
                print(searchByEmail)
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

        self.__cursor.execute("SELECT * FROM users WHERE username='" + username + "'")
        result = self.__cursor.fetchone()

        if result != None:
            return "User exists"
        else:
            sql = "INSERT INTO users (username, email, password) VALUES (%s, %s,%s)"
            val = (username, email, password)
            self.__cursor.execute(sql, val)
            self.__db.commit()
            return "User created"


    def __login(self):
        email = input('Enter email: ')
        password = input('Enter password: ')

        self.__cursor.execute("SELECT * FROM users WHERE email = '" + email + "' AND password = '" + password + "'")
        result = self.__cursor.fetchone()

        if result != None:
            return 'You are logged in'
        else:
            return 'False email or password'


    def __edit(self):
        user_edit = input('Enter username who you want edit : ')

        self.__cursor.execute("SELECT * FROM users WHERE username='" + user_edit + "'")
        result = self.__cursor.fetchone()

        if result != None:
            print("Enter your changes below")
        else:
            return 'User not found'

        username = input("Enter new username: ")
        email = input("Enter new email: ")
        password = input("Enter new password: ")
        re_password = input("Retype password: ")

        if password != re_password:
            return "Password dont match"

        if result != None:
            self.__cursor.execute("UPDATE users SET username = '" + username + "' , email = '" +  email + "'  , password = '" + password + "' WHERE username = '" + user_edit + "' ")
            self.__db.commit()
            return(" '" + user_edit + "' has changed ")
  

    def __delete(self):
        username = input("Enter username: ")
        self.__cursor.execute("SELECT * FROM users WHERE username='" + username + "'")
        result = self.__cursor.fetchone()

        if result != None:
            self.__cursor.execute("DELETE FROM users WHERE username = '" + username + "'")
            self.__db.commit()
        else:
            return 'No match found'

    
    def __showAllUsers(self):
        self.__cursor.execute('SELECT "User: " , username , " Email : " , email  FROM users')
        result = self.__cursor.fetchall()

        if result != None: 
            return result


    def __searchByUsername(self):
        username = input("Enter username: ")

        self.__cursor.execute('SELECT "User: " , username , " Email : " , email  FROM users WHERE username = "' + username +'"')
        result = self.__cursor.fetchall()
        
        
        if len(result) > 0:
            return result
        else:
            return "User not found"


    def __searchByEmail(self):
        email = input("Enter email: ")

        self.__cursor.execute('SELECT "User: " , username , " Email : " , email  FROM users WHERE email = "' + email +'"')
        result = self.__cursor.fetchall()

        if len(result) > 0:
            return result
        else:
            return "User not found"



        

    
    
              
           


    

