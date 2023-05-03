class PerceptronSimples:
    def __init__(self):
        self.pesos = [-0.3, 0.3]
        self.taxa_aprendizado = 0.2
        self.bias = -0.2

    def funcao_ativacao(self, soma_ponderada: float):
        # Função step
        return 1 if soma_ponderada >= 0 else -1

    def executar(self, entrada: list):
        soma_ponderada = sum(e * p for e, p in zip(entrada, self.pesos))

        return self.funcao_ativacao(soma_ponderada + self.bias)

    def alterar_pesos(self, entrada: list, erro: float):
        for i in range(len(self.pesos)):
            self.pesos[i] += self.taxa_aprendizado * erro * entrada[i]

        self.bias += self.taxa_aprendizado * erro

    def treinar(self, entradas: list, saidas_esperadas: list):
        terminou = False
        while not terminou:
            terminou = True
            for entrada, saida_esperada in zip(entradas, saidas_esperadas):
                saida_obtida = self.executar(entrada)

                if saida_esperada != saida_obtida:
                    terminou = False

                    erro = saida_esperada - saida_obtida

                    self.alterar_pesos(entrada, erro)


perceptron = PerceptronSimples()

entradas = [
    [-1, -1],
    [-1, 1],
    [1, -1],
    [1, 1]
]

# Porta lógica AND. É possível alterar essa lista para outras portas lógicas.
saidas_esperadas = [-1, -1, -1, 1]

perceptron.treinar(entradas, saidas_esperadas)

print(perceptron.executar([-1, -1]))
