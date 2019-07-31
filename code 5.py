'''Este mundo está diseñado para que el robot, Reeborg, 
camine la manzana que enceuntre la manzana, tomarla
y regresar a casa'''
print("Hola, soy Reeborg")
print("Voy a relizar una misión")

''' 
Funcionalidad: Encontrar la manzana
pre: Reeborg inicia en (1,1) y mira hacia el este 
pos: Reeborg termina en (1,1), en casa
'''
def Encontrar():
    while front_is_clear() and not object_here():
        move()
    else:
        if object_here():
            take()
            turn_left()
            turn_left()
            while front_is_clear():
                move()
Encontrar()
'''Autor: Juan F. Rivera'''
'''Fecha: 29/07/2019'''

    