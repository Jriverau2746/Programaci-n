"""En esta oportunidad, Reeborg debe atravesar un campo de 5x5 en zig-zag, en el que puede encontrar los siguientes elementos:

Manzana (apple): Es el alimento de Reeborg, le proporciona la energía suficiente para desplazarse por su mundo. Una manzana le da la energía para caminar hasta 7 casillas. Puede comerse hasta 3 manzanas seguidas y puede recolectar las que no se coma.
Goloso (token): Se come todas las manzanas que Reeborg haya recolectado hasta ese punto.
Tulipán (tulip): Le generan una fuerte alergia a Reeborg. Le restan energía: cada movimiento le cuesta el doble. Se vuelve inmune cuando consigue la medicina.
Medicina (triangle): Es el antídoto cuando se enferma a causa de un Tulipán. También funciona como vacuna cuando aún no se ha enfermado."""
e=7
while front_is_clear():
    if e>0:
        move()
        e=e-1
        while object_here("apple"):
            take("apple")
            e=e+7
        while object_here("tulip"):
            take("tulip")
            e=e/2
while wall_in_front():
    turn_left()
if e>0:
    move()
    e=e-1
turn_left()




            
