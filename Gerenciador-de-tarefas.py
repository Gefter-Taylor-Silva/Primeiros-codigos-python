tarefas = []

print("\nMENU DE OPÇÕES\n")
print("Opção 1: Adicionar tarefas")
print("Opção 2: Listar as tarefas")
print("Opção 3: Remover tarefas")
print("Opção 4: Sair do programa\n")

while True:
    opcao = input("Escolha uma das opções: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)
        print(f"Tarefa '{tarefa}' adicionada com sucesso!")

    elif opcao == "2":
        if not tarefas:
            print("Nenhuma tarefa encontrada!")
        else:
            print("\nLista de tarefas:")
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i} - {tarefa}")

    elif opcao == "3":
        if not tarefas:
            print("Nenhuma tarefa para remover!")
        else:
            print("\nLista de tarefas:")
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i} - {tarefa}")
            remover = input("Digite o número da tarefa que deseja remover: ")
            if remover.isdigit():
                remover = int(remover)
                if 1 <= remover <= len(tarefas):
                    removida = tarefas.pop(remover - 1)
                    print(f"Tarefa '{removida}' foi removida!")
                else:
                    print("Número inválido.")
            else:
                print("Digite um número válido.")

    elif opcao == "4":
        print("Saindo do programa...")
        break

    else:
        print("Nenhum valor válido foi digitado!")
