import math
x=0
y=0
R=10
ang=15
abertura=60
taxadereducaodoraio=0.5
vezes=0

def fazv(x,y,R,ang,abertura):
    return ((R*math.sin(ang),(R*math.cos(ang))),((R*math.cos(90-ang-abertura)),R*math.sin(90-ang-abertura)))

def repete(x,y,R,ang,abertura):
    vezes=0
    while vezes<2:
        vezes+=1
        print(fazv(x,y,R,ang,abertura))
        for i in range(len(fazv(x,y,R,ang,abertura))):
            a=fazv(x,y,R,ang,abertura)[i][0]
            b=fazv(x,y,R,ang,abertura)[i][1]
            R*=taxadereducaodoraio
            ang+=abertura
            fazv(a,b,R,ang,abertura)
            x+=a
            y+=b
            repete(x,y,R,ang,abertura)
repete(x,y,R,ang,abertura)