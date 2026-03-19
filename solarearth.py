
import math
from datetime import date

print("--- Earth, Sun and Moon Distance Simulator ---")

while True:
    try:
        year = int(input("Please enter the year: "))
        if  1 <= year <= 2100:
         break
        else:
            print("Only dates in the Comman Era are valid; please select year between 1 and 2100!")  
    except ValueError:
        print("Please enter the year correctly!(ex.1881)")

while True:
    try:
        month = int(input("Please enter the month: "))
        if 0 < month < 13:
            break
        else:
            print("Month value is not valid please select the month between 1 and 12!")
    except ValueError:
        print("Please enter the month correctly!(ex.1993)")

while True:
    try:
        day = int(input("Please enter the day: ")) 
        if day <= 0:
            print("Day cannot be 0 or less than 0, please enter valid day value!")
            continue
      
        if month in [1,3,5,7,8,10,12]:
            if day <= 31:
             break
            else:
                 print("This month only has 31 days, please enter value between 1-31!")
                 
        elif month in [4,6,9,11]:
            if day <= 30:
             break
            else:
                 print("This month only has 30 days, please enter value between 1-30!")     
   
        elif year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if month == 2 and day <= 29:
             break
            else:
                 print("This leap year February has only 29 days, please enter value between 1-29!")
        elif month == 2:
            if day <= 28:
             break
            else:
                 print("February has only 28 days in selected year, please enter value between 1-28!")
    except ValueError:
        print("Please enter your chocie as a number!(ex.17)")

selected_date = date(year, month, day)
begin_of_year = date(year, 1, 1)
reference_date = date(1900, 1, 1)

day_of_year = (selected_date - begin_of_year ).days + 1
sum_of_passed_day = (selected_date - reference_date ).days

sun_distance_km = 149597870 - 2500000 * math.cos((2 * math.pi / 365.25) * (day_of_year - 4))

moon_distance_km = 384400 - 21000 * math.cos((2 * math.pi / 27.55455) * sum_of_passed_day)

print("\n" + "-" * 40)
print(f"Selected Date:         {day:02d}/{month:02d}/{year}")
print(f"Earth - Sun Distance:  {sun_distance_km:,.0f} km")
print(f"Earth - Moon Distance: {moon_distance_km:,.0f} km")
print("-" * 40 + "\n")