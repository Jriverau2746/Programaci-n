'''
Descripción:
Reeborg debe llegar al la posición (x,10), el valor de 
x, o sea la columna dependerá del valor que se le asigne
a Reeborg. 
pre: Empieza en (1,1) y mirando este. Dis criminante 
debe ser mayor a cero.
pos:rerborg debe validar si es False o True, retornar 
a la casilla (1,1) y mirar al este si es False. 
Si es True, Reeborg debe quedar mirando el este
Autor:Juan Felipe Rivera Urieta
Fecha: 30/08/2019
'''

"""
Descripcion: Reeborg gira a la derecha. 
Pre:Valido.
Pos:Reeborg gira 270° Grados a su izquierda.
"""
def turn_right():
    repeat 3:
        turn_left()

"""
Descripcion: Reeborg da media vuelta. 
Pre:Valido.
Pos:Reeborg gira 180° Grados a su izquierda.
"""
def media_vuelta():
    repeat 2:
        turn_left()
        
def colum_(x):
    var=True
    cont=0
    while front_is_clear() and x>1:
        move()
        x=x-1
        if wall_in_front() and x>2:
            var=False
            media_vuelta()
            while front_is_clear():
                move()
            media_vuelta()
            done()
            return False
    turn_left()
    while front_is_clear():
        move()
        cont=cont+1
    turn_right()
    move()
    turn_right()
    mitad=cont/2
    while front_is_clear():
        if mitad==int:
            put()
        move()
        cont=cont-1

    return var 
colum_(2)