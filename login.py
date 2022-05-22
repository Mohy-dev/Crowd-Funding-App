from files_operations import is_file_empty
from database_operations import get_all_users
from const_injector import BACK


def login(users_file, email, password):
    if is_file_empty(users_file):
        return 0
    else:
        json_dict = get_all_users(users_file)
        for user in json_dict:
            if user["email"] == email and user["password"] == password:
                name = user["first_name"] + " " + user["last_name"]
                print(f"{BACK}Welcome back {name}")
                return 1
        return 0
