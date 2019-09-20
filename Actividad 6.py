'''
Autor:Juan Felipe Rivera Urieta
Fecha: 18/09/2019
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
        
"""
Descripcion: Reeborg da un paso adelante.
Pre:Reeborg mira al Norte 
Pos:Reeborg se desplaza hacia delante en sentido 
norte y valida si hay algun objeto (retorna True or False)
"""
def move_1():
    var=True
    
    move()
    #Valida si hay objetos en la casilla actual
    if object_here():
        var=False
        print("Encontre un objeto")
        media_vuelta()
        move()
        media_vuelta()
        break
    #retorna (False or True)
    return var   
"""
Descripcion: Reeborg da un paso adelante y luego uno
hacia la dirección oeste.
Pre:Reeborg mira al Norte 
Pos:Reeborg se desplaza hacia sentido noroeste
si hay algun objeto (retorna True or False)
"""
def move_2():
    var=True
    
    move()
    #Valida si hay objetos en la casilla actual
    if object_here():
        var=False
        print("Encontre un objeto")
        media_vuelta()
        move()
        media_vuelta()
        break
    turn_left()
    move()
    #Valida si hay objetos en la casilla actual
    if object_here():
        var=False
        print("Encontre un objeto")
        media_vuelta()
        move()
        turn_right()
        move()
        media_vuelta()
        break
    turn_right()
    #retorna (False or True)
    return var  
"""
Descripcion: Reeborg da vuelta a la izquierda y da un paso.
Pre:Reeborg mira al Norte 
Pos:Reeborg se desplaza hacia delante en sentido 
oeste y valida si hay algun objeto (retorna True or False)
"""
def move_3():
    var=True
  
    turn_left()
    move
    #Valida si hay objetos en la casilla actual
    if object_here():
        var=False
        print("Encontre un objeto")
        media_vuelta()
        move()
        turn_left()
        break
    turn_right()
    #retorna (False or True)
    return var
"""
Descripcion: Reeborg da vuelta a la izquierda, da un paso 
luego da vuelta a la izaquierda y da un paso.
Pre:Reeborg mira al Norte 
Pos:Reeborg se desplaza hacia setido suroeste y
valida si hay algun objeto (retorna True or False)
"""
def move_4():
    var=True
    
    turn_left()
    move()
    #Valida si hay objetos en la casilla actual
    if object_here():
        var=False
        print("Encontre un objeto")
        media_vuelta()
        move()
        turn_left()
        break
    turn_left()
    move()
    #Valida si hay objetos en la casilla actual
    if object_here():
        var=False
        print("Encontre un objeto")
        media_vuelta()
        move()
        turn_right()
        move()
        turn_left()
        break
    media_vuelta()
    #retorna (False or True)
    return var

"""
Descripcion: Reeborg da media vuelta y luego un paso adelante.
Pre:Reeborg mira al Norte 
Pos:Reeborg se desplaza hacia sentido sur y valida 
si hay algun objeto (retorna True or False)
"""
def move_5():
    var=True
  
    media_vuelta()
    move
    #Valida si hay objetos en la casilla actual
    if object_here():
        var=False
        print("Encontre un objeto")
        media_vuelta()
        move()
        break
    media_vuelta()
    #retorna (False or True)
    return var
"""
Descripcion: Reeborg da vuelta a la derecha, da un paso 
luego da vuelta a la derechay da un paso.
Pre:Reeborg mira al Norte 
Pos:Reeborg se desplaza hacia setido sureste y
valida si hay algun objeto (retorna True or False)
"""
def move_6():
    var=True
    
    turn_right()
    move()
    #Valida si hay objetos en la casilla actual
    if object_here():
        var=False
        print("Encontre un objeto")
        media_vuelta()
        move()
        turn_right()
        break
    turn_right()
    move()
    #Valida si hay objetos en la casilla actual
    if object_here():
        var=False
        print("Encontre un objeto")
        media_vuelta()
        move()
        turn_left()
        move()
        turn_right()
        break
    media_vuelta()
    #retorna (False or True)
    return var
"""
Descripcion: Reeborg da vuelta a la derecha y da un paso.
Pre:Reeborg mira al Norte 
Pos:Reeborg se desplaza hacia delante en sentido 
este y valida si hay algun objeto (retorna True or False)
"""
def move_7():
    var=True
  
    turn_right()
    move
    #Valida si hay objetos en la casilla actual
    if object_here():
        var=False
        print("Encontre un objeto")
        media_vuelta()
        move()
        turn_right()
        break
    turn_left()
    #retorna (False or True)
    return var
"""
Descripcion: Reeborg da un paso adelante y luego uno
hacia la dirección este.
Pre:Reeborg mira al Norte 
Pos:Reeborg se desplaza hacia sentido noreste
si hay algun objeto (retorna True or False)
"""
def move_8():
    var=True
    
    move()
    #Valida si hay objetos en la casilla actual
    if object_here():
        var=False
        print("Encontre un objeto")
        media_vuelta()
        move()
        media_vuelta()
        break
    turn_right()
    move()
    #Valida si hay objetos en la casilla actual
    if object_here():
        var=False
        print("Encontre un objeto")
        media_vuelta()
        move()
        turn_left()
        move()
        media_vuelta()
        break
    turn_left()
    #retorna (False or True)
    return var
'''
Descripción: Reeborg se mueve en cualquier dirección 
(norte, nor-oeste, oeste, sur-oeste, sur, sur-este,
este, nor-este) avanzando.
Pre: Reeborg debe miarar el norte
     Se debe expecificar la dirección siguiendo la 
     siguiente instrucción:
     
    - Dirección:Indica hacia qué dirección se mueve 
    Reeborg.
    1<=dirección<=8
    Siendo:
    1=norte
    2=nor-oeste
    3=oeste
    4=sur-oeste
    5=sur
    6=sur-este
    7=este
    8=nor-este
    
Pos:
    True si el rey se puede mover a la dirección dada
    False si el rey no se puede mover hasta la 
    dirección dada y retorna a su posicción oroginal.
'''

def mover_rey(y):
    var=True
    if 1<=y<=8:
        #Valida la dirección a tomar
        if y == 1:
            move_1()
        if y == 2:
            move_2()
        if y == 3:
            move_3()
        if y == 4:
            move_4()
        if y == 5:
            move_5()
        if y == 6:
            move_6()
        if y == 7:
            move_7()
        if y == 8:
            move_8()
    else:
        print("No cumple")

mover_rey(2)
            
    
    
   