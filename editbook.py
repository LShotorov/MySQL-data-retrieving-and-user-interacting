def edit(mydb, mycursor, user_book_select: str, action: str) -> str:
    '''Function to prompt the user to enter a new value for a specified field of a book.
    Updates the book value in the books table.'''

    confirmation = ''
    while confirmation != 'y':
        print(f'\nPlease enter the new {action} of the book')
        new_book_action = input('> ')
        
        print(f'\nCONFIRMATION\nAre you sure you want to use this {action}: {new_book_action}? (y/n)')
        confirmation = input('> ')
        while confirmation.lower() not in ['y', 'n']:
            print("\nInvalid confirmation. Please type 'y' to confirm or 'n' to decline.")
            confirmation = input('> ')
    mycursor.execute(f"UPDATE books SET {action.lower()} = %s WHERE id = %s", (new_book_action, user_book_select))
    mydb.commit()
    return f'\nBook {action} changed successfully!'


def continue_edit() -> bool:
    '''Function to check if the user wants to continue editing the book.
    Returns boolean value based on user input.'''

    print('\nWould you like to make another edit? (y/n)')
    continue_confirmation = input('\n> ').lower()
    while continue_confirmation not in ['y', 'n']:
        print("Invalid input. Please type 'y' to make another edit, or 'n' to exit.")
        continue_confirmation = input('\n> ').lower()
    return continue_confirmation == 'y'



def edit_book(mydb, mycursor, user_book_select: str) -> str:
    '''Function to ask the user to select a field to edit.
    Makes the edit and updates the book value in the books table.'''

    while True:
        print('\nPlease enter a field that you want to edit:' \
            '\n1 - Book title' \
            '\n2 - Book author' \
            '\n3 - Book genre' \
            '\n4 - Book publisher' \
            '\n0 - Exit the program')

        edit_commands = {'0': 'Exit',
                        '1': 'Title',
                        '2': 'Author',
                        '3': 'Genre',
                        '4': 'Publisher'}

        user_edit_command = input('> ')
        while user_edit_command not in edit_commands:
            print('Invalid command. Please try again.')
            user_edit_command = input('> ')

        if user_edit_command == '0':
            break
        
        print(edit(mydb, mycursor, user_book_select, edit_commands[user_edit_command]))
        if not continue_edit():
            break

    return '0'