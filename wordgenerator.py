import random



def getCount(choice):
    if choice == "country":
        number = random.randint(0,89)
        file = open('country.txt')
        content = file.readlines()
        return content[number]
    elif choice == "dogbreed":
        number = random.randint(0,38)
        file = open('dogbreed.txt')
        content = file.readlines()
        return content[number]
    elif choice == "sport":
        number = random.randint(0,39)
        file = open('sport.txt')
        content = file.readlines()
        return content[number]
    else:
        return "invalid"

