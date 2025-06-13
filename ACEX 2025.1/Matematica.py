class Matematica:
   # Classe demostração de funcionamento da numpy
   
   @staticmethod
   def media(lista):
      soma = 0
      n = len(lista)
      for valor in lista:
         soma += valor
      media = soma/n
      return media
   
   @staticmethod
   def mediana(lista):
      lista.sort()
      n = len(lista)
      meio = n // 2
      if n % 2 == 0:
        return (lista[meio] + lista[meio - 1]) / 2
      else:
        return lista[meio]
      
   @staticmethod
   def probabilidade(lista, elemento):
      quantidade = 0
      n = len(lista)
      for valor in lista:
         if valor == elemento:
            quantidade += 1
      return quantidade/n
   
   @staticmethod
   def probabilidadeComp(lista, elemento1, elemento2):
      return Matematica.probabilidade(lista, elemento1) * Matematica.probabilidade(lista, elemento2)
   
   @staticmethod
   def moda(lista):
      moda = 0
      repete = 0
      for valor in lista:
         quantidade = 0
         for elemento in lista:
            if valor == elemento:
               quantidade += 1
         if quantidade > repete:
            repete = quantidade
            moda = valor
      return moda

   @staticmethod
   def amplitudeTotal(lista):
      lista.sort()
      n = len(lista)
      return lista[n-1]-lista[0]
   
   @staticmethod
   def variancia(lista):
      lista.sort()
      n = len(lista)
      soma = 0
      for valor in lista:
         soma += (valor - Matematica.media(lista))**2
      return soma/(n-1)
   
   @staticmethod
   def desvioPadrao(lista):
      return (Matematica.variancia(lista))**0.5
   
   @staticmethod
   def coenficienteVariacao(lista):
      return (Matematica.desvioPadrao(lista)/Matematica.media(lista))*100
