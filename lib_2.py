import README
import math

"""Adición de vectores complejos."""



"""Inverso (aditivo) de un vector complejo."""

def inverso_vector(v):
  num =len(v)
  a =[(0,0] * num]
  i = 0
  while i in range(num):
    a[i] = README.producto_complejos((-1,0),v[i])
    i = i + 1
  return a
 
"""Multiplicación de un escalar por un vector complejo."""

def mult_escalar(v):
  
  a = int(input("Digite el numero escalar ")
  fila = [(0,0)] * len(v[0])
  multiplicacion = [fila] * len(v)
  for i in range(len(v)):
    multiplicacion[i] = [(0,0)] * len(v[0])
    for j in range(len(v[0])):
      multiplicacion[i][j] = README.producto_complejos((a,0), v[i][j])
  return multiplicacion
                                                
"""Adición de matrices complejas."""
       
def adicionmat(m1, m2):
  a = len(m1)
  b = len(m1[0])
  fila = [(0,0] * b
  suma = [fila] * a
  for i in range(a):
    suma[i] = [(0,0)] * b
    for j in range(b):
      suma[i][j] = README.sum_complejos(m1[i][j],m2[i][j])
  return suma  
           
"""Inversa (aditiva) de una matriz compleja."""                                                
 
def inverso(v):
  fila = [(0,0)] * len(v[0])
  inversa = [fila] * len(v)
  for i in range(len(v)):
    inversa[i] = [(0,0)] * len(v[0])
    for j in range(len(v[0])):
      inversa[i][j] = README.producto_complejos((-1,0), v[i][j]) 
  return inversa
 
"""Multiplicación de un escalar por una matriz compleja."""

def mult_escalar_matriz(e, mc1):
           
for i in range(len(m1)): 
        for j in range(len(m1[0])):
            m1[i][j] = README.producto_complejo(m1[i][j], e)
    return mc_1          
           
"""Transpuesta de una matriz/vector."""

def transpuesta(m_v1): 
    rta = crear_matriz1(len(m_v1[0]), len(m_v1))
    for i in range (len(m_v1[0])):
        for j in range (len(m_v1)):
            rta[i][j] = mvc_1[j][i]
    return rta    
 
"""Conjugada de una matriz/vector."""           
           
def conjugada_mv(m_v1):
    
    for i in range(len(m_v1)):
        for j in range(len(m_v1[0])):
            m_v1[i][j] = LC.conjugado(m_v1[i][j])
    return m_v1

"""Adjunta (daga) de una matriz/vector."""
           
def conjugada_mv(m_v1):
    for i in range(len(m_v1)):
        for j in range(len(m_v1[0])):
            m_v1[i][j] = LC.conjugado(m_v1[i][j])
    return mv1

"""Producto de dos matrices (de tamaños compatibles)"""
           
def adicion_matrices_complejas(m1, m2):   
    if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
        rta = crear_matriz(m1, m2)
        for i in range(len(m1)): 
            for j in range(len(m2[0])):
                rta[i][j] = LC.suma(m1[i][j], m2[i][j])
        return rta
           
"""Función para calcular la "acción" de una matriz sobre un vector."""
           
def accion(m,v):
    f =  len(m)
    a = [(0,0)] * len(m)
    for i in range(len(m)):
        for j in range(len(m)):   
            a[j] = README.sum_complejos(a[i],lc.producto_complejos(m[i][j],v[j]))
    return  a         
           
"""Producto interno de dos vectores."""    
           
def producto_interno(v1,v2):
    num = len(v1)
    a = (0,0)
    b = [(0,0)] * num 
    for i in range (num):
        b[i] = README.producto_complejos(README.conjugado(v1[i]),v2[i]) 
        a = README.sum_complejos(b[i],a)
    return (x)           
           
"""Norma de un vector"""
           
def norma_v(v_c1):
    rta = producto_interno(v_c1, v_c1)
    return math.sqrt(rta[0][0][0])      
           
"""Revisar si una matriz es unitaria."""
           
def mc_es_unitaria(m_c1):
    if len(m_c1) == len(m_c1[0]):
        a = adjunta(m_c1)
        aux = producto_matricial(m_c1, a)
        identidad = matriz_identidad(len(m_c1))
        for i in range(len(mc_1)):
            for j in range(len(mc_1)):
                for k in range(2):
                    if round(aux[i][j][k]) != identidad[i][j][k]:
                        return False
        return True
    else:
        return "Las matriz no es cuadrada"    
           
"""Producto tensor de dos matrices/vectores"""


           
           
           
           
