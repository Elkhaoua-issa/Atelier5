class Vecteur2D:
    #Constructeur avec les coordonnees par defaults
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    
#Vecteurs sans paramtre

V = Vecteur2D()
print("(",V.x,",",V.y,")")



#Vecteurs avec deux paramtre
V1 = Vecteur2D(3,6)

print("(",V1.x,",",V1.y,")")