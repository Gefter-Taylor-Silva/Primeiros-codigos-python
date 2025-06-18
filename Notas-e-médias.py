print(f"Nota dos alunos: ")

lista = []
while True:
    nota = input(f"Digite a nota: ")
    if nota.lower() == "c":
       break
    else:   
        try:
            nota = float(nota)
            lista.append(nota)
        except ValueError:
            print(f"Erro!! Digite um número ou calcular para encerrar")
if len(lista) > 0:
    media = sum(lista) / len(lista)        
    print(f"Esta é a lista de notas:")
    for i, nota in enumerate(lista, start=1):
        print(f"Aluno: {i} - {nota}")  
    print(f"A média dos alunos é: {media}") 
else:
    print(f"Nenhu valor foi digitado")
