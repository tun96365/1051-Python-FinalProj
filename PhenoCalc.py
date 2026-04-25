# PhenoCalc
# Sami Kazi TUID: 915970388
import itertools
from collections import Counter

gametesParent1 = []
gametesParent2 = []
offspring = []
phenotypes = {}
results = []

def Parent1():
    apple = True
    while apple == True:
        userGenotype1 = input("Enter the genotype of the first parent (we finna call this P1) Enter it as AaBb...: ")
        if len(userGenotype1) % 2 != 0 or not userGenotype1.isalpha():
            print("Invalid input. Please enter a valid genotype (e.g., AaBb).")
        else:
            apple = False

    pairsParent1 = []

    for i in range(0, len(userGenotype1), 2):
        pairsParent1.append(userGenotype1[i:i+2])

    rawCombos = itertools.product(*pairsParent1)
    
   
    for eachCombo in rawCombos:
        gametesParent1.append("".join(eachCombo))

    return gametesParent1

def Parent2():
    apple = True
    while apple == True:
        userGenotype2 = input("Enter the genotype of the second parent (we finna call this P2) Enter it as AaBb...: ")
        if len(userGenotype2) % 2 != 0 or not userGenotype2.isalpha():
            print("Invalid input. Please enter a valid genotype (e.g., AaBb).")
        else:
            apple = False

    pairsParent2 = []
    for i in range(0, len(userGenotype2), 2):
        pairsParent2.append(userGenotype2[i:i+2])

    rawCombos = itertools.product(*pairsParent2)

    for eachCombo in rawCombos:
        gametesParent2.append("".join(eachCombo))

    return gametesParent2

def modeSelection():
    banana = True
    while banana == True:
        chosenMode = input("Enter the mode you want to use (1: Mendelian, 2: Incomplete Dominance, 3: Co-Dominance, 4: Dominant Epistasis:, 5: Recessive Epistasis, 6: Mulit-Gene Epistasis): ")
        if chosenMode == "1":
            print("You have selected Mendelian mode.")
            return chosenMode
            banana = False
        elif chosenMode == "2":
            print("You have selected Incomplete Dominance mode.")
            return chosenMode
            banana = False
        elif chosenMode == "3":
            print("You have selected Co-Dominance mode.")
            return chosenMode
            banana = False
        elif chosenMode == "4":
            print("You have selected Dominant Epistasis mode.")
            return chosenMode
            banana = False
        elif chosenMode == "5":
            print("You have selected Recessive Epistasis mode.")
            return chosenMode
            banana = False
        elif chosenMode == "6":
            print("You have selected Gene Hierarchy mode.")
            return chosenMode
            banana = False
        else:
            print("Invalid mode selected. Please choose a valid mode (1, 2, 3, or 4).")

def sortAndCombine(gametesParent1, gametesParent2):
    sortedResult = ""
    for i in range(len(gametesParent1)):
        sortedPair = sorted([gametesParent1[i], gametesParent2[i]])
        sortedResult += "".join(sortedPair)
    return sortedResult

def produceOffspring(gametesParent1, gametesParent2):
    for eachGamete in gametesParent1:
        for aGamete in gametesParent2:
            offspring.append(sortAndCombine(eachGamete, aGamete))

    return offspring

def noEpistaticInteractions(offspring):
    sampleGenotype = offspring[0]
    if chosenMode == "1":
        for i in range(0, len(sampleGenotype), 2):

            gene = sampleGenotype[i].upper()
            dominant  = input(f"What is the dominant phenotype for gene {gene}? ")
            hetero    = input(f"What is the heterozygous phenotype for gene {gene}? ")
            recessive = input(f"What is the recessive phenotype for gene {gene}? ")
            phenotypes[gene] = {
        "dominant":  dominant,
        "hetero":    hetero,
        "recessive": recessive
       }
    if chosenMode == "2":
     for i in range(0, len(sampleGenotype), 2):

            gene = sampleGenotype[i].upper()
            dominant  = input(f"What is the dominant phenotype for gene {gene}? ")
            hetero    = input(f"What is the intermediate phenotype for gene {gene}? ")
            recessive = input(f"What is the recessive phenotype for gene {gene}? ")
            phenotypes[gene] = {
        "dominant":  dominant,
        "hetero":    hetero,
        "recessive": recessive
       }
     if chosenMode == "3":
         for i in range(0, len(sampleGenotype), 2):

            gene = sampleGenotype[i].upper()
            dominant  = input(f"What is the dominant phenotype for gene {gene}? ")
            hetero    = input(f"What is the intermediate phenotype for gene {gene}? ")
            recessive = input(f"What is the recessive phenotype for gene {gene}? ")
            phenotypes[gene] = {
        "dominant":  dominant,
        "hetero":    hetero,
        "recessive": recessive
       }

    return phenotypes

def DominantEpistasis(offspring):
    sampleGenotype = offspring[0]
    genes = []
    
    for i in range(0, len(sampleGenotype), 2):
        genes.append(sampleGenotype[i].upper())

    epistaticGene = input(f"Which gene is epistatic?: ")

    epistatic = input(f"Phenotype when {epistaticGene}_ is present (masks everything): ")
    hypoDom   = input(f"Phenotype when {epistaticGene.lower()}{epistaticGene.lower()} with dominant hypostatic gene: ")
    hypoRec   = input(f"Phenotype when all recessive (double recessive): ")

    phenotypes["epistaticMode"] = "dominant"
    phenotypes["epistaticGene"] = epistaticGene
    phenotypes["epistatic"]     = epistatic
    phenotypes["hypoDom"]       = hypoDom
    phenotypes["hypoRec"]       = hypoRec

    return phenotypes

def recessiveEpistasis(offspring):
    sampleGenotype = offspring[0]
    genes = []
    
    for i in range(0, len(sampleGenotype), 2):
        genes.append(sampleGenotype[i].upper())

    epistaticGene = input(f"Which gene is epistatic?: ")

    epistatic = input(f"Phenotype when {epistaticGene.lower()}{epistaticGene.lower()} is present (masks everything): ")
    hypoDom   = input(f"Phenotype when {epistaticGene}_ with dominant hypostatic gene: ")
    hypoRec   = input(f"Phenotype when all recessive (double recessive): ")

    phenotypes["epistaticMode"] = "recessive"
    phenotypes["epistaticGene"] = epistaticGene
    phenotypes["epistatic"]     = epistatic
    phenotypes["hypoDom"]       = hypoDom
    phenotypes["hypoRec"]       = hypoRec

    return phenotypes

def geneHierarchy(offspring):
    sampleGenotype = offspring[0]
    genes = []
    for i in range(0, len(sampleGenotype), 2):
        genes.append(sampleGenotype[i].upper())
    
    print(f"Rank the genes from most to least dominant ({'/'.join(genes)})")
    rankedGenes = []
    remaining = genes.copy()  
    
    for i in range(len(genes)):
        gene = input(f"Rank {i+1} (remaining: {'/'.join(remaining)}): ").upper()
        while gene not in remaining:
            print(f"Invalid. Choose from remaining genes: {'/'.join(remaining)}")
            gene = input(f"Rank {i+1}: ").upper()
        remaining.remove(gene)
        rankedGenes.append(gene)
        phenotype = input(f"Phenotype when {gene}_ is present (and all lower ranked genes absent): ")
        phenotypes[gene] = phenotype
    
    bottomPhenotype = input("Phenotype when all genes are recessive: ")
    phenotypes["allRecessive"] = bottomPhenotype
    phenotypes["rankedGenes"] = rankedGenes
    return phenotypes

def produceGenotypePunnet(gametesParent1, gametesParent2, offspring, phenotypes):
    cellSize = len(gametesParent1)
    cellWidth = len(offspring[0]) + 3

    header = " " * (cellWidth + 2)
    for gamete in gametesParent1:
        header += gamete.center(cellWidth)
    print(header)
    print("-" * len(header))

    
    rowTracker = 0
    for i in range(0, len(offspring), cellSize):
        row = offspring[i:i+cellSize]
        rowStr = gametesParent2[rowTracker].center(cellWidth) + "|"
        for genotype in row:
            rowStr += genotype.center(cellWidth) + "|"
        print(rowStr)
        rowTracker += 1

def phenotypeFiller(offspring, phenotypes):
    
    for eachGenotype in offspring:
        if "epistaticGene" in phenotypes:

            epistaticGene = phenotypes["epistaticGene"]

            for i in range(0, len(eachGenotype), 2):
                pair = eachGenotype[i:i+2]
                gene = pair[0].upper()
    
                if gene == epistaticGene:
                        
                        if phenotypes["epistaticMode"] == "dominant" and pair[0].isupper():
                            results.append(phenotypes["epistatic"])
                            break
                        elif phenotypes["epistaticMode"] == "recessive" and pair[0].islower() and pair[1].islower():
                            results.append(phenotypes["epistatic"])
                            break
                        continue  
                    

                if pair[0].isupper():
                    results.append(phenotypes["hypoDom"])
                    break
            else:
                results.append(phenotypes["hypoRec"])
        elif "rankedGenes" in phenotypes:
            rankedGenes = phenotypes["rankedGenes"]
            for gene in rankedGenes:
                
                for i in range(0, len(eachGenotype), 2):
                    pair = eachGenotype[i:i+2]
                    if pair[0].upper() == gene:
                        if pair[0].isupper():  
                            results.append(phenotypes[gene])
                            break
                else:
                    continue 
                break  
            else:
                results.append(phenotypes["allRecessive"])
        else:
            label = []
            for i in range(0, len(eachGenotype), 2):
                pair = eachGenotype[i:i+2]
                gene = pair[0].upper()
                dominant  = phenotypes[gene]["dominant"]
                hetero    = phenotypes[gene]["hetero"]
                recessive = phenotypes[gene]["recessive"]
                
                if pair[0].isupper() and pair[1].isupper():
                    label.append(dominant)
                elif pair[0].isupper():
                    label.append(hetero)
                else:
                    label.append(recessive)
            results.append(" / ".join(label))
    
    counts = Counter(results)
    total = len(offspring)
    for phenotype, count in counts.items():
        ratio = f"{count}:{total - count}"
        print(f"Phenotype: {phenotype} | Ratio: {ratio}")

def phenotypePunnet(gametesParent1, gametesParent2, results):
    longest = 0
    for r in results:
        if len(r) > longest:
            longest = len(r)
    cellWidth = longest + 2  
    cellSize = len(gametesParent1)

    header = " " * (cellWidth + 2)
    for gamete in gametesParent1:
        header += gamete.center(cellWidth)
    print(header)
    print("-" * len(header))

    
    rowTracker = 0
    for i in range(0, len(offspring), cellSize):
        row = results[i:i+cellSize]
        rowStr = gametesParent2[rowTracker].center(cellWidth) + "|"
        for phenotype in row:
            rowStr += phenotype.center(cellWidth) + "|"
        print(rowStr)
        rowTracker += 1


Parent1()
Parent2()
chosenMode = modeSelection()
if chosenMode == "1" or chosenMode == "2" or chosenMode == "3":
    offspring = produceOffspring(gametesParent1, gametesParent2)
    phenotypes = noEpistaticInteractions(offspring)
    produceGenotypePunnet(gametesParent1, gametesParent2, offspring, phenotypes)
    phenotypeFiller(offspring, phenotypes)
    phenotypePunnet(gametesParent1, gametesParent2, results)
elif chosenMode == "4":
    offspring = produceOffspring(gametesParent1, gametesParent2)
    phenotypes = DominantEpistasis(offspring)
    produceGenotypePunnet(gametesParent1, gametesParent2, offspring, phenotypes)
    phenotypeFiller(offspring, phenotypes)
    phenotypePunnet(gametesParent1, gametesParent2, results)
elif chosenMode == "5":
    offspring = produceOffspring(gametesParent1, gametesParent2)
    phenotypes = recessiveEpistasis(offspring)
    produceGenotypePunnet(gametesParent1, gametesParent2, offspring, phenotypes)
    phenotypeFiller(offspring, phenotypes)
    phenotypePunnet(gametesParent1, gametesParent2, results)
elif chosenMode == "6":
    offspring = produceOffspring(gametesParent1, gametesParent2)
    phenotypes = geneHierarchy(offspring)
    produceGenotypePunnet(gametesParent1, gametesParent2, offspring, phenotypes)
    phenotypeFiller(offspring, phenotypes)
    phenotypePunnet(gametesParent1, gametesParent2, results)

