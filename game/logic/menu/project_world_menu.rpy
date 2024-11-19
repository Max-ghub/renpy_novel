$ turn_around_passed = True

menu project_world_menu:
    "Где будем искать сначала?"

    "Пойти в город":
        return

    "Пойти к огньку":
        call project_world_vetrorosa
        return
    
    "Обернуться..." if not turn_around_passed:
        call project_world_turn_around
        call project_world_menu
        return
