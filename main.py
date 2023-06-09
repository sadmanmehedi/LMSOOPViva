from abc import ABC, abstractmethod

librarians = []
books = []
users = []

# =========================================================================

class Person():
    def __init__(self, username, password):
        self.username = username
        self.password = password


# ============================================================================

class Admin(Person):
  def seelibrarianlist(self):
    print(librarians)
  def addlibrarian(self):
    pass
  def removelibrarian(self):
    pass

  def seebooklist(self):
    print(books)

  def addbook(self):
    pass
  def removebook(self):
    pass


# ==============================================================================

class Librarian(Person):
  def changepassword(self):
    pass

  def createnewbook(self):
    pass

  def readbook(self):
    print(books)

  def updatebook(self):
      pass

  def deletebook(self):
      pass

  def createnewuser(self):
      pass

  def readuser(self):
      print(users)

  def updateuser(self):
      pass

  def deleteuser(self):
      pass


# ==============================================================================
class User(Person):

    def lendbook(self):
        pass

    def returnbook(self):
        pass


# ==============MAIN FUNCTION=====================================

admin = Admin("admin", "admin")


print("Hello There!")
print("Which Menu to Open(Give the number)?")
print("1.Admin 2.Librarian 3.User")
user = int(input())

if user == 1:
    print("Input your Username")
    email = input()
    print("Input your Password")
    password = input()
    if email == admin.username and password == admin.password:
        print("Congratulations you have logged in as Admin")
    else:
        print("Invalid Credentials")


elif user == 2:
    print("What you want?\n 1.Login 2.Register")
    choice = int(input())
    if choice == 1:
     print("WELCOME TO LIBRARIAN REGISTRATION")
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
