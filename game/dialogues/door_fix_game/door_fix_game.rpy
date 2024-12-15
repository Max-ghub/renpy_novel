default html_state = DoorFixGameState("HTML")
default css_state = DoorFixGameState("CSS", required_games=[html_state.name])
default js_state = DoorFixGameState("JavaScript", required_games=[html_state.name, css_state.name])
default completed_games = []

default description = "Первым делом нужно создать элемент двери. Выбери с помощью чего мы будет это делать."
label door_fix_game(description = description):
    menu:
        with Dissolve(0.25)
        "[description]"
        # HTML
        "[html_state.get_title(completed_games)]":
            if is_show_complated(html_state):
                call door_fix_game()
                return
            
            "HTML нужен, чтобы создавать различные элементы: текст, картинки, кнопки и так далее.
            В нашем случае — создать дверь, в которую мы затем украсим и сделаем её функциональной."
            call door_fix_game_html
            $ html_state.set_completed()
            $ completed_games.append(html_state.name)
            call door_fix_game("Дверь создали, теперь нужно её стилизовать и сделать анимацию для открытия.")

        # CSS
        "[css_state.get_title(completed_games)]":
            if is_show_watched(css_state):
                call door_fix_game("Начни с HTML, чтобы создать дверь.")
                return
            if is_show_complated(css_state):
                call door_fix_game()
                return
            
            if css_state.is_accessible(completed_games):
                "CSS нужен для стилизации, анимации и эффектов. Сейчас нам предстоит отобразить нашу дверь и задать анимацию при её открытии."
                call door_fix_game_css
                $ css_state.set_completed()
                $ completed_games.append(css_state.name)
                call door_fix_game("Хорошо, стиль готов. Теперь двигаемся дальше. Пусть эта дверь ещё и заработает как надо.")
            else:
                "CSS используется для стилизации, но нам пока что нечего стилизовать. Начни с HTML, с помощью его можно создать дверь."
                $ css_state.set_watched()
                call door_fix_game

        # JS
        "[js_state.get_title(completed_games)]":
            if is_show_watched(js_state):
                call door_fix_game("Сначала создай основу с помощью HTML и придай ей стиль с помощью CSS")
                return

            if js_state.is_accessible(completed_games):
                "JavaScript (JS) нужен, чтобы оживить элементы, добавив им функционал. В нашем случае сделать так, чтобы дверь могла открываться при нажатии."
                call door_fix_game_js
                $ js_state.set_completed()
                $ completed_games.append(js_state.name)
                return
            else:
                "JavaScript нужен, чтобы оживить элементы, добавив им функциональность. Но сначала создай основу с помощью HTML и придай ей стиль с помощью CSS, чтобы было чему добавлять функционал."
                $ js_state.set_watched()
                call door_fix_game
    return
