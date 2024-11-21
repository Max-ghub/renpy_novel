label office_intro:
    scene bg_office with fade

    show emrach at center with dissolve
    em "Очередной день в офисе. Тот же стол, те же задачи..."
    em "Дедлайн уже близко, а у меня проект всё ещё не доделан. Я даже не знаю, с чего начать..."

    play sound [ "door-knock.mp3", "door-open.mp3" ]
    pause 1
    show sergey at left with moveinleft
    sg "Эмрах, привет, сдача проекта уже завтра. Как обстоят дела с ним?"
    em "Эээ... Ну... Всё идёт по плану, Сергей Геннадьевич."
    sg "По плану, значит. Отлично! Надеюсь, всё будет готово. Если что, не стесняйся обращаться за помощью."
    play sound "door-open.mp3"
    hide sergey with moveoutleft

    em "Дедлайн завтра... Как я всё успею?!"

    # Экран начинает мерцать
    play music "computer-flicker.mp3"
    show flash_effect
    em "Что это за шум? Компьютер... он мигает. Что происходит?!"
    stop music

    # Экран мерцает сильнее
    play music "computer-flicker-grow.mp3" volume 0.1
    show flash_effect_grow
    em "Нет, только не это! Надеюсь, техника не сломалась. Мне только этого не хватало!"
    stop music fadeout 1.5

    # Вспышка света
    show full_flash_effect with Dissolve(1)
    em "Что за...?! Всё так ярко!"

    return
