# Genetic-TSP
A genetic algorithm to find solutions to the Travelling Salesman Problem (TSP)

Cost over many generations:
![Alt_Text](https://github.com/Scratchcat1/Genetic-TSP/blob/master/graph.png)

Comparison of Gene pool sizes:
![Alt_Text](https://github.com/Scratchcat1/Genetic-TSP/blob/master/GeneticTSP_Gene_Number.png)

Running:
```
p = TestSetup()
Simulate(p,250,1500)
```
This will generate a random graph and evolve for 250 generations with 1500 genes, alter to custom settings if desired.

Custom graph
```
graph = Graph()

#To Add a city
graph.Add_City(City_Name)

#To add a road (all cities must be connected to all other cities). The cities do not need to be in order, a road between CityA and CityB is also a road between CityB and CityA.
graph.Add_Road(CityA,CityB,Cost)

#To create the population
population = Population(graph)

#To add a gene
population.Add_Gene() #Creates random gene
population.Add_Gene(Gene) # Add a custom gene , must be of form [CityW,CityX...]

#To run
results = population.Evaluate()
population.Evolve(Pass_Mark,results,New_Population_Size) # Where Pass_Mark is the largest length a 'fit' gene may have.
population.Add_Gene(Gene) # Optional

```
It is recommended to use a smaller population size and a high generations count in order to converge on the solution in a shorter period of time. The closer one wants to get to the optimum the larger the population should be however, as smaller populations tend to get stuck in local minima.
