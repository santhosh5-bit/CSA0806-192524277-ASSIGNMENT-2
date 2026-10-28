# Task 1: State Electricity Subsidy Eligibility

households = [
    (1, 100, False, False),
    (2, 101, True, False),
    (3, 150, False, False),
    (4, 200, True, False),
    (5, 201, False, False),
    (6, 250, False, True),
    (7, 80, False, False),
    (8, 180, True, True)
]

print("STATE ELECTRICITY SUBSIDY ELIGIBILITY")
print("-" * 60)

for number, units, ration_card, member_above_80 in households:

    print(f"\nHousehold {number}")
    print("Units:", units)
    print("Ration card:", ration_card)
    print("Member above 80:", member_above_80)

    # Method 1: Separate if statements
    print("Separate if statements:")

    if units <= 100:
        print("Full Subsidy")

    if 101 <= units <= 200 and ration_card:
        print("Partial Subsidy")

    if units > 200 and not member_above_80:
        print("No Subsidy")

    if units > 200 and member_above_80:
        print("Subsidy for Senior Citizen")

    # Method 2: if-elif-else
    print("If-elif-else:")

    if units <= 100:
        print("Full Subsidy")
    elif 101 <= units <= 200 and ration_card:
        print("Partial Subsidy")
    elif units > 200 and member_above_80:
        print("Subsidy for Senior Citizen")
    else:
        print("No Subsidy")

