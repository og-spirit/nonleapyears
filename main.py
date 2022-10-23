

from pydoc import doc
from telnetlib import theNULL
from tkinter import Y


base_year = 1900 #base year 
max_year = 3000 #max year

non_leap_years_100 = {1900, 2100, 2200, 2300, 2500, 2600, 2700, 2900, 3000} #skip leap year for somee 100 years

print("\nThis small script will list all NON Leap Years from the date you enter as your start date and for a span of years you choose. \n")

while True:
    try:
        start_year = int(input(f"Please enter a start year greater than {base_year} and less than {max_year} \n"))
        if start_year < 1899 or start_year > 3000:
            raise ValueError
        break
    except ValueError:
        print("The value you entered is not valid, numbers(integers) only and between 1900 and 3000 please...\n")
        continue

while True:
    try:
        span_years = int(input("Enter how many years to display non leap years for eg. 300 (integers only) \n"))
        if span_years < 1 or span_years > 1000:
            raise ValueError
        break
    except ValueError:
        print("The value you entered is not valid, numbers(integers) only and between 1 and 1000 please...\n")
        continue

    
year = start_year
count = 0

# test for leap year function
def leap_year(test_year): 
    answer = False
    if (test_year%4 == 0 and test_year%100 != 0) or (test_year%400 == 0) :
        answer = True
    return answer


if max_year > start_year > base_year:

    while count <= span_years:
        if year in non_leap_years_100:
            year += 1
            #continue

        leap_year_answer = leap_year(year)

        if leap_year_answer == False:
            print(year, "is not a leap year. \n")
        
        year += 1
        count += 1

else:

    print(f"Perhaps you didn't enter a year greater than {base_year} and less than {max_year}, or another error has occered")

