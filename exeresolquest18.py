x=int(input("Digite um valor para x: "))
y=int(input("Digite um valor para y: "))
z=int(input("Digite um valor para z: "))

if x<y +z and y<x+z and z<x+y:
    if x ==y and y==z:
        print("Triângulo Equilátero")
    if x==y or x==z or y==z:
        print("Triângulo Isósceles") 
        if  x != y and x != z and y != z:
            print("Triângulo Escaleno")
else:
    print("Essas medidas não formam um triângulo")