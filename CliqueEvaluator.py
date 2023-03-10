from eckity.evaluators.simple_individual_evaluator import SimpleIndividualEvaluator
from Graph import Graph


class CliqueEvaluator(SimpleIndividualEvaluator):
    def __init__(self, graph) -> None:
        super().__init__()
        self.graph = graph
        self.evaluated_individuals = dict()

    def _evaluate_individual(self, individual):
        if(individual in self.evaluated_individuals.keys()):
            return self.evaluated_individuals.get(individual)
        else:
            individual_vector = individual.get_vector()
            biggest_clique_size = 0
            num_of_ones = 0

            for i in range(len(individual_vector)):
                if individual_vector[i] == 1:

                    num_of_ones += 1
                    cliques = []
                
                    # adds a clique for each vertex the vertex 'i' is connected to
                    # create new clique only for vertices with a bigger index than 'i'
                    # increment redundant_vertices_count if the vertex 'i' is not connected to any other vertex
                    for j in range(len(individual_vector)):
                        if individual_vector[j] == 1 and self.graph.is_neighbour(i,j):
                            if j > i:
                                cliques.append({i, j})

                    # for each clique in the list, add all vertices that are connected to all vertices in the clique
                    for c in cliques:
                        for j in range(i+1, len(individual_vector)):
                            if individual_vector[j] == 1 and all([self.graph.is_neighbour(j,k) for k in c]):
                                c.add(j)
                    
                    # update biggest_clique_size if needed
                    if len(cliques) > 0:
                        biggest_clique_size = max(biggest_clique_size, max([len(c) for c in cliques]))

            # add a bonus based on the ratio of the biggest clique size to the number of vertices in the individual
            bonus = biggest_clique_size/num_of_ones if num_of_ones != 0 else 0
            fitness = biggest_clique_size + bonus - 1
            self.evaluated_individuals[individual] = fitness
            return fitness