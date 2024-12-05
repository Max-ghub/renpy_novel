label door_fix_game_html:
    menu:
        "Выберите код для создания двери в HTML:"

        # Верный
        "<div id='door' class='door'></div>":
            sp "Вот это я понимаю! Всё чётко: у двери есть `class` — для стилизации и `id` — чтобы ею можно было управлять. Отличное решение!"
            ba "Согласен. С таким кодом удобно работать: `class` делает код более гибким для оформления, а `id` подходит для действий. Отличная работа!"
            $ html_game_state.select_option("correct", is_correct=True)
            return

        # Частично верный
        "<div class='door'></div>":
            ba "Работает. Дверь есть и выглядит нормально. Пошли дальше."
            sp "Нормально? А как ты будешь задавать действия для этой двери? Профессиональные разработчики избегают вешать события на `class`, потому что это может затронуть несколько элементов с одинаковым классом."
            ba "Ну, звучит умно, но сейчас ведь она одна и работает. Эмрах, решай сам: оставить или переделать."
            sp "Если хочешь, чтобы всё было не только рабочим, но и удобным для дальнейшей разработки, лучше это исправить. Что выберешь?"
            menu:
                "Оставить как есть":
                    ba "Вот это подход! Работает и ладно. Идём дальше."
                    sp "Твой выбор. Но, предупреждаю, работать с этим дальше будет неудобно."
                    $ html_game_state.select_option("partial", is_correct=True)
                    return
                "Исправить ошибку":
                    sp "Прекрасно! Именно так поступают те, кто думает на перспективу. Давай исправим."
                    call door_fix_game_html

        # Похожий на верный
        "<section class='door'></section>":
            ba "Ну, дверь на месте, отобразилась. А что ещё надо? Всё работает!"
            sp "Работает-то работает, но `<section>` — это тег для разделов страницы, вроде главы, раздела статей или блока контента."
            ba "Но она же есть и делает, что нужно. Какая разница?"
            sp "Разница в том, что <section> предназначен для разделов контента, а дверь — это отдельный объект интерфейса, а не часть структуры"
            $ html_game_state.select_option("close")
            call door_fix_game_html

        # С явной ошибкой
        "<a id='door' href='#'>Дверь</a>":
            sp "`a` - ссылка. Этот тег больше подходит для перехода между страницами, а не для двери. Такое точно не сработает."
            ba "Да, это точно мимо. Попробуй что-то другое."
            $ html_game_state.select_option("wrong")
            call door_fix_game_html

        # Абсурдный
        "<marquee class='door'>Дверь</marquee>":
            sp "`<marquee>` - маркированный текст для двери. Ты уверен, что мы не в 90-х? Попробуй ещё!"
            ba "Да уж, из всех вариантов это точно худший. Соберись и выбери что-то более подходящее."
            $ html_game_state.select_option("absurd")
            call door_fix_game_html

    return
