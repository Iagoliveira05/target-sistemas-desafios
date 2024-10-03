def verificarFibonacci(numeroDesejado):
    if (numeroDesejado < 0):
        print(f"O número {numeroDesejado} NÃO pertence a sequência!")
    elif (numeroDesejado <= 3):
        print(f"O número {numeroDesejado} pertence a sequência!")
    else:
        resultado = 0
        numeroAtual = 1
        numeroAnterior = 0
        for i in range(0, numeroDesejado+1):
            resultado = numeroAtual + numeroAnterior
            numeroAnterior = numeroAtual
            numeroAtual = resultado

            if (resultado == numeroDesejado):
                print(f"O número {numeroDesejado} pertence a sequência!")
                return

        print(f"O número {numeroDesejado} NÃO pertence a sequência!")

        

numero = int(input("Digite um número: "))
pertenceFibonacci = verificarFibonacci(numero)
