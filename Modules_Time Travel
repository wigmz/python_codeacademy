import datetime as dt
from decimal import Decimal
from random import randint, choice
from custom_module import generate_time_travel_message

current_date = dt.date.today()
current_time = dt.datetime.now().time()

print(f"Current date: {current_date}")
print(f"Current time: {current_time}")

year = dt.date.today()
destination = "Mars"
cost = Decimal('2000.00')

message = generate_time_travel_message(year, destination, cost)
print(message)

current_year = Decimal('2023')
target_year = Decimal('1985')

year_difference = abs(current_year - target_year)

base_cost = Decimal('2000.00') 

total_cost = base_cost + (year_difference * Decimal('10.00'))

print(f"Year difference: {year_difference}")
print(f"Total cost: ${total_cost}")

start_year_int = int(target_year)
end_year_int = int(current_year)

random_year = randint(start_year_int, end_year_int)

print(f"Random year for time travel: {random_year}")

destinations = ["Vulcan", "Borg", "Bajor", "Romulus", "Q-Dimension"]

random_destination = choice(destinations)

print(f"Random destination for space travel: {random_destination}")

message = generate_time_travel_message(random_year, random_destination, total_cost)
print(message)





