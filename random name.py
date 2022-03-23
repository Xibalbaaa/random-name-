### Vous pouvez egalement faire un programme qui tire au hasard une lettre du dictionnaire 
###et qui affiche le premier prenom de la liste des apprenants qui contient cette lettre.
import string
def listAlphabet():
  return list(string.ascii_lowercase)

alphab = (listAlphabet())
#####################################
import random
trainee = ["coraline" , "samira", "natalya", "nelly", "parisa", "hahaha", "gennnara", "abir", "khaoula" ]
c = alphab[random.randint(0,25)]

for elem in trainee:
    if c == elem[0]:
        print (elem)
        break
    else: 
        if c == elem[1] or c == elem[2]: # juste pour les 3 premières lettres 
            print (elem)
            break
c
################### well played