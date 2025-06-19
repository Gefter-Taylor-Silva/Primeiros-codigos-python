saldo = 1000

while True:
    print(f"\nMenu de Seleção")
    print(f"\nOpção 1: Ver Saldo")
    print(f"Opção 2: Sacar Dinheiro")
    print(f"Opção 3: Depositar Dinheiro")
    print(f"Opção 4: Sair do Programa")

    opcao = input(f"\nEscolha a Opção: ")
    if opcao == "1":
       print(f"\nSeu Saldo é de: R$ {saldo:.2f}")
    
    elif opcao == "2":
         saque = float(input(f"\nDe quanto é o seu saque? "))
         if saque > saldo:      
           print(f"\nSaldo insuficiente!")
         else:
           saldo -= saque
           print(f"\nSeu saque é de: R$ {saque:.2f}")
       
    elif opcao  == "3":
        deposito = float(input(f"\nFaça o seu depósito:"))
        saldo += deposito
        print(f"Seu deposito foi de: R$ {deposito:.2f},  seu saldo agora é de R$ {saldo:.2f}") 
        
    elif opcao == "4":
        print(f"\nSeu programa foi encerrado!")
        break 
    else:
        print(f"Opção inválida!")    
        
        
