# Programa Cálculo Média de Consumo - Energia Elétrica de um Aparelho Doméstico
# Autora: Juliana de Lima Custódio

#Entrada de dados
nome = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho (em Watts): "))
tempo = float(input("Digite o tempo de uso diário do aparelho (em horas):"))

#Processamento
consumo_diario = (potencia * tempo) / 1000
consumo_mensal = consumo_diario * 30

#Saída de dados
print(f"O consumo diário do aparelho {nome} é de {consumo_diario:.2f}Kw/h")
print(f"O consumo mensal do aparelho {nome} é de {consumo_mensal:.2f}Kw/h")
print(f"O custo mensal do aparelho {nome} é de R${consumo_mensal * 0.75:.2f}")
print("Obrigado por utilizar nosso programa! Vamos economizar energia e cuidar do meio ambiente!")
