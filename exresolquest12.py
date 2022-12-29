cargo=int(input("Digite o novo cargo(1,2,3,4,5)"))
salario=int(input("Digite o novo salario: "))
 
if cargo==1:
    print("O cargo é escrituário")
    aumento=salario*50/100
    print(f"O valor do aumento é: {aumento}")
    novosal=salario+aumento
    print(f"O novo salario é: {novosal}")

if cargo==2:
    print("O cargo é secretário")
    aumento=salario*35/100
    print(f"O valor do aumento é: {aumento}")
    novosal=salario+aumento
    print(f"O novo salario é: {novosal}")

if cargo==3:
    print("O cargo é caixa")
    aumento=salario*20/100
    print(f"O valor do aumento é: {aumento}")
    novosal=salario+aumento
    print(f"O novo salario é: {novosal}")   

if cargo==4:
    print("O cargo é gerente")
    aumento=salario*10/100
    print(f"O valor do aumento é: {aumento}")
    novosal=salario+aumento
    print(f"O novo salario é: {novosal}") 

if cargo==5:
    print("O cargo é diretor ")
    aumento=salario*0/100
    print(f"O valor do aumento é: {aumento}")
    novosal=salario+aumento
    print(f"O novo salario é: {novosal}")


    