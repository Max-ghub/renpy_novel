label arrival_go_vetrorosa:
    em "Смотрите, там вдалеке огонёк... Он какой-то странно притягательный. Может, это то самое место?"
    show spaghettinio thinking with dissolve
    sp "Честно говоря, это выглядит не очень безопасно. Не думаю, что идти туда — хорошая идея."
    show spaghettinio with dissolve
    show bagio happy with dissolve
    ba "Спаги, ты как всегда боишься всего подряд. Если мы хотим всё выяснить, нужно проверить все варианты, даже самые странные. Пошли уже!"
    show bagio with dissolve
    show spaghettinio offended with dissolve
    sp "Ну ладно... Но предупреждаю, если что-то пойдёт не так, это на твоей совести."
    show spaghettinio with dissolve
    em "Тихо, вы оба. Просто идём."

    scene lighthouse with dissolve
    show bagio at bagio_dynamic with moveinleft
    show spaghettinio at spagetinio_dynamic with moveinright
    ba "Так, мы на месте. Что это за странное здание? Оно выглядит... жутковато."
    show spaghettinio scared with dissolve
    sp "Ребят, мне кажется, или это здание... живое?"
    ve "Добро пожаловать, путники. Я — Ветророза, хранитель порядка и гармонии."
    ve "Ты, избранный, пришёл сюда неслучайно. Вопросов много, но путь твой ещё не ясен."
    em "Путь... Не ясен? Мы ищем ошибку в проекте. Может быть, она здесь?"
    ve "Нет, здесь её нет. Но я дам вам подсказку, хотя истина требует усилий."
    ve "Ищи там, где знания мира тяжелеют, где ответы скрыты за стенами. Сейчас вход закрыт, но путь откроется."
    show bagio offended with dissolve
    ba "Вот опять загадки! Почему нельзя прямо сказать, где искать?!"
    show bagio with dissolve
    show spaghettinio thinking with dissolve
    sp "Ба, подожди. 'Знания мира'? Может, она говорит о библиотеке?"
    show spaghettinio with dissolve
    em "\"Знания тяжелеют\"... Постойте, кажется, я понял. Это не библиотека. Это Радиофак!"
    show bagio offended
    ba "Радиофак? Серьёзно? Откуда такая уверенность?"
    show spaghettinio happy with dissolve
    sp "Нет, это действительно подходит! Там ведь всегда было связано всё с обучением и знаниями."
    show spaghettinio with dissolve
    ba "Ааа... Ну ладно. Идём уже, если ты уверен."
    show bagio with dissolve
    em "Да, пойдёмте."

    sp "Спасибо за помощь, Ветророза."
    ve "Удачи вам, путники. Пусть ваш путь приведёт к равновесию."
    sp "Да, мы постараемся как можно быстрее всё исправить."
    show spaghettinio scared with dissolve
    sp "Ой, а куда они ушли? Эй, ребята, подождите меня!"

    scene radik with fade
    play sound "audio/radik_sounds.mp3" loop volume 0.1
    show bagio at bagio_dynamic with moveintop
    show spaghettinio at spagetinio_dynamic with moveinright
    ba "Так, мы на месте. И что? Просто какое-то здание. Где тут проблема?"
    show spaghettinio offended with dissolve
    sp "Баггио, ты серьёзно? Ты не видишь, что тут вообще нет двери? Хотя... не удивительно, это же ты."
    show spaghettinio with dissolve
    em "Стоп... Постойте. Я вспомнил. Этот участок проекта делал я... и, похоже, совершенно забыл про дверь."
    sp "Ну что ж, теперь всё очевидно. Давай приступим к исправлению."

    hide bagio
    hide spaghettinio
    with Fade(0.4, 0.3, 0.4)
    return
