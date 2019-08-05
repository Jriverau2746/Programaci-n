'''Este mundo está diseñado para que el robot, Reeborg, 
llegue al centro del mundo y coloque el objeto que lleva'''




''' 
Funcionalidad: LLegar al centro y colocar el objeto    
pre: front is clear 
pos: reeborg deja el objeto en el centro 
'''

def vuelta():
    turn_left()
    turn_left()
 

def contar_pasos():
    contador=1    
    
    while front_is_clear():
        move()
        contador = contador+1

    vuelta()
    mitad = int(contador/2)
   
    while mitad>0:
        move()
        mitad=mitad-1
    
    put()

contar_pasos()    
    


'''Autor: Juan F. Rivera'''
'''Fecha: 05/07/2019'''

    