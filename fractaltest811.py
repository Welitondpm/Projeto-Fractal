import matplotlib.pyplot as plt


t=100
x = [-t/2,0, t/2]
y = [-t*3**0.5/2,0,-t*3**0.5/2]
print(x,y)
vez=0
vezes=3
primeiro=0
ultimo=len(x)
while vez<vezes:
    vez+=1
    queimportanox=x[:]
    queimportanoy=y[:]
    for i in queimportanox:
        for j in queimportanox:
            x.append((i+j)/2)
            print(x[-1])
    for i in queimportanoy:
        for j in queimportanoy:
            y.append((i+j)/2)
            print(y[-1])
    x=x[len(queimportanox):]
    y=y[len(queimportanoy):]
    print(x,y)

plt.scatter(x, y)
plt.show()