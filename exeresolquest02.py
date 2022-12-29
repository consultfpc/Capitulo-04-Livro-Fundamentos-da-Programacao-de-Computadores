nota1:int;nota2:int;nota3:int;media:float;notaExame:float;mediaArit:float;

nota1=int(input("Digite a nota1: "))
nota2=int(input("Digite a nota2: "))
nota3=int(input("Digite a nota3: "))

media=(nota1 + nota2 +nota3) / 3
print(f"A média é: {nota1 + nota2 +nota3 / 3 :.1f}")
 
if media >= 0 and media < 3:
    print("reprovado")
    if media >= 3 and media < 7:
        print("exame")
notaExame=12 - media
print(f"Deve tirar: {12 - media :.1f}para ser aprovado")
if media >= 7 and media <=10:
    print("aprovado")
    