init python:
    class DoorFixGameState:
        def __init__(self):
            self.html_passed = False
            self.css_passed = False
            self.js_passed = False
            self.css_watched = False
            self.js_watched = False

        def show_html(self):
            """Проверяет нужно ли отображать запуск CSS этапа"""
            return not html_passed

        def show_css(self):
            """Проверяет нужно ли отображать запуск CSS этапа"""
            return not self.css_passed and (self.html_passed or not self.css_watched)

        def show_js(self):
            """Проверяет нужно ли отображать запуск JS" этапа """
            return self.css_passed or not self.js_watched

        def show_css_watched(self):
            """Проверяет нужно ли отображать этап CSS просмотренным"""
            return not self.html_passed and not self.css_passed and self.css_watched

        def show_js_watched(self):
            """Проверяет нужно ли отображать этап JS просмотренным"""
            return not self.css_passed and self.js_watched
        
        def show_html_compeated(self):
            """Проверяет нужно ли отображать этап HTML пройденным"""
            return self.html_passed

        def show_css_compeated(self):
            """Проверяет нужно ли отображать этап CSS пройденным"""
            return self.css_passed

        def show_js_compeated(self):
            """Проверяет нужно ли отображать этап JS пройденным"""
            return self.js_passed