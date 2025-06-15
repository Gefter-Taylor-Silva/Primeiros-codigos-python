numero1 = float(input("Entre com o primeiro valor: "))
numero2 = float(input("Entre com o segundo valor: "))

print("Escolha uma operação:")
print("[ + ] Soma")
print("[ - ] Subtração")
print("[ * ] Multiplicação")
print("[ / ] Divisão")

operador = input("Digite a operação desejada: ")

if operador == "+":
    resultado = numero1 + numero2
    print(f"A soma dos números é {resultado}")
elif operador == "-":
    resultado = numero1 - numero2
    print(f"A subtração dos números é {resultado}")
elif operador == "*":
    resultado = numero1 * numero2        
    print(f"A multiplicação dos números é {resultado}")
elif operador == "/":
    if numero2 == 0:
        print("Erro! Divisão por zero não é permitida.")
    else:
        resultado = numero1 / numero2
        print(f"A divisão dos números é {resultado}")
else:
    print("Erro! Operação inválida.")
