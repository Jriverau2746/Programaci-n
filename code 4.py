'''Este mundo está diseñado para que el robot, Reeborg, 
camine la manzana que s eencentra en la casilla (3,3)
recoga la manzana. Luego este se devuelva a la 
la casilla (1,1)'''
print("Hola, soy Reeborg")
print("Voy a relizar una misión")

''' 
Funcionalidad: Realizar un zigzag
pre: Reeborg inicia en (1,1) y recoga la manzana en la
casilla (3,3)
pos: Reeborg termina en (5,5)
'''
def Encontrar():
    move()
    move()
    turn_left()
    move()
    move()
    take()
    turn_left()
    move()
    move()
    turn_left()
    move()
    move()
Encontrar()
'''Autor: Juan F. Rivera'''
'''Fecha: 29/07/2019'''

    