import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

Nx=50
Ny=50
L=1.0
D=L/(Nx-1)
ITR=5000

f=np.zeros((Nx,Ny))
f[:,0]=-100
g=0.0
u=f.copy()

for _ in range(ITR):
    #for j in range(1,Ny-1):
        #u[0,j]=u[1,j]+D*g
        #u[Nx-1,j]=u[Nx-2,j]-D*g
    for i in range(1,Nx-1):
        for j in range(1,Ny-1):
            u[i,j]=0.25*(u[i+1,j]+u[i-1,j]+u[i,j+1]+u[i,j-1]-D**2*f[i,j])
np.savetxt('possion1.csv',u,fmt='%.2f',delimiter=',')

plt.imshow(u,cmap="jet",origin="lower")
plt.colorbar()
plt.title("Poisson Equation Solution")
plt.show()
