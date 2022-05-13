monthCode = {
    "January": 5,
    "February": 1,
    "March": 1,
    "April": 4,
    "May": 6,
    "June": 2,
    "July": 4,
    "August": 0,
    "September": 3,
    "October": 5,
    "November": 1,
    "December": 3,
}
#formula
date = int(input("Enter the date: "))
if date > 31:
    print("Please write a number between 31")
month = input("Enter the month: ")
year = int(input("Enter the year: "))
guess_the_day_step1 = int(date) + int(monthCode[month])
guess_the_day_step2 = guess_the_day_step1 % 7
if guess_the_day_step2 == 1:
    print(f"On date {date}/{month}/{year} the day will be Monday")
elif guess_the_day_step2 == 2:
    print(f"On date{date}/{month}/{year} the day will be Tuesday")
elif guess_the_day_step2 == 3:
    print(f"On date{date}/{month}/{year} the day will be Wednesday")
elif guess_the_day_step2 == 4:
    print(f"On date{date}/{month}/{year} the day will be Thursday")
elif guess_the_day_step2 == 5:
    print(f"On date{date}/{month}/{year} the day will be Friday")
elif guess_the_day_step2 == 6:
    print(f"On date{date}/{month}/{year} the day will be Saturday")
elif guess_the_day_step2 == 0:
    print(f"On date{date}/{month}/{year} the day will be Sunday")
else:
    print("Oops! Something went wrong")