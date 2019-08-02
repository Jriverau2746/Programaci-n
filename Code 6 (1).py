'''Este mundo está diseñado para que el robot, Reeborg, 
recoja las semillas (cuadrados) y plante margaritas en
su lugar. El mundo es de 5x5 y las semillas se 
encuentran en (1, 1), (1, 5), (5, 5), (5, 1). '''

''' 
Funcionalidad: Recoger los cuadrados y plantar las y
plantar las margaritas, ubicadas en (1, 1), (1, 5), 
(5, 5), (5, 1).
pre: Reeborg está en la posición (1,1) y mira al Este. 
pos: Reeborg está en la posición (1,1), tiene 4 semillas 
(cuadrados) y mira al Norte.
'''
def Plantar():
    repeat 4:
        if object_here():
            take("square")
            put("daisy")
        repeat 4:
            move()
        if wall_in_front():
            turn_left()
    turn_left()            
Plantar()
'''Autor: Juan F. Rivera'''
'''Fecha: 29/07/2019'''

    