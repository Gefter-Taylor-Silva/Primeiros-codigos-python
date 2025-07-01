palavra = input(f"Escreva uma palavra para ela ser verificada: ")

vogais = "aeiouAEIOU"
vogais_encontradas = []

for letras in palavra: 
    if letras in vogais:
        vogais_encontradas.append(letras)
    
quantidade = len(vogais_encontradas)   
print(f" Existem {quantidade} vogais na palavra, {palavra}:")
print("São elas:", ", ".join(vogais_encontradas))
