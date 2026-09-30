# TO-DO TIME, REGISTRATION, DATE INVALID INPUT ADJUSTMENTS

# LIBRARY MANAGEMENT SYSTEM

from datetime import date, timedelta
from datetime import datetime

books = {
    101 : {
        "title" : "To Kill a Mockingbird",
        "author" : "Harper Lee",
        "category" : "Drama",
        "price" : 249,
        "available" : True
    },
    102 : {
        "title" : "Atomic Habits",
        "author": "James Clear",
        "category": "Self-help",
        "price": 499,
        "available": True
    },
    103 : {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "category": "Fiction",
        "price": 299,
        "available": True
    }
}

issued_books_details = {}

while True:
    try:
        print("\n**********LIBRARY MANAGEMENT SYSTEM**********\n")

        print("1. ADD BOOKS.")
        print("2. SHOW AVAILABLE BOOKS.")
        print("3. ISSUE BOOKS.")
        print("4. ISSUED BOOK AND STUDENT DETAILS.")
        print("5. BOOK SUBMISSION.")
        print("6. EXIT.\n")

        num = int(input("Enter the task you want to perform: "))
        print()

        if num == 1:
            print("**********BOOKS ADDITION**********\n")

            while True:
                try:
                    amount = int(input("Enter the number of books you want to add: "))
                    break
                except ValueError:
                    print("INVALID INPUT!")

            print()

            for i in range(amount):
                title = input("Enter the title of the book: ")
                author = input("Enter the name of the author of the book: ")
                category = input("Enter the category: ")

                while True:
                    try:
                        price = int(input("Enter the price: "))
                        break
                    except ValueError:
                        print("INVALID INPUT!")

                new_id = max(books.keys()) + 1

                books[new_id] = {
                    "title" : title,
                    "author" : author,
                    "category" : category,
                    "price" : price,
                    "available" : True
                }

                print(f"\nBOOK ID SET TO {new_id}")
                print("BOOK SUCCESSFULLY ADDED!\n")

        elif num == 2:

            print("**********BOOKS LIST**********\n")

            for items in books:
                print(f"\n-----{items}-----\n")
                print(f"Title = {books[items]['title']}")
                print(f"Author = {books[items]['author']}")
                print(f"Category = {books[items]['category']}")
                print(f"Price = {"Rs."+str(books[items]['price'])}")

                if books[items]['available']:
                    print("Book available\n")
                else:
                    print("Book not available\n")

        elif num == 3:

            print("\n**********ISSUE DESK**********\n")

            while True:
                try:
                    book = int(input("Enter the id of the book you want to issue: "))
                    break
                except ValueError:
                    print("INVALID INPUT")

            print()
            print("**********STUDENT DETAILS**********")
            print()

            if book not in books.keys():
                print("INVALID ID!")
                print("If you don't know the id of the book choose 2 to see the details of the books available.\n")

            else:
                if books[book]["available"] == True:
                    name = input("Enter your name: ").capitalize()
                    reg_no = None

                    while True:
                        reg_no = input("Enter your registration number: ").upper()
                        stream = reg_no[2:5]
                        year = int(reg_no[:2])

                        streams = ['BCE', 'BAI', 'BMR', 'BAS', 'BME', 'BCY', 'BHI', 'MIP', 'BEC', 'BCC', 'BLC', 'BEE', 'BCH']

                        if stream not in streams:
                            print("INVALID REGISTRATION NUMBER!")
                        elif year < 22:
                            print("INVALID REGISTRATION NUMBER!")
                        elif len(reg_no) != 10:
                            print("INVALID REGISTRATION NUMBER!")
                        else:
                            break

                    while True:
                        date_input = input("Enter the date(DD-MM-YYYY): ")

                        try:
                            date_input = datetime.strptime(date_input, "%d-%m-%Y")
                            break
                        except ValueError:
                            print("Invalid date! Please use DD-MM-YYYY.")

                    while True:
                        entry_time = input("Entry time(HH:MM 24 HOUR FORMAT): ")

                        try:
                            time = datetime.strptime(entry_time, "%H:%M")
                            break
                        except ValueError:
                            print("Invalid Time! Please use HH:MM.")

                    print()
                    print("Book Available")
                    print("BOOK ISSUED.\n")

                    while True:
                        exit_time = input("Exit time(HH:MM 24 HOUR FORMAT): ")

                        try:
                            time = datetime.strptime(exit_time, "%H:%M")
                            break
                        except ValueError:
                            print("Invalid Time! Please use HH:MM.")

                    book_submitted = None
                    print()

                    while book_submitted != "Y" and book_submitted != "N":
                        book_submitted = input("Do you want to return the book(Y/N): ").upper()

                    print()

                    if book_submitted == "Y":

                        books[book]["available"] = True
                        print("BOOK RETURNED\n")

                    elif book_submitted == "N":

                        books[book]["available"] = False
                        print("BOOK NOT RETURNED")

                        print(f"Last date to return: {date.today() + timedelta(days=7)}.")

                    issued_books_details[book] = {
                        "name" : name,
                        "reg_no" : reg_no,
                        'date' : date_input,
                        "entry_time" : entry_time,
                        "issued" : books[book]["available"],
                        "exit_time" : exit_time,
                        "return_date" : date.today() + timedelta(days=7)
                    }
                elif books[book]['available'] == False:
                    print("BOOK NOT AVAILABLE\n")
                    
        elif num == 4:

            for items in issued_books_details:
                print(f"BOOK ID: {items}")
                print(f"Student Name: {issued_books_details[items]['name']}")
                print(f"Registration Number: {issued_books_details[items]['reg_no']}")
                print(f"Date: {issued_books_details[items]['date']}")
                print(f"Entry Time: {issued_books_details[items]['entry_time']}")
                print(f"Return Date: {issued_books_details[items]['return_date']}")
                print(f"Exit Time: {issued_books_details[items]['exit_time']}")

                if issued_books_details[items]['issued']:
                    print("BOOK WAS RETEURNED\n")
                else:
                    print("BOOK WAS NOT RETURNED\n")

        elif num == 5:

            print("\n**********BOOK SUBMISSION**********\n")

            id = int(input("Enter the id of the book you want to submit: "))

            print()

            if id not in issued_books_details:
                print("The book was not issued.")

            else:
                if issued_books_details[id]['issued']:
                    print("The book was returned.")
                else:
                    while True:
                        submission_date = input("Enter date(DD-MM-YYYY): ")
                        try:
                            submission_date = datetime.strptime(submission_date, "%d-%m-%Y")
                            break
                        except ValueError:
                            print("INVALID DATE FORMAT!")

                    print("BOOK SUBMITTED")
                    books[id]['available'] = True

        elif num == 6:
            print("*********EXITING THE LIBRARY*********")
            break

        else:
            print("INVALID INPUT!")
    except ValueError:
        print("INVALID INPUT!")