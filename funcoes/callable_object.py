class Potencia:
    def __init__(self, expoente):
        self.expoente = expoente

    def __call__(self, base):
        return base ** self.expoente  # Agora o objeto pode ser chamado

    def __str__(self):
        return f"Potência de {self.expoente}"

if __name__ == '__main__':
    potencia = Potencia(7)
    cubo = Potencia(3)

    print(potencia)  # Vai imprimir "Potência de 7"
    print(potencia(2))  # Vai imprimir 2⁷ = 128
    print(cubo(2))  # Vai imprimir 2³ = 8
