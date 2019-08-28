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

def subir():
    contador_p=0
    repeat 4:
        while not front_is_clear():
            turn_left()
            move()
            turn_left()
            turn_left()
            turn_left()
        else: 
            while front_is_clear():
                
                if object_here("daisy"):
                    take()
                    contador_p=contador_p+1
                if object_here("beeper"):
                    take()
                    contador_p=contador_p*2
                if object_here("token"):
                    take()
                    contador_p=contador_p-5
                move()
                if object_here("daisy"):
                    take()
                    contador_p=contador_p+1
                if object_here("daisy"):
                    take()
                    contador_p=contador_p+1
                if object_here("daisy"):
                    take()
                    contador_p=contador_p+1
                if object_here("beeper"):
                    take()
                    contador_p=contador_p*2
                if object_here("beeper"):
                    take()
                    contador_p=contador_p*2
                if object_here("token"):
                    take()
                    contador_p=contador_p-5
    return contador_p
    
                    
print(subir())
