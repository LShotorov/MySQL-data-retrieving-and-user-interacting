def confirmation(book_id: str) -> bool:
    '''Function to ask for user confirmation before deleting a book with the given book ID.'''

    confirmation = ''
    while confirmation not in ['YES', 'NO']:
        print(f'\nAre you sure you want to delete book ID: {book_id}?\nATTENTION: YOU CAN NOT CANCEL THIS ACTION!')
        print("\nPlease type 'YES' (with uppercase letters) to confirm, or 'NO' (with uppercase letters) to cancel.")
        confirmation = input('> ')
    return confirmation == 'YES'


def continue_delete() -> bool:
    '''Function to ask the user if they want to delete another book.
    Returns a boolean value.'''

    print('\nWould you like to delete another book? (y/n)')
    continue_confirmation = input('\n> ').lower()
    while continue_confirmation not in ['y', 'n']:
        print("Invalid input. Please type 'y' to delete another book, or 'n' to exit.")
        continue_confirmation = input('\n> ').lower()
    return continue_confirmation == 'y'


def delete_book(mydb, mycursor, book_id: str):
    '''Function to delete a book with the given book ID from the books table.'''

    if confirmation(book_id):
        mycursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
        mydb.commit()
        print('Book successfully deleted!')