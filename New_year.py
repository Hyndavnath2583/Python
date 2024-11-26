'''Program to calculate time left for next new year'''
from datetime import datetime

def time_until_new_year(current_datetime_str):
    current_datetime = datetime.strptime(current_datetime_str, "%b %d %Y %I:%M %p")
    next_year = current_datetime.year + 1
    new_year_datetime = datetime(next_year, 1, 1, 0, 0)  
    time_difference = new_year_datetime - current_datetime
    total_minutes = time_difference.total_seconds() // 60
    hours = int(total_minutes // 60)
    minutes = int(total_minutes % 60)
    
    return f"{hours} hours {minutes} minutes"
if __name__ == "__main__":
    current_datetime_str = input()
    result = time_until_new_year(current_datetime_str)
    print(result)
