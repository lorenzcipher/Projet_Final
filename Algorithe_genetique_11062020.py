# -*- coding: utf-8 -*-
"""
Class
@author: Fateh Maamra
"""

###############################################################################
###----> Importation packages

import random
from functools import reduce
from operator import add
from os import getcwd
from os import mkdir
from pickle import dump as dp
from pickle import load as ld
from random import randint
from statistics import mean
from statistics import stdev

import numpy as np
from numpy import concatenate
from tqdm import tqdm


class AG() :
    ###---------------------------------------------------------------------###
    ###--------------------------------Initialisation des paramétres-------------------------###
    def __init__(self, nombre_individus, nombre_generation, probabilite_mutation, probabilite_croisement, data, capacity):
        self.nombre_individus = nombre_individus
        self.nombre_generation = nombre_generation
        self.probabilite_mutation = probabilite_mutation
        self.probabilite_croisement = probabilite_croisement
        self.data = data
        self.nombre_articles = len(self.data)
        self.capacity = capacity

        self.population_initiale = np.zeros([self.nombre_individus, self.nombre_articles ** 2 + 1])
        self.population_generation_old = np.zeros([self.nombre_individus, self.nombre_articles ** 2 + 1])
        self.population_generation = np.zeros([self.nombre_individus, self.nombre_articles ** 2 + 1])
        self.nombre_individus_mutation = int(round(self.nombre_individus * self.probabilite_mutation, 0))
        self.nombre_individus_croisement = int(round(self.nombre_individus * self.probabilite_croisement, 0))

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
    def get_individual_fitness(self, individual, nb):
        """ Compute the fitness of the given individual. """
        #comment retourner nb qui est une variable de la fonction individue

        length = len(self.data)
        #self.nombre_articles[4]
        C = self.capacity
        #self.capacity[2]
        fitness = 0
        som = 0
        for loop in range (0, length ** 2, length) :
            fi = 0
            for x in range(loop, loop + length):
                fi = fi + individual[x]
            som = som + ((fi / C) ** 2)
        fitness = som / nb

        return fitness


    ###---------------------------------------------------------------------###
    ###--------------> Creation de la population initiale
    def fct_tri(self):
        '''
        Fonction permettant de trier les individus en fonction de la fonction
        objective. Tri par ordre croissant.
        '''
        self.population_generation_old = np.array(sorted(self.population_generation.tolist(), key = lambda x: x[-1], reverse=False)).copy()

    def individue(self, data):
        """"
        length: la taille des objets
        C : la capaciter maximale d'un Bin
        k : le nombre de Bin calculer par une heuristique
        data : la liste des obejts avec leurs taille
        """
        length = len(data)
        #self.nombre_articles[1]
        C = 4
        #self.capacity[2]
        #le reste rem aprés l'insertion de l'objet
        rem = C
        #vecteur de zéro créer avec numpy le contenu est de type float
        chromo = np.zeros(length ** 2 + 1)
        #indice du chromosome
        i = 0
        #indice de la liste des objets
        j = 0
        #nombre de Bins
        nb = 1
        #boucle pour créer les chromosomes
        for x in range (len(data)):
            # si vérification que ça fit
            if (data[x] <= rem):
                chromo[i] = data[x]
                #soustraction la taille de l'objet de la capacité restante
                rem = rem - data[x]
                #sinon si ça rentre pas dans ce bin nb
            else:
                nb += 1
                #soustraction la taille de l'objet de la taille initiale du bin
                rem = C - data[x]
                #le décalage de case pour se placer dans le prochain bin
                i += length
                chromo[i] = data[x]

            if (i < length ** 2):
                i += 1
        return chromo, nb

    def fct_initialisation_population(self) :
        '''
        Fonction permettant la création d'un attribut 'population initiale'
        de manière aléatoire en fonction des paramètres variables saisis par
        l'utilisateur.
        '''
        list_individus = []
        list_evaluations = []
        for x in range(self.nombre_individus):
            # générateur de liste random sans répetition (le risque d'avoir des répetition )
            data_random = random.sample(self.data, len(self.data))
            ind = self.individue(data_random)[0]
            self.population_initiale[x] = ind
            list_individus.append(ind)
            self.population_initiale[x][-1] = self.get_individual_fitness(ind, self.individue(data_random)[1])
            list_evaluations.append(self.get_individual_fitness(ind, self.individue(data_random)[1]))
        print(list_individus)
        print(list_evaluations)
        result = list(zip(list_individus, list_evaluations))
        print(max(result, key=lambda x: x[1]))

        return self.population_initiale

if __name__ == "__main__":
    data = [1, 2, 3, 3]
    parameters = {
        "nombre_individus": 20,
        "nombre_generation": 2,
        "probabilite_mutation": .1,
        "probabilite_croisement": 1,
        "data": data,
        "capacity": 3
    }
    ag = AG(**parameters)
    p = ag.fct_initialisation_population()
    print(p)
