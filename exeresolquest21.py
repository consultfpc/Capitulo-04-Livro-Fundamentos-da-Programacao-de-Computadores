codesta=int(input("digite o codigo do  estado(1 ao 5): "))
codcarga=int(input("digite o codigo da carga: "))
pesoton=int(input("digite o peso em toneladas: "))
pesoq=int(input("Digite o  peso em quilos: "))
precarga=int(input("digite o preço da carga:  "))
impo=int(input("digite o valor do imposto: "))
valtotal=int(input("digite o valor total: "))

pesoq=pesoton*1000
print(pesoq)

if codcarga>=10 and codcarga<=20:
    precarga=100*pesoq
if codcarga>= 21 and codcarga<=30:
    precarga=250*pesoq
if codcarga>= 31 and codcarga<=40:
    precarga=340*pesoq
print(precarga)

if codesta==1:
    impo=35/100*precarga
if codesta==2:
    impo=25/100*precarga
if codesta ==3:
    impo=15/100*precarga
if codesta==4:
    impo=5/100*precarga
if codesta==5:
    impo=0
print(impo)

valtotal=precarga+impo
print(valtotal)