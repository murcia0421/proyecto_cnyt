import numpy
def canicas_booleanas():
  m1 = np.array([[0,0,0,0,0,0],[0,0,0,0,0,0],[0,1,0,0,0.1],[0,0,0,1,0,0],{0,0,1,0,0,0],[1,0,0,0,1,0]])
  n = int(input(" "))
  final= np.dot(m1, m1)
  for i in range(n-1):
    matr = np.dot(final, final)                                                                                                                                           
    final = matr                                                                      
  return(final)
                                                                          
                                                                          
                                                                          
