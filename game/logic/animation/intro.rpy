init python:
    def typewriter(text, delay=0.1, blinks=3, cursor_blink_delay=0.35):
        cursor = "|"
        displayed_text = ""
        text_settings = {
            "font": "RussoOne-Regular.ttf",
            "size": 60,
            "xpos": 0.5,
            "ypos": 0.5,
            "xanchor": "center",
            "yanchor": "center",
        }
        typing_sound = "keySound.mp3"
        
        for char in text:
            displayed_text += char
            ui.text(displayed_text + cursor, **text_settings)
            renpy.play(typing_sound, channel="sound", relative_volume=1)
            renpy.pause(delay)
            ui.clear()
        
        for _ in range(blinks):
            ui.text(displayed_text, **text_settings)
            renpy.pause(cursor_blink_delay)
            ui.clear()
            ui.text(displayed_text + cursor, **text_settings)
            renpy.pause(cursor_blink_delay)
            ui.clear()
        
        for i in range(len(displayed_text), -1, -1):
            ui.text(displayed_text[:i] + cursor, **text_settings)
            renpy.play(typing_sound, channel="sound", relative_volume=0.5)
            renpy.pause(delay / 2)
            ui.clear()

        renpy.music.stop(channel='sound')

label intro:
    play music "officeSounds.mp3" volume 0.3
    $ typewriter("Код Сюжета представляет")
    pause(1.5)
    $ typewriter("Внутри кода: Frontend", delay=0.2, blinks=6)
    pause(1)
    stop music fadeout 2.0

    return
