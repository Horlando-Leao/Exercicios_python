
# função: verifica se a entrada é uma sequência númerica simples
def ExisteSequenciaNumerica(sequencia):
#entrada = Array numeros #saída = Boleano
    quantidade_termos = len(sequencia) #quantidade de elementos
    todosElementos = [] # array de elementos, somente 0 e 1
    
    # interar sobre a paramento da função
    # primeiro FOR pega uma posição do array, começando pelo primeiro elemento.
    # depois o segundo FOR verifica outras posições no array (exceto a posição que está sendo usada pelo primeiro FOR)
    # somando +1 e -1 e comparando se é a algum elemento é a próxima sequência
    posicao1 = 0
    for termo in sequencia:
        termoAtual = (termo)
        
        posicao2 = 0
        for outrosTermos in sequencia:
            
            if(outrosTermos == termoAtual):
                if (posicao2  == posicao1):
                    print(".")
                    #A cada novo interação no primeiro primeiro loop, sempre terá um elemetno igual no segundo
                else:
                    todosElementos.append(0)
                    #há um elemento igual no array, então não é uma sequência, retorno será falso
            else:
                proximaSequencia = termoAtual + 1
                anteriorSequencia = termoAtual - 1
                if (proximaSequencia in sequencia or anteriorSequencia in sequencia):
                    todosElementos.append(1)
                    #há um elemento sequêncial
                else:
                    todosElementos.append(0)
                    #não há um elemento sequêncial retorno será falso
            posicao2 = posicao2 + 1
            
        posicao1 = posicao1 + 1
        

    if (0 in todosElementos):
        print("Não é uma sequência numerica simples")
        return False
        
    else:
        print("É uma sequência numerica simples")
        return True
    
                
#sequências para teste
sequencia_a = [1,2,3,4,5,6,7]
sequencia_b = [2,5,4,3,1]
sequencia_c = [1,2,3,1,4,5]
sequencia_d = [7,6,5,4,3,2,1]
sequencia_e = [2,1,5,2,4,3]


minhaSequencia = ExisteSequenciaNumerica(sequencia_a)
print(minhaSequencia)


