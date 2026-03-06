class Bookstore:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("---------------------")


# Number of books
n = int(input("Enter number of books: "))

# Array (list) of objects
books = []

# Reading book data
for i in range(n):
    print("\nEnter details of Book", i + 1)
    title = input("Enter title: ")
    author = input("Enter author: ")
    price = float(input("Enter price: "))
    
    book = Bookstore(title, author, price)
    books.append(book)

# Displaying book data
print("\nBook Details:")
for book in books:
    book.display()