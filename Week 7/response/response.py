from validator_collection import is_email

email = input("What's your email address? ").strip()

if is_email(email):
    print("Valid")
else:
    print("Invalid")

