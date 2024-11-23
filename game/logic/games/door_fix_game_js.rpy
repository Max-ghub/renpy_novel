label door_fix_game_js:
    menu:
        "Выберите способ назначения события на дверь:"
        
        # Полностью верный
        "1. document.querySelector('.door').addEventListener('click', openDoor);" if not dfg_watched_first:
            ba "Отлично! Ты использовал современный и удобный способ. Дверь теперь открывается по клику, всё работает как надо!"
            sp "Согласен. Такой подход я готов поставить в пример остальным. Красота и логика в одном флаконе!"
            $ dfg_watched_first = True
        
        # Верный, но стилистически неверный
        "2. document.querySelector('.door').onclick = openDoor;" if not dfg_watched_second:
            ba "Работает! Событие привязано, дверь открывается, и это главное!"
            sp "Но записывать обработчик прямо в свойство элемента — это старый стиль. Мы ведь хотим, чтобы код выглядел современно и поддерживаемо."
            $ dfg_watched_second = True
            menu:
                "Оставить всё как есть":
                    sp "Ну ладно, пусть так. Но я предупреждаю: такой стиль может вызвать вопросы на ревью."
                "Исправить ошибку":
                    sp "Вот это другой разговор. Давай сделаем всё на высшем уровне."
                    call door_fix_game_js
        
        # Похожий на верный
        "3. document.querySelector('.door').addEventListener('click', openDoor); openDoor();" if not dfg_watched_third:
            ba "Ты зачем сразу вызываешь функцию? Дверь открывается автоматически, даже без клика. Это явно не то, что нужно."
            $ dfg_watched_third = True
            call door_fix_game_js
        
        # С явной ошибкой
        "4. document.querySelector('.door').addEventListener('hover', openDoor);" if not dfg_watched_fourth:
            ba "Событие 'hover'? Ты хочешь, чтобы дверь открывалась, как только на неё посмотрят? Это же не автоматическая дверь в супермаркете!"
            $ dfg_watched_fourth = True
            call door_fix_game_js
        
        # Абсурдный
        "5. openDoor();" if not dfg_watched_fifth:
            ba "Ну ты просто вызвал функцию. Конечно, дверь открылась, но при чём тут событие? Ты забыл привязать функцию к клику."
            sp "Это не решение, это обман! Вернись и сделай правильно."
            $ dfg_watched_fifth = True
            call door_fix_game_js

    return
