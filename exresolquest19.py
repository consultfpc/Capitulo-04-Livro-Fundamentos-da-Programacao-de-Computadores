al=int(input("Digite sua  altura: "))
peso=int(input("Digite seu peso: "))

if al<1.20:
    if peso <= 60:
        print("A")
    if peso> 60 and peso <= 90:
        print("D")
    if peso > 90:
        print("G")
    
if al >= 1.20 and al<=1.70:
    if peso<=60:
        print("B")
    if peso >60 and peso <= 90:
        print("E")
    if peso > 90:
        print("H")

if al> 1.70:
    if peso<=60:
        print("C")
    if peso > 60 and peso<= 90:
        print("F")
    if peso > 90:
        print("I")
