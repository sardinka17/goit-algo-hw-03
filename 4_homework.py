from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    upcoming_birthdays = []
    date_today = datetime.today().date() # start of range/today
    date_today_plus_week = date_today + timedelta(days=7) # end of range/today + 1 week

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date().replace(year=date_today.year) # str to date object and replace birthday's year with the current year

        if birthday.timetuple().tm_yday >= date_today.timetuple().tm_yday and birthday.timetuple().tm_yday <= date_today_plus_week.timetuple().tm_yday: # check if birthday will be during next week
            birthday_day_of_week = birthday.timetuple().tm_wday # birthday's day of week
            congratulation_date = birthday # set initial value of congratulation date as birthday 

            if birthday_day_of_week  == 5 or birthday_day_of_week == 6: # check if birthday will be during a weekend
                next_monday = date_today + timedelta(days=7-date_today.timetuple().tm_wday) # calculates date of next Monday
                congratulation_date = next_monday
                
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date.strftime("%Y.%m.%d")}) # add user to the list with the correct congratulation date 

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Tom Bob", "birthday": "1975.01.26"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)