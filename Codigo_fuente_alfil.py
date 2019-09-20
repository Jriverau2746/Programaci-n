"""
Descripcion: Este programa esta diseñado para desplazar a Reeborg en forma de alfil 
en un tablero 8x8 debera contar con la funcion mov_alfil que tiene parametros
(direccion, pasos) donde 1<=pasos<8 y direccion 1<=direccion<=4 tal que represente
el plano cartesiano.
Autor: Sebastian Varon, Michael Garzoon, Sergio Jimenez
Fecha:26/08/2019
"""
"""
Descripcion: Reeborg gira. 
Pre:Valido.
Pos:Reeborg gira 180° Grados a su izquierda.
"""
def giro180():
    #Repetir numero de acciones
    repeat 2:
        turn_left()
"""
Descripcion: Reeborg gira. 
Pre:Valido.
Pos:Reeborg gira 270° Grados a su izquierda.
"""        
def giro270():
    #Repetir numero de acciones
    repeat 3:
        turn_left()
"""
Descripcion: Reeborg da un paso en forma de alfil.
Pre:Reeborg mira al Norte y debe tener un numero 
de pasos definido.
Pos:Reeborg se desplaza en forma de alfil sentido
Sureste y valida si hay algun objeto (retorna True or False)
"""
def zigzag_4(x):
    var=True
    cont=0
    #Ciclo para que reeborg siga caminando
    #Si el frente es claro 
    while front_is_clear():
        #Repetir numero de acciones
        repeat 2:    
            giro270()
            move()
        giro180()
        cont=cont+1
        #Valida si hay objetos en la casilla actual
        if object_here():
            var=False
            print("Rayos 😭 Encontre un objeto")
            zigzag_2(cont)
            break
        #Valida si el contador es igual al numero 
        #de pasos definidos por parametro
        if cont==x:
            break
    #retorna (False or True)
    return var        
"""
Descripcion: Reeborg da un paso en forma de alfil.
Pre:Reeborg mira al Norte y debe tener un numero 
de pasos definido.
Pos:Reeborg se desplaza en forma de alfil sentido
Suroeste y valida si hay algun objeto (retorna True or False)
"""
def zigzag_3(x):
    var=True
    cont=0
    #Ciclo para que reeborg siga caminando
    #Si el frente es claro 
    while front_is_clear(): 
        #Repetir numero de acciones
        repeat 2:
            turn_left()
            move()
        giro180()
        cont=cont+1
        #Valida si hay objetos en la casilla actual
        if object_here():
            var=False
            print("Rayos 😭 Encontre un objeto")
            zigzag_1(cont)
            break
        #Valida si el contador es igual al numero 
        #de pasos definidos por parametro
        if cont==x:
            break        
    #retorna (False or True)
    return var        
"""
Descripcion: Reeborg da un paso en forma de alfil.
Pre:Reeborg mira al Norte y debe tener un numero 
de pasos definido.
Pos:Reeborg se desplaza en forma de alfil sentido
Noroeste y valida si hay algun objeto (retorna True or False)
"""
def zigzag_2(x):
    var=True
    cont=0
    #Ciclo para que reeborg siga caminando
    #Si el frente es claro 
    while front_is_clear(): 
        #Repetir numero de acciones
        repeat 2:
            move()
            turn_left()
        giro180()
        cont=cont+1
        #Valida si hay objetos en la casilla actual
        if object_here(): 
            var=False
            print("Rayos 😭 Encontre un objeto")
            zigzag_4(cont)
            break
        #Valida si el contador es igual al numero 
        #de pasos definidos por parametro
        if cont==x:
            break
    #retorna (False or True)
    return var
"""
Descripcion: Reeborg da un paso en forma de alfil.
Pre:Reeborg mira al Norte y debe tener un numero 
de pasos definido.
Pos:Reeborg se desplaza en forma de alfil sentido
Noreste y valida si hay algun objeto (retorna True or False)
"""
def zigzag_1(x):
    var=True
    cont=0
    #Ciclo para que reeborg siga caminando
    #Si el frente es claro 
    while front_is_clear():
        move()
        giro270()
        move()
        turn_left() 
        cont=cont+1
        #Valida si hay objetos en la casilla actual
        if object_here(): 
            var=False
            print("Rayos 😭 Encontre un objeto")
            zigzag_3(cont)
            break
        #Valida si el contador es igual al numero 
        #de pasos definidos por parametro
        if cont==x:
            break
    #retorna (False or True)
    return var      
"""
Descripcion: Reeborg se desplaza
Pre: Reeborg esta mirando hacia al Norte
Pos: Reeborg termina en posicion (direccion, pasos) simpre que el movimiento sea valido
"""
def mov_alfil(direc,pasos):
    #Valida condicion inicial
    if 1<=direc<=4 and 1<=pasos<8:
        print("Soy un Alfil ♗")
        #Valida la direccion debe tomar
        if direc == 1:
            print("Direccion: Nor-este")
            print("Pasos:",pasos)
            zigzag_1(pasos)
        if direc == 2:
            print("Direccion: Nor-oeste")
            print("Pasos:",pasos)
            zigzag_2(pasos) 
        if direc == 3:
            print("Direccion: Sur-oeste")
            print("Pasos:",pasos)
            zigzag_3(pasos) 
        if direc == 4:
            print("Direccion: Sur-este")
            print("Pasos:",pasos)
            zigzag_4(pasos)
    else:
        print("No cumple las condiciones iniciales")
#Llamado a funcion e ingreso de parametros        
mov_alfil(1,2)        
