#Classe: Point
class Point:
        #Constructeur de classe Point
        def __init__(self, x=0.0, y=0.0):
                self.x = x
                self.y = y

#Classe: Segment
class Segment:
        #Constructeur de classe Segment
        def __init__(self, x1, y1, x2, y2):
                self.orig = Point(x1, y1)
                self.extrem = Point(x2, y2)
        #methode de l'affichage
        def affichage(self):
                print("Segment : [(",self.origine.x,", ",self.origine.y,"),(",self.extreme.x,", ",self.extreme.y,")]")

#Utilisation
s = Segment(1, 2, 3, 4)
s.affichage()
