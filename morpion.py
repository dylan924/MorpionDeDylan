#Debut du jeu
grille = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#Savoir si le jeu continue en le définissant sur True
game_on = True

#Definir le joueur actuel pour etre X
Joueur_actuel = "X"

#Definir la grille
def definir_grille():
    print(grille[0] + " | " + grille[1] + " | " + grille[2] + "      " + "1|2|3")
    print(grille[3] + " | " + grille[4] + " | " + grille[5] + "      " + "4|5|6")
    print(grille[6] + " | " + grille[7] + " | " + grille[8] + "      " + "7|8|9")

#Definir les joueurs
def joueurs():
    print("Choisir un joueur - X ou O")
    p1 = input("Joueur1: ")
    p2 = ""
    if p1 == "X":
        p2 = "O"
        print("Joueur2: " + p2)
    elif p1 == "O":
        p2 = "X"
        print("Joueur2: " + p2)
    elif p1 != "O" or p1 != "X":
        print("Erreur")
        jouer_au_morpion()

#Definir la position du joueur
def position_joueur():
    global Joueur_actuel
    print("Joueur actuel : " + Joueur_actuel)
    position = input("Choisis un chiffre entre 1 - 9: ")

    #Parcourez le programme jusqu'à ce qu'il y ait une victoire ou une égalité
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
          position = input("Choisir une position de  1 - 9: ")
        position = int(position) - 1

        if grille[position] == "-":
            valid = True
        else:
            print("Position deja prise")
    grille[position] = Joueur_actuel
    definir_grille()

#Fonction pour jouer à mon jeu
def jouer_au_morpion():
    print("Mon jeu du morpion")
    definir_grille()
    joueurs()
    
  #boucle pour retourner aux joueurs jusqu'à ce qu'il y ait une victoire
    while game_on:
        position_joueur()
        
        #Verifier le vainqueur
        def verifier_vainqueur():
            global game_on
            #Vérifiez les lignes s'il y a une victoire 
            if grille[0] == grille[1] == grille[2] != "-":
                game_on = False
                print("Felicitations " + grille[0]+" tu as gagné!")
            elif grille[3] == grille[4] == grille[5] != "-":
                game_on = False
                print("Felicitations " + grille[3]+" tu as gagné!")
            elif grille[6] == grille[7] == grille[8] != "-":
                game_on = False
                print("Felicitations " + grille[6]+" tu as gagné!")
             #Vérifiez les diagonales s'il y a une victoire
            elif grille[0] == grille[3] == grille[6] != "-":
                game_on = False
                print("Felicitations " + grille[0]+" tu as gagné!")
            elif grille[1] == grille[4] == grille[7] != "-":
                game_on = False
                print("Felicitations " + grille[1]+" tu as gagné!")
            elif grille[2] == grille[5] == grille[8] != "-":
                game_on = False
                print("Felicitations " + grille[2]+" tu as gagné!")
             #Vérifiez les diagonales s'il y a une victoire
            elif grille[0] == grille[4] == grille[8] != "-":
                game_on = False
                print("Felicitations " + grille[0]+" tu as gagné!")
            elif grille[2] == grille[4] == grille[6] != "-":
                game_on = False
                print("Felicitations "+ grille[6]+" tu as gagné!")
             #Si aucune des réponses ci-dessus alors c'est égalité
            elif "-" not in grille:
                game_on = False
                print("c'est une égalité")
                exit()

        #Fonction pour retourner aux joueurs
        def retourner_aux_joueurs():
            global Joueur_actuel
            if Joueur_actuel == "X":
                Joueur_actuel = "O"
            else:
                Joueur_actuel = "X"
        retourner_aux_joueurs()
        verifier_vainqueur()
#Jouer au morpion
jouer_au_morpion()