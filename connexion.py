class Client:
    def __init__(self, name, numeroCompte):
        self.name = name
        self.numeroCompte = numeroCompte

class Connexion:
    def __init__(self):
        self.name = input('Votre login: ')
        self.password = input('Votre password: ')
        self.login()

    def login(self):
        if self.name == 'felix' and self.password == 'felix':
            return True
        else:
            return False

if __name__ == "__main__":
    print('# -- Bien venu a la banque L2IN -- #', end='\n')

    while True:
        print('1- Faire un versement')
        print('2- Faire un retrait')
        print('3- Faire un virement')
        print("4- Faire un virement a l'international")
        print('0- Quitter')

        reponse = int(input('Que voulez vous faire: '))
        
        if reponse == 0:
            sys.exit()

        Guichetier(reponse)
    

    
