'''Este mundo está diseñado para que el robot, Reeborg, 
camine cuando se genere en una posición que no tenga pared
en su frente. Es una caminata de 5*5'''
def walk():
    if front_is_clear():
        repeat 4:
            move()                
walk()
'''Autor: Juan F. Rivera'''
'''Fecha: 29/07/2019'''

    