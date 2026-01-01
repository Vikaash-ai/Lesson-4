num = int(input("Enter your days: "))

years = num//365
left_over = num%365
months = left_over//30
left_over = left_over%30
weeks = left_over//7
left_over = left_over%7
days = left_over//7
left_over = left_over%7

print(f"The Number of years: {years}")
print(f"The number of months: {months}")
print(f"The number of weeks: {weeks}")
print(f"The number of days: {days}")