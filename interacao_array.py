"""readme: interação como array para buscar o valor maximo e mino da metade do array até a ulitma posição do array"""
def quantidade_numero():
    quat_num = int(input('quantos numeros pretende digitar: '))
    numero_array = []
    numero_elementos = 0
    entrada_numeros(quat_num, numero_array, numero_elementos)

def entrada_numeros(quat_num, numero_array, numero_elementos):
    while quat_num != 0:
        numero = int(input('Digite o numero: '))
        numero_array.append(numero)
        numero_elementos = numero_elementos +1
        quat_num = quat_num -1
        
    mostrar_elementos(numero_elementos, numero_array)

def mostrar_elementos(numero_elementos, numero_array):
    elemento_max = int(numero_elementos)
    metade_elementos = int(numero_elementos/2)
    print('O elemento maximo da metade do Array é {}'.format(max(numero_array[metade_elementos : elemento_max ])))
    print('O elemento minímo da metade do Array é {}'.format(min(numero_array[metade_elementos : elemento_max ])))

quantidade_numero()