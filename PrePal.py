import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi

# Fonction personnalisée pour la racine carrée
def racine_carree(x):
    if x < 0:
        # Pour le contexte du BAC SI, on suppose x >= 0 pour la fonction Premier.
        return 0.0 
    if x == 0:
        return 0.0
    
    guess = x / 2.0
    epsilon = 0.00001 # Précision pour la convergence
    
    # Méthode de Newton pour le calcul itératif de la racine carrée
    while abs(guess * guess - x) > epsilon:
        guess = (guess + x / guess) / 2.0
    return guess

# Fonction personnalisée pour la longueur d'une chaîne
def long(ch):
    compteur = 0
    for _ in ch:
        compteur += 1
    return compteur

# a. Fonction Premier(A)
def Premier(A):
    """
    Vérifie si un nombre entier A est premier.
    Retourne True si A est premier, False sinon.
    """
    if A <= 1:
        return False
    # On teste la divisibilité de 2 jusqu'à la racine carrée de A
    i = 2
    while i <= racine_carree(A): # Utilisation de la fonction personnalisée racine_carree
        if A % i == 0:
            return False
        i += 1
    return True

# b. Fonction Palindrome(CH)
def Palindrome(CH):
    """
    Vérifie si une chaîne de caractères CH est un palindrome.
    Implémentation de l'algorithme fourni.
    Retourne True si CH est un palindrome, False sinon.
    """
    # Adaptation de l'algorithme 1-indexé au 0-indexé de Python
    long_ch = long(CH) # Utilisation de la fonction personnalisée long()
    i = 0
    j = long_ch - 1 # Utiliser la variable pre-calculée
    pal = True
    while i < j and pal:
        if CH[i] != CH[j]:
            pal = False
        else:
            i = i + 1
            j = j - 1
    return pal

# c. Fonction Verif(N)
def Verif(N):
    """
    Vérifie si un nombre N est un "premier palindrome".
    Retourne True si N est à la fois premier et palindrome, False sinon.
    """
    # Un nombre est premier palindrome s'il est premier ET palindrome.
    # On convertit N en chaîne pour la fonction Palindrome.
    return Premier(N) and Palindrome(str(N))

# Classe de la fenêtre principale
class FenetrePrincipale(QMainWindow):
    def __init__(self):
        super(FenetrePrincipale, self).__init__()
        # Charger le fichier d'interface .ui
        loadUi('Interface.ui', self)
        
        # Connecter le bouton "Vérifier" à la fonction Play
        self.btn_verifier.clicked.connect(self.Play)

    # d. Module de connexion Play
    def Play(self):
        """
        Slot exécuté lors du clic sur le bouton "Vérifier".
        """
        # Récupérer le texte saisi
        saisie_n = self.input_N.text()
        
        # Contrôle de la validité de la saisie
        long_saisie = long(saisie_n) # Utilisation de la fonction personnalisée long()
        if not saisie_n.isdecimal() or long_saisie < 3:
            # Afficher un message d'erreur si la saisie est invalide
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Erreur de saisie !")
            msg.setInformativeText("Veuillez saisir un nombre entier d'au moins 3 chiffres.")
            msg.setWindowTitle("Erreur")
            msg.exec_()
            # Effacer le champ de saisie et le résultat
            self.input_N.clear()
            self.label_resultat.clear()
        else:
            # La saisie est valide, on la convertit en entier
            n = int(saisie_n)
            
            # Appeler la fonction Verif et construire le message de résultat
            if Verif(n):
                resultat = f"{n} est premier palindrome."
            else:
                resultat = f"{n} n'est pas premier palindrome."
            
            # Afficher le résultat dans le label
            self.label_resultat.setText(resultat)

# Programme principal pour lancer l'application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = FenetrePrincipale()
    fenetre.show()
    sys.exit(app.exec_())