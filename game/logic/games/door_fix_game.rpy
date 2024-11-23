init python:
    def can_start_css():
        return not dfg_css_passed and (dfg_html_passed or not dfg_css_watched)
    def watched_css():
        return not dfg_html_passed and not dfg_css_passed and dfg_css_watched

    def can_start_js():
        return dfg_css_passed or not dfg_js_watched
    def watched_js():
        return not dfg_css_passed and dfg_js_watched
        

default dfg_html_passed = False
default dfg_css_passed = False
default dfg_css_watched = False
default dfg_js_watched = False

label door_fix_game(responder = ba, answer = "Так, что будем исправлять сначала?"):
    $ dfg_watched_first = False
    $ dfg_watched_second = False
    $ dfg_watched_third = False
    $ dfg_watched_fourth = False
    $ dfg_watched_fifth = False
    
    menu:
        responder "[answer]"

        # HTML
        "HTML" if not dfg_html_passed:
            sp "Начнём с основы. Без HTML структуры наша дверь даже не будет существовать!"
            call door_fix_game_html
            $ dfg_html_passed = True
            call door_fix_game(ba, "Ну вот, дверь создана. Что дальше?")
        "HTML (завершено)" if dfg_html_passed:
            call door_fix_game(responder, answer)

        # CSS
        "CSS" if can_start_css():
            if dfg_html_passed:
                sp "А теперь моё любимое. Давай зададим вид нашей двери, а то сейчас она больше похожа на коробку из-под картона."
                call door_fix_game_css
                $ dfg_css_passed = True
                call door_fix_game(ba, "Хорошо, стиль готов. Теперь двигаемся дальше. Пусть эта дверь ещё и заработает как надо.")
            else:
                sp "Ой, я хоть и люблю всё стилизовать, но ты хочешь начать это делать до того, как мы создали дверь? Давай сначала создадим её, а потом уже перейдём сюда."
                em "Да, ты прав."
                $ dfg_css_watched = True
                call door_fix_game(responder, answer)
        "CSS (просмотрено)" if watched_css():
            call door_fix_game(sp, "Мы же договорились, что сначала создаём дверь, а потом уже работаем над стилем. Давай придерживаться плана.")
        "CSS (завершено)" if dfg_css_passed:
            call door_fix_game(responder, answer)

        # JS
        "JavaScript" if can_start_js():
            if dfg_css_passed:
                ba "Теперь займёмся функционалом. Пусть дверь открывается при нажатии. Что толку от неё, если она просто стоит?"
                call door_fix_game_js
                ba "Готово. Теперь дверь открывается, как и должна. Вот это работа!"
            else:
                if not dfg_html_passed:
                    sp "Ты хочешь, чтобы дверь открывалась? Но её пока даже нет! Давай сначала создадим основу, добавим стиль, а потом займёмся функционалом."
                    em "Согласен. Давай сделаем всё по порядку."
                else: 
                    sp "Функциональность — это важно, но, может, сначала сделаем дверь красивой? Так будет проще работать и смотреть на результат."
                    em "Да, ты прав. Давай сначала займёмся оформлением."
                $ dfg_js_watched = True
                call door_fix_game(responder, answer)
        "JavaScript (просмотрено)" if watched_js():
            if not dfg_html_passed:
                call door_fix_game(sp, "Сначала создаём дверь, потом стиль, потом функционал. Мы же договорились!")
            else:
                call door_fix_game(sp, "Уже обговаривали, что функционал делаем после стиля.")

    return
