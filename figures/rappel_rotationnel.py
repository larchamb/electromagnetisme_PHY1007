import pylab as plt
from pylab import cm
import numpy as np

pas = 0.01

# Le monde:
Y, X = np.mgrid[-3:3:pas, -3:3:pas]

def rotationnel_z(x, y,pas):
    """ Retourne la composante 'z' du rotationnel
    
    Note:
     - Derive par la methode des differences finies. Peu d'erreur numerique si le pas est petit
       (http://en.wikipedia.org/wiki/Finite_difference_method)
     - La grille du 'monde' doit avoir un espacement (pas) uniforme en x et en y
     - l'axe 0 est 'y' et l'axe 1 est 'x', car le monde est definis par Y, X = mgrid()
       (l'inversion est necessaire pour utiliser 'streamplot'
    """
    # l'operation de difference retourne un array de dimension plus courte vers 'axis'
    xp = np.diff(x,axis=0)/pas
    xp = xp[:,1:] # on tronque d'un element pour conserver les matrices de meme dimension
    yp = np.diff(y,axis=1)/pas
    yp = yp[1:,:] # on tronque d'un element pour conserver les matrices de meme dimension
    #print xp, yp
    #print xp.shape, yp.shape
    return  xp-yp

# Champ simple: 
# \mathbf A = y \hat{\mathbf x} -x \hat{\mathbf y} 

Ax = Y
Ay = -X
R = rotationnel_z(Ax,Ay,pas)

# figure
f,ax = plt.subplots()
p = ax.pcolor(X[1:,1:],Y[1:,1:],R,cmap=cm.RdBu,vmin=0, vmax=3)
cb = f.colorbar(p,ax=ax)
sp = ax.streamplot(X,Y,Ax,Ay)

# Champ plus complexe:
# \mathbf A = \left(\sin^2(x) + y\right)\hat{\mathbf x} + \left(\cos\left(x+y^2\right)\right)\hat{\mathbf y}

Ax = np.sin(X)**2+Y
Ay = np.cos(X+Y**2)
R = rotationnel_z(Ax,Ay,pas)
# figure
f,ax = plt.subplots()
p = ax.pcolor(X[1:,1:],Y[1:,1:],R,cmap=cm.RdBu,vmin=0, vmax=3)
cb = f.colorbar(p,ax=ax)
sp = ax.streamplot(X,Y,Ax,Ay,density = 1.5)

plt.show()
