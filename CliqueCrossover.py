import random
from RandomGraph import RandomGraph
from eckity.genetic_operators.genetic_operator import GeneticOperator
from random import randrange


class CliqueCrossover(GeneticOperator):
    def __init__(self, crossover_type, probability=1, arity=2, events=None):
        super().__init__(probability, arity, events)
        self.crossover_type = crossover_type

    def apply(self, individuals):
        for i in range(0, len(individuals) - 1, 2):
            if (i+1<len(individuals)):
                if(self.crossover_type == "one_index_swap"):
                    individuals[i], individuals[i+1] = self.one_index_swap(individuals[i], individuals[i+1])
                elif(self.crossover_type == "two_index_swap"):
                    individuals[i], individuals[i+1] = self.two_index_swap(individuals[i], individuals[i+1])
                elif(self.crossover_type == "uniform"):
                    individuals[i], individuals[i+1] = self.uniform(individuals[i], individuals[i+1])
        self.applied_individuals = individuals
        return individuals
        
    # swap the values from an index to the end of the list 
    def one_index_swap(self, individual1, individual2):
        index = randrange(0, len(individual1))
        for i in range(index, len(individual1)): 
            individual1[i], individual2[i] = individual2[i], individual1[i]
        return individual1, individual2 

    # swap the values between two indexes
    def two_index_swap(self, individual1, individual2):
        index1, index2 = sorted(random.sample(range(len(individual1)), 2)) # randomly select two indexes and make sure that index1 < index2 
        for i in range(index1, index2):
            individual1[i], individual2[i] = individual2[i], individual1[i] 
        return individual1, individual2
    
    # swap each value with a 50% chance
    def uniform(self, individual1, individual2):
        for i in range(len(individual1)):
            if random.random() < 0.5:
                individual1[i], individual2[i] = individual2[i], individual1[i] 
        return individual1, individual2
    
    