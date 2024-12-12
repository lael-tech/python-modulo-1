# entrada 
valor = int(input("Digite o valor: "))

# processamento
notas100 = valor // 100
valor = valor % 100
notas50 = valor // 50
valor = valor % 50
notas20 = valor // 20
valor = valor % 20
notas10 = valor // 10
valor = valor % 10
notas5 = valor // 5
valor = valor % 5
notas1 = valor // 1
valor = valor % 1 

# saida
print(f"{notas100} nota(s) de R$100,00")
print(f"{notas50} nota(s) de R$50,00")
print(f"{notas20} nota(s) de R$20,00")
print(f"{notas10} nota(s) de R$10,00")
print(f"{notas5} nota(s) de R$5,00")
print(f"{notas1} nota(s) de R$1,00")