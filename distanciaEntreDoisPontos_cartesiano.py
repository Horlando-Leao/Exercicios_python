import math

cordernadaX_A = float(input("Posição de X para A: "))
cordernadaY_A = float(input("Posição de Y para A: "))

cordernadaX_B = float(input("Posição de X para B: "))
cordernadaY_B = float(input("Posição de Y para B: "))

#definindos pontos de a e b
pontoA = [cordernadaX_A,cordernadaY_A]
pontoB = [cordernadaX_B,cordernadaY_B]

#formula para calcular distância entre dois pontos no cartesiano, sem raiz
# distancia = √(x_b - x_a)² + (y_b - y_a)² 
distancia = math.sqrt( ( (pontoB[0] - pontoA[0]) ** 2) + ( (pontoB[1] - pontoA[1]) ** 2) )
print(distancia)



    
    

