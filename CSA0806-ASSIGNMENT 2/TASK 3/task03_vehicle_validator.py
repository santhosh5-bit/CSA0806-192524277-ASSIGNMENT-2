# Task 3: Vehicle Registration Number Validator

def normalise(text):
    """Remove spaces and hyphens and convert to uppercase."""
    return text.replace(" ", "").replace("-", "").upper()


def is_valid(reg):
    """Check the vehicle registration number."""
    if len(reg) not in (9, 10):
        return False

    if not reg[:2].isalpha():
        return False

    if not reg[2:4].isdigit():
        return False

    if len(reg) == 9:
        if not reg[4:5].isalpha():
            return False
        if not reg[5:].isdigit():
            return False

    if len(reg) == 10:
        if not reg[4:6].isalpha():
            return False
        if not reg[6:].isdigit():
            return False

    return True


def format_number(reg):
    """Format a valid number for printing."""
    if not is_valid(reg):
        return "Invalid registration number"

    return reg[:2] + " " + reg[2:4] + " " + reg[4:-4] + " " + reg[-4:]


# Test six inputs
vehicles = [
    "tn 09 ab 1234",
    "KA-01-M-0007",
    "TN9AB1234",
    "TN 22 1234 AB",
    "MH 12 CD 5678",
    "KL-07-P-1234"
]

print("VEHICLE REGISTRATION VALIDATOR")
print("-" * 55)

for raw in vehicles:
    reg = normalise(raw)

    if is_valid(reg):
        print(f"{raw:18} -> {reg:10} VALID")
        print("Formatted:", format_number(reg))
    else:
        print(f"{raw:18} -> {reg:10} INVALID")

