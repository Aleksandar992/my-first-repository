
class Library():
    def __init__(self,listofBooks):
        self.availableBooks = listofBooks

    def displayAvailableBooks(self):
        print("\n------------------------------------------\n")
        print("Available books in library are: ")
        print("\n------------------------------------------\n")
        for book in self.availableBooks:
            print(book)

    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("\n------------------------------------------\n")
            print("Now you borrowed a book")
            print("\n------------------------------------------\n")
            self.availableBooks.remove(requestedBook)
        else:
            print("\n------------------------------------------\n")
            print("Sorry, but that book isn't available")
            print("\n------------------------------------------\n")

    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("\n------------------------------------------\n")
        print("You have return a book. Thank you, I really hope that you enjoy redding.")
        print("\n------------------------------------------\n")

class Reader():
    def requestBook(self):
        print("\n------------------------------------------\n")
        print("Which book you want to lend?")
        print("\n------------------------------------------\n")
        self.book = input()
        return self.book

    def returnBook(self):
        print("\n------------------------------------------\n")
        print("Please, tell me which book are you returning? ")
        print("\n------------------------------------------\n")
        self.book = input()
        return self.book

library = Library(["Igra Andjela", "Znakovi pored puta", "Prokleta Avlija", "Stranac", "Majsor i Margarita"])
reader = Reader()

while True:
    print("Press 1 to display available books.")
    print("Press 2 to borrow a book.")
    print("Press 3 to return a book.")
    print("Press 4 to exit.")
    userChoice = int(input())
    if userChoice is 1:
        library.displayAvailableBooks()
    elif userChoice is 2:
        requestedBook = reader.requestBook()
        library.lendBook(requestedBook)
    elif userChoice is 3:
        returnedBook = reader.returnBook()
        library.addBook(returnedBook)
    elif userChoice is 4:
        quit()
   