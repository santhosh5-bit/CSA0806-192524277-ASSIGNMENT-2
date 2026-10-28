import time

# Create 200,000 items
items = [f"Item{i}:Rs{i % 50}" for i in range(200_000)]


# Method 1: Using +=
def build_plus(parts):
    text = ""
    for p in parts:
        text += p + ";"
    return text


# Method 2: Using join()
def build_join(parts):
    return "".join(p + ";" for p in parts)


# Method 3: Using f-strings
def build_fstring(parts):
    text = ""
    for i, p in enumerate(parts):
        text += f"{p};"
    return text


# Measure +=
start = time.perf_counter()
a = build_plus(items)
t_plus = time.perf_counter() - start

# Measure join()
start = time.perf_counter()
b = build_join(items)
t_join = time.perf_counter() - start

# Measure f-string method
start = time.perf_counter()
c = build_fstring(items)
t_fstring = time.perf_counter() - start

# Display results
print("STRING BUILDING PERFORMANCE")
print("-" * 45)

print("Same text (+ and join):", a == b)
print("Same text (+ and f-string):", a == c)
print("Length:", len(b))

print(f"+= time       : {t_plus:.4f} seconds")
print(f"join() time   : {t_join:.4f} seconds")
print(f"f-string time : {t_fstring:.4f} seconds")

