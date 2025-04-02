class Carro:
    def __init__(self, valocidade_max):
        self.velocidade_max = valocidade_max
        self.velocidade_atual = 0
        self.velocidade_min = 0

    def acelerar(self, delta=5):
        if delta <= self.velocidade_max:
            if delta > self.velocidade_max:
                return f'A velocidade atual do carro é {self.velocidade_max}'
            self.velocidade_atual += delta


    def freiar(self, delta=10):
        if self.velocidade_atual > self.velocidade_min:
            self.velocidade_atual -= delta
            return f'A velocidade atual do carro é {self.velocidade_atual}'
        return f'A velocidade atual do carro é {self.velocidade_min}'



if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(20):
        print(c1.acelerar(8))

    for _ in range(10):
        print(c1.freiar(delta=20))
