import json
import files_operations
import registartion
from const_injector import db_file_path
import projects


# Post method for the user
def create_user(users_file, user):
    users = get_all_users(users_file)
    file = None
    try:
        files_operations.create_the_dir(db_file_path)
        file = open(users_file, "w")
        if not registartion.is_email_exists(user["email"], users_file):
            users.append(user)
            file.write(json.dumps(users))
    except Exception as ex:
        print(f"Exception from create_user: {ex}")
    finally:
        if file is not None:
            file.close()


# Get method for the all users
def get_all_users(users_file):
    if files_operations.is_file_empty(users_file):
        return []
    else:
        file = None
        try:
            with open(users_file, "r") as file:
                return json.load(file)
        except Exception as ex:
            print(f"Exception from get_all_users: {ex}")
        finally:
            if file is not None:
                file.close()


# Get method for all project
def get_projects_list(projects_file):
    if files_operations.is_file_empty(projects_file):
        return []
    else:
        projects_list = None
        try:
            with open(projects_file, "r") as projects_list:
                return json.loads(projects_list.read())
        except Exception as ex:
            print(f"Exception from get_projects_list: {ex}")
        finally:
            if projects_list is not None:
                projects_list.close()


# Get method to check the existence of specific project
def is_project_exists(entered_title, projects_file):
    all_projects = get_projects_list(projects_file)
    if all_projects is None:
        print("There is no projects yet")
        return 0
    i = 0
    print(all_projects)
    # # print(all_projects[0]['title'])
    for project in all_projects:
        # print("entered")
        # print(type(project))
        # print(project['title'])
        # print(type(project['title']))
        if project["title"] == entered_title:
            print("found")
            # print(project)
            # print(project[0])
            return True
    #     i += 1
    return False


# Post method for project
def create_project(projects_file):
    title = input("Enter project title please to check: ")
    if is_project_exists(title, projects_file):
        print("The project already exists.")
        return
    all_projects = get_projects_list(projects_file)
    print("Now you can enter the rest information about the new project \n")
    details = projects.project_details()
    target = projects.project_target()
    start_date = projects.project_start_date()
    end_date = projects.project_end_date()

    new_project = {
        "title": title,
        "details": details,
        "target": target,
        "start_date": start_date,
        "end_date": end_date,
    }

    # Need optimization you should do the operation on the exists projects, not coping it all
    all_projects.append(new_project)

    projects_list = None
    try:
        files_operations.create_the_dir(db_file_path)
        projects_list = open(projects_file, "w")
        projects_list.write(json.dumps(new_project))
        print("Project created")
    except Exception as ex:
        print(f"Exception from create_project: {ex}")
    finally:
        if projects is not None:
            projects_list.close()


# patch method for project
def edit_project(projects_file):
    title = input("Enter project title please: ")

    if not is_project_exists(title, projects_file):
        print("The project not exists.")
        return

    all_projects = get_projects_list(projects_file)

    for project in all_projects:
        if project["title"] == title:

            print(f"You wanna edit the details of {title}, press y/n")
            decision = input("")
            if decision == "y":
                project["details"] = input("Enter the new details: ")

            print(f"You wanna edit the target of {title}, press y/n")
            decision = input("")
            if decision == "y":
                # need validation
                project["target"] = input("Enter the new target: ")

            projects_list = None

            try:
                projects_list = open(projects_file, "w")
                projects_list.write(json.dumps(all_projects))
                print("Edit succeeded")
            except Exception as ex:
                print(f"Exception from edit_project: {ex}")
            finally:
                if projects is not None:
                    projects_list.close()
        break


# Delete method for project
def delete_project(projects_file):
    entered_title = input("Enter project title please: ")

    if not is_project_exists(entered_title, projects_file):
        print("The project not exists.")
        return

    all_projects = get_projects_list(projects_file)
    after_projects = list(
        filter(lambda i: i['title'] != entered_title, all_projects))

    projects_list = None

    try:
        with open(projects_file, "w") as projects_list:
            projects_list.write(json.dumps(after_projects))
    except Exception as ex:
        print(f"Exception from delete_project: {ex}")
    finally:
        if projects is not None:
            projects_list.close()
