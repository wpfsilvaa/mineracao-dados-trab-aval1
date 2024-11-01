import numpy as np
from collections import Counter

def ler_arquivo(file):
    seq = ''
    with open(file, 'r') as f:
        f.readline()
        for line in f:
            seq += line.strip()
    return seq

def contar_aminoacidos(seq):
    return Counter(seq)

def distancia_manhattan(v1, v2):
    total_distance = 0
    for i in range(len(v1)):
        distance = abs(v1[i] - v2[i])  #diferença absoluta
        total_distance += distance
    return total_distance

def distancia_euclidiana(v1, v2):
    total_squared_distance = 0
    for i in range(len(v1)):
        distance = (v1[i] - v2[i]) ** 2
        total_squared_distance += distance
    return np.sqrt(total_squared_distance)

def distancia_supremum(v1, v2):
    max_distance = 0
    for i in range(len(v1)):
        distance = abs(v1[i] - v2[i]) 
        if distance > max_distance:
            max_distance = distance 
    return max_distance

def similaridade_cossena(v1, v2):
    produto = 0
    norm_v1 = 0
    norm_v2 = 0
    for i in range(len(v1)):
        produto += v1[i] * v2[i]
        norm_v1 += v1[i] ** 2
        norm_v2 += v2[i] ** 2
    norm_v1 = np.sqrt(norm_v1)
    norm_v2 = np.sqrt(norm_v2)
    return produto / (norm_v1 * norm_v2)

def criar_vetor(counts):
    amino_acids=['A', 'C', 'G', 'T']
    vetor = []
    for aminoacido in amino_acids:
        vetor.append(counts.get(aminoacido, 0))
    return vetor

file_rat = 'rat.fasta'
file_horse = 'horse.fasta'
file_hamster = 'hamster.fasta'

seq_rat = ler_arquivo(file_rat)
seq_horse = ler_arquivo(file_horse)
seq_hamster = ler_arquivo(file_hamster)

counts_rat = contar_aminoacidos(seq_rat)
counts_horse = contar_aminoacidos(seq_horse)
counts_hamster = contar_aminoacidos(seq_hamster)

#DEBUG
# print(counts_rat) #Retorna um dicionario com a quantidade de letras

vetor_ratos = criar_vetor(counts_rat)
vetor_cavalos = criar_vetor(counts_horse)
vetor_hamster = criar_vetor(counts_hamster)
#DEBUG
# print(vetor_ratos)

#Rato e Cavalo
manhattan_rato_cavalo = distancia_manhattan(vetor_ratos, vetor_cavalos)
euclidiano_rato_cavalo = distancia_euclidiana(vetor_ratos, vetor_cavalos)
supremum_rato_cavalo = distancia_supremum(vetor_ratos, vetor_cavalos)
cosseno_rato_cavalo = similaridade_cossena(vetor_ratos, vetor_cavalos)

#Rato e Hamster
manhattan_rato_hamster = distancia_manhattan(vetor_ratos, vetor_hamster)
euclidiano_rato_hamster = distancia_euclidiana(vetor_ratos, vetor_hamster)
supremum_rato_hamster = distancia_supremum(vetor_ratos, vetor_hamster)
cosseno_rato_hamster = similaridade_cossena(vetor_ratos, vetor_hamster)

#Cavalo e Hamster
manhattan_cavalo_hamster = distancia_manhattan(vetor_cavalos, vetor_hamster)
euclidiano_cavalo_hamster = distancia_euclidiana(vetor_cavalos, vetor_hamster)
supremum_cavalo_hamster = distancia_supremum(vetor_cavalos, vetor_hamster)
cosseno_cavalo_hamster = similaridade_cossena(vetor_cavalos, vetor_hamster)

print("=== Rato e Cavalo ===")
print(f">> Distância Manhattan: {manhattan_rato_cavalo}")
print(f">> Distância Euclidiana: {euclidiano_rato_cavalo}")
print(f">> Distância Supremum: {supremum_rato_cavalo}")
print(f">> Similaridade do Cosseno: {cosseno_rato_cavalo}")

print("\n=== Rato e Hamster ===")
print(f">> Distância Manhattan: {manhattan_rato_hamster}")
print(f">> Distância Euclidiana: {euclidiano_rato_hamster}")
print(f">> Distância Supremum: {supremum_rato_hamster}")
print(f">> Similaridade do Cosseno: {cosseno_rato_hamster}")

print("\n=== Cavalo e Hamster ===")
print(f">> Distância Manhattan: {manhattan_cavalo_hamster}")
print(f">> Distância Euclidiana: {euclidiano_cavalo_hamster}")
print(f">> Distância Supremum: {supremum_cavalo_hamster}")
print(f">> Similaridade do Cosseno: {cosseno_cavalo_hamster}")