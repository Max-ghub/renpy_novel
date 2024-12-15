transform spagetinio_dynamic:
    align (0.99, 0.95)
    parallel:
        renpy.random.randint(8, 20)
        easein 0.30 yoffset -200
        easeout 0.30 yoffset 0
        repeat
    parallel:
        renpy.random.randint(8, 20)
        choice:
            linear 0.001 xzoom 1
        choice:
            linear 0.001 xzoom -1
        repeat
    
transform spagetinio_dynamic_show:
    align (1.25, 1.5)
    easeout 1.0:
        align (0.99, 0.95)
    pause 0.1
    spagetinio_dynamic