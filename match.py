#parlons un peu du match
fruit="pomme"
match fruit:
    case "pomme":
        print("j'aime les pommes")
    case "banane":
        print("je n'aime pas les bananes.")
    case "orange":
        print("les oranges sont bonnes pour la sante.")
    case _:
        print("je ne connais pas ce fruit.")
