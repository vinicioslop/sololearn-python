class Plano2D:
    def __init__(self, valorX, valorY):
        self.valorX = valorX
        self.valorY = valorY
        self.plano = []
        self.linhaX = []
        self.linhaY = []

        self.monta_plano()
        self.monta_guia()

    def monta_guia(self):
        auxX = self.valorX * -1
        auxY = self.valorY * -1

        while auxX <= self.valorX:
            self.linhaX.append(auxX)
            auxX += 1

        while auxY <= self.valorY:
            self.linhaY.append(auxY)
            auxY += 1

    def monta_plano(self):
        tempY = self.valorY
        while tempY >= self.valorY * -1:
            tempX = self.valorX * -1
            linha = []

            while tempX <= self.valorX:
                if tempX == 0 and not tempY == 0:
                    linha.append("|")
                elif tempY == 0 and not tempX == 0:
                    linha.append("-")
                elif tempX == 0 and tempY == 0:
                    linha.append("+")
                else:
                    linha.append(" ")
                tempX += 1

            self.plano.append(linha)
            tempY -= 1

    def adiciona_ponto(self, x, y):
        indiceX = self.linhaX.index(x)
        indiceY = self.linhaY.index(y)

        self.plano[indiceY][indiceX] = "*"

    def exibe_plano(self):
        for y in range(self.valorY * 2, 0, -1):
            linha = ""
            for x in range(0, self.valorX * 2):
                linha += str(self.plano[y][x])
            print(linha)


def main():
    print("Bem vindo ao gerador de Plano Cartesiano!")

    planoX = int(input("X: "))
    planoY = int(input("Y: "))

    plano = Plano2D(planoX, planoY)

    print("\nInforme um valor de X e Y para adicionar um ponto no plano")
    pontoX = int(input("X: "))
    pontoY = int(input("Y: "))

    plano.adiciona_ponto(pontoX, pontoY)
    plano.exibe_plano()


main()
