print("Menu de Opções")
print("1-imposto")
print("2-novo salario")
print("3-Classificação")
novoSal=int(input("Digite o seu salario: "))
op=int(input("digite a opção desejada: "))
salario=int(input("Digite o seu salario: "))
imp=int(input("Digite o valor do imposto: "))
aum=int(input("Digite o aumento: "))
if op ==1:
    if salario<500:
        imp=salario*5/100
        if  500 and salario <= 850 :
            imp=salario*10/100
            if salario>850:
                imp=salario*15/100
                print(imp)

if op ==2:
    if salario>1500:
       aum =25
       if salario>= 750 and salario<=1500:
          aum=50
          if salario >=450 and salario<750:
             aum=75
             if salario<450:
                aum=100 ,novoSal<=salario+aum
                print(novoSal)            

if op ==3:
    if salario <= 700:
        print("Mal remunerado")
        if salario>700:
            print("Bem remunerado") 

if op<1 or op>3:
    print("Opção inválida")       






