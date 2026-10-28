# TASK 7: DIAGNOSE, REDESIGN AND VALIDATE

import time

# ORIGINAL PROGRAM: Normal recursion

original_calls = 0


def original_ways(n):
    global original_calls
    original_calls += 1

    if n <= 1:
        return 1

    return original_ways(n - 1) + original_ways(n - 2)


# REDESIGNED PROGRAM: Iterative method

def redesigned_ways(n):
    if n <= 1:
        return 1

    previous = 1
    current = 1

    for i in range(2, n + 1):
        previous, current = current, previous + current

    return current


# TESTING AND COMPARISON

print("TASK 7: REDESIGN AND VALIDATION")
print("=" * 50)

print("\n1. ORIGINAL PROGRAM")
print("Method: Normal recursion")

n = 30

original_calls = 0

start = time.perf_counter()
original_result = original_ways(n)
original_time = time.perf_counter() - start

print("Input steps:", n)
print("Number of ways:", original_result)
print("Function calls:", original_calls)
print(f"Execution time: {original_time:.6f} seconds")


print("\n2. REDESIGNED PROGRAM")
print("Method: Iterative loop")

start = time.perf_counter()
redesigned_result = redesigned_ways(n)
redesigned_time = time.perf_counter() - start

print("Input steps:", n)
print("Number of ways:", redesigned_result)
print("Execution time:", f"{redesigned_time:.6f} seconds")


print("\n3. VALIDATION")
print("Original result:", original_result)
print("Redesigned result:", redesigned_result)
print("Results match:", original_result == redesigned_result)


print("\n4. LARGE INPUT TEST")

large_n = 1000

start = time.perf_counter()
large_result = redesigned_ways(large_n)
large_time = time.perf_counter() - start

print("Input steps:", large_n)
print("Calculation successful:", large_result > 0)
print("Number of digits:", len(str(large_result)))
print(f"Execution time: {large_time:.6f} seconds")


print("\n5. FINAL CONCLUSION")

if original_result == redesigned_result:
    print("The redesigned program produces the correct result.")
    print("The loop avoids repeated recursive calculations.")
    print("The iterative method is suitable for large inputs.")
else:
    print("The results do not match. Check the programs.")