#Exercício 1 - Apresentação personalizada
#Peça nome e cidade e exiba uma frase de apresentação.
nome = input("Qual o seu nome? ")
cidade = input("Qual a sua cidade? ")
print(nome, cidade)

#Exercício 2 - Segundos em minutos e segundos
#Peça ao usuário para digitar uma quantidade inteira de segundos e converta para minutos e segundos.
segundos = int(input("Digite a quantidade de segundos: "))
print(f"{segundos//60} Minutos e {segundos%60} Segundos")

#Exercício 3 - Contando letras e caracteres
#Peça uma frase e conte:
#total de caracteres
#quantidade de 'a' (maiúsculo/minúsculo)
frase = input("Digite uma frase: ")
total_car = len(frase)
total_mai = frase.count("A")
total_min = frase.count("a")
print(f"Total de caracteres: {total_car}\nTotal Maiusculo: {total_mai}\nTotal Minúsculo: {total_min}")