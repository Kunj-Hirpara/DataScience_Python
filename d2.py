books = {}

while True:
    print("\n===== BOOK RECORD MANAGEMENT =====")
    print("1. Add Book.")
    print("2. Search Book.")
    print("3. Update Book.")
    print("4. Delete Book.")
    print("5. Display All Books.")
    print("6. Exit.")

    choice = int(input("Enter your choice: "))

    # Create - Add Book
    if choice == 1:
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Book Author: ")
        copies = int(input("Enter Available Copies: "))
        if book_id in books:
            print("Book ID already exists. Please use a unique ID.")
        else:
            books[book_id] = {
                "Title": title,
                "Author": author,
                "Copies": copies
            }
            print("Book added successfully.")

    # Read - Search Book
    elif choice == 2:
        book_id = int(input("Enter Book ID to search: "))
        if book_id in books:
            print("\nBook ID: ", book_id)
            print("Title: ", books[book_id]["Title"])
            print("Author: ", books[book_id]["Author"])
            print("Available Copies: ", books[book_id]["Copies"])
        else:
            print("Book not found.")

    # Update - Update Copies
    elif choice == 3:
        book_id = int(input("Enter Book ID to Update: "))
        if book_id in books:
            copies = int(input("Enter new available copies: "))
            books[book_id]["Copies"] = copies
            print("Book copies updated successfully.")
        else:
            print("Book not found.")

    # Delete - Delete Book
    elif choice == 4:
        book_id = int(input("Enter Book ID to Delete: "))
        if book_id in books:
            del books[book_id]
            print("Book deleted successfully.")
        else:
            print("Book not found.")

    # Display all books
    elif choice == 5:
        if len(books) == 0:
            print("No book records available.")
        else:
            print("\nBook Records")
            print(("----------------------------"))
            for book_id, data in books.items():
                print("Book ID: ", book_id)
                print("Title: ", data["Title"])
                print("Author: ", data["Author"])
                print("Copies: ", data["Copies"])
                print("----------------------------")

    # Exit
    elif choice == 6:
        print("Program Ended.")
        break
    else:
        print("Invalid Choice! Please try again.")