import json
from datetime import datetime

tarefas = []

def carregar_tarefas():
    global tarefas
    try:
        with open("tarefas.json", "r", encoding="utf-8") as arquivo:
            tarefas = json.load(arquivo)
    except FileNotFoundError:
        tarefas = []
        
def salvar_tarefas():
    with open("tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)        

def adicionar_tarefas():
        descricao = input("Digite a tarefa: ")
        data_criacao = datetime.now().strftime("%d/%m/%Y %H:%M")
        tarefa = {
            "descricao": descricao,
            "data": data_criacao,
            "concluida": False
        }
        tarefas.append(tarefa)
        salvar_tarefas()
        print(f"Tarefa '{descricao}' adicionada com sucesso!")
        
def listar_tarefas():
        if not tarefas:
            print("Nenhuma tarefa encontrada!")
        else:
            print("\nLista de tarefas:")
            for i, tarefa in enumerate(tarefas, start=1):
                status = "✔️" if tarefa["concluida"] else "❌️"
                print(f"{i} - {tarefa['descricao']} ({tarefa['data']}) - {status}")
                
def concluir_tarefas():
        if not tarefas:
                print(f'Não há tarefas na lista')
        else:
                listar_tarefas()
                escolha = input(f'O número da tarefa que deseja concluir: ') 
                if escolha.isdigit():
                    escolha = int(escolha)
                    if 1 <= escolha <= len(tarefas):
                            tarefas[escolha - 1]["concluida"] = True
                            salvar_tarefas()
                            print(f"Tarefa '{tarefas[escolha - 1]['descricao']}' concluida com sucesso!!")
                    else:
                                print(f"Número inválido")
                else:
                     print(f'Digite um número válido.')  
                     
   
def editar_tarefas():
    if not tarefas:
        print("Não há tarefas para editar!")
    else:
        listar_tarefas()
        escolha = input("Digite o número da tarefa que deseja editar: ")
        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= len(tarefas):
                nova_tarefa = input("Digite a nova descrição da tarefa: ")
                tarefas[escolha - 1]["descricao"] = nova_tarefa
                salvar_tarefas()
                print(f"Tarefa editada com sucesso! Agora é: '{nova_tarefa}'")
            else:
                print("Número inválido.")
        else:
            print("Digite um número válido.")
                         
                         
def remover_tarefas():    
        if not tarefas:
            print("Nenhuma tarefa para remover!")
        else:
            print("\nLista de tarefas:")
            listar_tarefas()
            remover = input("Digite o número da tarefa que deseja remover: ")
            if remover.isdigit():
                remover = int(remover)
                if 1 <= remover <= len(tarefas):
                    removida = tarefas.pop(remover - 1)
                    salvar_tarefas()
                    print(f"Tarefa '{removida['descricao']}' foi removida!")
                else:
                    print("Número inválido.")
            else:
                print("Digite um número válido.")   
                
def encerrar_programa():               
            print("Saindo do programa...")

carregar_tarefas()

print("\nMENU DE OPÇÕES\n")
print("Opção 1: Adicionar tarefas")
print("Opção 2: Listar as tarefas")
print("Opção 3: Remover tarefas")
print("Opção 4: Concluir tarefas")
print("Opção 5: Editar tarefas")
print("Opção 6: Sair do programa\n")

while True:
    opcao = input("Escolha uma das opções: ")
    if opcao == "1":
       adicionar_tarefas()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        remover_tarefas()
    elif opcao == "4":
        concluir_tarefas()
    elif opcao == "5":
        editar_tarefas()
    elif opcao == "6":
        encerrar_programa()
        break
    else:
        print("Nenhum valor válido foi digitado!")
