label door_fix_game_js:
    menu:
        "Выберите способ назначения события на дверь:"
        
        # Верный
        "1. document.querySelector('.door').addEventListener('click', openDoor);":
            ba "Отлично! Ты использовал современный и удобный способ. Дверь теперь открывается по клику, всё работает как надо!"
            sp "Согласен. Такой подход я готов поставить в пример остальным. Красота и логика в одном флаконе!"
            $ js_game_state.select_option("correct", is_correct=True)
        
        # Верный, но стилистически неверный
        "2. document.querySelector('.door').onclick = openDoor;":
            ba "Работает! Событие привязано, дверь открывается, и это главное!"
            sp "Но записывать обработчик прямо в свойство элемента — это старый стиль. Мы ведь хотим, чтобы код выглядел современно и поддерживаемо."
            menu:
                "Оставить всё как есть":
                    sp "Ну ладно, пусть так. Но я предупреждаю: такой стиль может вызвать вопросы на ревью."
                    $ js_game_state.select_option("partial", is_correct=True)
                "Исправить ошибку":
                    sp "Вот это другой разговор. Давай сделаем всё на высшем уровне."
                    call door_fix_game_js
        
        # Похожий на верный
        "3. document.querySelector('.door').addEventListener('click', openDoor); openDoor();":
            ba "Ты зачем сразу вызываешь функцию? Дверь открывается автоматически, даже без клика. Это явно не то, что нужно."
            $ js_game_state.select_option("close")
            call door_fix_game_js
        
        # С явной ошибкой
        "4. document.querySelector('.door').addEventListener('hover', openDoor);":
            ba "Событие 'hover'? Ты хочешь, чтобы дверь открывалась, как только на неё посмотрят? Это же не автоматическая дверь в супермаркете!"
            $ js_game_state.select_option("wrong")
            call door_fix_game_js
        
        # Абсурдный
        "5. openDoor();":
            ba "Ну ты просто вызвал функцию. Конечно, дверь открылась, но при чём тут событие? Ты забыл привязать функцию к клику."
            sp "Это не решение, это обман! Вернись и сделай правильно."
            $ js_game_state.select_option("absurd")
            call door_fix_game_js

    return
