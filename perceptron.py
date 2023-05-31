import random
import copy
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np


class Perceptron:
    def __init__(
        self,
        amostras_n,
        saidas,
        taxa_aprendizado=0.1,
        epocas=1000,
        limiar=-0.8649,
        pesos=[0.3092, 0.3129],
    ):
        self.amostras = amostras_n
        self.saidas = saidas
        self.taxa_aprendizado = taxa_aprendizado
        self.epocas = epocas
        self.limiar = limiar
        self.n_amostras = len(amostras)
        self.n_atributos = len(amostras[0])
        self.pesos = pesos

    def treinar(self):
        for amostra in self.amostras:
            amostra.insert(0, self.limiar)

        for i in range(self.n_atributos):
            self.pesos.append(random.random())

        # self.pesos.insert(0, self.limiar)
        n_epocas = 0  # contador de épocas\n"

        while True:
            erro = False  # erro inicialmente inexiste\n"
            for i in range(self.n_amostras):
                u = 0
                for j in range(self.n_atributos + 1):
                    u += self.pesos[j] * self.amostras[i][j]
                y = self.sinal(u)  # obtém a saída da rede\n"
                # verifica se a saída da rede é diferente da saída desejada\n"
                if y != self.saidas[i]:
                    # calcula o erro\n",
                    erro_aux = self.saidas[i] - y
                    # faz o ajuste dos pesos para cada elemento da amostra\n"
                    for j in range(self.n_atributos + 1):
                        self.pesos[j] = (
                            self.pesos[j]
                            + self.taxa_aprendizado * erro_aux * self.amostras[i][j]
                        )
                    erro = True  # o erro ainda existe\n"

            n_epocas += 1  # incrementa o número de épocas\n"
            # critério de parada\n",
            if not erro or n_epocas > self.epocas:
                break

    def teste(self, amostra):
        amostra.insert(0, -1)
        u = 0
        for i in range(self.n_atributos + 1):
            u += self.pesos[i] * amostra[i]
        y = self.sinal(u)
        print("Classe: %d" % y)

    def sinal(self, u):
        if u >= 0:
            return 1
        return -1

    def graph(self, formula, x_range):
        a = np.array(x_range)
        y = formula(a)  # <- note now we're calling the function 'formula' with x
        plt.plot(a, y / np.linalg.norm(y))

    def plot(self, x, y):
        plt.figure(figsize=(7, 5))
        self.graph(
            lambda a: +(
                (-(self.limiar / self.pesos[1]) / (self.limiar / self.pesos[0])) * a
                + (-self.limiar / self.pesos[1])
            ),
            range(-10, 10),
        )
        plt.plot(x, y, "ro")
        plt.show()


# Exemplo
amostras = [[1, 1], [1, 0], [0, 1], [0, 0]]
saidas = [[1], [1], [1], [0]]

for j in range(len(saidas[0])):
    saidas_rede = []
    amostras_n = copy.deepcopy(amostras)
    for i in range(len(saidas)):
        saidas_rede.append(saidas[i][j])
    print("amostras_n: ", amostras_n)
    print("saidas_rede: ", saidas_rede)
    rede = Perceptron(amostras_n, saidas_rede)
    rede.treinar()

rede.teste([0, 0])
rede.teste([0, 1])
rede.teste([1, 0])
rede.teste([1, 1])
rede.plot(amostras, saidas)
del rede
del saidas_rede
del amostras_n
