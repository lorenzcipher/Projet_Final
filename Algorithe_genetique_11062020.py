# -*- coding: utf-8 -*-
"""
Class
@author: Fateh Maamra
"""

###############################################################################
###----> Importation packages

from random import randint
from functools import reduce
from operator import add
import numpy as np
import random
from pickle import dump as dp
from pickle import load as ld
from os import getcwd, mkdir
from tqdm import tqdm
from statistics import stdev, mean
from numpy import concatenate
class AG () :
 
    ###---------------------------------------------------------------------###
    ###--------------------------------Initialisation des paramétres-------------------------###
    def __init__ (self,parametres_algorithme) :
    
        #taille de la population 
        self.nombre_individus         = parametres_algorithme[0]
            
        #nombre de génération 
        self.nombre_generation        = parametres_algorithme[1]

        #probabilité de faire une mutation sur l'individu 
        self.probabilite_mutation     = parametres_algorithme[2]

        #probabilité de faire un croisement  sur l'individu 
        self.probabilite_croisement   = parametres_algorithme[3]

        #nombre d'articles 
        self.nombre_articles         = parametres_algorithme[4]

        #Capacité du Bin
        self.capacity         = parametres_algorithme[5]

        self.population_initiale     = np.zeros([self.nombre_individus,self.nombre_articles**2+1])
        print(self.population_initiale)
        self.population_generation_old= np.zeros([self.nombre_individus,self.nombre_articles**2+1])
        print(self.population_generation_old)
        self.population_generation    = np.zeros([self.nombre_individus,self.nombre_articles**2+1])
        print(self.population_generation)
        self.nombre_individus_mutation= int(round(self.nombre_individus * self.probabilite_mutation,0))
        print(self.probabilite_mutation)
        self.nombre_individus_croisement= int(round(self.nombre_individus * self.probabilite_croisement,0))
        print(self.probabilite_croisement)

        self.dossier_travail            = getcwd()
        self.dossier_sauvegarde         = self.dossier_travail + str('\sauvegarde')
        self.dossier_figures            = self.dossier_travail + str('\Figures')
            
            
        #probabilité de faire une mutation sur l'individu 
        #CHANCE_TO_MUTATE = 0.1
        #probabilité l'individu avec le la valeur de fitness gradé qui sera gardé pour la prochaine génération
        #GRADED_RETAIN_PERCENT = 0.2
        #probabilité de l'individu le moins gradé par la valeur de fitness (ça va permettre la variété et évité optimum local)
        #CHANCE_RETAIN_NONGRATED = 0.05
        #taille de la population 
        #POPULATION_COUNT = 100
        #nombre des génération 
        #GENERATION_COUNT_MAX = 100000
        #nombre d'individu bien gradé gardé 
        #GRADED_INDIVIDUAL_RETAIN_COUNT = int(POPULATION_COUNT * GRADED_RETAIN_PERCENT)
    
    ###---------------------------------------------------------------------###
    ###--------------> Fonctions objectif et contraintes
    def get_individual_fitness(self,individual,nb):
        """ Compute the fitness of the given individual. """
        #comment retourner nb qui est une variable de la fonction individue 
        
        length = self.nombre_articles[1]
        C = self.capacity[2]
        fitness = 0
        som=0
        for loop in range (0,(length**2)-1,length) :
            fi = 0 
            for x in range(loop,loop+length):
                fi=fi+individual[x]
            som=som+((fi/C)**2)
        fitness=som/nb
            
        return fitness


###---------------------------------------------------------------------###
###--------------> Creation de la population initiale
def fct_tri(self) :
    '''
    Fonction permettant de trier les individus en fonction de la fonction
    objective. Tri par ordre croissant.
    '''
    self.population_generation_old = np.array(sorted(self.population_generation.tolist(), key = lambda x: x[-1], reverse = False)).copy()
                
def individue(self,data):
    """"
    length: la taille des objets 
    C : la capaciter maximale d'un Bin
    k : le nombre de Bin calculer par une heuristique 
    data : la liste des obejts avec leurs taille 
    """
    length = self.nombre_articles[1]
    C = self.capacity[2]
    #le reste rem aprés l'insertion de l'objet
    rem = C
    #vecteur de zéro créer avec numpy le contenu est de type float
    chromo = np.zeros(length**2+1)
    #indice du chromosome 
    i=0
    #indice de la liste des objets
    j=0
    #nombre de Bins 
    nb=1
    #boucle pour créer les chromosomes 
    for x in range (len(data)):
        #si vérification que ça fit
        if(data[x] <= rem):
            chromo[i]=data[x] 
            #soustraction la taille de l'objet de la capacité restante  
            rem = rem - data[x]
        #sinon si ça rentre pas dans ce bin nb 
        else :
            nb += 1
            
            #soustraction la taille de l'objet de la taille initiale du bin 
            rem = C - data[x]
            #le décalage de case pour se placer dans le prochain bin
            i+=length
            chromo[i]=data[x]
        if( i< length**2):
            i+=1
    return chromo,nb

def fct_initialisation_population (self,data) :
    '''
    Fonction permettant la création d'un attribut 'population initiale' 
    de manière aléatoire en fonction des paramètres variables saisis par
    l'utilisateur.
    '''
    length = self.nombre_articles[1]
    POPULATION_COUNT =  self.nombre_individus[2]
    
    for x in range(POPULATION_COUNT):
        #générateur de liste random sans répetition (le risque d'avoir des répetition )
        data_random = random.sample(data,length)
        self.population_initiale[x]= individue(self,data_random)
        self.population_initiale[x][-1] = self.get_individual_fitness(self,self.individue(self,data_random),self.individue.nb)
    
    self.population_generation = self.population_initiale.copy()
    try:
        mkdir(self.dossier_sauvegarde)
    except:
        pass
        self.fct_tri()
        
        with open(self.dossier_sauvegarde + str('\sauvegarde.ppj'), 'wb') as sauvegarde:
            dp(self.population_generation_old, sauvegarde)
            sauvegarde.close()

    return self.population_initiale
if __name__ == "__main__":
    ag = AG()
    print(ag)
    param = [10,2,1,1,4,3]
    ag.__init__(param) 
    
