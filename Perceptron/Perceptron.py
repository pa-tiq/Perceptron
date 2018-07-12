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
        self.n_saidas = len(saidas[0])
        self.pesos = []
 
    def treinar(self):        
 
        for amostra in self.amostras:
            amostra.insert(0, self.limiar)     
 
        for k in range(self.n_saidas): 
            del self.pesos[0:self.n_atributos]
            for i in range(self.n_atributos):
                self.pesos.append(random.random())    
            self.pesos.insert(0, self.limiar) 
            n_epocas = 0 # contador de épocas"
            while True:    
                erro = False # erro inicialmente inexiste"    
                for i in range(self.n_amostras):
                    u = 0
                    for j in range(self.n_atributos + 1):
                        u += self.pesos[j] * self.amostras[i][j]
                    y = self.sinal(u) # obtém a saída da rede"    
                    # verifica se a saída da rede é diferente da saída desejada"
                    if y != self.saidas[i][k]:
                    # calcula o erro",
                        erro_aux = self.saidas[i][k] - y
                        # faz o ajuste dos pesos para cada elemento da amostra"
                        for j in range(self.n_atributos + 1):
                            self.pesos[j] = self.pesos[j] + self.taxa_aprendizado * erro_aux * self.amostras[i][j]
                        erro = True # o erro ainda existe"  
 
                n_epocas += 1 # incrementa o número de épocas"    
                # critério de parada",
                if not erro or n_epocas > self.epocas:
                    break 
 
    def teste(self, amostra):
        amostra.insert(0, self.limiar)        
        y = []
        for i in range(self.n_saidas):
            u = 0
            for i in range(self.n_atributos + 1):
                u += self.pesos[i] * amostra[i]
            y.append(self.sinal(u))
        for k in range(len(y)):    
            print('Classe na posição', k+1,' : ',y[k])
 
    def sinal(self, u):
        if u >= 0:
            return 1
        return -1


amostras = [[1, 1, 1], [1, 1, 0], [1, 0, 1], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
saidas = [[1,1], [1,1], [1,-1], [1,-1], [-1,1], [-1,1], [-1,-1], [-1,-1]]
rede = Perceptron(amostras, saidas)
rede.treinar()
rede.teste([0, 1, 0])
