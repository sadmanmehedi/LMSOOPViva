librarians = []
books = []
users = []

#...........................................................................
class Person():
    def __init__(self,username):
        self.username=username

#============================================================================
class Admin(Person):
  def seeLibrarianList(self):
      pass
  def addLibrarian(self):
      pass
  def removeLibrarian(self):
      pass
  def seeBookList(self):
      pass
  def addBook(self):
      pass
  def removeBook(self):
      pass




#==============================================================================


class Librarian(Person):
  def changePassword(self):
      pass


# ==============================================================================
class User(Person):
    pass

# ==============================================================================


