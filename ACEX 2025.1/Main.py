#oooooooooooooooooooooooooooooooooo CLASSE PARA TESTE DE FUNÇÕES CRIADAS E GRÁFICOS ooooooooooooooooooooooooooooooooooooooooo
from Matematica import Matematica
import matplotlib.pyplot as plt
import numpy as np
# import random


# --------- Exemplos usados -------------
# dados = [84, 68, 30, 52, 47, 73, 68, 61, 73, 77, 74, 71, 81, 91, 39, 69, 89, 98, 42, 54]
# dados.sort()
# lista = [7.5 , 8.0 , 6.5 ,9.0 , 10 , 15 , 18, 20 , 25]
# valores_unicos = list(set(dados))
# probabilidades = [Matematica.probabilidade(dados, val) for val in valore_unicos]
# valorAleatorio1 = random.randint(1, 10)
# valorAleatorio2 = random.randint(1, 10)


# ------------- Probabilidade para eventos simples e compostos ----------------
# print("A probabilidade do número ", valorAleatorio1, " sair na lista é de ",
#         Matematica.probabilidade(lista, valorAleatorio1))
# print("A probabibidade do númeor ", valorAleatorio1, " e do número ",
#        valorAleatorio2, "saírem na lista é de ", 
#        Matematica.probabilidadeComp(lista, valorAleatorio1, valorAleatorio2))


# ----------- Medidas de tendência central ----------
# print(Matematica.media(lista))
# print(Matematica.mediana(lista))
# print(Matematica.moda(lista))


# ------------- Medidas de dispersão -------------
# print(Matematica.amplitudeTotal(lista))
# print(Matematica.variancia(lista))
# print(Matematica.desvioPadrao(lista))
# print(Matematica.coenficienteVariacao(lista))


# --------- Gráfico de Pizza ------------
# plt.pie(probabilidades, labels=valores_unicos, autopct='%1.1f%%')
# plt.title("Probabilidades")
# plt.show()


# --------- Gráfico de barra --------------
# plt.bar(valores_unicos, probabilidades, color='skyblue', edgecolor='black')
# plt.title("Probabilidade de cada valor")
# plt.xlabel("Valores")
# plt.ylabel("Probabilidade")
# plt.show()


# -------------- Histograma ----------------- nao mt eficiente
# plt.hist(lista, bins=10, color='yellow', edgecolor='green')
# plt.title("Distribuição de Frequência (Histograma)")
# plt.xlabel("Valores")
# plt.ylabel("Frequência")
# plt.show()


# ----------- Gráfico de linhas -------------- 
# plt.plot(dados, marker='o', label='Dados')
# plt.axhline(y=Matematica.media(dados), color='red', linestyle='--', label=f'Média: {Matematica.media(dados):.2f}')
# plt.axhline(y=Matematica.mediana(dados), color='green', linestyle='--', label=f'Mediana: {Matematica.mediana(dados):.2f}')
# plt.axhline(y=Matematica.moda(dados), color='yellow', linestyle='--', label=f'Moda: {Matematica.moda(dados):.2f}')
# plt.title("Dados com linha da média")
# plt.legend()
# plt.show()


# --------- Questão 3 lista 1 ----------------
# tamanhos = [38, 40, 39, 38, 41, 39, 38]
# maisRepetido = 0
# maior = 0
# for tamanho in tamanhos:
#     quantidade = 0
#     for tam in tamanhos:
#         if tamanho == tam:
#             quantidade += 1
#     if quantidade > maior:
#         maior = quantidade
#         maisRepetido = tamanho
# print(f"O número de calçado mais usado é {maisRepetido}!")    

# --------------- Questão 7 - lista 1 -----------------
# Evento Composto (Lançamento de Dados): 
# Ao lançar um dado justo de 6 faces (numeradas de 1 a 6), 
# qual é a probabilidade de obter um número par E maior que 3?
# possibilidade = [1, 2, 3, 4, 5, 6]
# favoraveis = []
# for numero in possibilidade:
#     if numero%2 == 0 and numero>3:
#         favoraveis.append(numero)
# probabilidade = (len(favoraveis)/len(possibilidade))*100
# print(f"A probabilidade de sair um número par e maior que 3 é de {probabilidade:.2f}%")


#-------- Questão 5 lista 2 ---------------------
# from collections import Counter
# idades = [22, 25, 22, 30, 28, 25, 22, 35, 28, 25]

# # Calcular a frequência para identificar as idades mais frequentes
# contagem_idades = Counter(idades)
# maior_freq = max(contagem_idades.values())
# idades_mais_frequentes = [idade for idade, freq in contagem_idades.items() if freq == maior_freq]
# print(f"As idades mais frequentes são: {idades_mais_frequentes}")

# plt.figure(figsize=(8, 5))
# plt.hist(idades, bins=np.arange(min(idades), max(idades) + 2, 2), edgecolor='black', alpha=0.7)
# plt.title('Distribuição de Idades')
# plt.xlabel('Idade')
# plt.ylabel('Frequência')
# plt.xticks(np.arange(min(idades), max(idades) + 1, 2)) # Ajusta os rótulos do eixo x
# plt.grid(axis='y', alpha=0.75)
# plt.show()