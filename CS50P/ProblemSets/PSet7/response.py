import validators

validator = validators.email(input("What's your email address? "))

if validator == True:
    print("Valid")
else:
    print("Invalid")