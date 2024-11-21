label start:
    call office_intro

    call digital_arrival

    # Появление меню выбора пути
    menu:
        "Обернуться и попытаться выбраться":
            jump escape_project

        "Пойти к огоньку вдалеке":
            call go_to_light

        "Отправиться в город":
            call go_to_city

    call city_exploration

    call journey_end

    call return_to_reality

    call epilogue

    return
