#une petite calculatrice
nombre1=float(input("Entrez le premier nombre: "))
nombre2=float(input("Entrez le deuxieme nombre: "))
print('='*20)
print("choisissez un signe (ex: +,-,x,:)) \n + ADDITION \n - SOUSTRACTION \n x MUTIPLICATION \n : DIVISION")
signe=input("")
match signe:
    case "+":
        print(f"{nombre1} + {nombre2} = {nombre2+nombre1}")
    case "-":
        print(f"{nombre1} - {nombre2} = {nombre1-nombre2}")
    case "x":
        print(f"{nombre1} x {nombre2} = {nombre1*nombre2}")
    case ":":
        print(f"{nombre1} : {nombre2} = {nombre1/nombre2}")
    case _:
        print("Reponse non connue")

    

