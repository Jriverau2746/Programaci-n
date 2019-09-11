#Descripción: Reeborg irá desde la posición (1,1) hasta la posición (col,N) en un tablero de dimensiones NxN, al llegar a esta posición mirará al este y luego regresará poniendo un objeto en cada casilla, el objeto varia dependiendo si es par o impar la columna
#Autor: Cristian Monroy
#Fecha: 02/09/2019

#Descripción: Este procedimiento permite que Reeborg gire hacia la derecha
#Pre: No tiene precondiciones
#Pos: No tiene postcondiciones
def turn_right():
    turn_left()
    turn_left()
    turn_left()

#Descripción: Este procedimiento permite que Reeborg gire 180º
#Pre: No tiene precondiciones
#Pos: No tiene postcondiciones
def media_vuelta():
    turn_left()
    turn_left()

#Descripción: Esta función hace que Reeborg vaya hasta la columna definida gire a la izquierda suba hasta el final del tablero y finalice mirando al este
#Pre: Reeborg debe iniciar mirando al este y estar en la posición (1,1)
#Pos: Reeborg finalizará en la posición (col,N) mirando al este
def recorrer_columna(col):
    think(1)
    x=1
    while front_is_clear() and x<col:
        move()
        x=x+1
    if x==col:
        turn_left()
        while front_is_clear():
            move()
        turn_right()
        return True
    if not front_is_clear():
        media_vuelta()
        while front_is_clear():
            move()
        media_vuelta()
        return False
    print(x)

#Descripción: Esta función hace que Reeborg regrese a la posición (1,1) desde (col,N) poniendo un objeto en cada casilla durante su trayecto, dicho objeto varia dependiendo si la columna es par o impar
#Pre: Reeborg debe iniciar mirando al este y estar en la posición (col,N)
#Pos: Reeborg finalizará en la posición (1,1) mirando al este
def volver_a_casa_con_rastro(x):
    turn_right()
    es_par(x)
    media_vuelta()
    x=1

#Descripción: Esta función hace que Reeborg identifique si es par o impar la columna y ponga un objeto en cada casilla durante su trayecto, dicho objeto varia dependiendo si la columna es par o impar
#Pre: No tiene precondicones 
#Pos: Reeborg colocará un objeto en cada casilla
def es_par(n):
    if n%2==0:
        while front_is_clear():
            put("apple")
            move()
        turn_right()
        while front_is_clear():
            put("apple")
            move()
        put("apple")
        return True
    if n%2!=0:
        while front_is_clear():
            put("strawberry")
            move()
        turn_right()
        while front_is_clear():
            put("strawberry")
            move()
        put("strawberry")
        return False

#Descripción: Esta función hace que Reeborg ejecute todas las funciones
#Pre: Debe iniciar mirando hacia el este en la casilla (1,1)
#Pos: Debe finalizar en la casilla (1,1) mirando hacia el este
def recorrido_completo(valor):
    set_max_nb_steps(2000)
    recorrer_columna(valor)
    volver_a_casa_con_rastro(valor)

for i in range (1,11):
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
recorrido_completo(10)'''