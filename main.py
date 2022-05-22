import registartion
from login import login
import projects
import database_operations
from const_injector import db_file_path, YELLOW, RED, BLUE, GRAY, NORMAL


users_file = db_file_path + "/users.json"
projects_file = ""


def user_json_file(email):
    global projects_file
    projects_file = db_file_path + "/" + email + ".json"


def stout_login():
    email = input(f"{YELLOW}Enter you email: ")
    password = input("Enter you password: ")
    if login(users_file, email, password):
        user_json_file(email)
        stdout_db_operations()
    else:
        print(f"{RED}Wrong credentials!!")
        stdout_panel_login()


def stdout_panel_login():
    print("Please select your choice: ")
    print(f"{BLUE}1- Register")
    print("2- login")
    choice = input("")
    if choice.isdigit() and int(choice) in [1, 2]:
        if int(choice) == 1:
            registartion.register(users_file)
            stdout_panel_login()
        elif int(choice) == 2:
            stout_login()
    else:
        print("\n" * 3)
        print(f"{RED}Enter valid choice!")
        stdout_panel_login()


def stdout_db_operations():
    print(f"{NORMAL}Select your operation: ")
    print("1- View the projects")
    print("2- Create a project")
    print("3- Edit a project")
    print("4- Delete a project")

    select = input("")

    if select.isdigit() and int(select) in [1, 2, 3, 4]:
        if int(select) == 1:
            projects.stout_all_projects(projects_file)
        elif int(select) == 2:
            database_operations.create_project(projects_file)
        elif int(select) == 3:
            database_operations.edit_project(projects_file)
        elif int(select) == 4:
            database_operations.delete_project(projects_file)

        print("\n" * 3)
        stdout_db_operations()
    else:
        print("\n" * 3)
        print("Enter valid choice!")
        stdout_panel_login()


stdout_panel_login()
