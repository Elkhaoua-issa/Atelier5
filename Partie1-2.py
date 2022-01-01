#Class
class Vecteur2D:
    #Constructeur avec les coordonnees par defaults
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    
    def affichage(self):
            print("(",self.x,",",self.y,")")

    def Somme(self,v):
        s = Vecteur2D(self.x + v.x, self.y + v.y)
        return s

#utilisation de la methode affichage
V2 = Vecteur2D(2,8)
V3 = Vecteur2D(5,1)
print("Les deux vecteurs:")
V2.affichage()
V3.affichage()


#utilisation de la methode Somme
print("Leur somme:")
V3.Somme(V2).affichage()
