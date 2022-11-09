
fast = {"quick", "fast", "speedy", "rapid"}
family = ("family", "kids")
economical = ("economical", "cheap", "efficient")

fastcar = "Ferrari"
familycar = "Fiat"
economicalcar = "Seat"
carpick = "yes"
while carpick == "yes":
    userin = input(f" What type of car are you looking for? ").lower()
    choices = [fast, family, economical]
    print(f" you chose {userin}. ")
    if userin in list(fast):
           print(f" We think you would like a  {fastcar} ")
    elif userin in list(family):
            print(f" We think you would like a  {familycar} ")
    elif userin in list(economical):
            print(f" We think you would like a  {economicalcar} ")
    elif userin == 'x':
                print("Bye")
                break
