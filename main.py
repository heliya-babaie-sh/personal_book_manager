from books import show_books
name = input("please enter your name: ")
print("welcome", name)
books = []
count = int(input("how many books do you want? "))
for i in range(count):
    book = input("plaese enter a library name: ")
    books.append(book)

show_books(books)