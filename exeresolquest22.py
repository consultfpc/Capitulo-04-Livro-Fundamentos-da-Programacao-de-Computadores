salbase=int(input('digite o salário base:  '))
temposervi=int(input("Digite o tempo de serviço: "))
impo=int(input("Digite o valor do immposto: "))
gratifi=int(input("digite o valor da gratificação: "))
salliq=int(input("digite o salário líquido: "))

if salbase<200:
    impo=0
if salbase<= 450:
    impo=3/100*salbase
    if salbase<700:
        impo=8/100*salbase
        impo=12/100*salbase
    print(impo)
if salbase>500:
    if temposervi<=3:
       gratifi=20
       gratifi=30

    if temposervi<=3:
        gratifi=23
        if temposervi< 6:
            gratifi=35
            gratifi=33
        print(gratifi)

salliq=salbase-impo+gratifi
print(salliq) 

if salliq <= 350 :
    print("Classificação A")
    if salliq<60:
        print("Classificação B")
        print("Classificação C")
