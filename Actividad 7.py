'''
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
'''
Descripción:
Reeborg debe llegar al la posición (x,10), el valor de 
x, o sea la columna dependerá del valor que se le asigne
a Reeborg.
pre:Empieza en (1,1) y mirando este. Dis criminante 
debe ser mayor a cero y menor a diez.
pos:Reeborg debe mirar al este 
'''

def recorrer_columna(col):
    think(1)
    var=True
    x=col
    
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
    turn_right()
    return var
'''
Descripción:
Reeborg se desplaza hasta la casilla (1,1), 
dejando en cada casilla un objeto. Deja objetos diferentes si 
la columna es par o impar. Antes de llamar el procedimiento, 
Reeborg está ubicado en la casilla (col, N) mirando en sentido 
Este
pre: Empieza en (1,1) y mirando este. Dis criminante 
debe ser mayor a cero y menor a diez.
pos:Reebor queda mirando en sentido este
'''
def volver_a_casa_con_rastro(valor):
    turn_right()
    si_es_par(valor)
    si_es_impar(valor)

'''
Descripción: Si la columna es par Reeborg hará la función volver_a_casa_con_rastro
dejando estrellas a su paso
pos:retorna si es True
'''
def si_es_par(col):
    #Para cuando la columna sea un número par
    if col%2==0:
        while front_is_clear():
            put("star")
            move()
        turn_right()
        while front_is_clear():
            put("star")
            move()
        media_vuelta()
        put("star")
    return True
'''
Descripción: Si la columna es par Reeborg hará la función volver_a_casa_con_rastro
dejando Triangulos a su paso
pos:retorna si es False
'''
def si_es_impar(col):
    #Para cuando la columna sea un número impar
    if col%2!=0:
        while front_is_clear():
            put("triangle")
            move()
        turn_right()
        while front_is_clear():
            put("triangle")
            move()
        media_vuelta()
        put("triangle")
    return False

def recorrido_completo(valor):
    recorrer_columna(valor)
    volver_a_casa_con_rastro(valor)

for i in range(1,11):
    recorrido_completo(i)

'''
recorrido_completo(1)
recorrido_completo(2)
recorrido_completo(3)
recorrido_completo(4)
recorrido_completo(5)
recorrido_completo(6)
recorrido_completo(7)
recorrido_completo(8)
recorrido_completo(9)
recorrido_completo(10)
'''