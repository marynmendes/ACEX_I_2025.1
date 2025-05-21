# from Matematica import Matematica
# import matplotlib.pyplot as plt
# # import random


#--------- Exemplos usados -------------
# dados = [1, 2, 3, 4, 5, 5]
# lista = [3, 4, 5, 2, 9, 2]
# probabilidades = [Matematica.probabilidade(dados, val) for val in valores_unicos]
# valores_unicos = list(set(dados))
# valorAleatorio1 = random.randint(1, 10)
# valorAleatorio2 = random.randint(1, 10)


#------------- Probabilidade para eventos simples e compostos ----------------
# print("A probabilidade do número ", valorAleatorio1, " sair na lista é de ",
#         Matematica.probabilidade(lista, valorAleatorio1))
# print("A probabibidade do númeor ", valorAleatorio1, " e do número ",
#        valorAleatorio2, "saírem na lista é de ", 
#        Matematica.probabilidadeComp(lista, valorAleatorio1, valorAleatorio2))


#----------- Medidas de tendência central ----------
# print(Matematica.media(lista))
# print(Matematica.mediana(lista))
# print(Matematica.moda(lista))


#------------- Medidas de dispersão -------------
# print(Matematica.amplitudeTotal(lista))
# print(Matematica.variancia(lista))
# print(Matematica.desvioPadrao(lista))
# print(Matematica.coenficienteVariacao(lista))


#--------- Gráfico de Pizza ------------
# plt.pie(probabilidades, labels=valores_unicos, autopct='%1.1f%%')
# plt.title("Probabilidades")
# plt.show()


#--------- Gráfico de barra --------------
# plt.bar(valores_unicos, probabilidades, color='skyblue', edgecolor='black')
# plt.title("Probabilidade de cada valor")
# plt.xlabel("Valores")
# plt.ylabel("Probabilidade")
# plt.show()


#-------------- Histograma -----------------
# plt.hist(lista, bins=7, edgecolor='green')
# plt.title("Distribuição de Frequência (Histograma)")
# plt.xlabel("Valores")
# plt.ylabel("Frequência")
# plt.show()