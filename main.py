# =========================================================================

class Person():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def addbook(self):
        book_name = input("Enter the name of the book: ")
        book_price = input("Enter the price of the book: ")

        with open("books.txt", "a") as file:
            file.write(f"{book_name},{book_price}\n")

        print("Book added successfully.")

    def seebooklist(self):
        with open("books.txt", "r") as file:
            for line in file:
                book_name, book_price = line.strip().split(",")
                print(f"Book: {book_name} | Price: {book_price}")

    def removebook(self):
        print("Input the book name")
        bookname = input()

        with open("books.txt", "r") as file:
            lines = file.readlines()

        with open("books.txt", "w") as file:
            for line in lines:
                stored_book_name, stored_book_price = line.strip().split(",")
                if stored_book_name != bookname:
                    file.write(line)

        print(f"Book '{bookname}' removed successfully.")


# ============================================================================

class Admin(Person):
    def seelibrarianlist(self):
        with open("librarians.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                print(username)

    def addlibrarian(self):
        print("Write User Name")
        name = input()
        print("Write PassWord")
        password = input()
        with open("librarians.txt", "a") as file:
            file.write(f"{name},{password}\n")
            print("New Librarian added successfully.")

    def removelibrarian(self):
        print("Input the username")
        username = input()
        with open("librarians.txt", "r") as file:
            lines = file.readlines()

        with open("librarians.txt", "w") as file:
            for line in lines:
                if not line.startswith(username + ","):
                    file.write(line)

        print(f"Username '{username}' removed successfully.")


# ==============================================================================

class Librarian(Person):
    def changepassword(self, username):
        print("Input New Password")
        newpassword = input()

        with open("librarians.txt", "r") as file:
            lines = file.readlines()

        with open("librarians.txt", "w") as file:
            for line in lines:
                if line.startswith(username + ","):
                    line = f"{username},{newpassword}\n"
                file.write(line)

        print("Password changed successfully.")

    def updatebook(self):
        print("Input Bookname")
        book = input()

        print("Input Price")
        price = input()

        print("Input New Bookname")
        newbookname = input()

        print("Input New Password")
        newprice = input()

        with open("books.txt", "r") as file:
            lines = file.readlines()

        with open("books.txt", "w") as file:
            for line in lines:
                if line.startswith(book + ","):
                    line = f"{newbookname},{newprice}\n"
                file.write(line)

        print("Book has been updated")

    def adduser(self):
        print("Write User Name")
        name = input()
        print("Write PassWord")
        password = input()
        with open("users.txt", "a") as file:
            file.write(f"{name},{password}\n")
            print("New User added successfully.")

    def seeuserlist(self):
        with open("users.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                print(username)

    def updateuser(self):
        print("Input Old Username")
        username = input()

        print("Input Old Password")
        userpassword = input()

        print("Input New Username")
        newusername = input()

        print("Input New Password")
        newpassword = input()

        with open("users.txt", "r") as file:
            lines = file.readlines()

        with open("users.txt", "w") as file:
            for line in lines:
                if line.startswith(username + ","):
                    line = f"{newusername},{newpassword}\n"
                file.write(line)

        print("User has been updated")

    def removeuser(self):
        print("Input the user name")
        username = input()

        with open("users.txt", "r") as file:
            lines = file.readlines()

        with open("users.txt", "w") as file:
            for line in lines:
                stored_user_name, stored_user_password = line.strip().split(",")
                if stored_user_name != username:
                    file.write(line)

        print(f"Book '{username}' removed successfully.")


# ==============================================================================
class User(Person):
    def lendbook(self):
        print("Input the book name:")
        bookname = input()

        found_book = False  # Flag to track if the book is found

        with open("books.txt", "r") as file:
            lines = file.readlines()

        with open("books.txt", "w") as file:
            with open("StockOutBooks.txt", "a") as stock_out_file:
                for line in lines:
                    stored_book_name, stored_book_price = line.strip().split(",")
                    if stored_book_name != bookname:
                        file.write(line)
                    else:
                        found_book = True
                        stock_out_file.write(f"{stored_book_name},{stored_book_price}\n")

        if found_book:
            print(f"Book '{bookname}' removed successfully and added to StockOutBooks.txt.")
        else:
            print(f"Book '{bookname}' is currently out of stock.")

    def returnbook(self):
        print("Input the book name:")
        bookname = input()

        found_book = False  # Flag to track if the book is found

        with open("StockOutBooks.txt", "r") as stock_out_file:
            lines = stock_out_file.readlines()

        with open("StockOutBooks.txt", "w") as stock_out_file:
            for line in lines:
                stored_book_name, stored_book_price = line.strip().split(",")
                if stored_book_name != bookname:
                    stock_out_file.write(line)
                else:
                    found_book = True

        if found_book:
            with open("books.txt", "a") as file:
                file.write(f"{bookname},{stored_book_price}\n")
            print(f"Book '{bookname}' returned successfully.")
        else:
            print(f"Book '{bookname}' was not found in StockOutBooks.txt.")


# ==============MAIN FUNCTION=====================================

admin = Admin("admin", "admin")
librarian = Librarian("librarian", "librarian")
user = User("user", "user")

print("Hello There!")
print("Which Menu to Open(Give the number)?")
print("1.Admin 2.Librarian 3.User")
users = int(input())

if users == 1:
    print("Input your Username")
    email = input()
    print("Input your Password")
    password = input()
    if email == admin.username and password == admin.password:
        print("Congratulations you have logged in as Admin")
        print("Input The Number of the operation you want to do")
        print("1.See Librarian List\n2.Add Librarian\n3.Remove Librarian\n4.See Book List\n5.Add Book\n6.Remove Book\n")
        x = int(input())
        if x == 1:
            admin.seelibrarianlist()
        elif x == 2:
            admin.addlibrarian()
        elif x == 3:
            admin.removelibrarian()
        elif x == 4:
            admin.seebooklist()
        elif x == 5:
            admin.addbook()
        elif x == 6:
            admin.removebook()
        else:
            print("Wrong Input")
    else:
        print("Invalid Credentials")


elif users == 2:
    print("What you want?\n 1.Login 2.Register")
    choice = int(input())
    if choice == 1:
        print("WELCOME TO LIBRARIAN LOGIN")
        print("Input your Username")
        username = input()
        print("Input your Password")
        password = input()
        found = False

        with open("librarians.txt", "r") as file:
            for line in file:
                line = line.strip()
                users, passwords = line.split(",")

                if users == username and passwords == password:
                    found = True
                    break

        if found:
            print("Email and password Matched!")
            print("Which Operation You want to perform(Input the Number)")
            print("1.Change Password\n2.Add Book\n3.See Booklist\n4.Update Any Book\n5.Remove Any Book6.ADD "
                  "user\n7.See User List\n8.Update User\n 9.Remove User")
            x = int(input())
            if x == 1:
                librarian.changepassword(username)
            elif x == 2:
                librarian.addbook()
            elif x == 3:
                librarian.seebooklist()
            elif x == 4:
                librarian.updatebook()
            elif x == 5:
                librarian.removebook()
            elif x == 6:
                librarian.adduser()
            elif x == 7:
                librarian.seeuserlist()
            elif x == 8:
                librarian.updateuser()
            elif x == 9:
                librarian.removeuser()
            else:
                print("Invalid Input")



        else:
            print("Wrong Credentials")


    else:
        print("WELCOME TO LIBRARIAN REGISTRATION")
        print("Input your new Username")
        username = input()
        print("Input your new Password")
        password = input()
        with open("librarians.txt", "a") as file:
            file.write(f"{username},{password}\n")
        librarian = Librarian(username, password)


else:
    print("What you want?\n 1.Login 2.Register")
    choice = int(input())
    if choice == 1:
        print("WELCOME TO USER LOGIN")
        print("Input your Username")
        username = input()
        print("Input your Password")
        password = input()
        found = False

        with open("users.txt", "r") as file:
            for line in file:
                line = line.strip()
                users, passwords = line.split(",")

                if users == username and passwords == password:
                    found = True
                    break

        if found:
            print("Email and password Matched!")
            print("What Operation Do you want to do?")
            print("1.Lend Book 2.Give Back Book")
            x=int(input())
            if x == 1:
              user.lendbook()
            else:
              user.returnbook()
        else:
            print("Wrong Credentials")

    else:
        print("WELCOME TO USER REGISTRATION")
        print("Input your new Username")
        username = input()
        print("Input your new Password")
        password = input()
        with open("users.txt", "a") as file:
            file.write(f"{username},{password}\n")
