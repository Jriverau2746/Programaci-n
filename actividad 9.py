'''
Autor:Juan Felipe Rivera Urieta
Fecha: 06/09/2019
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
def recoger_daisy():
    cont=0
    
    while object_here("daisy"):
        take()
        cont=cont+1
    return cont
"""        
Descripcion: Reeborg recoge los objetos en la casilla. 
Pre:Valido.      
"""        
def recoger_dandelion():
    cont1=0
    
    while object_here("dandelion"):
        take()
        cont1=cont1+1
    return cont1
"""        
Descripcion: Reeborg recoge los objetos en la casilla. 
Pre:Valido.      
"""        
def recoger_leaf():
    cont2=0
    
    while object_here("leaf"):
        take()
        cont2=cont2+1
    return cont2
"""        
Descripcion: Reeborg recoge los objetos en la casilla. 
Pre:Valido.      
"""        
def recoger_tulip():
    cont3=0
    
    while object_here("tulip"):
        take()
        cont3=cont3+1
    return cont3

"""        
Descripcion: Reeborg suma los valores de las bananas y
sa el valor número en pesos vendidas por unidad. 
Pre:Valido.      
"""   

def Cosecha(flores):
    Suma = 0
    for i in flores:
        Suma = Suma + i*100
    return Suma

"""        
Descripcion: Reeborg hace un recorrido por todo el mundo recogiendo las bananas
y retornando los valores de cada grupo de bananas 
Pre: En el mundo, la corrdenada (y) siempre debe 
ser un número par. (No intentar con mundo (100*100) jajaj)
pos: Reeborg queda mirando en dirección sur.
"""
def recolectar_flores(): 
    think(1)
    set_max_nb_steps(5000)
    flores=["daisy","dandelion","leaf","tulip"]
    daisy=[]
    dandelion=[]
    leaf=[]
    tulip=[]
    
    while front_is_clear():        
        tmp=recoger_daisy()
        if tmp!=0: 
            daisy.append(tmp)
        tmp1=recoger_dandelion()
        if tmp1!=0: 
            dandelion.append(tmp1)
        tmp2=recoger_leaf()
        if tmp2!=0: 
            leaf.append(tmp2)
        tmp3=recoger_tulip()
        if tmp3!=0: 
            tulip.append(tmp3)
            
        move()
        if tmp!=0: 
            daisy.append(tmp)
        if tmp1!=0: 
            dandelion.append(tmp1)
        if tmp2!=0: 
            leaf.append(tmp2)
        if tmp3!=0: 
            tulip.append(tmp3)
        while wall_in_front() and wall_on_right():
            turn_left()
            if not is_facing_north():
                print(flores)
                print(Cosecha(flores))
                
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
            
    return flores

recolectar_flores()



    
            
            
        
    
    
    