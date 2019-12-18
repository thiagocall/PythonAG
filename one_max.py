import random, sys

def gerar_individo(qte_genes):
    ind = ''
    for i in range(qte_genes):
        ind += str(random.randint(0,1))
    return ind


def gerar_populacao(tam_pop, qte_genes):
    pop=[]
    for i in range(tam_pop):
        pop.append(gerar_individo(qte_genes))
    return pop

def fitness(ind):
    return  sum(int(gene) for gene in ind)


def selecionar_pais(pop, tam_pop, K=3):
    pais = []

    for torneio in range(tam_pop):
        competidores = []

        for i in range(K):
            indice = random.randint(0, tam_pop - 1)
            competidores.append(pop[indice])
        
        maior_avaliacao = fitness(competidores[0])
        vencedor = competidores[0]
        for i in range(1, K):
            avaliacao = fitness(competidores[i])
            if avaliacao > maior_avaliacao:
                maior_avaliacao = avaliacao
                vencedor = competidores[i]
                
        pais.append(vencedor)
    
    return pais 


def gerar_filhos(pais, tam_pop, taxa_crossover = 0.7):

    nova_pop = []
    for i in range(tam_pop//2):
        pai1 = random.choice(pais)
        pai2 = random.choice(pais)

        if random.random() < taxa_crossover:

            corte = random.randint(1, len(pai1) - 1)
            filho1 = pai1[0:corte] + pai2[corte:]
            filho2 = pai2[0:corte] + pai1[corte:]
            nova_pop.append(filho1)
            nova_pop.append(filho2)
        
        else:
            nova_pop.append(pai1)
            nova_pop.append(pai2)

    return nova_pop

def mutacao(pop, tam_pop, qte_genes, taxa_mutacao = 0.005):
    nova_pop = []
    for i in range(tam_pop):
        individuo = ''
        for j in range(qte_genes):
            if random.random() < taxa_mutacao:
                if pop[i][j] == '0':
                    individuo += '1'
                else:
                    individuo += '1'
            else:
                individuo += pop[i][j]
        
        nova_pop.append(individuo)
    
    return nova_pop

def melhor_individuo(pop, tam_pop):
    melhor_avaliacao = fitness(pop[0])
    indice_melhor = 0
    for i in range(1, tam_pop):
        avaliacao = fitness(pop[i])
        if avaliacao > melhor_avaliacao:
            melhor_avaliacao = avaliacao
            indice_melhor = i
    return pop[indice_melhor]


# uso: python3 one_max.py <tam_pop> <qte_genes>
tam_pop, qte_genes = int(sys.argv[1]), int((sys.argv[2]))
taxa_crossover, taxa_mutacao = float(sys.argv[3]), float(sys.argv[4])
geracoes = int(sys.argv[5])
pop = gerar_populacao(tam_pop, qte_genes)

for geracao in range(geracoes):     
    pais = selecionar_pais(pop, tam_pop)
    nova_pop = gerar_filhos(pais, tam_pop, taxa_crossover)
    pop = mutacao(nova_pop, tam_pop, qte_genes)

melhor_individuo = melhor_individuo(pop, tam_pop)

print('Melhor individuo: ', melhor_individuo )
print('Melhor avaliacao: ', fitness(melhor_individuo) )
