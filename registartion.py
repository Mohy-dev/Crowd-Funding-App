import re
import database_operations


name_pattern = r'[a-zA-Z\s]+$'
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


# Patterns check

def is_valid_name(name):
    return re.match(name_pattern, name)


def is_valid_password(password, confirm_password):
    if not (re.match('^.{0,8}$', password)):
        return 0
    else:
        return password == confirm_password


def is_valid_email(email):
    return re.match(email_pattern, email)


def is_email_exists(email, users_file):
    json_dict = database_operations.get_all_users(users_file)
    for key in json_dict:
        if key["email"] == email:
            return 1
    return 0


def is_valid_phone(entered_phone):
    return re.match(r"^(010|011|012)[0-9]{8}$", entered_phone)


# Input validations

def name_first_validation():
    first_name = input("Enter you first name:")
    if not is_valid_name(first_name):
        print("Enter a valid name please.")
        return name_first_validation
    return first_name


def name_last_validation():
    last_name = input("Enter you last name:")
    if not is_valid_name(last_name):
        print("Enter a valid name please.")
        return name_last_validation
    return last_name


def email_validation(users_file):
    email = input("Enter your email:")
    while(1):
        if not is_valid_email(email):
            print("Enter a valid email format please.")
            email = input("Enter your email:")
        elif is_email_exists(email, users_file):
            email = input("Enter a different email:")
        else:
            break
    return email


def password_validation():
    password = input("Enter you password:")
    password_confirmed = input("Enter you confirmation password:")
    if not is_valid_password(password, password_confirmed):
        print("Enter a valid password (From to 0 to 8 digits to pass).")
        return password_validation
    return password


def phone_validation():
    entered_phone = input("Enter you phone number:")
    if not is_valid_phone(entered_phone):
        print("Enter a valid name phone number please (Egyptian format phones to pass).")
        return phone_validation
    return entered_phone


# Registration logic

def register(users_file):
    first_name = name_first_validation()
    email = email_validation(users_file)
    last_name = name_last_validation()
    password = password_validation()
    phone = phone_validation()

    user = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "phone_number": phone
    }
    database_operations.create_user(users_file, user)
