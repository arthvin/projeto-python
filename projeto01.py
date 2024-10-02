def sequencia(limit):
    fib_sequencia = [0, 1]
    while fib_sequencia[-1] < limit:
        fib_sequencia.append(fib_sequencia[-1] + fib_sequencia[-2])
    return fib_sequencia

def is_in_fibonacci(num):
    fib_sequencia = sequencia(num)
    if num in fib_sequencia:
        return f'O número {num} pertence à sequência de Fibonacci.'
    else:
        return f'O número {num} NÃO pertence à sequência de Fibonacci.'

numero = int(input("Informe um número: "))
print(is_in_fibonacci(numero))