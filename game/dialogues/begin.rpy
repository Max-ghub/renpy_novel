label begin:
    scene office with irisout
    play music "audio/office_music.mp3" volume 0.1 fadein 0.5

    show emrach sad at center with dissolve
    em "Начало рабочего дня. Надеялся, что свежая голова поможет, но нет."
    em "Дедлайн уже сегодня, а во фронтенде ошибка, которую я не могу найти уже три дня."

    play sound "door_knock_open.mp3" volume 0.3
    pause 2

    show sergey at left with moveinleft
    show emrach with dissolve
    sg "Доброе утро, Эмрах. Cдача проекта уже завтра. Как обстоят дела с ним?"
    em "Утро доброе, Сергей Геннадьевич. Ну... Всё идёт по плану. Доделываю последние детали."

    show sergey happy with dissolve
    sg "Последние детали? Хорошо. Надеюсь, всё будет готово. Если что, не стесняйся обращаться за помощью."
    hide sergey happy with moveoutleft

    play sound "door_open.mp3" volume 0.3
    pause 1

    show emrach sad with dissolve
    em "Последние детали... Если бы. Ошибка всё ещё там, и я понятия не имею, где искать."
    stop music fadeout 1.5

    $ renpy.sound.play("audio/flickering_sound.mp3", channel='sound', loop=True, fadein=1.0)
    $ renpy.sound.set_volume(0.3, delay=0, channel='sound')
    show flash_effect
    show emrach surprised with Dissolve(3.0)

    em "Что за шум? Почему всё вокруг мерцает?!"

    $ renpy.sound.set_volume(1.0, delay=1.5, channel='sound')
    show flash_effect_grow

    show emrach scared with dissolve
    em "Звуки становятся громче, свет всё ярче... Это уже не нормально!"
    em "Голова кружится... Что за чертовщина?!"

    stop sound fadeout 1.0
    pause 1.0
    play sound "audio/movingе_next_location.mp3" 
    scene full_flash with Fade(0.5, 0.5, 0, color="#fff")

    return
