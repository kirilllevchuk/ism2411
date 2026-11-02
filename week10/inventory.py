
# Reflection 1:
# The most surprising thing about Python lists is how easily I can add,
# remove, sort, and access items without having to manually change everything.
# I also learned that lists can be modified, while tuples cannot.

# Reflection 2:
# In a retail business, a Python list could help organize product inventory
# and sales numbers. Instead of manually updating and calculating everything
# in Excel, I could use Python to quickly sort, filter, and calculate totals.

# EXERCISE 1 - Build the list
inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print("Exercise 1:")
print(inventory)
print(len(inventory))


# EXERCISE 2 - Index practice
print("\nExercise 2:")
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])


# EXERCISE 3 - Slicing
print("\nExercise 3:")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])


# EXERCISE 4 - Modify
print("\nExercise 4:")

inventory.append("envelope")
print("After append:", inventory)

inventory.remove("tape")
print("After remove:", inventory)

inventory.sort()
print("After sort:", inventory)


# EXERCISE 5 - Tuple comparison
print("\nExercise 5:")

coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Tuples are useful for coordinates because they cannot be changed accidentally.")

print(coords)


# EXERCISE 6 - Average of sales
print("\nExercise 6:")

sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count
best = max(sales)
worst = min(sales)

print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", best)
print("Worst:", worst)


# EXERCISE 7 - Accumulator pattern
print("\nExercise 7:")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    discounted.append(round(price * 0.90, 2))

print("Original prices:", prices)
print("Discounted prices:", discounted)


# EXERCISE 8 - Filter above threshold
print("\nExercise 8:")

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print("High sales:", high_sales)
print("Count:", len(high_sales))
print("Average:", round(sum(high_sales) / len(high_sales), 2))
