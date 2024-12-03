init python:
    class DoorFixGameState:
        def __init__(self, name, required_games=None):
            self.name = name
            self.required_games = required_games if required_games else []
            self.selected_options = set()
            self.correct_answer_selected = False
            self.watched = False

        def select_option(self, option, is_correct=False):
            self.selected_options.add(option)
            if is_correct:
                self.correct_answer_selected = True

        def is_accessible(self, completed_games):
            return all(game in completed_games for game in self.required_games)

        def is_completed(self):
            return self.correct_answer_selected

        def is_watched(self):
            return self.watched

    def is_show_game(state):
        return not state.is_completed() and (not state.is_watched() or state.is_accessible(completed_games))
    def is_show_watched(state):
        return not state.is_completed() and not state.is_accessible(completed_games) and state.is_watched()
    def is_show_complated(state):
        return state.is_completed()

default html_game_state = DoorFixGameState("HTML")
default css_game_state = DoorFixGameState("CSS", required_games=[html_game_state.name])
default js_game_state = DoorFixGameState("JavaScript", required_games=[html_game_state.name, css_game_state.name])
default completed_games = []

default responder = ba
default description = "Давай выберем с чего начнём."
label door_fix_game(responder = responder, description = description):
    menu:
        responder "[description]"

        # HTML
        "HTML" if is_show_game(html_game_state):
            sp "Начнём с основы. Без HTML структуры наша дверь даже не будет существовать!"
            call door_fix_game_html
            $ completed_games.append(html_game_state.name)
            call door_fix_game(ba, "HTML готов. Что дальше?")

        "HTML (завершено)" if is_show_complated(html_game_state):
            call door_fix_game

        # CSS
        "CSS" if is_show_game(css_game_state):
            if css_game_state.is_accessible(completed_games):
                sp "А теперь моё любимое. Давай зададим вид нашей двери, а то сейчас она больше похожа на коробку из-под картона."
                call door_fix_game_css
                $ completed_games.append(css_game_state.name)
                call door_fix_game(ba, "Хорошо, стиль готов. Теперь двигаемся дальше. Пусть эта дверь ещё и заработает как надо.")
            else:
                sp "Ой, я хоть и люблю всё стилизовать, но ты хочешь начать это делать до того, как мы создали дверь? Давай сначала создадим её, а потом уже перейдём сюда."
                em "Да, ты прав."
                $ css_game_state.watched = True
                call door_fix_game

        "CSS (просмотрено)" if is_show_watched(css_game_state):
            call door_fix_game(sp, "Мы же договорились, что сначала создаём дверь, а потом уже работаем над стилем. Давай придерживаться плана.")

        "CSS (завершено)" if is_show_complated(css_game_state):
            call door_fix_game

        # JS
        "JavaScript" if is_show_game(js_game_state):
            if js_game_state.is_accessible(completed_games):
                ba "Теперь займёмся функционалом. Пусть дверь открывается при нажатии. Что толку от неё, если она просто стоит?"
                call door_fix_game_js
                $ completed_games.append(js_game_state.name)
                ba "Готово. Теперь дверь открывается, как и должна. Вот это работа!"
            else:
                sp "Ты хочешь, чтобы дверь открывалась? Но её пока даже нет! Давай сначала создадим основу, добавим стиль, а потом займёмся функционалом."
                em "Согласен. Давай сделаем всё по порядку."
                $ js_game_state.watched = True
                call door_fix_game
        "JavaScript (просмотрено)" if is_show_watched(js_game_state):
            call door_fix_game(sp, "Сначала создаём дверь, потом стиль, потом функционал. Мы же договорились!")
        "JavaScript (завершено)" if is_show_complated(js_game_state):
            return

    return
