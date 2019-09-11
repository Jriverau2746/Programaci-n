'''
Autor:Juan Felipe Rivera Urieta
Fecha: 11/09/2019
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
Descripcion: Reeborg recoge las Daisy en la casilla y suma
un contador. 
Pre:Valido.      
"""        
def recoger_daisy():
    cont=0
    
    while object_here("daisy"):
        take()
        cont=cont+1
        
    return cont
"""        
Descripcion: Reeborg recoge las dandelion en la casilla y suma
un contador. 
Pre:Valido.      
"""        
def recoger_dandelion():
    cont1=0
    
    while object_here("dandelion"):
        take()
        cont1=cont1+1
    return cont1

"""        
Descripcion: Reeborg recoge las leaf en la casilla y suma
un contador. 
Pre:Valido.      
"""        
def recoger_leaf():
    cont2=0
    
    while object_here("leaf"):
        take()
        cont2=cont2+1
    return cont2

"""        
Descripcion: Reeborg va a validar qué tipo de objeto
existen en la casilla y los clasifica en una lista. 
Pre:Valido.      
"""   

def recoger_planta():
    total = []
  
    if object_here("daisy"):
        total.append("daisy")
        total.append(recoger_daisy())      
    if object_here("dandelion"):
        total.append("dandelion")
        total.append(recoger_dandelion())
    if object_here("leaf"):
        total.append("leaf")
        total.append(recoger_leaf())
        
    return total




"""        
Descripcion: Reeborg hace un recorrido por todo el mundo recogiendo las bananas
y retornando los valores de cada tipo de plantas que 
encuentre. 
luego las clasifica y señala cuántas plantas recoge
de cada tipo.
Pre: En el mundo, la corrdenada (y) siempre debe 
ser un número par. (No intentar con mundo (100*100) jajaj)
pos: Reeborg queda mirando en dirección sur.
"""
def recolectar_flores(): 
    think(1)
    set_max_nb_steps(5000)
    flores=[]
    #guardar en 0:Daisy. 1:Dandelion. 2:Leaf.
    flores_0=0
    flores_1=0
    flores_2=0
    
    while front_is_clear():
        
        tmp=recoger_planta()
        if len(tmp)!=0:
            if tmp[0]=="daisy":                
                flores_0 += tmp[1]
            if tmp[0]=="dandelion":                
                flores_1 += tmp[1]
            if tmp[0]=="leaf":                
                flores_2 += tmp[1]
        move()
        
              
        while wall_in_front() and wall_on_right():
            turn_left()
            if not is_facing_north():
                flores.append(("Daisy",flores_0))
                flores.append(("Dandelion",flores_1))
                flores.append(("leaf",flores_2))
                
                return (flores)
                               
                done()
                
            if is_facing_north():
                tmp=recoger_planta()
                if len(tmp)!=0:
                    if tmp[0]=="daisy":                
                        flores_0 += tmp[1]
                    if tmp[0]=="dandelion":                
                        flores_1 += tmp[1]
                    if tmp[0]=="leaf":                
                        flores_2 += tmp[1]
                move()
                
                turn_left()
           
        while wall_in_front() and not wall_on_right():
            turn_left()
            
            if not is_facing_north():
                media_vuelta()
                tmp=recoger_planta()
                if len(tmp)!=0:
                    if tmp[0]=="daisy":                
                        flores_0 += tmp[1]
                    if tmp[0]=="dandelion":                
                        flores_1 += tmp[1]
                    if tmp[0]=="leaf":                
                        flores_2 += tmp[1]
                move()
                
                turn_right()
                
            if is_facing_north():
                tmp=recoger_planta()
                if len(tmp)!=0:
                    if tmp[0]=="daisy":                
                        flores_0 += tmp[1]
                    if tmp[0]=="dandelion":                
                        flores_1 += tmp[1]
                    if tmp[0]=="leaf":                
                        flores_2 += tmp[1]
                move()
                
                turn_left()
       
    
    
    

print(recolectar_flores())


    
            
            
        
    
    
    