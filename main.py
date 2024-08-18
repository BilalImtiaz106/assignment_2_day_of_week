import datetime

date_input_str = input("Enter the date in YYYY-MM-DD format: ")
date_input = datetime.datetime.strptime(date_input_str, "%Y-%m-%d").date()
day_of_week_num = date_input.weekday()
if day_of_week_num == 0:
    print(f"{date_input} is a Monday.")
elif day_of_week_num == 1:
    print(f"{date_input} is a Tuesday.")
elif day_of_week_num == 2:
    print(f"{date_input} is a Wednesday.")
elif day_of_week_num == 3:
    print(f"{date_input} is a Thursday.")
elif day_of_week_num == 4:
    print(f"{date_input} is a Friday.")
elif day_of_week_num == 5:
    print(f"{date_input} is a Saturday.")
elif day_of_week_num == 6:
    print(f"{date_input} is a Sunday.")
else:
    print("Something went wrong!")

