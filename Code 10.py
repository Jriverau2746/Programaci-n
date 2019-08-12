'''En esta oportunidad, Reeborg debe ir a una posición (x,y). y poner una estrella en dicha  
coordenada, luego debe vover a la coordenada (1,1).'''

'''
pre: mira hacia el norte y sale desde la coordenada (1,1). Definir (x,y).
post: reeborg, vuelve a la coordenada (1,1) e informa la distancia entre (1,1) y (x,y)
'''

def función_D(x,y):
    
    Coordenada_x=x
    Coordenada_y=y
    
    while Coordenada_y>1:
        move()
        Coordenada_y=Coordenada_y-1
    else:
        turn_left()
        turn_left()
        turn_left()
        while Coordenada_x>1:
            move()
            Coordenada_x=Coordenada_x-1
        put()
        repeat 2:
            turn_left()
            turn_left()
            turn_left()
            while front_is_clear():
                move()
                
    print("Distancia:", (((y-1)*2)+((x-1)*2))**(1/2) )

función_D(5,6)

'''Autor: Juan F. Rivera'''
'''Fecha: 12/08/2019'''

            
