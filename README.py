"""proyecto_cnyt"""
"""Juan Daniel Murcia Sanchez"""

import math
"""suma de complejos"""

def sum_complejos(n1,n2):
    return ((n1[0]+n2[0]),(n1[1]+n2[1]))
  
"""Producto de complejos"""

def producto_complejos(n1,n2):
    real=(n1[0]*n2[0])-(n1[1]*n2[1])
    imaginario=(n1[0]*n2[1])+(n1[1]*n2[0])
    return ((real,imaginario))
  
"""Resta de complejos"""

def rest_complejos(n1,n2):
    return ((n1[0]-n2[0]),(n1[1]-n2[1]))
  
"""Division de complejos"""
 
def div_complejos(x,y):
        real=((x[0]*y[0])+(x[1]*y[1]))/((x[0]**2)+(y[1]**2))
        imaginario=((y[0]*x[1])-(x[0]*y[1]))/((y[0]**2)+(y[1]**2))
        return (real,imaginario)
      
"""Modulo de un complejo"""

def mod_complejos(x):
        return math.sqrt((x[0]**2)+(x[1]**2))
 
"""Conjugado de un complejo"""

 def conjugado(n):
        return (n[0],-1*n[1])
    
"""Conversión entre representaciones polar y cartesiano"""

 def pol_catersiano(n):
        real=n[0]*math.cos(n[1])
        imaginario =n[0]*math.sin(n[1])
        return (real,imaginario)
    
"""Retornar la fase de un número complejo"""

def fas_complejo(n1):
    theta=(n1[1]/n1[0])
    return ((math.degrees(math.atan(theta))))

