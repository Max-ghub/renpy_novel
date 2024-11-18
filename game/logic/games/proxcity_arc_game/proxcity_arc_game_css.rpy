define answer1 = False
define answer2 = False
define answer3 = False
define answer4 = False
define answer5 = False
label proxcity_arc_game_css:
    menu:
        "Отобрази дверь"
        
        "Answer 1(false)" if not answer1:
            $ answer1 = True
            call proxcity_arc_game_html
            
        "Answer 2(false)" if not answer2:
            $ answer2 = True
            call proxcity_arc_game_html
            
        "Answer 3(false)" if not answer3:
            $ answer3 = True
            call proxcity_arc_game_html
            
        "Answer 4(false)" if not answer4:
            $ answer4 = True
            call proxcity_arc_game_html
            
        "Answer 5(true)":
            $ answer5 = True
    
    return