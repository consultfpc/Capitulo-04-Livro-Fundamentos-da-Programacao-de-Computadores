num1:int;num2:int;num3:int;num4:int;
print("Digite 3 números em ordem crescente: ")
num1=int(input("digite um num:"))
num2=int(input("digite num2:"))
num3=int(input("digite num3:"))

print("Digite um num (fora de ordem): ")
num4=int(input("digite num4: "))

if num4 > num3:
   print(f"A ordem decrescente é: {num4,num3,num2,num1}")
   if num4 > num2 and num4 <num3:
     print(f"A ordem decrescente é: {num3,num4,num2,num1}")
   if num4 > num1 and num4 <num2:
     print(f"A ordem decrescente é: {num3,num2,num4,num1}")
   if num4 < num1:
     print(f"A ordem decrescente é: {num3,num2,num1,num4}")
