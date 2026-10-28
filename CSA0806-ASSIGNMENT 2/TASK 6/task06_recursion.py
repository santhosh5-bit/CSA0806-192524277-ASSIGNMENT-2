# TASK 6: RECURSION AND ITS LIMITS

from functools import lru_cache
import sys
import time

calls = 0


# 1. Normal recursive function
def ways_naive(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_naive(n - 1) + ways_naive(n - 2)


# 2. Recursive function with memoisation
@lru_cache(maxsize=None)
def ways_memo(n):
    global calls
    calls += 1

    if n <= 1:
        return 1

    return ways_memo(n - 1) + ways_memo(n - 2)


# 3. Iterative function using a loop
def ways_loop(n):
    if n <= 1:
        return 1

    previous, current = 1, 1

    for i in range(2, n + 1):
        previous, current = current, previous + current

    return current


# MAIN PROGRAM

print("1. ANSWERS FOR 1 TO 6 STEPS")
for n in range(1, 7):
    print("Steps:", n, "Ways:", ways_loop(n))


print("\n2. CALL TREE FOR n = 5")
print("ways(5)")
print("|-- ways(4)")
print("|   |-- ways(3)")
print("|   |   |-- ways(2)")
print("|   |   |-- ways(1)")
print("|   |-- ways(2)")
print("|-- ways(3)")
print("    |-- ways(2)")
print("    |-- ways(1)")


print("\n3. FUNCTION CALL COMPARISON")

for n in [10, 20, 25, 30]:
    calls = 0
    start = time.perf_counter()
    answer1 = ways_naive(n)
    naive_time = time.perf_counter() - start
    naive_calls = calls

    ways_memo.cache_clear()
    calls = 0

    start = time.perf_counter()
    answer2 = ways_memo(n)
    memo_time = time.perf_counter() - start
    memo_calls = calls

    print("\nn =", n)
    print("Naive answer:", answer1)
    print("Memo answer:", answer2)
    print("Answers match:", answer1 == answer2)
    print("Naive calls:", naive_calls)
    print("Memo calls:", memo_calls)
    print(f"Naive time: {naive_time:.6f} seconds")
    print(f"Memo time: {memo_time:.6f} seconds")


print("\n4. TESTING n = 1000")
print("Python recursion limit:", sys.getrecursionlimit())

ways_memo.cache_clear()
calls = 0

try:
    answer = ways_memo(1000)
    print("Memoised answer:", answer)
except RecursionError:
    print("RecursionError occurred at n = 1000.")
    print("The recursive calls exceeded the permitted depth.")


print("\n5. ITERATIVE SOLUTION FOR n = 1000")

start = time.perf_counter()
answer = ways_loop(1000)
loop_time = time.perf_counter() - start

print("Answer calculated successfully.")
print("Number of digits:", len(str(answer)))
print(f"Loop time: {loop_time:.6f} seconds")