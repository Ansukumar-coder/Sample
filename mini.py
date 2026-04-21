#! MAIN BODY
books = []
issued_books = []
def add_books():
    book_name = input("enter the book name:")
    books.append(book_name)
    print("book added successfully")
def show_books():
    if len(books) == 0:
        print("no books available")
    else:
        print("available books:")
        for b in books:
            print(b)
def issue_books():
    show_books()
    book_name = input("enter the book name to issue:")
    if book_name in books:
        books.remove(book_name)
        issued_books.append(book_name)
        print("book issued successfully")
    else:
        print("book not available")
def return_books():
    book_name = input("enter the book name to return:")
    if book_name in issued_books:
        issued_books.remove(book_name)
        books.append(book_name)
        print("book returned successfully")
    else:
        print("book not issued")

def libraray():
    while True:
        print("1.Add Books")
        print("2.Show Books")
        print("3.Issue Books")
        print("4.Return Books")
        print("5.Exit")

        choice = int(input("enetr the choice:"))

        if choice == 1:
            add_books()
        elif choice == 2:
            show_books()
        elif choice == 3:
            issue_books()
        elif choice == 4:
            return_books()
        elif choice == 5:
            print("thank you")
            break
        else:
            print("invalid choice")

libraray()



