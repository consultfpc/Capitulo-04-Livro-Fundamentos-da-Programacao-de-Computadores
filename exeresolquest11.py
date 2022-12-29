


horaIni:int;minIni:int;minFin:int;horad:int;min_Duracao:int
horaF:int;hora:int;minuto:int

horaIni=int(input("Digite o horário inicial: "))
minIni=int(input("Digite o  minuto inicial: "))
horaf=int(input("Digite a hora final: "))
minFin=int(input("Minutofi: "))

if minIni>minFin:
    minFin=minFin+60
    horaf=horaf-1

if horaIni>horaf:
    horaf=horaf+24
    mind=horaf-horaIni
    horaDura=horaf-horaIni

print(f" {horaIni,horaf,minFin}")
