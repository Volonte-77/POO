# la classe cake

class Cake:
    def __init__(self,flavor):
        self.flavor=flavor
    def cut_in_part(self):
        print("le gateau est decoupe en 4 partie")

cake1=Cake("chocolate")
print(cake1.flavor)
cake1.cut_in_part()