def poner_caminar():
    put("token")    
    moverse()
    put()
    devolverse()
    moverse()
def moverse():
    while wall_in_front():
        turn_left()
    while front_is_clear():
        move()
        if object_here():
            recorrido()
def devolverse():
    turn_left()
    turn_left()
    while wall_in_front():
        turn_left()   
def recorrido():
    while object_here("token"):
        take("token")
        turn_left()
        turn_left()
        move()
        if object_here():
            take()
            put()
            if not right_is_clear():
                break
            else:
                if is_facing_north():
                    break
                turn_left()
                turn_left()
                turn_left()
                moverse()
                put()              
        else:
            put()
            moverse()