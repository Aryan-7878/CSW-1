# Define the Book class
class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        self.available = copies > 0   

    
    def issue_book(self):
        if self.copies > 0:
            self.copies -= 1
            self.available = self.copies > 0
            print(f"Book issued: {self.title}")
        else:
            print(f"Book not available: {self.title}")

    
    def return_book(self):
        self.copies += 1
        self.available = True
        print(f"Book returned: {self.title}")

    # Method to check availability
    def is_available(self):
        return self.available

    # Method to display book details
    def show_details(self):
        print("Title      :", self.title)
        print("Author     :", self.author)
        print("ISBN       :", self.isbn)
        print("Copies     :", self.copies)
        print("Available  :", "Yes" if self.available else "No")
        print("-" * 35)



book1 = Book("Python Programming", "Guido van Rossum", "ISBN101", 3)
book2 = Book("Data Structures", "Mark Allen Weiss", "ISBN102", 1)


print("Initial Book Details:")
book1.show_details()
book2.show_details()


print("\nIssuing Books:")
book1.issue_book()
book2.issue_book()
book2.issue_book()   


print("\nBook Details After Issuing:")
book1.show_details()
book2.show_details()


print("\nReturning Books:")
book1.return_book()
book2.return_book()


print("\nFinal Book Details:")
book1.show_details()
book2.show_details()