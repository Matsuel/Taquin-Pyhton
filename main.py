import random #On importe le module random pour  effectuer des mouvements aléatoirement.
import time #On import time pour créer un timer.

def ListToStr(tab):
  """
  Entrée: liste
  Sortie: Chaine de caractère
  Renvoie sous forme de chaine de caractère une liste
  """
  a=""
  for el in tab: #On parcourt la liste 
    a+= el            #On ajoute l'élément dans la chaine de caractères 
  return a          #On renvoie la chaine de caractère.

def PuzzleEgaux(P1,P2):
    """
    Entrée: 2 Puzzles
    Sortie: booléen 
    Renvoie True ou False si les puzzles sont égaux
    """
    tuile_p=P1.GetTuiles() #On copie les tuiles de P1
    tuile_p1=P2.GetTuiles() #On copie les tuiles de P2
    for i in range(len(P1.GetTuiles())): #On parcourt la longueur de P1
      for j in range(len(P1.GetTuiles()[0])):  #On parcourt la largeur de P1
        if tuile_p[i][j].GetValTuile()!=tuile_p1[i][j].GetValTuile(): #On compare les éléments à la même position dans P1 et P2
          return False #Si ils sont différents on renvoie False
    return True  #Si ils ne sont pas différents on renvoie True

  
class Tuile:
  def __init__(self,val):
    """
    Entrée: valeur
    Créer la tuile avec la valeur passée en paramètre
    """
    self.__valeur=val 

  def GetValTuile(self):
    """
    Renvoie la valeur de la tuile
    """
    return self.__valeur #On renvoie l'attribut valeur de la tuile.

  def EstTrou(self):
    """
    Sortie: Booléen pour savoir si la tuile est le trou donc avec une valeur de 9
    """
    return self.__valeur==9 #La valeur du trou est 9 donc on renvoie True/False si la valeur de la tuile est 9 

  def __repr__(self):
    """
    Sortie: représentation de la tuile soit avec sa valeur soit un espace si c'est le trou.
    """
    if self.EstTrou(): #On vérifie si la tuile est le trou
      return " " #On affiche le trou avec un espace vide
    else:
      return str(self.__valeur) #On affiche les tuiles avec les valeurs correspondantes

class Puzzle:
  def __init__(self,tab):
    """
    Entrée: Liste de 3 listes de tuiles.
    """        
    self.__Puzzle=[[Tuile(tab[j][i]) for i in range(len(tab))]for j in range(len(tab[0]))] #On créer la grille avec la liste de tuiles passée en paramètre.
    self.__ListeDepl=[] #On initialise la liste des déplacements effectués.
    self.__solution=[]  #On initialise la liste qui va contenir les déplacemnts nécessaires pour résoudre le puzzle.
    
  def GetTuiles(self):
    """
    Sortie: Renvoie la liste des 9 tuiles.
    """
    return self.__Puzzle #On renvoie l'attribut Puzzle.

  def GetTrou(self): 
    """
    Sortie: Coordonnées du trou.
    """
    for i in range(len(self.__Puzzle)): #On parcourt la longueur du puzzle.
      for j in range(len(self.__Puzzle[0])):  #On parcourt la hauteur du puzzle.
        if self.__Puzzle[i][j].EstTrou(): #Si l'élément est le trou donc, avec un valeur de 9
          return (i,j)                    #On renvoie les indices i et j, qui sont les coordonnées du trou.

  def __repr__(self):
    """
    Sortie: Renvoie le puzzle sous forme de grille.
    """
    rep="" #Représentation de puzzle
    for i in range(len(self.__Puzzle)):
      rep+="+---+---+---+"+"\n" #Permet de séparer chaque ligne du puzzle
      for j in range(len(self.__Puzzle[0])):
        rep+="| "+str(self.__Puzzle[i][j])+" " #Permet de séparer chaque colone du puzzle
      rep+="|"+"\n" #Permet de rajouter une colone à droite du puzzle
    rep+="+---+---+---+"+'\n' #Permet de rajouter une ligne en bas du puzzle
    return rep  #Renvoie la représentation du puzzle

  def SetTuiles(self,tab):
    """
    Entrée: Liste de 3 listes de tuiles.
    """ 
    self.__Puzzle=[[Tuile(tab[j][i]) for i in range(len(tab))]for j in range(len(tab[0]))] #On définit l'attribut Puzzle avec la liste de tuiles passée en paramètre.

  def NbCasesEnPlace(self):
    """
    Sortie: Entier représentant le nombre de tuiles bien positionnées.
    """
    ValCaseTheorique=0
    cpt=0 #Nombre de cases en place
    for i in range(len(self.__Puzzle)): #Parcourt la longueur puzzle
      for j in range(len(self.__Puzzle[i])):#Parcourt la largeur du puzzle
        ValCaseTheorique+=1
        tuile= self.GetTuiles()[i][j]
        if tuile.GetValTuile()== ValCaseTheorique : #Si la tuile est égal à sa valeur théorique
          cpt= cpt+1 #Augmente le nombre de case en place de 1
    return cpt #Renvoie le nombre de case en place
    #On sait que la case 1 ([0][1]) doit valoir 1 on vérifie pour chaque tuile.

  def EstFini(self):
    """
    Renvoie le booléen pour savoir si le puzzle est résolu ou non.
    """
    return self.NbCasesEnPlace()== 9 #Renvoie True/False si le puzzle à toutes ses cases en place

  def DeplacementsPossibles(self):
    """
    Sortie: Renvoie la liste des mouvements que le joueur peut effectuer.
    """
    pos=self.GetTrou() #Coordonnées du trou
    deplacement=[] #Liste des déplacements possibles
    if pos[0]==0: #Si le trou est sur la 1ère ligne
      deplacement.append("b") #Ajoute aux déplacement possible le déplacement vers le bas
      if pos[1]==0: #Si le trou est sur la 1ère colonne
        deplacement.append("d") #Ajoute aux déplacement possible le déplacement vers la droite
      elif pos[1]==2: #Si le trou est sur la 3ème colonne
        deplacement.append("g") #Ajoute aux déplacement possible le déplacement vers la gauche
      else: #Si le trou est sur la 2ème colonne
        deplacement.append("d") #Ajoute aux déplacement possible le déplacement vers la droite
        deplacement.append("g") #Ajoute aux déplacement possible le déplacement vers la gauche
    elif pos[0]==2: #Si le trou est sur la 3ème ligne
      deplacement.append("h") #Ajoute aux déplacement possible le déplacement vers le haut
      if pos[1]==0: #Si le trou est sur la 1ère colonne
        deplacement.append("d") #Ajoute aux déplacement possible le déplacement vers la droite
      elif pos[1]==2: #Si le trou est sur la 3ème colonne
        deplacement.append("g") #Ajoute aux déplacement possible le déplacement vers la gauche
      else: #Si le trou est sur la 2ème colonne
        deplacement.append("d") #Ajoute aux déplacement possible le déplacement vers la droite
        deplacement.append("g") #Ajoute aux déplacement possible le déplacement vers la gauche
    else: #Si le trou est sur la 2ème ligne
      deplacement.append("h") #Ajoute aux déplacement possible le déplacement vers le haut
      deplacement.append("b") #Ajoute aux déplacement possible le déplacement vers le bas
      if pos[1]==0: #Si le trou est sur la 1ère colonne
        deplacement.append("d") #Ajoute aux déplacement possible le déplacement vers la droite
      elif pos[1]==2: #Si le trou est sur la 3ème colonne
        deplacement.append("g") #Ajoute aux déplacement possible le déplacement vers la gauche
      else: #Si le trou est sur la 2ème colonne
        deplacement.append("d") #Ajoute aux déplacement possible le déplacement vers la droite
        deplacement.append("g") #Ajoute aux déplacement possible le déplacement vers la gauche
    return deplacement #Renvoie la liste des déplacement possible

  def Gauche(self):
    """
    Réalise si il est possible le mouvement du trou vers la gauche
    """
    Puzzle=self.GetTuiles() #On récupère la liste de tuiles du Puzzle.
    Trou= self.GetTrou() #On récupère les coordonnées du trou.
    CaseGauche= self.GetTrou()[0],self.GetTrou()[1]-1 #On récupère les coordonnées de la case de gauche de trou.
    Puzzle[Trou[0]][Trou[1]],Puzzle[CaseGauche[0]][CaseGauche[1]]=Puzzle[CaseGauche[0]][CaseGauche[1]],Puzzle[Trou[0]][Trou[1]] #On inverse les valeur des cases en inversant les places du trou et de la case gauche , donc on déplace le trou vers la gauche.
  
  def Droite(self):
    """
    Réalise si il est possible le mouvement du trou vers la droite
    """
    Puzzle=self.GetTuiles() #On récupère la liste de tuiles du Puzzle.
    Trou= self.GetTrou()  #On récupère les coordonnées du trou.
    CaseDroite= self.GetTrou()[0],self.GetTrou()[1]+1 #On récupère les coordonnées de la case de droite de trou.
    Puzzle[Trou[0]][Trou[1]],Puzzle[CaseDroite[0]][CaseDroite[1]]=Puzzle[CaseDroite[0]][CaseDroite[1]],Puzzle[Trou[0]][Trou[1]]  #On inverse les valeur des cases en inversant les places du trou et de la case droite, donc on déplace le trou vers la droite.
    
  def Haut(self):
    """
    Réalise si il est possible le mouvement du trou vers le haut
    """
    Puzzle=self.GetTuiles() #On récupère la liste de tuiles du Puzzle.
    Trou= self.GetTrou()  #On récupère les coordonnées du trou.
    CaseHaut= self.GetTrou()[0]-1,self.GetTrou()[1] #On récupère les coordonnées de la case au-dessus du trou.
    Puzzle[Trou[0]][Trou[1]],Puzzle[CaseHaut[0]][CaseHaut[1]]=Puzzle[CaseHaut[0]][CaseHaut[1]],Puzzle[Trou[0]][Trou[1]]
    #On inverse les valeur des cases en inversant les places du trou et de la case du haut, donc on déplace le trou vers le haut
    
  def Bas(self):
    """
    Réalise si il est possible le mouvement du trou vers le bas
    """
    Puzzle=self.GetTuiles() #On récupère la liste de tuiles du Puzzle.
    Trou= self.GetTrou()  #On récupère les coordonnées du trou.
    CaseBas= self.GetTrou()[0]+1,self.GetTrou()[1] #On récupère les coordonnées de la case en-dessous du trou.
    Puzzle[Trou[0]][Trou[1]],Puzzle[CaseBas[0]][CaseBas[1]]=Puzzle[CaseBas[0]][CaseBas[1]],Puzzle[Trou[0]][Trou[1]]
    #On inverse les valeur des cases en inversant les places du trou et de la case du bas, donc on déplace le trou vers le bas.

  def Deplacement(self,depl):
    """
    Entrée: type str:("g","h","d","b")
    """
    DeplPossible = self.DeplacementsPossibles() #Récupère la liste des déplacements possibles
    if depl=="r" and self.GetNbCoupsJoues()>1: #Si le déplacement est 'r', soit annulé.
      self.Annule() #Annule le dernier coup
    for el in DeplPossible: #Parcourt les déplacements possibles 
      if depl==el: #Si le déplcement effectué est le même que le déplacment possible
        if el=="g": #Si le déplacement est 'g', soit gauche
          self.Gauche() #Déplace le trou à gauche
        elif el=="d": #Si le déplacement est 'd', soit droite
          self.Droite() #Déplace le trou à droite
        elif el=="h": #Si le déplacement est 'h', soit haut
          self.Haut() #Déplace le trou en bas
        elif el=="b": #Si le déplacement est 'b', soit bas
          self.Bas() #Déplace le trou en haut
          #On effectue le déplacement du trou lorsqu'il est possile.

  def Jouer(self):
    """
    Permet au joueur de tenter de résoudre le puzzle.
    """
    cpt=0
    h_debut= time.time() #On récupère l'heure de départ 
    liste=self.PuzzleAleatoireV1() #On récupère la liste des déplacements effectués aléatoirement.
    self.DonnerSolutionBase(liste)#On définit la solution de base avec la liste des déplacments aléatoires.
    self.ResolutionPuzzle()
    while not self.EstFini(): #Tant que le puzzle n'est pas résolu.
      cpt+=1 #On initialise le nombre de coup en rajoutant 1.
      print(self) #On affiche le Puzzle au début.
      print("\n") #Saut de ligne pour ensuite demander quel mouvement le joueur souhaite effectuer.
      MouvJoueur=str(input("Coup Numero {} ? ".format(cpt))) #On demande au joueur quel déplacement il veut faire.
      if MouvJoueur=="r" and self.GetNbCoupsJoues()!=0 and cpt>1:
        cpt-=2
        self.Deplacement(MouvJoueur) #On effectue le mouvement du joueur en annulant son dernier coup.
      elif MouvJoueur=="a": #Si le joueuer veut abandonner.
        return self.Abandon()  #On renvoie la solution de départ et on arrête la partie.
      #Sinon :
      self.Deplacement(MouvJoueur) #On effectue le déplacement du trou.
      self.SauvegardeDeplacement(MouvJoueur) #On sauvegarde ce déplacement dans l'attribut Deplacements.
      print("\n") #Saut de lignes.
    h_fin= time.time() #On récupère l'heure à laquelle le joueur a terminé sa partie.
    temps_resolution= h_fin- h_debut #On soustrait l'heure final et l'haure de début pour obtenir le temps de résolution.
    temps_resolution= round(temps_resolution, 2) #On arrondit à 2 décimales les secondes.
    return "Problème Résolu en {} coups !\nVoici la liste des coups effectués  {} et le temps de résolution {} secondes".format(cpt,ListToStr(self.__ListeDepl), temps_resolution) #Si le puzzle est finit on renvoie le nombre de coups du joueur et sa liste des déplacements qu'il a effectué, ainsi que le temps de résolution.
  
  def DonnerSolutionBase(self,liste):
    """
    Entrée: liste des déplacements du trou
    Donne la solution du puzzle.
    """
    for i in range(len(liste)-1,-1,-1): #Parcourt la liste des déplacement effectués en commencant par le dernier
      if liste[i]=="g": #Si le déplacement est 'g', soit gauche
        self.__solution.append("d") #Déplace le trou à droite
      if liste[i]=="d": #Si le déplacement est 'd', soit droite
        self.__solution.append("g") #Déplace le trou à gauche
      if liste[i]=="h": #Si le déplacement est 'h', soit haut
        self.__solution.append("b") #Déplace le trou en bas
      if liste[i]=="b": #Si le déplacement est 'b', soit bas
        self.__solution.append("h") #Déplace le trou en haut
        #On récupère les 50déplacements effectués au début aléatoirement puis on parcourt la liste à l'envers et pour chaque déplacement on l'inverse.

  def PuzzleAleatoireV1(self):
    """
    Mélange le puzzle en effectuant 50 mouvements du trou.
    """
    deplacement=[] #Créer une liste vide qui va contenir les déplacements effectués
    for i in range(50): #Répète 50 fois
      dir=self.DeplacementsPossibles() #Récupère la liste des déplacements possibles
      rand=random.randint(0,len(dir)-1) #Choisis un nombre aléatoire entre 0 et le nombre de déplacement possible
      deplacement.append(dir[rand]) #Ajoute a la liste des déplacement l'élément d'indice rand
      self.Deplacement(deplacement[i]) #Effectue le déplacement ajouté dans la liste des déplacements 
    return deplacement #Renvoie la liste des déplacements
    #On récupère la liste des déplacements possibles à partir de la position, puis on effectue un mouvement aléatoire de la liste des déplacements possibles.

  def SauvegardeDeplacement(self,depl):
    """
    Enregistre les déplacements effectués.
    """
    self.__ListeDepl.append(depl) #Ajoute à l'attribut, correspondant à la liste des déplacements effectués, le déplacement effectué
    return self.__ListeDepl #Renvoie la liste des déplacements effectués
  
  def Annule(self):
    """
    Annule le dernier coup joué.
    """
    if self.__ListeDepl != []:
      dernier_coup=self.__ListeDepl.pop()
      if dernier_coup=="g": #Si le dernier coup est 'g', soit gauche
        self.Deplacement("d") #Déplace le trou à droite
      if dernier_coup=="d": #Si le dernier coup est 'd', soit gauche
        self.Deplacement("g") #Déplace le trou à gauche
      if dernier_coup=="h": #Si le dernier coup est 'h', soit gauche
        self.Deplacement("b") #Déplace le trou en bas
      if dernier_coup=="b": #Si le dernier coup est 'b', soit gauche
        self.Deplacement("h") #Déplace le trou en haut
        #On effectue le mouvement inverse pour annuler le coup.

  def Abandon(self):
    """
    Arrête la partie en cours et renvoie la solution de départ
    """
    return "Dommage !\nLa solution à partir de la situation donnée au début :\n{}".format(ListToStr(self.__solution)) #Renvoie un message de fin de partie avec la solution du puzzle, lorsque le joueur abandonne la partie.
    
  def Voisins(self):
    """
    Simule les déplacements possibles en les renvoyant sous forme de puzzle.
    """
    ListeDepl= self.DeplacementsPossibles() #Récupère la liste des déplacements possibles
    ListeVoisins=[] #Créé une liste vide qui contiendra la liste des puzzles voisins
    for i in range(len(ListeDepl)): #Parcourt par indice les déplacements possibles
      self.Deplacement(ListeDepl[i]) #Effectue le déplacement d'indice i
      P=Puzzle(self.GetTuiles()) #Créé le puzzle voisins du puzzle de départ
      ListeVoisins.append(P) #Ajoute le puzzle à la liste des puzzles voisins
      self.__ListeDepl.append(ListeDepl[i]) #Ajoute aux déplacement effectués le déplacement d'indice i
      self.Annule() #Annule le dernier déplacement
    return ListeVoisins #Renvoie la liste des puzzles voisins

       

  def ResolutionPuzzle(self):
    """
    Renvoie la solution du puzzle plus simplifiée, si deux déplacements à la suite sont contraires on peut les annuler.
    """
    solution_base=self.__solution
    solution=[]
    for i in range(1,len(self.__solution)):
      if solution_base[i]=="g" and solution_base[i-1]!="d":
        solution.append(solution_base[i])
      elif solution_base[i]=="d" and solution_base[i-1]!="g":
        solution.append(solution_base[i])  
      elif solution_base[i]=="h" and solution_base[i-1]!="b":
        solution.append(solution_base[i])
      elif solution_base[i]=="b" and solution_base[i-1]!="h":
        solution.append(solution_base[i])    
    self.__solution=solution

    #Si le déplacement effectué est annulé au coup d'après, ça ne sert à rien de garder les 2 car au final on aura pas avancer.
    
      
  
P=Puzzle([[1,2,3],[4,5,6],[7,8,9]])
print(P.Jouer())

