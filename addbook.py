def confirmation(action: str) -> str:
    '''Function to get user confirmation.
    Returns confirmed book action (e.g new book title, new book author, etc)'''

    confirmation = ''
    while confirmation != 'y':
        print(f'\n{action} of the book')
        new_book_action= input('> ')
        
        print(f'\nCONFIRMATION\nAre you sure you want to use this {action}: {new_book_action}? (y/n)')
        confirmation = input('> ')
        while confirmation.lower() not in ['y', 'n']:
            print("\nInvalid confirmation. Please type 'y' to confirm or 'n' to decline.")
            confirmation = input('> ')
    return new_book_action


def continue_add() -> bool:
    '''Function to check if the user wants to continue adding books.
    Returns boolean value based on user input (True if user wants to add another book)'''

    print('\nWould you like to add another book? (y/n)')
    continue_confirmation = input('\n> ').lower()
    while continue_confirmation not in ['y', 'n']:
        print("Invalid input. Please type 'y' to add another book, or 'n' to exit.")
        continue_confirmation = input('\n> ').lower()
    return continue_confirmation == 'y'


def add_book(mydb, mycursor, library_id: str) -> str:
    '''Function to add a new book to the books table'''
    while True:
        print('Please enter book details:')
        title = confirmation('Title')
        author = confirmation('Author')
        genre = confirmation('Genre')
        publisher = confirmation('Publisher')
        mycursor.execute(
            "INSERT INTO books (title, author, genre, publisher, library_id) VALUES (%s, %s, %s, %s, %s)",
            (title, author, genre, publisher, library_id)
        )
        mydb.commit()
        print('Book successfully added!')

        if not continue_add():
            break
    return '0'