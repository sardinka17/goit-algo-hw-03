from datetime import datetime


def get_days_from_today(date: str) -> int:
    try:
        date_object = datetime.strptime(date, "%Y-%m-%d")
        date_today_object = datetime.today()
        difference = date_today_object - date_object

        return difference.days
    except Exception as e:
        print(e)
        
        return


date_str = "20-12-12"
days = get_days_from_today(date_str)
print(days)
