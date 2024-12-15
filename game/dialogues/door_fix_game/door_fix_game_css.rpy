label door_fix_game_css:
    call screen dfg_menu_scroll({
        "title": "Выберите стили для двери в закрытом состоянии. В дальнейшем мы добавим её открытие.",
        "menu": [
            {
                "caption": '.door {{\n  width: 100px;\n  height: 200px;\n  background-image: url("door-closed.png");\n  background-size: cover;\n  transform-origin: left;\n  transition: transform 0.5s ease, background-image 0.5s ease;\n}',
                "action": Return("first")
            },
            {
                "caption": '.door {{\n  width: 100px;\n  height: 200px;\n  background-image: url("door-closed.png");\n  background-size: contain;\n  transform-origin: left;\n  transition: transform 0.5s ease;\n}',
                "action": Return("second")
            },
            {
                "caption": 'door {{\n  width: 100px;\n  height: 200px;\n  background-image: url("door-closed.png");\n  background-size: cover;\n  transform-origin: left bottom;\n  transition: transform 0.5s ease;\n}',
                "action": Return("third")
            },
            {
                "caption": '.door {{\n  width: 100px;\n  height: 200px;\n  background-image: url("door-closed.png");\n  background-size: cover;\n  transform-origin: left;\n  transition: transform 2s linear;\n}',
                "action": Return("fourth")
            },
        ]
    })
    $ result = _return

    if result == "first":
        "Отлично! Все параметры выглядят уместно: корректный фон, точка поворота и плавная анимация."
        call door_fix_game_css_continue
    elif result == "second":
        "Вариант близкий к нужному, но фон будет масштабироваться не всегда красиво, и анимация двери ограничена."
        call door_fix_game_css
    elif result == "third":
        "Селектор 'door' выглядит как нестандартный тег, а точка поворота снизу может дать странный визуальный эффект."
        call door_fix_game_css
    elif result == "fourth":
        "Плавное открытие есть, но переход слишком медленный и не учитывает смену фона."
        call door_fix_game_css

    return


label door_fix_game_css_continue:
    call screen dfg_menu_scroll({
        "title": "Теперь настройте стили для двери в открытом состоянии, учитывая предыдущие параметры.",
        "menu": [
            {
                "caption": '.door[[data-status="open"] {{\n  transform: rotateY(90deg);\n  background-image: url("door-open.png");\n}',
                "action": Return("first")
            },
            {
                "caption": '.door[[data-status="open"] {{\n  transform: rotateY(90deg);\n  background: url("door-open.png") center/cover;\n}',
                "action": Return("second")
            },
            {
                "caption": '.door[[data-status="open"] {{\n  transform: rotateY(100deg);\n  background-image: url("door-open.png");\n}',
                "action": Return("third")
            },
            {
                "caption": '.door[[data-status="open"] {{\n  transform: rotateY(90deg);\n  background-image: url("door_opened.png");\n}',
                "action": Return("fourth")
            },
        ]
    })

    $ result = _return

    if result == "first":
        "Превосходно! Дверь поворачивается ровно на 90°, а фон меняется на корректное изображение."
    elif result == "second":
        "Неплохо, но при масштабировании окна фон может отображаться непредсказуемо."
        call door_fix_game_css_continue
    elif result == "third":
        "Угол поворота нестандартный 100°, дверь может выглядеть немного криво."
        call door_fix_game_css_continue
    elif result == "fourth":
        "Изображение двери в открытом состоянии указано неверно {i}door_opened.png{/i}, может вызвать несоответствие задумке."
        call door_fix_game_css_continue

    return
