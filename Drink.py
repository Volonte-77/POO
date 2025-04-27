#creation de la class Drink
class Drink:
    """Une boisson"""
    def __hash__(self,price):
        self.price=price
    def drink(self):
        """Boire la boisson"""
        print("je ne sais pas ce que c'est, mais je le bois")

#creation de la class Coffee
class Coffee(Drink):
    """Un café"""
    prices={"simple":1,"serre":1,"allonge":1.5}
    def __init__(self,type):
        """Initialise le type du cafe"""
        self.type=type
        super().__init__(price=self.prices.get(type,1))
    def drink(self):
        """Boire le café"""
        print(f"un bon cafe de {self.type} qui coute {self.price} $ pour me reveiller ! ")

coffee=Coffee("serre")
boire=coffee.drink()
