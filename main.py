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
      with open("librarians.txt", "r") as file:
          for line in file:
              username, password = line.strip().split(",")
              print(username)
  def addlibrarian(self, name, password):
      self.name=name
      self.password=password
      with open("librarians.txt", "a") as file:
          file.write(f"{name},{password}\n")
          print("New Librarian added successfully.")
  def removelibrarian(self,username):
    with open("librarians.txt", "r") as file:
        lines = file.readlines()

    with open("librarians.txt", "w") as file:
        for line in lines:
            if not line.startswith(username + ","):
                file.write(line)

    print(f"Username '{username}' removed successfully.")

  def seebooklist(self):
      with open("books.txt", "r") as file:
          for line in file:
              book_name = line.strip()
              print(book_name)

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
        print("Input The Number of the operation you want to do")
        print("1.See Librarian List\n2.Add Librarian\n3.Remove Librarian\n4.See Book List\n5.Add Book\n6.Remove Book\n")
        x=int(input())
        if x == 1:
            admin.seelibrarianlist()
        elif x == 2:
            print("Write User Name")
            name = input()
            print("Write PassWord")
            password = input()
            admin.addlibrarian(name, password)
        elif x == 3:
            print("Input the username")
            username=input()
            admin.removelibrarian(username)
        elif x == 4:
            admin.seebooklist()
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
