from validator_collection import checkers

user_input = input("What is your email adress? ")

if checkers.is_email(user_input):
    print("Valid")
else:
    print("Invalid")
