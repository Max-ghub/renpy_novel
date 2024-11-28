label begin:
    scene office with irisout
    show emrach at center with dissolve
    em "Начало рабочего дня. Надеялся, что свежая голова поможет, но нет."
    em "Дедлайн уже сегодня, а во фронтенде ошибка, которую я не могу найти уже три дня."

    play sound "door_knock_open.mp3" volume 0.3
    pause 2
    show sergey at left with moveinleft
    sg "Доброе утро, Эмрах. Cдача проекта уже завтра. Как обстоят дела с ним?"
    em "Утро доброе, Сергей Геннадьевич. Ну... Всё идёт по плану. Доделываю последние детали."
    sg "Последние детали? Хорошо. Надеюсь, всё будет готово. Если что, не стесняйся обращаться за помощью."
    hide sergey with moveoutleft
    play sound "door_open.mp3" volume 0.3
    pause 1

    em "Последние детали... Если бы. Ошибка всё ещё там, и я понятия не имею, где искать."

    play sound "computer-flicker.mp3" loop volume 0.5 fadein 1.0
    show flash_effect
    em "Что за шум? Почему всё вокруг мерцает?!"

    play sound "computer-flicker.mp3" loop volume 1
    show flash_effect_grow
    em "Звуки становятся громче, свет всё ярче... Это уже не нормально!"
    em "Голова кружится... Что за чертовщина?!"
    stop music fadeout 1.5

    scene full_flash
    with Fade(1.5, 2, 0, color="#fff")
    stop sound fadeout 0.5
    return
