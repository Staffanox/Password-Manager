import menu

choice = menu.menu()

while choice != 'Q':
    if choice == '1':
        menu.create_password()
    if choice == '2':
        menu.delete_password()
    if choice == '3':
        menu.find_mail()
    if choice == '4':
        menu.find_website()
    if choice == '5':
        menu.find_website_and_mail()
    else:
        choice = menu.menu()
exit(0)
