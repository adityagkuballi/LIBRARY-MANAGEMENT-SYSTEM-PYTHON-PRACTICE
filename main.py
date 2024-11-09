from crud import add_book, get_book, add_member, view_member, issue_book, return_book, member_Transactions, delete_book


def addNewBook():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    isbn = input("Enter book ISBN: ")
    count = int(input("Enter number of copies: "))
    add_book(title,author,isbn,count)
    print("New Book Added")

def printBooks():
    books=get_book()
    for book in books:
        # available=""
        # if book.count > 0:
        #    available = "Available"
        # else:
        #    available = "Not Available"
        available = "Available" if book.count > 0 else "Not Available"
        print(f"{book.id}: '{book.title}' by {book.author} (ISBN: {book.isbn}) - {available} {book.count} copies")

def addNewMember():
    name = input("Enter member name: ")
    email = input("Enter member email: ")
    add_member(name, email)
    print("New Member Added")

def viewMember():
    views = view_member()
    for view in views:
        print(f"Member name: {view.name} (Email: {view.email})")

def issueABook():
    book_id = int(input("Enter book ID:"))
    member_id = int(input("Enter member ID:"))
    issue_book(book_id,member_id)

def returnBook():
    transaction_id = int(input("Enter transaction ID:"))
    return_book(transaction_id)

def get_transactions_by_member():
    member_id = int(input("Enter member ID:"))
    transactions = member_Transactions(member_id)
    for transaction in transactions:
        return_status = "Returned" if transaction.return_date else "Not Returned"
        print(f"Member transactions Details Book Id: {transaction.book_id}, Book Issue Date: {transaction.issue_date}, Book Return Date: {transaction.return_date}, Return Status: {return_status}")

def deleteBook():
    book_id = int(input("Enter book Id:"))
    delete_book(book_id)
    print("Book Deleted")

def main():
    while True:
        print("************************************************")
        print("1. Add Book")
        print("2. View Book")
        print("3. Add Member")
        print("4. View Member")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. View Transactions by Member")
        print("8. Delete Book")
        print("9. Exit")
        print("************************************************")
        choice = input("Enter your choice: ")


        if choice == "1":
            addNewBook()
        elif choice == "2":
            printBooks()
        elif choice == "3":
            addNewMember()
        elif choice == "4":
            viewMember()
        elif choice == "5":
            issueABook()
        elif choice == "6":
            returnBook()
        elif choice == "7":
            get_transactions_by_member()
        elif choice == "8":
            deleteBook()
        elif choice == "9":
            print("Exited")
            break
        else:
            print("Invalid choice")

if __name__== "__main__":
    main()