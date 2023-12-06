# =============================================================================
# EXO 1
# =============================================================================

def armstrong(nombre):
    total = 0
    for chiffre in str(nombre):
        total += int(chiffre)**3
    return total == int(nombre)


def all_armstrong():
    limite = int(input("Veuillez entrer un entier : "))
    for i in range(limite):
        if armstrong(i):
            print(i)
            

all_armstrong()      
            
# =============================================================================
# EXO 2 version 1
# =============================================================================
         
def diviseurs(integer):
    """
    Parameters
    ----------
    integer : INT
        Entier dont on veut récupérer tous les diviseurs.

    Returns
    -------
    liste_diviseurs : LIST
        Diviseurs de integer.

    """
    liste_diviseurs = list()
    for tested in range(1, integer + 1):
        if integer % tested == 0:
            liste_diviseurs.append(tested)
    return liste_diviseurs


## Ou version 2 ##

def diviseurs2(integer):
    """
    Parameters
    ----------
    integer : INT
        Entier dont on veut récupérer tous les diviseurs.

    Returns
    -------
    diviseurs : LIST
        Diviseurs de integer.

    """
    assert type(integer) == int
    diviseurs = [tested for tested in range(1, integer+1) if not integer%tested]
    

    return diviseurs

#tester si le resultat est correct    
assert diviseurs2(127) == [1, 127]

integer = int(input("Veuillez entrer un entier : "))
print("methode 1 :" , diviseurs(integer))
print('méthode 2 :', diviseurs2(integer))



# =============================================================================
# EXO 3
# =============================================================================

def amicaux():
    """
    vérifie si deux nombres entiers sont amicaux
    
    Returns
    -------
    Bool

    """ 
    n1 = int(input('veuillez entrer un entier n1 : '))
    n2 = int(input('veuillez entrer un entier n2 : '))
    
    n1_diviseurs = diviseurs2(n1)
    n2_diviseurs = diviseurs2(n2)
    
    n1_diviseurs.remove(n1)
    n2_diviseurs.remove(n2)
    
    n1_somme = 0
    n2_somme = 0
    
    for diviseur in n1_diviseurs: 
        n1_somme += diviseur 
        
    for diviseur in n2_diviseurs:
        n2_somme += diviseur
        
    return n1_somme == n2 and n2_somme == n1



# =============================================================================
# EXO 4
# =============================================================================

def doublons(L):
    """
    Supprime les doublons

    Parameters
    ----------
    L : list
        liste dont on veut supprimer les doublons.

    Returns
    -------
    L_clean : list
              liste après suppression des doublons

    """
    L_clean = list()
    
    for e  in L:
        if not e in L_clean:
            L_clean += [e]
            
    return L_clean


assert doublons([1,2,5,8,6,2,5,9,1,8,8]) == [1, 2, 5, 8, 6, 9]


# =============================================================================
# EXO 5
# =============================================================================

liste_eleves = ['a','b','c','d','e','f','g','h','i','j'] 
liste_notes = [1, 40, 80, 60, 58, 80, 75, 80, 60, 24] 
def meilleures_notes(): 
    note_maxi = 0 
    nb_eleves_note_maxi = 0
    liste_maxi = [] 
 
    for compteur in range(len(liste_eleves)): 
        if liste_notes[compteur] == note_maxi: 
            nb_eleves_note_maxi = nb_eleves_note_maxi + 1 
            liste_maxi.append(liste_eleves[compteur]) 
        if liste_notes[compteur] > note_maxi: 
            note_maxi = liste_notes[compteur] 
            nb_eleves_note_maxi = 1
            liste_maxi = [liste_eleves[compteur]] 
    return (note_maxi,nb_eleves_note_maxi,liste_maxi)



# =============================================================================
# EXO 6
# =============================================================================

def recherche(gene, seq_adn): 
    n = len(seq_adn) 
    g = len(gene) 
    i = 0
    trouve = False 
    while i < n and trouve == False : 
        j = 0 
        while j < g and gene[j] == seq_adn[i+j]: 
            g = 0
        if j == g: 
            trouve = True 
        i += 1
    return trouve



















