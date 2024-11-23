label start:
    call office_intro

    call digital_arrival

    # Появление меню выбора пути
    menu:
        ba "Выбирай. Мы поддержим тебя на любом маршруте."

        "Отправиться в город":
            call go_to_city
            
        "Пойти к огоньку вдалеке":
            call go_to_light
        
        "Попытаться выбраться":
            jump escape_project

    call door_fix_game

    return
