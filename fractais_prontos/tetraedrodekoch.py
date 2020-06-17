import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
<<<<<<< HEAD
from matplotlib.backends.backend_pdf import PdfPages
=======
>>>>>>> 812230f1f5cda8076c4fa3c432a8823c796dd233
import math


def faztetraedro(xx, yy, zz, vez):
    x = [xx[0] + (xx[1] - xx[0]) / 2, xx[0] + (xx[2] - xx[0]) / 2, xx[1] + (xx[2] - xx[1]) / 2]
    y = [yy[0] + (yy[1] - yy[0]) / 2, yy[0] + (yy[2] - yy[0]) / 2, yy[1] + (yy[2] - yy[1]) / 2]
    z = [zz[0] + (zz[1] - zz[0]) / 2, zz[0] + (zz[2] - zz[0]) / 2, zz[1] + (zz[2] - zz[1]) / 2]
    p1x, p1y, p1z = x[0], y[0], z[0]
    p2x, p2y, p2z = x[1], y[1], z[1]
    p3x, p3y, p3z = x[2], y[2], z[2]
    d = 0.5 * (((xx[0] - xx[1]) ** 2 + (yy[0] - yy[1]) ** 2 + (zz[0] - zz[1]) ** 2) ** 0.5)
    p4x = ((2.0 ** 1.5) / (3 * d)) * ((y[2] - y[1]) * (z[1] - z[0]) - (y[1] - y[0]) * (z[2] - z[1])) + sum(x) / 3.0
    p4y = ((2.0 ** 1.5) / (3 * d)) * ((z[2] - z[1]) * (x[1] - x[0]) - (z[1] - z[0]) * (x[2] - x[1])) + sum(y) / 3.0
    p4z = ((2.0 ** 1.5) / (3 * d)) * ((x[2] - x[1]) * (y[1] - y[0]) - (x[1] - x[0]) * (y[2] - y[1])) + sum(z) / 3.0
    f1 = [[p1x, p2x, p3x], [p1y, p2y, p3y], [p1z, p2z, p3z]]
    f2 = [[p2x, p1x, p4x], [p2y, p1y, p4y], [p2z, p1z, p4z]]
    f3 = [[p4x, p1x, p3x], [p4y, p1y, p3y], [p4z, p1z, p3z]]
    f4 = [[p2x, p4x, p3x], [p2y, p4y, p3y], [p2z, p4z, p3z]]
    t1 = [[xx[0], x[0], x[1]], [yy[0], y[0], y[1]], [zz[0], z[0], z[1]]]
    t2 = [[x[0], xx[1], x[2]], [y[0], yy[1], y[2]], [z[0], zz[1], z[2]]]
    t3 = [[x[1], x[2], xx[2]], [y[1], y[2], yy[2]], [z[1], z[2], zz[2]]]
    if vez == 0:
        return f1, f2, f3, f4
    return t1, t2, t3, f2, f3, f4


fig = plt.figure()
sub = fig.add_subplot(1, 1, 1, projection='3d')
t = 1
x = [[-t / 2, 0, t / 2, 0]]
y = [[(3**.5*t/2)*-1/3, (3**.5*t/2)*2/3, (3**.5*t/2)*-1/3, 0]]
z = [[0, 0, 0, 0]]
# sub.plot(x[0], y[0], z[0])

# EIXOS
# sub.plot([0,0],[-.5,.5],[0,0])
# sub.plot([0,0],[0,0],[-.5,.5])
# sub.plot([-.5,.5],[0,0],[0,0])

lx, ly, lz = [], [], []
t1, t2, t3, t4 = faztetraedro(x[0], y[0], z[0], 0)
nx, ny, nz = [], [], []
for f in [t1, t2, t3, t4]:
    nx += f[0]
    ny += f[1]
    nz += f[2]
    sub.plot(nx, ny, nz, color="000000")
    lx += [nx]
    ly += [ny]
    lz += [nz]
    nx, ny, nz = [], [], []
x, y, z = lx[::], ly[::], lz[::]
for vez in range(1, 3):
    print(vez)
    for i in range(len(x)):
        t1, t2, t3, f2, f3, f4 = faztetraedro(x[i], y[i], z[i], vez)
        nx, ny, nz = [], [], []
        nt = len(x)
        for f in [t1, t2, t3, f2, f3, f4]:
            nx += f[0]
            ny += f[1]
            nz += f[2]
            sub.plot(nx, ny, nz, color="000000")
            lx += [nx]
            ly += [ny]
            lz += [nz]
            nx, ny, nz = [], [], []
    x, y, z = lx[::], ly[::], lz[::]


<<<<<<< HEAD
with PdfPages(r'tetraedrodekoch.pdf') as export_pdf:
    export_pdf.savefig()


=======
>>>>>>> 812230f1f5cda8076c4fa3c432a8823c796dd233
print("montando grafico")
plt.show()