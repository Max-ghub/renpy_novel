label proxcity_arc_game_css:
    ba "Теперь нужно привести дверь в порядок. Давай зададим ей стиль, чтобы она выглядела как дверь. Что выберем?"

    menu:
        "Выберите CSS для стилизации двери:"
        
        # Полностью верный
        "1. .door {{ width: 100px; height: 200px; background-color: brown; }":
            ba "Превосходно! Теперь это действительно похоже на дверь. Всё выглядит как надо!"
            sp "Да, согласен. Код не только функционален, но и аккуратен. Молодец, Эмрах!"
        
        # Верный, но стилистика нарушена
        "2. .door {{ width: 100px; height: 200px; background: brown; }":
            ba "Ну, сработало, дверь выглядит как надо. Отлично, идём дальше!"
            sp "Стоп-стоп. Вместо 'background-color' тут написали просто 'background'. Работает, но это не совсем точно."
            ba "Работает же, а ты хочешь идеала? Решай, Эмрах, оставляем так или исправляем."
            menu:
                "Оставить всё как есть":
                    sp "Ну ладно, живите тогда с этим. Хотя я бы сделал лучше."
                "Исправить ошибку":
                    sp "Вот это другой разговор! Лучше сделать правильно."
                    call proxcity_arc_game_css
        
        # Похожий на верный
        "3. .door {{ width: 100px; background-color: brown; }":
            ba "Эй, высоты у двери нет! Теперь это просто коричневый прямоугольник. Попробуй ещё раз."
            call proxcity_arc_game_css
        
        # С явной ошибкой
        "4. .door {{ widht: 100px; height: 200px; background-color: brown; }":
            sp "Тут явная опечатка в 'widht'. Такой код даже не сработает!"
            call proxcity_arc_game_css
        
        # Абсурдный
        "5. .door {{ animation: spin 2s infinite; }":
            ba "Ага, дверь, которая крутится как волчок? Это точно не то, что нам нужно."
            call proxcity_arc_game_css

    return