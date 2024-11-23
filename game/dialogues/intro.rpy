label intro:
    scene bg_office with fade

    show emrach at center with dissolve
    em "Начало рабочего дня. Надеялся, что свежая голова поможет, но нет."
    em "Дедлайн уже сегодня, а во фронтенде ошибка, которую я не могу найти уже три дня."

    play sound [ "door-knock.mp3", "door-open.mp3" ]
    pause 1
    show sergey at left with moveinleft
    sg "Доброе утро, Эмрах. Cдача проекта уже завтра. Как обстоят дела с ним?"
    em "Утро доброе, Сергей Геннадьевич. Ну... Всё идёт по плану. Доделываю последние детали"
    sg "Последние детали? Хорошо. Надеюсь, всё будет готово. Если что, не стесняйся обращаться за помощью."
    play sound "door-open.mp3"
    hide sergey with moveoutleft

    em "Последние детали... Если бы. Ошибка всё ещё там, и я понятия не имею, где искать."

    play music "computer-flicker.mp3"
    show flash_effect
    em "Что за шум? Почему всё вокруг мерцает?!"
    stop music

    play music "computer-flicker-grow.mp3" volume 0.1
    show flash_effect_grow
    em "Звуки становятся громче, свет всё ярче... Это уже не нормально!"
    em "Голова кружится... Что за чертовщина?!"
    stop music fadeout 1.5

    show full_flash_effect with Dissolve(1)

    return
