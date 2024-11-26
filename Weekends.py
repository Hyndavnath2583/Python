'''count no of saturdays and sundays from a given date D1 to D2'''
from datetime import datetime, timedelta

def count_weekends(d1, d2):
    start_date = datetime.strptime(d1, "%d %b %Y")
    end_date = datetime.strptime(d2, "%d %b %Y")
    saturday_count = 0
    sunday_count = 0
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() == 5: 
            saturday_count += 1
        elif current_date.weekday() == 6: 
            sunday_count += 1
        current_date += timedelta(days=1)
    
    return saturday_count, sunday_count

if __name__ == "__main__":
    d1 = input()
    d2 = input()
    saturday_count, sunday_count = count_weekends(d1, d2)
    print(f"Saturday: {saturday_count}")
    print(f"Sunday: {sunday_count}")

