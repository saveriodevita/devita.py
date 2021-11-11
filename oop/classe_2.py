Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math 
class calcComb():

    def __init__(self, stringa):

        self.__N = len(stringa)
        self.__stringa = stringa
        self.__listStringa = list(stringa)

    def get_stringa(self):
        return self.__stringa

    def get_listStringa(self):
        return self.__listStringa

    def setStringa(self,str):
        self.__N=len(stringa)
        self.__stringa=str
        self.__liststringa=list(stringa)
        
        return self.__listStringa

    def charRipetuti(self):
        '''
        questo metodo deve creare un dictionary all'interno del quale la chiave deve essere
        il singolo carattere, il valore deve essere il numero di ripetizioni di quel carattere
        
        esempi di dictionary sono presenti nel file elementi_base/dictionary.py
        '''
        word = list(parola) 
        caratteriRipetuti={}
        nCaratteri = 0
        count = 0

        for i in word:
            if (i in caratteriRipetuti): 
                caratteriripetuti[str(i)] += 1
        else:
            caratteriRipetuti[str(i)] = 1 
        for i in caratteriRipetuti:
            if caratteriRipetuti[i]>1:
                count+=1
                nCaratteri += caratteriRipetuti[i] 
        

    def confUtil(self):
        '''
        verificare se la STRINGA attributo di istanza è presente
        nel file word.italian.txt 
        '''
        p=open("word.italian.txt", "r")
        stringaParole == False
        for riga in p:
            if self.__stringa in riga:
                stringaParole == True
            p.close()
        
        return stringaParole

    

    def fattoriale(n):

        
        return math.factorial(n)
    
   



        
        
    def coeffBinom(n, k):
        if y == 1 or y == x:
        
           return(1)
        if y > x:
            return(0)
        else:
            a = math.factorial(x)
            b = math.factorial(y)
            d = a // (b*(x-y))
        return(d)  
        
        
        
        

    # PERMUTAZIONI

    def nPermutSenzaRip(self):
        
        n= len(self.__stringa)
        PermutSenzaRip=math.factorial(n)
        
        return PermutSenzaRip

    def nPermutConRip(self):
        '''
        restituire il numero di permutazioni CON ripetizione
        '''
        return 0

    def permutSenzaRip(self):
        '''
        generare e restituire la lista di permutazioni SENZA ripetizione
        '''
        return 0

    def permutConRip(self):
        '''
        generare e restituire la lista di permutazioni CON ripetizione
        '''
        return 0

    # DISPOSIZIONI

    def nDispSemplSenzaRip(self):
        
        n = len(self.__stringa)
        if n >= k:
            DispSemplSenzaRip = math.factorial(n) / (math.factorial(n-k))
        
        return DispSemplSenzaRip

    def nDispSemplConRip(self):
        
        n=len(self.__stringa)
        DispSemplConRip=n**k
        
        return DispSemplConRip

    def dispSemplSenzaRip(self):
        '''
        generare e restituire la lista delle disposizioni semplici SENZA ripetizione
        '''
        return 0


    def dispSemplConRip(self):
        '''
        generare e restituire la lista delle disposizioni semplici CON ripetizione
        '''
        return 0

    # COMBINAZIONI

    def nCombSemplSenzaRip(self):
        
        n = len(self.__stringa)
        CombSemplSenzaRip = math.factorial(n) / (math.factorial(k) * (math.factorial(n-k))
        
        return CombSemplSenzaRip

    def nCombSemplConRip(self):
        
        n = len(self.__stringa)
        CombSemplConRip = math.factorial(n+k-1) / (math.factorial(k) * math.factorial(n-1))
        return CombSemplConRip

    def combSenzaRip(self):
        '''
        generare e restituire la lista delle combinazioni SENZA ripetizione
        '''
        return 0


    def combConRip(self):
        '''
        generare e restituire la lista delle combinazioni CON ripetizione
        '''
        return 0



parola= calcComb(str(input("inserisci una stringa")))
parola.combUtil()