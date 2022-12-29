import os
num1:int;num2:int;soma:float;raiz:float;opcao:int

print("Menu ")
num1=int(input("Digite um número: "))
num2=int(input("Digite outro número: "))
print(f"A soma desses dois números é: {num1+num2}")
print(f"A raiz quadrada de um desses números: {num1^2}")

os.system("cls")
print("Digite sua opção: ")

if opcao== 1:
    num1=int(input("Digite um  valor para o primeiro número: "))
    print("{num1}")

    num2=int(input("Digite um valor para o segundo número: "))
    print("{num2}")

soma= num1+num2
print(f"A soma:{num1+num2}")

if opcao ==2:
        print("Digite um valor: ")
        print("{num1}")
        raiz=num1^2
        print(f"A raiz quadrada do {num1^2} é: ")

if opcao !=1 :
        print("Opção inválida! ")
elif opcao != 2 :
        print("Opção inválida!")
