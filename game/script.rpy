﻿label start:
    call intro

    call arrival
    menu:
        ba "Выбирай. Мы поддержим тебя на любом маршруте."

        "Отправиться в город":
            call arrival_go_city
            
        "Пойти к огоньку вдалеке":
            call arrival_go_vetrorosa
        
        "Попытаться выбраться":
            jump arrival_go_escape

    call door_fix_game

    return
