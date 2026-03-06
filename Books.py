# Class Definition
class Book:
    # Constructor
    def __init__(self, book_id, title, author, price, copies_available):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price
        self.copies_available = copies_available

    # Method to display book details
    def display_book(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Copies Available:", self.copies_available)
        print("---------------------------")

    # Method to issue books
    def issue_book(self, quantity):
        if quantity <= self.copies_available:
            self.copies_available -= quantity
            print(quantity, "copies issued successfully.")
        else:
            print("Not enough copies available")

    # Method to add copies
    def add_copies(self, quantity):
        self.copies_available += quantity
        print(quantity, "copies added successfully.")

    # Method to calculate total value
    def book_value(self):
        return self.price * self.copies_available


# Main Program

# Creating book objects
book1 = Book(101, "Python Programming", "Mark Lutz", 750, 5)
book2 = Book(102, "Data Structures and Algorithms", "Thomas H. Cormen", 1200, 3)
book3 = Book(103, "Machine Learning Basics", "Andrew Ng", 950, 4)

# List (Array) of objects
library = [book1, book2, book3]

# Display all books
print("Library Books")
print("=================")
for book in library:
    book.display_book()

# Issue copies
print("Issuing Books")
book1.issue_book(2)

# Add copies
print("Adding Copies")
book2.add_copies(2)

# Display updated books
print("\nUpdated Book Details")
for book in library:
    book.display_book()

# Calculate total library value
total_value = 0
for book in library:
    total_value += book.book_value()

print("Total value of all books in library:", total_value)