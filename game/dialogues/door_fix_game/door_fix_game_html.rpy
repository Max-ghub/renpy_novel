label door_fix_game_html:
    call screen dfg_menu({
        "title": "Выберите код для создания двери в HTML. В дальнейшем мы будем стилизовать дверь и делать возможным её открывать.",
        "menu": [
            {
                "caption": '<div class="door" data-openable="true" data-status="closed"></div>',
                "action": Return("first")
            },
            {
                "caption": '<div id="door" class="door"></div>',
                "action": Return("second")
            },
            {
                "caption": '<door data-openable="true" data-status="closed"></door>',
                "action": Return("third")
            },
            {
                "caption": 'div.door(data-openable="true", data-status="closed")',
                "action": Return("fourth")
            },
        ]
    })
    $ result = _return
    
    if result == "first":
        "{i}class{/i} задаёт стиль двери, {i}data-openable{/i} определяет возможность открытия, а {i}data-status{/i} показывает текущее состояние.
        Это верный вариант, он позволяет создавать любое количество дверей с нужным нам функционалом."
    elif result == "second":
        "{i}id{/i} позволяет задать функциональность, а {i}class{/i} — стиль.
        Но {i}id{/i} можно использовать только для одного элемента, что нехорошо, если мы захотим добавить ещё одну дверь.
        Попробуй выбрать более подходящий вариант."
    elif result == "third":
        "{i}door{/i} — нестандартный тег, его использование некорректно. {i}data-status{/i} показывает состояние двери, но без {i}class{/i} сложно задать стиль,
        а нестандартные теги вызывают проблемы с совместимостью. Выбери что-то другое."
        call door_fix_game_html
    elif result == "fourth":
        "Вариант был бы полностью корректен для фреймворка {i}Pug{/i}, который используется для упрощения написания {i}HTML{/i},
        но мы работаем с нативным {i}HTML{/i}, поэтому этот вариант нам не подходит."
        call door_fix_game_html

    return
    with dissolve