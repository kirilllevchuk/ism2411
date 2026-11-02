# ISM 2411 - Functions Lab
#
# Self-Assessment 1:
# The first bug I noticed was that total = sale replaced the running
# total instead of adding each sale. Reading the code and error messages
# also helped identify the missing colon and the while-loop boundary
# error. This showed me that debugging means checking both error messages
# and the logic of assignments and loop conditions.
#
# Self-Assessment 2:
# apply_discount(price, tier) takes a price and a discount tier.
# It returns the price after applying the discount for that tier:
# gold is 15%, silver is 10%, bronze is 5%, and other tiers get 0%.
# A colleague can use it by passing a price and a tier such as "gold".
#
# Self-Assessment 3 - AI disclosure:
# No AI used


# --- Exercise 1 ---

def calculate_tax(price, rate):
    return price * rate


print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")


# --- Exercise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0

    return price * (1 - discount)


print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")


# --- Exercise 3 ---

discounted_price = apply_discount(200, "gold")
print(f"After gold discount: ${discounted_price:.2f}")

tax_amount = calculate_tax(discounted_price, 0.07)
print(f"After tax: ${discounted_price + tax_amount:.2f}")


def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax_amount = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax_amount


print(
    f'final_price(200, "gold", 0.07) = '
    f"${final_price(200, 'gold', 0.07):.2f}"
)


# --- Exercise 4 ---

orders = [
    (200, "gold"),
    (150, "silver"),
    (80, "bronze"),
    (500, "none")
]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# --- Exercise 5 ---

# Corrected version of broken_sales.py:
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale  # Bug 1 fixed: accumulate each sale instead of replacing total.
print(f"Total: ${total}")

count = 0
for sale in sales:  # Bug 2 fixed: add the missing colon after the for statement.
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):  # Bug 3 fixed: < avoids indexing past the last item.
    print(sales[i])
    i += 1


# --- Exercise 6 ---

x = 100  # Global variable

def double_it():
    x = 999  # Local variable; it is separate from the global x.
    return x * 2


print(x)            # Prints 100
print(double_it())  # Prints 1998
print(x)            # Prints 100 again

# Scope means where a variable can be accessed. The x inside
# double_it() is local to that function, so it does not change
# the global x.
