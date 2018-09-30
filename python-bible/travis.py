# a data structure basic
known_users = ["Alice", "Fred", "Bob", "Mathieu", "Julie", "Caroline"]

print("My name is Travis ...")
name = input(" What is your name? ").strip().title();
if name in known_users:
    print("Happy to see you again")
else:
    print("Welcome new user")
    addMe = input("Would you like to be added to our users?").strip().lower()
    if addMe == 'y':
        known_users.append(name)
        print(known_users)

print("Work on even numbers")

even_numbers = [x for x in range(1,101) if x % 2 == 0]
print(even_numbers)

print("play with words")
words = ["the","fox","jump","over","the","lazy","dog"]
answers = [(w.upper(),w.lower(),len(w)) for w in words]
print(answers)
