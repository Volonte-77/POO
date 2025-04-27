# class animal avec autres class
class Animal:
    def crier(self):
        print("Un cri d'animal")
class Chat(Animal):
    def crier(self):
        print("miau !")

class Chien(Animal):
    def crier(self):
        print("woauf ! Woauf")

class Inconnu(Animal):
    def crier(self):
        return super().crier()

animal=Animal()
cri_animal=animal.crier()

