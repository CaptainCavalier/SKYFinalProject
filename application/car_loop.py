
sports = ("quick", "fast", "speedy", "rapid", "sports")
family = ("family", "kids")
economical = ("economical", "cheap", "efficient")
estate = ("pets", "luggage")
hybrid = ("green", "environment", "electric")
suv = ("suv", "people carrier", "sports utility vehicle", "chelsea tractor")
convertible = ("convertible", "soft top")


sportscar = "Ferrari"
familycar = "Fiat"
economicalcar = "Seat"
estatecar = "BMW"
hybridcar = "Tesla"
suvcar = "Hummer"
convertiblecar = "Corvette"
carpick = "yes"
while carpick == "yes":
    userin = input(f" What type of car are you looking for? ").lower()
    choices = [sports, family, economical]
    print(f" you chose {userin}. ")
    if userin in list(sports):
        print(f" We think you would like a : {sportscar} or a {convertiblecar} ")
    elif userin in list(family):
        print(f" We think you would like a : {familycar}, {estatecar} or {suvcar} ")
    elif userin in list(economical):
        print(f" We think you would like a : {economicalcar} or {hybridcar} ")
    elif userin in list(estate):
        print(f" We think you would like a : {estatecar}")
    elif userin in list(hybrid):
        print(f" We think you would like a : {hybridcar}")
    elif userin in list(suv):
        print(f" We think you would like a : {suvcar}")
    elif userin in list(convertible):
        print(f" We think you would like a : {convertiblecar}")
    elif userin == 'x':
                print("Bye")
                break
