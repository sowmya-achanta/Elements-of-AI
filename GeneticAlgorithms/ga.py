'''
This file contains support code for B551 Hw6                                 # File version:  November 19, 2015                                            #

For questions related to genetic algorithms or the knapsack problem, any AI can be of help. For questions related to the support code itself, contact Alex at aseewald@indiana.edu.
'''
import math
import random
import pickle
import numpy as np
import pandas as pd
from scipy.stats import norm
import itertools
import copy
global elitism
elitism = True

def fitness(max_volume,volumes,prices):
    '''
    This should return a scalar which is to be maximized.
    max_volume is the maximum volume that the knapsack can contain.
    volumes is a list containing the volume of each item in the knapsack.
    prices is a list containing the price of each item in the knapsack, which is aligned with 'volumes'.
    '''
    sum_vol = 0
    sum_price = 0
    sum_vol = sum(volumes)
    sum_price = sum(prices)
    if sum_vol > max_volume:
        return 0
    else:
        return sum_price
    pass

def randomSelection(population,fitnesses):
    '''
    This should return a single chromosome from the population. The selection process should be random,
    but with weighted probabilities proportional to the corresponding 'fitnesses' values.
    '''
    '''using the roulette-wheel selection, return a chromosome that matches a random value
    from the range(0, total fitness)'''
    total_fitness = sum(fitnesses)
    limit = random.uniform(0,total_fitness)
    current_fitness = 0
    for i in range(len(fitnesses)):
        chromosome = population[i]
        current_fitness += fitnesses[i]
        if current_fitness > limit:
            return chromosome
        else:
            return random.choice(population)

def reproduce(mom,dad):
    "This does genetic algorithm crossover. This takes two chromosomes, mom and dad, and returns two chromosomes."
    #select cross-over point
    #print("In reproduce:",mom,dad)
    crossover_point = math.ceil(len(mom) / 2 )
    #print("COP", crossover_point)

    #create children
    child1 = np.concatenate((mom[0:crossover_point],dad[crossover_point:len(dad)]))
    child2 = np.concatenate((dad[0:crossover_point],mom[crossover_point:len(mom)]))

    return child1,child2

def mutate(child,mut_prob):
    '''Takes a child, produces a mutated child where each bit of chromosome is chosen for flip if a random prob is
    less than mut_prob'''
    for i in range(0,len(child)):
        if random.random() < mut_prob:
            child[i] = 1 - child[i]
    return child

def compute_fitnesses(world,chromosomes):
    '''
    Takes an instance of the knapsack problem and a list of chromosomes and returns the fitness of these chromosomes, according to your 'fitness' function.
    Using this is by no means required, if you want to calculate the fitnesses in your own way, but having a single definition for this is convenient because
    (at least in my solution) it is necessary to calculate fitnesses at two distinct points in the loop (making a function abstraction desirable).

    Note, 'chromosomes' is required to be a 2D numpy array of boolean values (a fixed-size boolean array is the recommended encoding of a chromosome, and there should be multiple of these arrays, hence the matrix).
    '''
    return [fitness(world[0], world[1] * chromosome, world[2] * chromosome) for chromosome in chromosomes]

def genetic_algorithm(world,popsize,max_years,mutation_probability):
    '''
    world is a data structure describing the problem to be solved, which has a form like 'easy' or 'medium' as defined in the 'run' function.
    The other arguments to this function are what they sound like.
    genetic_algorithm *must* return a list of (chromosomes,fitnesses) tuples, where chromosomes is the current population of chromosomes, and fitnesses is
    the list of fitnesses of these chromosomes.
    '''

    #chromosomes is a list of chromosomes in the current population
    max_volume = world[0]
    volume_list = np.array(world[1], dtype = bool)
    chromosomes_list = [[random.choice((0,1)) for i in range(len(volume_list))]for j in range(popsize)]
    chromosomes = np.asarray(chromosomes_list)
    #print("Initial_population",chromosomes)
    fitnesses = compute_fitnesses(world, chromosomes)
    #print("Initial_population fitnesses", fitnesses)
    all_pop_fit = [] #the  list of (chromosomes,fitnesses) tuples to return
    all_pop_fit.append((chromosomes, fitnesses))
    max_years -= 1
    #print("all_pop_fit", all_pop_fit)

    #generate new_population for each year from previous year
    while max_years >= 1:
        #generate new-population using mutation, cross-over, random-selection combined with elitism
        new_population = []
        new_chromosomes = np.array
        new_fitnesses = []

        #select elite individuals in this generation
        temp_fitneses = fitnesses
        max_fit1 = max(temp_fitneses)
        max_fit1_index = temp_fitneses.index(max_fit1)
        temp_fitneses[max_fit1_index] = -1

        max_fit2 = max(temp_fitneses)
        max_fit2_index = temp_fitneses.index(max_fit2)
        temp_fitneses[max_fit1_index] = max_fit1

        #choose elite parents if elitism true or select random parents using random selection
        if elitism:
            mom = chromosomes[max_fit1_index]
            dad = chromosomes[max_fit2_index]
        else:
            mom = randomSelection(chromosomes, fitnesses)
            dad = randomSelection(chromosomes, fitnesses)
            while (mom == dad).all():
                dad = randomSelection(chromosomes, fitnesses)

        #append parents to new_population
        new_population.append(mom)
        new_population.append(dad)
        #print("elite_mom = ",mom,"elite_dad = ",dad)

        #perform cross-over of the parents and mutate the resulting children. Repeat this until the rest of
        #the population is generated
        for i in range(int((popsize-2)/2)):
            #perform cross-over
            child1,child2 = reproduce(mom,dad)

            #perform mutation
            child1 = mutate(child1,mutation_probability)
            child2 = mutate(child2,mutation_probability)
            new_population.append(child1)
            new_population.append(child2)

        new_chromosomes = np.asarray(new_population)
        new_fitnesses = compute_fitnesses(world, new_chromosomes)
        chromosomes = new_chromosomes
        fitnesses = new_fitnesses
        max_years -= 1
        all_pop_fit.append((new_chromosomes, new_fitnesses))
    return all_pop_fit

def run(popsize,max_years,mutation_probability):
    '''
    The arguments to this function are what they sound like.
    Runs genetic_algorithm on various knapsack problem instances and keeps track of tabular information with this schema:
    DIFFICULTY YEAR HIGH_SCORE AVERAGE_SCORE BEST_PLAN
    '''
    table = pd.DataFrame(columns=["DIFFICULTY", "YEAR", "HIGH_SCORE", "AVERAGE_SCORE", "BEST_PLAN"])
    sanity_check = (10, [10, 5, 8], [100,50,80])
    chromosomes = genetic_algorithm(sanity_check,popsize,max_years,mutation_probability)
    for year, data in enumerate(chromosomes):
        year_chromosomes, fitnesses = data
        table = table.append({'DIFFICULTY' : 'sanity_check', 'YEAR' : year, 'HIGH_SCORE' : max(fitnesses),
            'AVERAGE_SCORE' : np.mean(fitnesses), 'BEST_PLAN' : year_chromosomes[np.argmax(fitnesses)]}, ignore_index=True)
    easy = (20, [20, 5, 15, 8, 13], [10, 4, 11, 2, 9] )
    chromosomes = genetic_algorithm(easy,popsize,max_years,mutation_probability)
    for year, data in enumerate(chromosomes):
        year_chromosomes, fitnesses = data
        table = table.append({'DIFFICULTY' : 'easy', 'YEAR' : year, 'HIGH_SCORE' : max(fitnesses),
            'AVERAGE_SCORE' : np.mean(fitnesses), 'BEST_PLAN' : year_chromosomes[np.argmax(fitnesses)]}, ignore_index=True)
    medium = (100, [13, 19, 34, 1, 20, 4, 8, 24, 7, 18, 1, 31, 10, 23, 9, 27, 50, 6, 36, 9, 15],
                   [26, 7, 34, 8, 29, 3, 11, 33, 7, 23, 8, 25, 13, 5, 16, 35, 50, 9, 30, 13, 14])
    chromosomes = genetic_algorithm(medium,popsize,max_years,mutation_probability)
    for year, data in enumerate(chromosomes):
        year_chromosomes, fitnesses = data
        table = table.append({'DIFFICULTY' : 'medium', 'YEAR' : year, 'HIGH_SCORE' : max(fitnesses),
            'AVERAGE_SCORE' : np.mean(fitnesses), 'BEST_PLAN' : year_chromosomes[np.argmax(fitnesses)]}, ignore_index=True)
    hard = (5000, norm.rvs(50,15,size=100), norm.rvs(200,60,size=100))
    chromosomes = genetic_algorithm(hard,popsize,max_years,mutation_probability)
    for year, data in enumerate(chromosomes):
        year_chromosomes, fitnesses = data
        table = table.append({'DIFFICULTY' : 'hard', 'YEAR' : year, 'HIGH_SCORE' : max(fitnesses),
            'AVERAGE_SCORE' : np.mean(fitnesses), 'BEST_PLAN' : year_chromosomes[np.argmax(fitnesses)]}, ignore_index=True)
    print("Population size= ", popsize, "Generations=", max_years, "Mutation_prob", mutation_probability)
    #print(table)
    for difficulty_group in ['sanity_check','easy','medium','hard']:
        group = table[table['DIFFICULTY'] == difficulty_group]
        bestrow = group.ix[group['HIGH_SCORE'].argmax()]
        print("Best year for difficulty {} is {} with high score {} and chromosome {}".format(difficulty_group,int(bestrow['YEAR']), bestrow['HIGH_SCORE'], bestrow['BEST_PLAN']))
    table.to_pickle("results.pkl") #saves the performance data, in case you want to refer to it later. pickled python objects can be loaded back at any later point.

run(10,3,0.01)
run(10,3,0.02)
run(35,5,0.01)
run(35,5,0.02)
run(75,10,0.01)
run(75,15,0.02)
run(100,25,0.02)
run(100,15,0.01)
