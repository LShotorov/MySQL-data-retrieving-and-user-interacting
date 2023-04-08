import mysql.connector
import editbook
import addbook
import deletebook

mydb = mysql.connector.connect(
    host = 'localhost', # TODO add host
    user = 'root', # TODO add user
    password = 'admin', # TODO add password
    database = 'libraries_and_books', # TODO change the database name if needed
)
mycursor = mydb.cursor()



def show_libraries(mycursor) -> list:
    '''Executes a SELECT query to retrieve all libraries from the database.
    Returns a list of library IDs.'''

    mycursor.execute("SELECT * FROM libraries")
    all_libraries = mycursor.fetchall()
    libraries_id = ['0']
    for library in all_libraries:
        print(f"ID: {library[0]}  Name: {library[1]}\nLocation: {library[2]}\n")
        libraries_id.append(str(library[0]))
    print('0 - Exit the program')
    return libraries_id
    

def show_books(mycursor, library_id: str) -> list:
    '''Executes a SELECT query to retrieve all books from a given library.
    Returns a list of book IDs.'''

    mycursor.execute(f"SELECT id, title, author, genre, publisher FROM books WHERE library_id = {library_id}")
    all_books = mycursor.fetchall()
    books_id = ['0']
    for book in all_books:
        print(f'ID: {book[0]} Name: {book[1]}\nAuthor: {book[2]}\nGenre: {book[3]}\nPublisher: {book[4]}\n')
        books_id.append(str(book[0]))
    print('0 - Exit the program')
    return books_id


def library_commands() -> str:
    '''Display available commands for library-related actions and returns user input.'''

    print('\nPlease enter a command:' \
        '\n1 - Show books' \
        '\n2 - Add book' \
        '\n3 - Delete book' \
        '\n0 - Exit the program')
    
    commands = ['0', '1', '2', '3']    
    user_command = input('> ')
    while user_command not in commands:
        print('\nInvalid command. Please try again.')
        user_command = input('> ') 
    return user_command


def book_commands() -> str:
    '''Display available commands for book-related actions and returns user input.'''

    print('\nPlease enter a command:' \
        '\n1 - Edit book' \
        '\n0 - Exit the program')
        
    user_book_command = input('> ')
    while user_book_command not in ['0', '1']:
        print('\nInvalid command. Please try again.')
        user_book_command = input('> ')
    return user_book_command


def validate_input(user_input: str, validator: list, action: str) ->str:
    '''Validates user input against a given validator list for a specific action (e.g. library ID, book ID).
    Returns the validated user input.'''

    while user_input not in validator:
        print(f'Invalid {action}. Please try again.')
        user_input = input('> ')
    return user_input




user_interacting = True
while user_interacting:
    # Display available commands for library-related actions.
    print('\nPlease enter a command:' \
        '\n1 - Show libraries' \
        '\n0 - Exit the program')
    
    user_input = input('> ')
    # Validates user input against a list of valid commands.
    user_input = validate_input(user_input, ['0', '1'], 'command')

    if user_input == '0':
        print('\nThank you for using our services.')
        break
    
    # Display all libraries and their information.
    libraries = show_libraries(mycursor)
    user_chosen_library = input('\nPlease select a library by entering the library ID, or 0 to exit the program.\n> ')
    user_chosen_library = validate_input(user_chosen_library, libraries, 'library ID')
 
    if user_chosen_library == '0':
        print('\nThank you for using our services.')
        break
    
    # Display available commands for library-related actions.
    user_command = library_commands()

    if user_command == '0':
        print('\nThank you for using our services.')
        break
    elif user_command == '1':
        # Display all books in the selected library and their information.
        books = show_books(mycursor, user_chosen_library)

        user_book_select = input('\nPlease select a book by entering the book ID, or 0 to exit the program.\n> ')
        user_book_select = validate_input(user_book_select, books, 'book ID')

        if user_book_select == '0':
            print('\nThank you for using our services.')
            break

        # Display available commands for book-related actions.
        user_book_command = book_commands()
        if user_book_command == '0':
            print('\nThank you for using our services.')
            break
        
        # If user chooses to edit a book, calls the edit_book() function from the editbook module.
        book_edit = editbook.edit_book(mydb, mycursor, user_book_select)
        if book_edit == '0':
            print('\nThank you for using our services.')
            break
        
    elif user_command == '2':
        # If user chooses to add a book, calls the add_book() function from the addbook module.
        add_book = addbook.add_book(mydb, mycursor, user_chosen_library)
        if add_book == '0':
            print('\nThank you for using our services.')
            break
    
    else:
        # If user chooses to delete a book, calls the delete_book() function from the deletebook module.
        while True:
            books = show_books(mycursor, user_chosen_library)
            user_book_delete = input('\nPlease select a book to delete by entering the book ID, or 0 to exit the program.\n> ')
            user_book_delete = validate_input(user_book_delete, books, 'book ID')

            if user_book_delete == '0':
                print('\nThank you for using our services.')
                user_interacting = False
                break
            
            deletebook.delete_book(mydb, mycursor, user_book_delete)

            if deletebook.continue_delete():
                continue
            print('\nThank you for using our services.')
            user_interacting = False
            break

mydb.close()