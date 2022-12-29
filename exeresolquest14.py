sal=int(input("Digite o su salrio: "))
novoSal=int(input("digite o novo sal: "))
boni=int(input("Digite o valor da bonificação: "))
aux=int(input("digite o valor do auxílio escolar: "))

if sal <= 500:
    boni=sal*5/100
    if sal <= 1200:
        boni=sal*12/100
        boni=0
        if sal<= 600:
            aux=150
            if aux==100:
                novoSal=sal+boni+aux
print(novoSal)
            