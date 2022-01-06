# Tuplas

# Você recebe coordenadas de 2 pontos e precisa encontrar
# a distância em linha reta entre eles.

# As coordenadas são fornecidas em uma tupla, por exemplo:

# p = (8, 11)

# O primeiro valor representa a coordenada x, enquanto o
# segundo valor representa a coordenada y do ponto p.

# Complete o código fornecido para calcular e produzir o
# distância entre os dois pontos dados.
# A distância linear é a raiz quadrada do quadrado de
# a distância horizontal mais o quadrado da vertical
# distância entre dois pontos.

# A função math.sqrt () pode ser usada para calcular o
# raiz quadrada.

import math

p1 = (23, -88)
p2 = (6, 42)

# your code goes here
distanceX = p1[0] - p2[0]
distanceY = p1[1] - p2[1]

horizontalDistance = distanceX * distanceX
verticalDistance = distanceY * distanceY

linearDistance = math.sqrt(horizontalDistance + verticalDistance)
print(linearDistance)
