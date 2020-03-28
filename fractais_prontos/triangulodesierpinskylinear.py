import matplotlib.pyplot as plt

x=[[0,2,3,2,3,5,6,5,6,8]]
y=[[0,0,1,2,3,3,2,1,0,0]]

x=[[0,2],[2,3],[3,2],[2,3],[3,5],[5,6],[6,5],[5,6],[6,8]]
y=[[0,0],[0,1],[1,2],[2,3],[3,3],[3,2],[2,1],[1,0],[0,0]]

'''x=[[0,1]]
y=[[0,1]]'''

vezes=7

def f(ox,oy):
    ax,ay=[],[]
    for j in range(len(ox)):
        x=ox[j]
        y=oy[j]
        if y[1]-y[0]==0:
            x1=x[0]
            x2=x[0]+(x[1]-x[0])/4
            x3=x[0]+(x[1]-x[0])*3/4
            x4=x[1]
            y1=y[0]
            y2=y[0]+abs(x[1]-x[0])/4
            y3=y2
            y4=y[1]
        elif x[1]-x[0]==0:
            y1=y[0]
            y2=y[0]+(y[1]-y[0])/3
            y3=y[0]+(y[1]-y[0])*2/3
            y4=y[1]
            x1=x[0]
            x2=x[0]+(y[1]-y[0])/3
            x3=x2
            x4=x[1]
        elif x[1]>x[0] and y[1]>y[0]:#/^
            y1=y[0]
            y2=y1
            y3=y[0]+(y[1]-y[0])/2
            y4=y[1]
            x1=x[0]
            x2=x[1]
            x3=x2+(y[1]-y[0])/2
            x4=x2
        elif x[1]<x[0] and y[1]>y[0]:#^\
            y1=y[0]
            y2=y1
            y3=y[0]+(y[1]-y[0])/2
            y4=y[1]
            x1=x[0]
            x2=x[1]
            x3=x2-(y[1]-y[0])/2
            x4=x2
        elif x[1]<x[0] and y[1]<y[0]:#_/
            y1=y[0]
            y2=y[0]+(y[1]-y[0])/2
            y3=y[1]
            y4=y[1]
            x1=x[0]
            x2=x[0]-(y[1]-y[0])/2
            x3=x1
            x4=x[1]
        elif x[1]>x[0] and y[1]<y[0]:#\_
            y1=y[0]
            y2=y[0]+(y[1]-y[0])/2
            y3=y[1]
            y4=y[1]
            x1=x[0]
            x2=x[0]+(y[1]-y[0])/2
            x3=x1
            x4=x[1]
        ax+=[[x1,x2],[x2,x3],[x3,x4]]
        ay+=[[y1,y2],[y2,y3],[y3,y4]]
    return ax,ay

for vez in range(vezes):
    x,y=f(x,y)

lx,ly=[],[]

for i in x:
    for j in i:
        lx.append(j)

for i in y:
    for j in i:
        ly.append(j)

#plt.scatter(lx,ly)
plt.plot(lx,ly)
plt.show()