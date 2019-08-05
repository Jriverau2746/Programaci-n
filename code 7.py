'''Este mundo está diseñado para que el robot, Reeborg, 
llegue al centro del mundo y coloque el objeto que lleva'''

''' 
Funcionalidad: LLegar al centro y colocar el objeto    
pre: fron is clear 
pos: reeborg deja el objeto en el centro 
'''
def vuelta():
    turn_left()
    turn_left()
    
def Centro():
    while front_is_clear():
        move()
    else:
        vuelta()
        move()
        vuelta()
        build_wall()
        vuelta()

while front_is_clear():
    Centro()
else:
    put()
 
'''Autor: Juan F. Rivera'''
'''Fecha: 05/07/2019'''

    