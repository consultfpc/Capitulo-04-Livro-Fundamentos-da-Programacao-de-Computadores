prevenda=int(input("Digite o valor de pré venda: "))
venda=int(input("Digite o valor das vendas: "))
pre=int(input("digite o valor do preço: "))
preAtual=int(input("digite o preço atual: "))

if venda<500 or pre<30:
    preAtual=pre+10/100*pre
    if (venda >= 500 and venda <1200) or (pre>=30 and pre<80):
        preAtual=pre+15/100*pre
        if venda >=1200 or pre>=80:
            preAtual=pre-20/100*pre
print(preAtual)