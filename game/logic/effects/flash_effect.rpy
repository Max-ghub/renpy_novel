image flash_effect:
    Solid("#fff")  # Белый фон
    alpha 0.0           # Начальное состояние: полностью прозрачный
    linear 1.5 alpha 0.2  # Плавное появление до 30% непрозрачности
    linear 1.5 alpha 0.0  # Плавное исчезновение
    repeat              # Повтор анимации

image flash_effect_grow:
    Solid("#fff")  # Белый фон
    alpha 0.0           # Начальное состояние: полностью прозрачный
    linear 1 alpha 0.3  # Плавное появление до 30% непрозрачности
    linear 1 alpha 0.0  # Плавное исчезновение
    repeat   

image full_flash_effect:
    Solid("#fff")  # Белый фон
    alpha 1.0