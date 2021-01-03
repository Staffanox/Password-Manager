import db_functions
import getpass

private_key_pw = getpass.getpass("Please provide the password to your private key : ")


def menu():
    print('-' * 30)
    print(('-' * 13) + 'Menu' + ('-' * 13))
    print('1. Create new password')
    print('2. Delete a password')
    print('3. Find all sites and apps connected to an email')
    print('4. Find a password for a site or app')
    print('5. Find a password for a website and email')
    print('Q. Exit')
    print('-' * 30)
    return input(': ')


def create_password():
    website = input("Please enter the website you want to create a password for : ")
    email = input("Please enter an E-Mail to sign up : ")
    pw = input("Please enter a password : ")
    username = input("Please provide a username for this app or site (if applicable) : ")
    if username is None:
        username = ''
    db_functions.store_password(username, email, pw, website)


def delete_password():
    username = input("Please provide the username of the entry : ")
    website = input("Please provide the website of the entry : ")
    email = input("Please provide the email of the entry : ")
    db_functions.delete_password(username, email, website)


def find_mail():
    email = input("Please provide the E-Mail you want to search for : ")
    db_functions.find_by_mail(private_key_pw, email)


def find_website():
    website = input("Please provide the website you want to search for : ")
    db_functions.find_by_website(private_key_pw, website)


def find_website_and_mail():
    website = input("Please provide the website you want to search for : ")
    email = input("Please provide the E-Mail you want to search for : ")
    db_functions.find_by_website_and_email(private_key_pw, website, email)
