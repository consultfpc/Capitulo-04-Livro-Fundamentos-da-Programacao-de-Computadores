notaTrab:int;avaSemes:int;exameFin:int;media:float;mediaPon:float;a:float;b:float;c:float;d:float;e:float;

notaTrab=0
avaSemes=0
exameFin=0
media=0
mediaPon=0
a=0
b=0
c=0
d=0
e=0


notaTrab=int(input("Digite a nota do trabalho de laboratório: "))
avaSemes=int(input("Digite a nota da avaliação semestral: "))
exameFin=int(input("Digite a nota do exame final: "))

media = (notaTrab*2 + avaSemes*3 + exameFin*5 ) / 10 
print(f"a media ponderada é: {notaTrab*2 + avaSemes*3 + exameFin*5  / 10  :1f}")

if media >= 8 and media< 10:
    media==a
    print("obteve conceito A")
    if media >= 7 and media <8:
        media==b
        print("obteve conceito B")
    if media >= 6 and media <7:
        media==c
        print("obteve conceito C")
    if media >= 5 and media <6:
        media==d
        print("obteve conceito D")
    if media >= 0 and media<5:
        media==e
        print("obteve conceito E")
        

    