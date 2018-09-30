# play with tuples, dictionaries

films = {"Finding Dory":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5],
  }

# get the movie for adult
for key in films.keys():
    for age in films[key]:
        if age > 17:
            print(key)
            
while True:
    choice = input("what is the movie you want to see? ").strip().title()
    if not choice in films:
         print(" we do not have that film yet...")
    else:
        age = int(input("What is your age?").strip())
        if age >= films[choice][0]:
            # enough seats?
            if films[choice][1] > 0:
                print("Enjoy this film")
                films[choice][1] = films[choice][1] - 1
            else:
                print("The session is fully booked")
        else:
            print("You are too young to watch this film..")
