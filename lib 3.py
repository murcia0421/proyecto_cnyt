import math
import math
import matplotlib
import matplotlibpyplot as plt

import lib_1
import lib_2

def Rendija(ren,blan,click):
    tam = 7
    ren1 = ren
    blan1 = blan
    a = 2
    if ren > 2 or blan > 3:
        ren = ren - 2 
        tam = ren * 3 + tam
        a = ren * 2 + a
        blan = blan - 3
        tam = tam + blan
    matriz = [[(0,0) for i in range (-1,tam)] for i in range (-1,tam)] 
    for i in range (0,tam+1):
        for j in range (0,tam+1):
            if i == 0 and 0 < j < ren+1:
                matriz[i][j] = (1/ren,0)
            elif 0 < i <= ren:
                if i == 1 and 2 * (ren1-2) + 2 - (ren1-2) < j < 2 * (ren1-2) + blan1 + 3 - (ren1-2):
                    matriz[i][j] = (1/blan1,0)
                if i == 2 and 2 * (ren1-2) + 4 - (ren1-2) < j < 2 * (ren1-2) + blan1 + 5 - (ren1-2) and ren1 >= 2:
                    matriz[i][j] = (1/blan1,0)
                if i == 3 and 2 * (ren1-2) + 6 - (ren1-2) < j < 2 * (ren1-2) + blan1 + 7 - (ren1-2) and ren1 >= 3:
                    matriz[i][j] = (1/blan1,0)
                if i == 4 and 2 * (ren1-2) + 8 - (ren1-2) < j < 2 * (ren1-1) + blan1 + 9 - (ren1-2) and ren1 >= 4:
                    matriz[i][j] = (1/blan1,0)
            elif i > ren1 and j == i:
                matriz[i][j] = (1,0)
    m = lib_2.transpuesta(matriz)
    for i in range (clk):
        s = lib_2.producMat(m,m)
    return s
  
  
  def RendijaCuantico(ren,blan,click):
    xren = math.sqrt(2 * numoRen)
    xblan = math.sqrt(2 * numBlan)
    tam = 7
    ren1 = ren
    blan1 = blan
    a = 2
    if ren > 2 or blan > 3:
        ren = ren - 2 
        tam = ren * 3 + tam
        a = ren * 2 + a
        blan = blan - 3
        tam = tam + blan
    matriz = [[(0,0) for i in range (-1,tam)] for i in range (-1,tam)] 
    for i in range (0,tam+1):
        for j in range (0,tam+1):
            if i == 0 and 0 < j < ren+1:
                matriz[i][j] = (1/xren((-1)**j/2),(1/xren)*((-1)**j))
            elif 0 < i <= ren:
                if i == 1 and 2 * (ren1-2) + 2 - (ren1-2) < j < 2 * (ren1-2) + blan1 + 3 - (ren1-2):
                    matriz[i][j] = ((1/xblan)*((-1)**(j/2)),(1/xblan)*((-1)**j))
                if i == 2 and 2 * (ren1-2) + 4 - (ren1-2) < j < 2 * (ren1-2) + blan1 + 5 - (ren-2) and ren >= 2:
                    matriz[i][j] = ((1/xblan)*((-1)**(j/2)),(1/xblan)*((-1)**j))
                if i == 3 and 2 * (ren-2) + 6 - (ren-2) < j < 2 * (ren-2) + blan + 7 - (ren-2) and ren >= 3:
                    matriz[i][j] = ((1/xblan)*((-1)**(j/2)),(1/xblan)*((-1)**j))
                if i == 4 and 2 * (ren-2) + 8 - (ren-2) < j < 2 * (ren-1) + blan + 9 - (ren-2) and ren >= 4:
                    matriz[i][j] = ((1/xblan)*((-1)**(j/2)),(1/xblan)*((-1)**j))
            elif i > ren and j == i:
                matriz[i][j] = (1,0)
    m = lE.transpuesta(matriz)
    for i in range (clk):
        s = lE.producMat(m,m)
    return s
  
  
def diagramaEstados(a):
    eje_x = a
    eje_y = [0,1]
    plt.bar(eje_x, eje_y)
    plt.show()
                                                                          
                                                                          
                                                                          
