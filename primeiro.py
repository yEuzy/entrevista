def fibonacci(numero):
    num1 = 0
    num2 = 1
    fibonacci = []
    for i in range(numero + 1):
        
        fibonacci.append(num1)
        num1, num2 = num2, num1 + num2
    return fibonacci

num = int(input("Digite um numero para saber se esta presente na sequência de Fibonacci: "))

fibo = fibonacci(num)

if num in fibo:
    print(f"O numero {num} pertence a sequencia de Fibonacci")
