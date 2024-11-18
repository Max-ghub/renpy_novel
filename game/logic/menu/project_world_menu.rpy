
define is_proxcity_arc = False
define is_project_world_vetrorosa = False
define is_project_world_turn_around = False

label project_world_menu:
    menu:
        "Где будем искать сначала?"

        "Пойти в город":
            return

        "Пойти к огньку":
            call project_world_vetrorosa
            return

        "Обернуться..." if not is_turn_around_scene:
            $ is_turn_around_scene = True
            call project_world_turn_around
            call project_world_menu

    return