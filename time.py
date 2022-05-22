from datetime import datetime
import time


def is_valid_date():
    year = int(input('Enter a year: '))
    month = int(input('Enter a month: '))
    day = int(input('Enter a day: '))
    new_date = f"{day}/{month}/{year}"
    if datetime.strptime(new_date, "%d/%m/%Y") < datetime.now():
        return 0
    return 1


print(is_valid_date())
