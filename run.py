from numpy import mean
Studenti={
    "Mario":{"Matematica":6,"Italiano":6,"Scienze":7,"Inglese":4},
    "Giovanni":{"Matematica":4,"Italiano":6,"Scienze":5,"Inglese":7},
    "Paola":{"Matematica":9,"Italiano":6,"Scienze":8,"Inglese":8}
    }
voti_mario=list(Studenti["Mario"].values())
voti_giovanni=list(Studenti["Giovanni"].values())
voti_paola=list(Studenti["Paola"].values())
print("La media di Mario è: " + str(mean(voti_mario)))
print("La media di Giovanni è: " + str(mean(voti_giovanni)))
print("La media di Paola è: " + str(mean(voti_paola)))                                       
