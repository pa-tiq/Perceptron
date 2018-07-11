
import random

class Perceptron:

    def __init__(self, amostras, saidas, taxa_aprendizado=0.1, epocas=1000, limiar=-1):
        self.amostras = amostras
        self.saidas = saidas
        self.taxa_aprendizado = taxa_aprendizado
        self.epocas = epocas
        self.limiar = limiar
        self.n_amostras = len(amostras)
        self.n_atributos = len(amostras[0])
        self.pesos = []
    
    def treinar(self):
    
        for amostra in self.amostras:
            amostra.insert(0, -1)
    
        for i in range(self.n_atributos):
            self.pesos.append(random.random())
    
        self.pesos.insert(0, self.limiar)
        n_epocas = 0 # contador de épocas\n"
    
        while True:    
            erro = False # erro inicialmente inexiste\n"    
            for i in range(self.n_amostras):
                u = 0
                for j in range(self.n_atributos + 1):
                    u += self.pesos[j] * self.amostras[i][j]
                y = self.sinal(u) # obtém a saída da rede\n"    
                # verifica se a saída da rede é diferente da saída desejada\n"
                if y != self.saidas[i]:
                # calcula o erro\n",
                    erro_aux = self.saidas[i] - y
                    # faz o ajuste dos pesos para cada elemento da amostra\n"
                    for j in range(self.n_atributos + 1):
                        self.pesos[j] = self.pesos[j] + self.taxa_aprendizado * erro_aux * self.amostras[i][j]
                    erro = True # o erro ainda existe\n"    
                n_epocas += 1 # incrementa o número de épocas\n"    
                # critério de parada\n",
                if not erro or n_epocas > self.epocas:
                    break

#não sei se a identação tá certa
"\t\twhile True:\n",
    "\n",
    "\t\t\terro = False # erro inicialmente inexiste\n",
    "\n",
    "\t\t\tfor i in range(self.n_amostras):\n",
    "\t\t\t\tu = 0\n",
    "\t\t\t\tfor j in range(self.n_atributos + 1):\n",
    "\t\t\t\t\tu += self.pesos[j] * self.amostras[i][j]\n",
    "\t\t\t\ty = self.sinal(u) # obtém a saída da rede\n",
    "\n",
    "\t\t\t\t# verifica se a saída da rede é diferente da saída desejada\n",
    "\t\t\t\tif y != self.saidas[i]:\n",
    "\t\t\t\t\t# calcula o erro\n",
    "\t\t\t\t\terro_aux = self.saidas[i] - y\n",
    "\t\t\t\t\t# faz o ajuste dos pesos para cada elemento da amostra\n",
    "\t\t\t\t\tfor j in range(self.n_atributos + 1):\n",
    "\t\t\t\t\t\tself.pesos[j] = self.pesos[j] + self.taxa_aprendizado * erro_aux * self.amostras[i][j]\n",
    "\t\t\t\t\terro = True # o erro ainda existe\n",
    "\n",
    "\t\t\tn_epocas += 1 # incrementa o número de épocas\n",
    "\n",
    "\t\t\t# critério de parada\n",
    "\t\t\tif not erro or n_epocas > self.epocas:\n",
    "\t\t\t\tbreak\n",

    def teste(self, amostra):
        amostra.insert(0, -1)
        u = 0
        for i in range(self.n_atributos + 1):
            u += self.pesos[i] * amostra[i]
            y = self.sinal(u)
            print('Classe: %d' % y)

    def degrau(self, u):
        if u >= 0:
            return 1
        return 0

    def sinal(self, u):
        if u >= 0:
            return 1
        return -1