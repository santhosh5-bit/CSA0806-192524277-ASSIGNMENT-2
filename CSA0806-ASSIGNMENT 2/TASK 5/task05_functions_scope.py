# TASK 5: FUNCTIONS, PARAMETERS AND SCOPE

# 1. Function with a mutable default argument (incorrect method)
def add_item_buggy(item, order=[]):
    order.append(item)
    return order


# 2. Correct method using None
def add_item(item, order=None):
    if order is None:
        order = []

    order.append(item)
    return order


# 3. Function returning two values
def calculate_bill(price, quantity=1, gst_rate=0.05):
    subtotal = price * quantity
    gst = subtotal * gst_rate
    total = subtotal + gst

    return total, gst


# 4. Global variable
order_count = 0


def count_order():
    global order_count
    order_count += 1
    return order_count


# 5. Nonlocal variable
def customer_counter():
    count = 0

    def add_customer():
        nonlocal count
        count += 1
        return count

    return add_customer


# MAIN PROGRAM

print("1. MUTABLE DEFAULT ARGUMENT")

print("Buggy orders:")
print(add_item_buggy("Tea"), add_item_buggy("Vada"))

print("\nCorrect orders:")
print(add_item("Tea"))
print(add_item("Vada"))
print(add_item("Coffee"))


print("\n2. FUNCTION PARAMETERS")

# Positional arguments
total1, gst1 = calculate_bill(100, 2)

print("Positional arguments:")
print("Total:", total1)
print("GST:", gst1)

# Keyword arguments
total2, gst2 = calculate_bill(
    price=200,
    quantity=1,
    gst_rate=0.05
)

print("\nKeyword arguments:")
print("Total:", total2)
print("GST:", gst2)

# Default arguments
total3, gst3 = calculate_bill(50)

print("\nDefault arguments:")
print("Total:", total3)
print("GST:", gst3)


print("\n3. GLOBAL VARIABLE")

print("Order count:", count_order())
print("Order count:", count_order())


print("\n4. NONLOCAL VARIABLE")

counter = customer_counter()

print("Customers:", counter())
print("Customers:", counter())
print("Customers:", counter())