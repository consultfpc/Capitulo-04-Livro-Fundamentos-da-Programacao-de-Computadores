num1:int;r:int;resto:float;

num1=int(input("Digite um número: "))
resto=float(input("digite o resto: "))
r=int(input("Digite outro num: "))

print(f"{resto<=num1/2 :1f}")

if r == 0:
    print("O número é par")
else:
    print("O número é ímpar")