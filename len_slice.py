# code 28-30 got solve using a tuple

# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives","anchovies", "mushrooms"]

slices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = slices.count(2)
print(num_two_dollar_slices)

num_pizzas = len(toppings)
print('We sell' + ' ' + str(num_pizzas) + ' ' + 'different kinds of pizza')

pizzas_and_prices = [[2, 'pepperoni'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']]

print(pizzas_and_prices)

pizzas_and_prices.sort()
print(pizzas_and_prices)

cheapest_pizza = pizzas_and_prices[0]

priciest_pizza = pizzas_and_prices[6]

pizzas_and_prices.pop()
print(pizzas_and_prices)

new_item = (2.5, 'peppers')
pizzas_and_prices.insert(4, new_item)
print(pizzas_and_prices)

three_cheapest = pizzas_and_prices[:3]
print(three_cheapest)
