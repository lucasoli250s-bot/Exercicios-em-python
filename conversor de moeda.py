real = float(input("Digite quantos reais você tem na carteira: R$ "))

dolar = real / 5.12 #Para converter a Moeda locar para outro , é apenas pegar o valor da moeda e dividor pela cotação.

print("Com R${:.2f} você pode comprar US${:.2f}".format(real, dolar))
