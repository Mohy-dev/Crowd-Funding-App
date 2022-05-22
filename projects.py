from datetime import datetime
import database_operations


def is_valid_date(entered_date):
    if datetime.strptime(entered_date, "%d/%m/%Y") < datetime.now():
        return 0
    return 1


def stout_all_projects(projects_file):
    all_projects = database_operations.get_projects_list(projects_file)
    if len(all_projects) == 0:
        print("There is no projects yet")
        return
    for project in all_projects:
        print(project)


def project_title():
    title = input("Enter the project title: ")
    return title


def project_details():
    details = input("Enter the project details: ")
    return details


def project_target():
    target = input("Enter the project target: ")
    if not target.isdigit():
        print("Only valid numbers are valid")
        project_target()
    return target


def check_digit(digit):
    if not digit.isdigit():
        print("Enter a valid digit.")
        return 0
    return 1


def project_start_date():
    print("Enter the project start date: ")
    while(1):
        year = input('Enter the year: ')
        if check_digit(year):
            break
    while(1):
        month = input('Enter the month: ')
        if check_digit(month):
            break
    while(1):
        day = input('Enter the day: ')
        if check_digit(day):
            break
    start_date = f"{day}/{month}/{year}"
    if not is_valid_date(start_date):
        print("Enter valid date, format is (YYYY-MM-DD)")
        project_start_date()
    return start_date


def project_end_date():
    print("Enter the project end date: ")
    while(1):
        year = input('Enter the year: ')
        if check_digit(year):
            break
    while(1):
        month = input('Enter the month: ')
        if check_digit(month):
            break
    while(1):
        day = input('Enter the day: ')
        if check_digit(day):
            break
    end_date = f"{day}/{month}/{year}"
    if not is_valid_date(end_date):
        print("Enter valid date, format is (YYYY-MM-DD)")
        project_end_date()
    return end_date
