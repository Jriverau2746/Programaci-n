'''
Autor:Juan Felipe Rivera Urieta
Fecha: 04/09/2019
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
Descripcion: Reeborg valida si hay un objeto en la casilla. 
Pre:Valido.
'''
def validar():
    #Valida si hay objetos en la casilla actual
    if object_here():
        var=False
        print("Encontre un objeto")
        break

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
def mover_rey(x):
    var=True
    
    #Ciclo para que reeborg siga caminando
    #Si el frente es claro
    while front_is_clear():
        move()
    if x==1:
        move()
        validar()
    if x==2:
        move()
        validar()
        turn_left()
        move()
        validar()
        turn_right()
    if x==3:
        turn_left()
        move()
        turn_right()
    if x==4:
        turn_left()
        move()
        validar()
        turn_left()
        move()
        validar()
        media_vuelta()  
    if x==5:
        media_vuelta()
        move()
        validar()
        media_vuleta()        
    if x==6:
        media_vuelta()
        move()
        validar()
        turn_left()
        move()
        validar()
        turn_left()
    if x==7:
        turn_right()
        move()
        validar()
        turn_left()

    if x==8:

        move()
        validar()
        turn_right()
        move()
        validar()
        turn_left() 
        
    #retorna (False or True)
    return var  

mover_rey(2)
