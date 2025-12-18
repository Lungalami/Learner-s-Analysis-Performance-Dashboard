import cowsay

def main():
    name = input("What's your name? ")
    year = input("What year were you born? ")
    x = get_int("What's x? ")

    message = (" House you are in is " + house(name) + ", Colour you wear is " + year_born(year),  " Amount you have paid " + str(x))

    cowsay.stegosaurus(message)

def house(name):
    if name in("Hlengiwe", "Nokwand", "Sibongile", "Thando"):
        return "Shepard"
    elif name in("Musawenkosi", "Nokuthula", "Masabata", "Tshiamo", "Nthabiseng"):
        return "Armstrong"
    elif name in("Thembalethu", "Kgomotso", "Ntabatse", "Dikeledi", "Martha"):
        return "Mitchell"
    elif name in("Nompilo", "Sinethemba", "Asande", "Matsatsi", "Sbongile"):
        return "Aldrin"
    else:
        return "InValid"

def year_born(year):
    if year in("2017", "2016"):
        return "Red"
    elif year in("2015", "2014"):
        return "Yellow"
    elif year in("2013", "2012"):
        return "Green"
    elif year in("2011", "2018"):
        return "Blue"
    else:
        return "InValid"

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("x is an integer")


if __name__ == "__main__":
    main()
