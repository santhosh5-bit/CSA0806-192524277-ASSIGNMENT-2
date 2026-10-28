# Task 2: OTP Verification Using For Loop

correct_otp = "1234"

for attempt in range(3):
    otp = input("Enter OTP: ")

    if otp == "":
        print("Blank entry! Try again.")
        continue

    if otp == correct_otp:
        print("OTP Verified Successfully!")
        break
    else:
        print("Wrong OTP!")

else:
    print("Account locked for 30 minutes.")

