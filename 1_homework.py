from datetime import datetime

date_format = "%Y-%m-%d"

def input_date() -> str:
    date_str = input("Enter date: ")
    try:
       datetime.strptime(date_str, date_format)
       return date_str
    except:
        print(f"Date isn't correct. Date should match {date_format} format.")
        return input_date()      
    
def get_days_from_today(date: str) -> int:
    date_object = datetime.strptime(date, "%Y-%m-%d")
    date_today_object = datetime.today()
    difference = date_today_object - date_object
    return difference.days

date_str = input_date()
days = get_days_from_today(date_str)
print(days)