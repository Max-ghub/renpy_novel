label escape_project:
    em "Нет, я не собираюсь участвовать в этом безумии. Мне нужно просто выйти отсюда!"

    ba "Эй-эй, стой. Ты что делаешь?!"
    sp "Нелогичное решение! Если уйдёшь, проект точно провалится."

    stop music
    scene bg_office with Pixellate(1.2, 9)
    show emrach at center with dissolve
    em "Уф... Кажется, всё обошлось."

    show sergey at left with moveinleft
    sg "Эмрах, я посмотрел твой проект. Что это? Ты вообще ничего не делаешь? Мы потеряем клиентов из-за тебя!"

    em "Сергей Геннадьевич, я старался... Всё вышло из-под контро..."

    sg "Этого недостаточно! Я вынужден прекратить наше сотрудничество. Ты уволен!"
    hide sergey at left with moveoutleft

    em "Такого я точно не ожидал. Это провал..."

    return
