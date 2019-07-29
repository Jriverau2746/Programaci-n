'''Este mundo está diseñado para que el robot, Reeborg, 
camine cuando se genere en una posición en la posición 
(1,1) hasta la casilla (5,5). Esto en zig-zag'''
print("Hola, soy Reeborg")
print("Voy a relizar una misión")

''' 
Funcionalidad: Realizar un zigzag
pre: Reeborg inicia en (1,1) y camina hacia el norte
pos: Reeborg termina en (5,5)
'''
def Zigzag():
    repeat 4:
        move()
        repeat 3:
            turn_left()
        move()
        turn_left()
Zigzag()
'''Autor: Juan F. Rivera'''
'''Fecha: 29/07/2019'''

    