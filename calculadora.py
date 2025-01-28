preco_original = float(input("Digite o preço original do produto: "))
percentual = float(input("Digite o percentual de desconto: "))


desconto = preco_original * (percentual / 100)


preco_final = preco_original - desconto


print("O preço final após o desconto é: ", preco_final)