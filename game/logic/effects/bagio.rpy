transform bagio_dynamic_show:
    bagio_show_left
    bagio_dynamic

transform bagio_dynamic:
    parallel:
        ease 3.5 yalign 0.375
        ease 3.5 yalign 0.525
        repeat
    parallel:
        ease 4 rotate -0.8
        ease 4 rotate 0.8
        repeat
    parallel:
        ease 5 xalign -0.090
        ease 5 xalign -0.050
        repeat

transform bagio_show_left:
    xalign -0.15 yalign -0.5
    zoom 0.1
    alpha 0.0
    rotate -720
    parallel:
        easeout 1.25:
            yalign 0.75
            xalign 0.1
    parallel:
        easeout 1.25 zoom 1.0
    parallel:
        easeout 1.25 alpha 1.0
    parallel:
        easein 1.25 rotate 10
