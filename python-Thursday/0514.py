import numpy as np 

sample=([1.2,1.44,2.56],[5.2,6.44,7.56])
np.savetxt('data.csv',sample,delimiter=',',fmt='%1.4f')
a=np.loadtxt('data.csv',delimiter=',')
print(a)

#ビルの金属板に穴があったら場合、シュミレーション
#金属板に穴がある場合、金属板の電位分布に変化が生じる、
#電流は電位差に比例するので、穴あき金属板の電流を調査すれば、穴の状態を推定可能性
#これが非破壊検査の基本技術である
#Poisson方程式のシュミレーションで、境界条件を工夫してあなあき金属板をシュミレーションしてみる

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

Nx=20
Ny=20
L=1.0
D=L/(Nx-1)
ITR=5000
ITT=0.001*0.001

f=np.zeros((Nx,Ny))
f[:,0]=-100
g=0.0
u=f.copy()
s=np.ones((Nx,Ny))
s[:,0]=0
s[:,Nx-1]=0
s[0,:]=0
s[Nx-1,:]=0
s[10,5]=0
s[12,10]=0
s[8,15]=0
s[5,7]=0
s[15,17]=0



for cnt in range(ITR):
    u0=u.copy()
    for j in range(0,Ny):
        u0[0,j]=u[0,j]
        u0[Nx-1,j]=u[Nx-1,j]
        u[0,j]=u[1,j]+D*g
        u[Nx-1,j]=u[Nx-2,j]-D*g
    for i in range(1,Nx-1):
        for j in range(1,Ny-1):
            u[i,j]=s[i,j]*0.25*(u[i+1,j]+u[i-1,j]+u[i,j+1]+u[i,j-1]-D**2*f[i,j]+(1-s[i,j])*f[i,j])

    cnv=(np.sum((u0-u)*(u0-u)))**0.5
    if cnv <ITT:
        print(cnt,cnv)
        break

np.savetxt('possion01.csv',u,fmt='%.2f',delimiter=',')

#結果を可視化
plt.imshow(u,cmap="jet",origin="lower")
plt.colorbar()
plt.title("Poisson Equation Solution")
plt.show()

#右端の電流、その一個左を測定するのがベスト
