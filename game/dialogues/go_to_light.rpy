label go_to_light:
    scene bg_misty_path with fade
    em "Этот огонёк... Он кажется странно притягательным. Может, это выход?"

    ba "Плохая идея, если честно. Куда ты нас тащишь?"
    sp "Возможно, там кто-то или что-то, что может помочь."

    scene bg_lighthouse with dissolve
    show ve at center
    ve "Добро пожаловать, путники. Я Ветророза, хранитель порядка и гармонии."

    em "Вы можете помочь нам с проектом?"

    ve "Возможно. Ваш путь труден, но я направлю вас. Следуйте в город, где вы найдёте ответы."

    ba "А нельзя поконкретнее? Какая у вас любовь к загадкам..."
    sp "Слушай, Багио. В её словах всё предельно ясно. Нам в город."

    hide ve
    scene bg_city with fade
    em "Город... Теперь осталось найти Радик."
    return