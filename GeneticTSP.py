import random,copy

def Mutate(Gene,count=2):
    for n in range(count):
        a = random.randint(0,len(Gene)-1)
        b = random.randint(0,len(Gene)-1)
        x,y = Gene[a],Gene[b]
        Gene[a] = y
        Gene[b] = x

    return Gene

def Cross(GeneA,GeneB,count,max_length):
    GeneA = copy.deepcopy(GeneA)
    GeneBBackup = GeneB
    for n in range(count):
        GeneB = copy.deepcopy(GeneBBackup)
        start = random.randint(0,len(GeneA)-1)
        end = min([start+random.randint(1,max_length),len(GeneA)-1])

        Offspring = [-1 for n in range(len(GeneA))]
        Offspring[start:end] = GeneA[start:end]
        for x in range(len(Offspring)):
            if Offspring[x] == -1:
                NewItem = GeneB.pop(0)
                while NewItem in Offspring:
                    NewItem = GeneB.pop(0)
                Offspring[x] = NewItem
        GeneA = copy.deepcopy(Offspring)
##                NewItem = GeneB.pop(0)
##                if NewItem not in Offspring:
##                    Offspring[x] = NewItem
    return Offspring

def Order(A,B):
    if A < B:
        return (A,B)
    else:
        return (B,A)

def Measure(graph,Gene):
    CurrentCity = Gene.pop(0)
    Cost = 0
    while len(Gene) > 0:
        NextCity = Gene.pop(0)
        Cost += graph.Get_Cost(CurrentCity,NextCity)
        CurrentCity = NextCity
    return Cost
        
        
    
        
class Graph:
    def __init__(self):
        self.Cities = []
        self.Roads = {}

    def Add_City(self,City):
        self.Cities.append(City)

    def Get_Cities(self):
        return self.Cities

    def Add_Edge(self,CityA,CityB,Cost):
        self.Roads[Order(CityA,CityB)] = Cost

    def Get_Cost(self,CityA,CityB):
        return self.Roads[Order(CityA,CityB)]




class Population:
    def __init__(self,graph):
        self.GenePool = []
        self.graph = graph
        self.Generation = 0

    def Add_Gene(self,Gene = None):
        if Gene == None:
            Gene = [x for x in self.graph.Get_Cities()]
            random.shuffle(Gene)
        self.GenePool.append(Gene)

    def Evaluate(self):
        results = []
        for gene in self.GenePool:
            Cost = Measure(self.graph,copy.deepcopy(gene))
            results.append(Cost)
        return results

    def Evolve(self,pass_value, results_set, Population_Size = 1000):
        print("Evolving Generation:",self.Generation,"..")
        self.Generation += 1
        BestGene = self.GenePool[results_set.index(min(results_set))]
        Fittest = []
        for x in range(len(self.GenePool)):
            if results_set[x] < pass_value:
                Fittest.append(self.GenePool[x])
        self.GenePool = []
        while len(self.GenePool) < Population_Size-1:
            GeneA,GeneB = random.choice(Fittest),random.choice(Fittest)
            NewGeneA = Cross(GeneA,GeneB,2,4)
            NewGeneB = Mutate(copy.deepcopy(NewGeneA))
            #print(Measure(self.graph,copy.deepcopy(NewGeneA)),Measure(self.graph,copy.deepcopy(NewGeneB)),NewGeneB == NewGeneA, BestGene in [NewGeneB,NewGeneA])
            self.GenePool.append(NewGeneA)
            self.GenePool.append(NewGeneB)
            if random.randint(0,10) == 0:
                self.GenePool.append(GeneA)
        self.GenePool.append(BestGene)
        

    def Get_Generation(self):
        return self.Generation

            
        
            
def TestSetup():
    graph = Graph()
    n = [chr(65+x) for x in range(40)]
    for x in n:
        graph.Add_City(x)

    for a in n:
        for b in n:
            if a!=b:
                graph.Add_Edge(a,b,random.randint(0,1000))

    p = Population(graph)
    for f in range(1000):
        p.Add_Gene()
    return p

    
def Simulate(p,count = 25,Size = 250):
    abc = []
    for f in range(count):
        x = p.Evaluate()
        p.Evolve(sum(x)/len(x)+10,x,Size)
        print(min(x))
        abc.append(min(x))
    return p,abc
