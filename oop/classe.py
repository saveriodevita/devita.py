class Studente:
    #attributi della Classe
    studenti= 0
    ragazzi= 0
    ragazze= 0

    #metodo costruttore
    def __init__(self, nome, cognome, genere, eta, classe):

        #attributi di istanza
        
        self.nome = nome
        self.cognome = cognome
        self.genere = genere
        self.eta = eta
        self.classe = classe
        Studente.studenti += 1
        if self.genere == "ragazzo":
            Studente.ragazzi += 1
        else:
            Studente.ragazze +=1


        #metodo get
    def scheda(self):
        return str("Scheda:\nNome: " + self.nome + "\nCognome: " + self.cognome + "\nGenere: " +self.genere + "\nEta: " + str(self.eta) + "\nClasse: " + self.classe)

    def studenti_totali():
        return str("\nNumero totale di studenti: " + str(Studente.studenti) + "\nNumero ragazzi: " + str(Studente.ragazzi) + "\nNumero ragazze: " + str(Studente.ragazze))
            

            #metodo set
    def set_eta(self, eta):
        self.eta = eta
    
                           
                    
#inizio del main
#costruzione oggetti

Lorenzo = Studente("Lorenzo","De Vita","ragazzo",13,"primaD")
Mario = Studente("Mario","Russo","ragazzo",18,"quintaF")


#print("il tipo di variabile costruita è: ")
#print(Lorenzo)
#print(Mario)

#utilizzo metodo get

print("la singola scheda è: ")
print (Lorenzo.scheda())
print (Mario.scheda())

print(Studente.studenti_totali())



#utilizzo metodo set
Lorenzo.set_eta(13)
print(Lorenzo.scheda())

#altro metodo per visualizzare le informazioni, (_dict_)
#print()
#print(Lorenzo._dict_)
#print(Mario._dict_)
