default html_passed = False
default css_passed = False
default css_watched = False
default js_watched = False

label proxcity_arc_game_menu(description = "Что вы хотите исправить сначала?"):
    menu:
        "[description]"

        # HTML
        "HTML" if not html_passed:
            ba "Для начала нужно создать саму дверь. Без HTML структуры её просто не существует!"
            call proxcity_arc_game_html
            $ html_passed = True
            call proxcity_arc_game_menu("Отлично, HTML сделали. Давай перейдём к остальному")

        "HTML (завершено)" if html_passed:
            call proxcity_arc_game_menu(description)

        # CSS
        "CSS" if not css_passed and (html_passed or not css_watched):
            if html_passed:
                ba "Дверь есть, но она пока выглядит, как коробка из картона. Нам нужно привести её в порядок."
                call proxcity_arc_game_css
                $ css_passed = True
                call proxcity_arc_game_menu("Отлично, CSS осилили, остался JavaScript")
            else:
                sp "Ой-ой, ты хочешь стилизовать то, чего нет? Давай сначала сделаем дверь!"
                $ css_watched = True
                call proxcity_arc_game_menu(description)

        "CSS (просмотрено)" if not html_passed and not css_passed and css_watched:
            call proxcity_arc_game_menu("Сначала нужно создать дверь перед заданием ей стилей!")
        
        "CSS (завершено)" if css_passed:
            call proxcity_arc_game_menu(description)

        # JS
        "JavaScript" if css_passed or not js_watched:
            if css_passed:
                ba "Теперь нужно назначить событие на дверь. Функция для открытия уже готова, тебе осталось только правильно привязать её к двери. Как это сделать?"
                call proxcity_arc_game_js
                ba "Отлично, ты справился!"
            else:
                sp "Ты правда хочешь оживить дверь, которая даже не красивая? Сначала займись стилями."
                $ js_watched = True
                call proxcity_arc_game_menu(description)

        "JavaScript (просмотрено)" if not css_passed and js_watched:
            if not html_passed:
                call proxcity_arc_game_menu("Ты ещё не создал дверь, а уже хочешь её начать открывать!")
            else:
                call proxcity_arc_game_menu("Правильнее будет сначала задать стили для двери")
    return