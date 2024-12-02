transform blink_pause:
    choice:
        3
    choice:
        renpy.random.randint(7, 10)
    choice:
        renpy.random.randint(7, 10)
    choice:
        renpy.random.randint(9, 15)
    choice:
        renpy.random.randint(9, 15)

transform blink(base, blink):
    base
    blink_pause 
    blink
    pause 0.2   
    repeat