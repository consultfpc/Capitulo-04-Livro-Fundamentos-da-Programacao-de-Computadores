a:int;b:int;c:int;i:int

a=int(input("Digite um valor para A: "))
b=int(input("Digite um valor para B: "))
c=int(input("Digite um valor para C: "))
i=int(input("Digite um valor para I(1,2 ou 3): "))


if i==1:
  if a < b and a<c:
     if b < c:
        print(f"A ordem crescente dos números é: {a,b,c}")
        print(f"A ordem crescente dos números é: {a,c,b}")
  if b  < a and b < c:
     if a<c:
       print(f"A ordem crescente dos números é: {b,a,c}")
       print(f"A ordem crescente dos números é: {b,c,a}")
  if c <a and c<b:
    if a <b:
         print(f"A ordem crescente dos números é: {c,a,b}")
         print(f"A ordem crescente dos números é: {c,b,a}")

if i ==2:
     if a>b and a>c:
       if b>c :
        print(f"A ordem decrescente dos números é: {a,b,c}")
        print(f"A ordem decrescente dos números é: {a,c,b}")
     if b>a and b>c:
        if a>c:
            print(f"A ordem decrescente dos números é: {b,a,c}")
            print(f"A ordem decrescente é: {b,c,a}")
     if c >a and c>b :
        if a >b:
            print(f"A ordem decrescente dos números é: {c,a,b}")
            print(f"A ordem decrescente dos números é: {c,b,a}")

if i==3:
    if a >b and a >c:
        print(f"A ordem desejada é: {b,a,c}")
    if b>a and b>c:
        print(f"A ordem desejada é: {a,b,c}")
    if c>a and c > b:
        print(f"A ordem desejada é: {a,c,b}")
        

