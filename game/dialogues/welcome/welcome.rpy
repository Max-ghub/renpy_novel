label welcome:
    call welcome_meeting_boss
    call welcome_meeting_debuggers

    menu:
        "ЧТО ЖЕ ДЕЛАТЬ?"

        "Вырваться из рук":
            call welcome_ending
        "Довериться":
            return
            
    return
    