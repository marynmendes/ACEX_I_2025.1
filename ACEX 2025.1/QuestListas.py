#--------------Lista 1---------------
# Q1.
notas = [7.5, 8.0, 6.5, 9.0]
media = sum(notas) / len(notas)
print(f"A média das notas é: {media}")
# Ou usando numpy:
# import numpy as np
# media_np = np.mean(notas)
# print(f"A média das notas (numpy) é: {media_np}")

# Q2.
import numpy as np # Importar a biblioteca numpy
dados = [15, 20, 10, 25, 18]
mediana = np.median(dados)
print(f"A mediana dos dados é: {mediana}")

# Q3.
import Matematica
numeros_calcado = [38, 40, 39, 38, 41, 39, 38]
print(f"A moda entre os números de claçado é: {Matematica.moda(numeros_calcado)}")

# Q4.
bolas_vermelhas = 5
total_bolas = 5 + 3 + 2
probabilidade_vermelha = bolas_vermelhas / total_bolas
print(f"A probabilidade de ser vermelha é: {probabilidade_vermelha:.2f}")

# Q5.
bolas_azuis = 3
bolaA = 3
bolaVd = 2
total = 5 + 3 + 2
probabilidadeAouV = (bolaA + bolaVd)/total
print(f"A probabilidade de sair uma bola azul ou verde é de: {(probabilidadeAouV*100):.2f}%")

# Q6.
precos = [25.00, 15.00, 30.00, 20.00, 15.00]
print(f"A média dos preços é de: {media(precos)}")
print(f"A mediana dos preços é: {mediana(precos)}")

# Q7.
dado = [1, 2, 3, 4, 5, 6]
resultadosFavoraveis = []
for numero in dado:
    if numero>3 and numero%2 == 0:
        resultadosFavoraveis.append(numero)

probabilidade = len(resultadosFavoraveis)/len(dado)
print(f"A probabilidade de sair um número par e maior que 3 é: {(probabilidade*100):.2f}%")

#-------------Lista 2----------------
# Q5.
import matplotlib.pyplot as plt
import numpy as np # Para calcular a frequência
from collections import Counter

idades = [22, 25, 22, 30, 28, 25, 22, 35, 28, 25]

# Calcular a frequência para identificar as idades mais frequentes
contagem_idades = Counter(idades)
maior_freq = max(contagem_idades.values())
idades_mais_frequentes = [idade for idade, freq in contagem_idades.items() if freq == maior_freq]
print(f"As idades mais frequentes são: {idades_mais_frequentes}")

plt.figure(figsize=(8, 5))
plt.hist(idades, bins=np.arange(min(idades), max(idades) + 2, 2), edgecolor='black', alpha=0.7)
plt.title('Distribuição de Idades')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.xticks(np.arange(min(idades), max(idades) + 3, 2)) # Ajusta os rótulos do eixo x
plt.grid(axis='y', alpha=0.75)
plt.show()

# Q6.
import matplotlib.pyplot as plt

frutas = ['Maçã', 'Banana', 'Laranja', 'Uva']
quantidades = [40, 30, 20, 10]
cores = ['#ff9999','#66b3ff','#99ff99','#ffcc99'] # Cores amigáveis

# explode = (0.1, 0, 0, 0) # Opcional: "explode" a fatia da Maçã

plt.figure(figsize=(8, 8))
plt.pie(quantidades, labels=frutas, autopct='%1.1f%%', startangle=90, colors=cores) # autopct para porcentagens
plt.title('Preferência de Frutas')
plt.axis('equal') # Garante que o gráfico de pizza seja um círculo.
plt.show()

# Q7.
import numpy as np

salarios = [2500, 3000, 2200, 3500, 2800]

amplitude_salarios = max(salarios) - min(salarios)
desvio_padrao_salarios = np.std(salarios, ddof=1) # ddof=1 para desvio padrão amostral

print(f"A amplitude total dos salários é: R$ {amplitude_salarios:.2f}")
print(f"O desvio padrão dos salários da amostra é: R$ {desvio_padrao_salarios:.2f}")

#-----------------Exemplos--------------
import matplotlib.pyplot as plt 
import random
#Histograma
idades = [random.randint(10, 60) for _ in range(50)]

bins = [10, 20, 30, 40, 50, 60]

plt.hist(idades, bins = bins, edgecolor = 'black', alpha = 0.7)

plt.title("Distribuição de idades")
plt.xlabel("idades")
plt.ylabel("Quantidade de pessoas")

plt.grid(axis='y', alpha=0.75)

print(idades)
plt.show()

#Gráfico de pizza
atividades = ['Aulas', 'Intervalo', 'Almoço', 'Estudos livres', 'Deslocamento', 'Lazer', 'Dormir', 'Estágio']
tempo = [5, 1, 1, 2, 1, 2, 8, 4]
cores = ['skyblue', 'lightgreen', 'gold', 'lightcoral', 'plum', 'orange', 'red', 'pink']

plt.pie(tempo, labels=atividades, autopct='%1.1f%%', startangle=90, colors=cores)
plt.title("Distribuição de tempo no dia")
plt.show()


