'''Descripción: El mundo consta de que el robot vaya hasta la casilla
(5,1), recoga la manzana y ponga una banana en el 
mismo punto'''
print("¡Hola! Yo soy reeborg")
print("Voy realizar una misión")
move()
move()
move()
move()
#pause()
if object_here():
    take()
#pause()
put("banana")
#pause()
turn_left()
turn_left()
#pause()
move()
move()
move()
move()
'''Autor: Juan F. Rivera'''
'''Fecha: 29/07/2019'''