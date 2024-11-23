label door_fix_game_css:
    menu:
        "Выберите CSS для стилизации двери:"
        
        # Верный
        "1. .door {{ width: 100px; height: 200px; background-color: brown; }" if not dfg_watched_first:
            ba "Превосходно! Теперь это действительно похоже на дверь. Всё выглядит как надо!"
            sp "Да, согласен. Код не только функционален, но и аккуратен. Молодец, Эмрах!"
            $ dfg_watched_first = True
        
        # Верный, но стилистика нарушена
        "2. .door {{ width: 100px; height: 200px; background: brown; }" if not dfg_watched_second:
            ba "Ну, сработало, дверь выглядит как надо. Отлично, идём дальше!"
            sp "Стоп-стоп. Вместо 'background-color' тут написали просто 'background'. Работает, но это не совсем точно."
            ba "Работает же, а ты хочешь идеала? Решай, Эмрах, оставляем так или исправляем."
            $ dfg_watched_second = True
            menu:
                "Оставить всё как есть":
                    sp "Ну ладно, живите тогда с этим. Хотя я бы сделал лучше."
                "Исправить ошибку":
                    sp "Вот это другой разговор! Лучше сделать правильно."
                    call door_fix_game_css
        
        # Похожий на верный
        "3. .door {{ width: 100px; background-color: brown; }" if not dfg_watched_third:
            ba "Эй, высоты у двери нет! Теперь это просто коричневый прямоугольник. Попробуй ещё раз."
            $ dfg_watched_third = True
            call door_fix_game_css
        
        # С явной ошибкой
        "4. .door {{ widht: 100px; height: 200px; background-color: brown; }" if not dfg_watched_fourth:
            sp "Тут явная опечатка в 'widht'. Такой код даже не сработает!"
            $ dfg_watched_fourth = True
            call door_fix_game_css
        
        # Абсурдный
        "5. .door {{ animation: spin 2s infinite; }" if not dfg_watched_fifth:
            ba "Ага, дверь, которая крутится как волчок? Это точно не то, что нам нужно."
            $ dfg_watched_fifth = True
            call door_fix_game_css

    return
