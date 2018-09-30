# remove any space added before or after the name entered
# and uppercase the first letter
name = input("what is your name? ").strip().capitalize()

# As input is always returning a string, convert it
age = int(input("What is your age? "))

print("Hello " + name + " " + str(age))

print("Hello {} you are {} years old".format(name,age))

# count the number of char in a string
# strings are immutables but we can chain function.
print(name.lower().count("e"));


# separate name from domain in email
email = input("What is your email address? ").strip()
arobaceIdx=email.index("@")
name = email[:arobaceIdx]
domain = email[arobaceIdx+1:]
print("Your name is {} and the email domain is {}".format(name,domain))
