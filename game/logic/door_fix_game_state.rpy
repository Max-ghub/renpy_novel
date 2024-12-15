init python:
    class DoorFixGameState:
        def __init__(self, name, required_games=None):
            self.name = name
            self.title = name
            self.watched = False
            self.completed = False
            self.required_games = required_games if required_games else []

        def set_watched(self):
            self.watched = True

        def is_watched(self):
            return self.watched

        def set_completed(self):
            self.completed = True
            
        def is_completed(self):
            return self.completed

        def is_accessible(self, completed_games):
            return all(game in completed_games for game in self.required_games)

        def get_title(self, completed_games):
            if self.completed:
                return f"{{s}}{self.name}{{/s}}"
            elif not self.completed and self.watched and not self.is_accessible(completed_games):
                return f"{self.name} (просмотрено)"
            return self.title

init python:
    def is_show_watched(state):
        return not state.is_completed() and not state.is_accessible(completed_games) and state.is_watched()
    def is_show_complated(state):
        return state.is_completed()