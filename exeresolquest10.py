dia:int;mes1:int;ano1:int;d2:int;mes2:int;ano2:int;data:int

dia=int(input('Digite um dia: '))
data=int(input("Digite a primeira data: "))
print(f"dia{dia}")

mes1=int(input("Digite um mes: "))
print(f"mes1{mes1}")
ano1=int(input("Digite ano: " ))
print(f"ano1{ano1}")

d2=int(input("Digite a segunda data: "))
print(f"d2{d2}")

mes2=int(input("Digite o segundo mes: "))
print(f"mes2{mes2}")
ano2=int(input("Digite o outro ano: "))
print(f"ano2{ano2}")

if ano1>ano2:
    print(f"A maior data é:{dia,mes1,ano1}")
elif ano2>ano1:
    print(f"A maior data é: {d2,mes2,ano2}")
elif mes1>mes2:
    print(f"A maior data é: {dia,mes1,ano1}")
elif mes2>mes1:
    print(f"A maior data é: {d2,mes2,ano2}")
elif dia>d2:
    print(f"A maior data é: {dia,mes1,ano1}")
elif d2>dia:
    print(f"A maior data é: {d2,mes2,ano2}")
print("As datas são iguais!")