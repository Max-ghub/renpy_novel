transform shake:
    on show:
        linear 0.05 xpos 0.48
        linear 0.05 xpos 0.52
        repeat 4
    on hide:
        linear 0.1 xpos 0.5



label start:
    # Пролог
    call prologue

    # Появление Багио и Спагетио
    call introduction_bagio_spagetio

    # Выбор пути
    menu:
        "Обернуться и попытаться выбраться":
            jump escape_project

        "Пойти к огоньку вдалеке":
            call go_to_light
            call go_to_city

        "Отправиться в город":
            call go_to_city

    # Исправление и обучение
    call fix_and_learn

    # Завершение путешествия
    call journey_end

    # Возвращение в реальность
    call return_to_reality

    # Эпилог
    call epilogue

    # Конец игры
    return
