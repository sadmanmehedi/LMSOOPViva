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
    choice=int(input())
    if choice==1:
     print("Input your Username")
     email = input()
     print("Input your Password")
     password = input()
    else:
        f = open("librarians.txt", "w")

else:
    print("What you want?\n 1.Login 2.Register")
    choice = int(input())
    if choice == 1:
        print("Input your Username")
        email = input()
        print("Input your Password")
        password = input()
    else:
        f = open("users.txt", "w")
