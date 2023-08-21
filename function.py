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

