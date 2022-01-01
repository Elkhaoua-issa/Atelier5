class etudiant:
    def __init__(self,nom,prenom,age,cne,moyenne):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne



list = []
l1 = []
l2 = []
# ajouter instances de classe etudiant dans list
list.append( etudiant('issa','elkhaoua',20,'AA212421',18.31) )
list.append( etudiant('simo','merdid',22,'AJ134249',16.43) )
list.append( etudiant('fouad','berada',17,'DR978684',14.57) )


for obj in list:
    #ajouter l'age des classe  dans l1
    l1.append(obj.age)
    #ajouter le moyenne des classe  dans l2
    l2.append(obj.moyenne)
i=1
#trier l1 qui contient l'age 
l1.sort()
print("Les ages tries:")
#Affiche les information par rapport a l'age
for obj in l1:
    for obj1 in list:
        if obj1.age == obj:
            print(i,": ",obj1.nom,"     ",obj1.prenom,"     ",obj1.age,"     ",obj1.cne,"     ",obj1.moyenne)
            i+=1

print("------------------------------------------------------")
i=1
#trier l2 qui contient les moyenne
l2.sort()
print("Les moyenne tries:")
#Affiche les information par rapport a la moyenne
for obj in l2:
    for obj1 in list:
        if obj1.moyenne == obj:
            print(i,": ",obj1.nom,"     ",obj1.prenom,"     ",obj1.age,"     ",obj1.cne,"     ",obj1.moyenne)
            i+=1