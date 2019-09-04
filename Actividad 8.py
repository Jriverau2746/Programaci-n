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
"""        
Descripcion: Reeborg recoge los objetos en la casilla. 
Pre:Valido.      
"""        
def recoger_objeto():
    cont=0
    while object_here():
        take()
        
        cont=cont+1
        
    return cont     

"""        
Descripcion: Reeborg hace un recorrido por todo el mundo recogiendo las bananas
y retornando los valores de cada grupo de bananas 
Pre: El mundo debe ser menor o igual a 8*8, la corrdenada y siempre debe 
ser un número par
pos: Reeborg queda mirando hacia el sur y muestra la lista de banas que recogió 
por cada grupo
"""
def recolectar_bananas(): 
    think(1)
    bananas=[]
    
    
    while front_is_clear():        
        tmp=recoger_objeto()
        if tmp!=0: 
            bananas.append(tmp) 
                
        move()
             
        while wall_in_front() and wall_on_right():
            turn_left()
            if not is_facing_north():
                print(bananas)
                done()
                
            if is_facing_north():
                move()
                
                turn_left()
           
        while wall_in_front() and not wall_on_right():
            turn_left()
            
            if not is_facing_north():
                media_vuelta()
                move()
                
                turn_right()
            if is_facing_north():
                move()
                
                turn_left()
            
    return bananas

recolectar_bananas()

            
            
        
    
    
    