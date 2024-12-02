init python:
    def typewriter(text, delay=0.1, blinks=3, cursor_blink_delay=0.35):
        cursor = "|"
        displayed_text = ""
        typing_sound = "/audio/intro/key_sound.mp3"
        text_settings = {
            "font": "RussoOne-Regular.ttf",
            "size": 60,
            "xpos": 0.5,
            "ypos": 0.5,
            "xanchor": "center",
            "yanchor": "center",
        }
        
        for char in text:
            displayed_text += char
            ui.text(displayed_text + cursor, **text_settings)
            renpy.play(typing_sound, channel="sound", relative_volume=0.75)
            renpy.pause(delay)
        
        for _ in range(blinks):
            ui.text(displayed_text, **text_settings)
            renpy.pause(cursor_blink_delay)
            ui.text(displayed_text + cursor, **text_settings)
            renpy.pause(cursor_blink_delay)
        
        for i in range(len(displayed_text), -1, -1):
            ui.text(displayed_text[:i] + cursor, **text_settings)
            renpy.play(typing_sound, channel="sound", relative_volume=0.5)
            renpy.pause(delay / 2.5)
            
        ui.clear()
        renpy.music.stop(channel='sound')

label intro:
    play audio "/audio/intro/intro_start.mp3"
    pause 1.0
    stop audio fadeout 0.5
    play music "/audio/intro/intro_music.mp3" volume 0.3 fadein 1.0
    pause 2.0
    $ typewriter("Код Сюжета представляет")
    pause 1.5
    $ typewriter("Внутри кода: Frontend", delay=0.175, blinks=6)
    pause 1.0
    stop music fadeout 1.0

    return
