# Defining a Function
# A function consists of many parts, so let’s first get familiar with its core - a function definition.

# Here’s an example of a function definition:
def function_name():
# functions tasks go here

# Key components:
# The def keyword indicates the beginning of a function (also known as a function header). The function header is followed by a name in snake_case format that describes the task the function performs. It’s best practice to give your functions a descriptive yet concise name.
# Following the function name is a pair of parenthesis ( ) that can hold input values known as parameters (more on parameters later in the lesson!). In this example function, we have no parameters.
# A colon: to mark the end of the function header.
# Lastly, we have one or more valid python statements that comprise the function body (where we have our python comment).
# Notice we’ve indented our # function tasks go here comment. Like loops and conditionals, code inside a function must be indented to show that they are part of the function.
# Here is an example of a function that greets a user for our trip-planning application:

def trip_welcome():
  print("Welcome to Tripcademy!") 
  print("Let's get you to your destination.")

# Calling a Function
# To call our function, we must type out the function’s name followed by a pair of parentheses and no indentation:

directions_to_timesSq()

# Whitespace & Execution Flow
# the print statements all run together when trip_welcome() is called. This is because they have the same base level of indentation (2 spaces).
# In Python, the amount of whitespace tells the computer what is part of a function and what is not part of that function.
# If we wanted to write another statement outside of trip_welcome(), we would have to unindent the new line:

def trip_welcome():
  # Indented code is part of the function body
  print("Welcome to Tripcademy!") 
  print("Let's get you to your destination.")

# Parameters & Arguments

def generate_trip_instructions(location):
  print('Looks like you are planning a trip to visit', location)
  print('You can use the public subway system to get to', location)

generate_trip_instructions('Central Park')
generate_trip_instructions('Grand Central Station')

# Multiple Parameters
# We can write a function that takes in more than one parameter by using commas:

def my_function(parameter1, parameter2, parameter3):
  
# Types of Arguments
# In Python, there are 3 different types of arguments we can give a function.
# Positional arguments: arguments that can be called by their position in the function definition.
# Keyword arguments: arguments that can be called by their name.
# Default arguments: arguments that are given default values.

# Positional Arguments are arguments we have already been using! Their assignments depend on their positions in the function call. Let’s look at a function called calculate_taxi_price() that allows our users to see how much a taxi would cost to their destination 🚕.
def calculate_taxi_price(miles_to_travel, rate, discount):
  print(miles_to_travel * rate - discount )

# In this function, miles_to_travel is positioned as the first parameter, rate is positioned as the second parameter, and discount is the third. When we call our function, the position of the arguments will be mapped to the positions defined in the function declaration.
# 100 is miles_to_travel
# 10 is the rate
# 5 is discount

# calculate_taxi_price(100, 10, 5)
# Alternatively, we can use Keyword Arguments where we explicitly refer to what each argument is assigned to in the function call. Notice in the code example below that the arguments do not follow the same order as defined in the function declaration.
# calculate_taxi_price(rate=0.5, discount=10, miles_to_travel=100)
# Lastly, sometimes we want to give our function parameters default values. We can provide a default value to a parameter by using the assignment operator (=). This will happen in the function declaration rather than the function call.

# Here is an example where the discount argument in our calculate_taxi_price function will always have a default value of 10:
def calculate_taxi_price(miles_to_travel, rate, discount = 10):
  print(miles_to_travel * rate - discount )

# When using a default argument, we can either choose to call the function without providing a value for a discount (and thus our function will use the default value assigned) or overwrite the default argument by providing our own:

# Using the default value of 10 for discount.
calculate_taxi_price(10, 0.5)

# Overwriting the default value of 10 with 20
calculate_taxi_price(10, 0.5, 20)

# Built-in Functions vs User Defined Functions
# There are two distinct categories for functions in the world of Python. What we have been writing so far in our exercises are called User Defined Functions - functions that are written by users (like us!).

# There is another category called Built-in functions - functions that come built into Python for us to use. Remember when we were using print or str? Both of these functions are built into the language for us, which means we have been using built-in functions all along!

destination_name = "Venkatanarasimharajuvaripeta"

# Built-in function: len()
length_of_destination = len(destination_name)

# Built-in function: print()
print(length_of_destination)

# Variable Access
# As we expand our programs with more functions, we might start to ponder, where exactly do we have access to our variables? To examine this, let’s revisit a modified version of the first function we built out together:

def trip_welcome(destination):
  print(" Looks like you're going to the " + destination + " today. ")

# What if we wanted to access the variable destination outside of the function? Could we use it? Take a second to think about what the following program will output, then check the result below!

def trip_welcome(destination):
  print(" Looks like you're going to the " + destination + " today. ")

print(destination)

# Returns
# At this point, our functions have been using print() to help us visualize the output in our interpreter. Functions can also return a value to the program so that this value can be modified or used later. We use the Python keyword return to do this.

# Here’s an example of a program that will return a converted currency for a given location a user may want to visit in our trip planner application.

def calculate_exchange_usd(us_dollars, exchange_rate):
  return us_dollars * exchange_rate

new_zealand_exchange = calculate_exchange_usd(100, 1.4)

print("100 dollars in US currency would give you " + str(new_zealand_exchange) + " New Zealand dollars")

# This would output:

100 dollars in US currency would give you 140 New Zealand dollars

# Saving our values returned from a function like we did with new_zealand_exchange allows us to reuse the value (in the form of a variable) throughout the rest of the program.

# When there is a result from a function that is stored in a variable, it is called a returned function value.
