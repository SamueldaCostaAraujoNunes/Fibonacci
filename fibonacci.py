'''
Tabela de Fibonacci:
                  0
    1ª            1
    2ª    0+1=    1
    3ª    1+1=    2
    4ª    1+2=    3
    5ª    2+3=    5
    6ª    3+5=    8
    7ª    5+8=    13
    8ª    8+13=   21
    9ª    13+21=  34
'''
#https://sites.google.com/site/leonardofibonacci7/o-problema-dos-coelhos

def lerInt():#Função que retorna um numero natural maior que 1
    while True: #Enquanto o usuario não insere um valor válido, a função se repete.
        try:#Caso, a entrada de dado, for inválida, repete-se a solicitação de dados  
            entrada = int(input('Digite um numero natural > 1: '))
            if(entrada <= 0):
                raise NameError('NumberNegative')#Caso, o número for negativo, um erro é induzido.
            return entrada #retorna o número.
        except:
            print('Número inválido!!')

#Sem Recursão
def fibonacci(n):
    fibo = 1
    anterior = 0
    for contador in range(2, n+1):
        temporario = fibo #Guarda o valor de fibonacci, numa variavel auxiliar.
        fibo = fibo + anterior #Incrementa o valor do antecessor, a fibonnaci
        anterior = temporario #O valor anterior, passa a ser o valor de fibonacci, quando ele foi salvo nuam variavel auxiliar. 
    return fibo 

#Com Recursão
# def fibonacci(n): 
#     if (n == 0) or (n == 1):#Caso base, quando o valor passado por parametro for igual a 0 ou a 1, retorna-se seu proprio valor.
#         return n#Retorna 0 ou 1
#     else:#Caso, o parametro ainda não respeite o caso base.
#         return fibonacci(n-1) + fibonacci(n-2)#Retorna a soma do valor de fibonacci do seu antecessor, com o valor de fibonacci do antecessor do antecessor.

#Com Recursão e Dicionario
# cache = dict()#Cria um dicionario que guardará os resultados dos numeros já calculados para melhorar a perfomance.
# def fibonacci(n): 
#     aux = n

#     if aux in cache:#Verifica se este número já foi calculado anteriormente, para avaliar se é necessario calcular seu valor fibonacci novamente.
#         return cache[aux]#Existindo, o seu valor fibonacci é retornado

#     if (n == 0) or (n == 1):  #Caso pertença a um caso base, ele guarda o "n" em uma varival auxiliar.("Ans -> Answer")
#         ans = n
#     else:
#         ans = fibonacci(n-1) + fibonacci(n-2) #Caso não pertença a um caso base, ele faz uma chamada recursiva, guardando seu retorno na variavel "Ans"
#     cache[aux] = ans #A resposta é guardada no dicionario.

#     return ans    #E por fim, e retornado para o user.


#Programa Principal
# n = lerInt()
# print('Fibonacci de %d é %d.' % (n, fibonacci(n)))

#Testes
try:
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13
    assert fibonacci(8) == 21
    assert fibonacci(9) == 34
    assert fibonacci(10) == 55
    assert fibonacci(11) == 89
    assert fibonacci(12) == 144
    print("Passou em todos os testes!! A função de fibonacci funciona!")
except AssertionError:
    print("Não passou nos testes!! A sua função fibonacci, não funciona!")





