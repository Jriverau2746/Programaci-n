'''
Descripción:
Reeborg debe llegar hasta el final de la escalera, 
es decir, la casilla (10, 4); recolectar los elementos
que encuentre en su camino y calcular el número total 
de puntos que estos elementos representan. Cada 
elemento afecta el número total de puntos de la 
siguiente manera:

Margarita: Cada margarita suma un punto.
Beeper: Cada beeper duplica el número de puntos 
        acumulados hasta ese instante.
Carita: Cada carita resta 5 puntos.

'''


def recolectar(valor_inicial):
    
    contador_puntos=valor_inicial
    
    while front_is_clear():
        
        while object_here("daisy"):
            take()
            contador_puntos=contador_puntos+1
            
        while object_here("beeper"):
            take()
            contador_puntos=contador_puntos+contador_puntos
            
        while object_here("token"):
            take()
            contador_puntos=contador_puntos-5
        
        move()
        
        while object_here("daisy"):
            take()
            contador_puntos=contador_puntos+1
            
        while object_here("beeper"):
            take()
            contador_puntos=contador_puntos+contador_puntos
            
        while object_here("token"):
            take()
            contador_puntos=contador_puntos-5    
            
    return contador_puntos  

def subir_escalon():
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()

    
def total():
    total=0
    repeat 4:
        subir_escalon()
        total=recolectar(total)
        print(total)
total()

    
    