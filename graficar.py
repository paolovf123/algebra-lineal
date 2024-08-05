import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

def graficar_vectores(vecs, cols, alpha=1):
    plt.figure()
    plt.axvline(x=0, color="grey", zorder = 0)
    plt.axhline(y=0, color="grey", zorder = 0)
    for i in range(len(vecs)):
        x = np.concatenate([[0,0],vecs[i]])
        plt.quiver([x[0]],[x[1]],[x[2]],[x[3]], angles='xy', scale_units='xy', scale=1, color=cols[i], alpha =alpha)
    print(x[:])

def suma_vectores(vecs):
    v_aux = np.array([vecs[0][2],vecs[0][3],vecs[1][2],vecs[1][3]])
    v1_v2 = vecs[0]+vecs[1]
    plt.figure()
    plt.axvline(x=0, color="grey", zorder = 0)
    plt.axhline(y=0, color="grey", zorder = 0)
    for i in range(len(vecs)):
        x = np.concatenate([[0,0],vecs[i]])
        plt.quiver([vecs[0][0],v_aux[0],v1_v2[0]],[vecs[0][1],v_aux[1],v1_v2[1]],[vecs[0][2],v_aux[2],v1_v2[2]],[vecs[0][3],v_aux[3],v1_v2[3]], angles='xy', scale_units='xy', scale=1,color=sns.color_palette())
    plt.xlim(-1,6)
    plt.ylim(-1,15)

def espacio_generado_2d(vecs):
    plt.figure()
    for a in range(-10,10):
      for b in range(-10,10):
        plt.scatter(vecs[0][0]*a+vecs[1][0]*b ,vecs[0][1]*a+vecs[1][1]*b , marker='.')

def espacio_generado_3d(vecs):
   fig = plt.figure()
   ax = fig.add_subplot(111, projection='3d')
   for c in range(-10,10):
    for a in range(-10,10):
        for b in range(-10,10):
            ax.scatter(vecs[0][0]*a+vecs[1][0]*b+vecs[2][0]*c ,vecs[0][1]*a+vecs[1][1]*b+vecs[2][1]*c,vecs[0][2]*a+vecs[1][2]*b +vecs[2][2]*c, marker='.')