import matplotlib.pyplot as plt

t=100
x = [-t/2,0, t/2]
y = [-t*3**0.5/2,0,-t*3**0.5/2]
xant=[]
yant=[]
comeco=0
vez=0
vezes=3
while vez<vezes:
    vez+=1
    for i in x:
        for j in x:
            xant.append((i+j)/2)
        comeco+=1
    x=xant[::]
    comeco=0
    print(x)
    for i in y:
        for j in y[comeco:]:
            yant.append((i+j)/2)
        comeco+=1
    y=yant[::]
    comeco=0
y.reverse()
plt.scatter(x, y)
plt.show()