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


image emrach = blink(
        "/characters/emrach/emrach.png",
        "/characters/emrach/emrach blink.png",
    )
image bagio = blink(
        "/characters/bagio/bagio.png",
        "/characters/bagio/bagio blink.png",
    )
image spaghettinio = blink(
        "/characters/spaghettinio/spaghettinio.png",
        "/characters/spaghettinio/spaghettinio blink.png",
    )
image sergey = blink(
        "/characters/sergey/sergey.png",
        "/characters/sergey/sergey blink.png",
    )