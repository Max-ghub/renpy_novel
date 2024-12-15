transform bagio_dynamic:
    parallel:
        ease 4:
            xoffset -30
            rotate -2
        ease 4:
            xoffset 30
            rotate 2
        repeat 
    parallel:
        ease 3.5 yoffset 15
        ease 3.5 yoffset -15
        repeat

transform bagio_dynamic_show:
    xalign -0.15 yalign -0.5
    zoom 0.1
    alpha 0.0
    rotate -720

    parallel:
        easeout 1.25 align (0.040, 0.40)
    parallel:
        easein 1.25 rotate -10
    parallel:
        easeout 1.25:
            zoom 1.0
            alpha 1.0
    pause 0.0
    parallel:
        easein 1.5:
            align (0.0, 0.25)
            rotate -2
    parallel:
        bagio_dynamic