class Rectangle:
        #Constructeur de classe Rectangle
        def __init__(self, longueur=30, largeur=15):
                self.longueur = longueur
                self.largeur = largeur
                self.nom = "rectangle"
        #methode qui calcule la surface
        def surface(self):
                return self.longueur*self.largeur
        #methode affiche la surface et au
        def affichage(self):
                print("Le Surface de ",self.nom," de largeur ",self.largeur," et de longueur ",self.longueur," est: ",self.surface())

class Carre(Rectangle):
        #Constructeur de classe Carre
        def __init__(self, cote):
                Rectangle.__init__(self, cote, cote)
                self.nom = "carre"

#Utilsation
rect = Rectangle(10, 5)
rect.affichage()
car = Carre(6)
car.affichage()