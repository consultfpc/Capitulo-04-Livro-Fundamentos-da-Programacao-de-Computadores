codprod=int(input("Digite o código do produto: "))
pesoquilos=int(input("Digite o peso em quilos: "))
codpais=int(input("Digite o código  do país: "))
pesogramas=int(input("Digite o peso em gramas: "))
pretotal=int(input("Digite o preço total: "))
impo=int(input("Digite o valor do imposto: "))
valtotal=int(input("digite o valor total de tudo: "))
pregrama=int(input("digite o preço em gramas: "))

pesogramas=pesoquilos*1000
print(pesogramas)

if codprod>= 1 and codprod<=4:
    pregrama=10
if codprod>=5 and codprod<=7:
    pregrama=25
if codprod >=8 and codprod<=10:
    pregrama=35
pretotal=pesogramas*pregrama
print(pretotal)

if codpais==1:
    impo=0
if codpais==2:
    impo=pretotal*15/100
if codpais ==3:
    impo=pretotal*25/100
print(impo)  

valtotal=pretotal+impo
print(valtotal)