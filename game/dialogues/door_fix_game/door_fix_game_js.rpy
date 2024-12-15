label door_fix_game_js:
    call screen dfg_menu_scroll({
        "title": "Определите, как назначить событие на дверь, чтобы при клике она открывалась и закрывалась.",
        "menu": [
            {
                "caption": 'document.querySelector(".door").addEventListener("click", function () {{\n  const isClosed = this.getAttribute("data-status") === "closed";\n  this.setAttribute("data-status", isClosed ? "open" : "closed");\n});',
                "action": Return("first")
            },
            {
                "caption": 'var door = document.querySelector(".door");\ndoor.onclick = function () {{\n  var isClosed = door.getAttribute("data-status") === "closed";\n  door.setAttribute("data-status", isClosed ? "open" : "closed");\n};',
                "action": Return("second")
            },
            {
                "caption": 'document.querySelector(".door").addEventListener("click", () => {{\n  const isClosed = this.getAttribute("data-status") === "closed";\n  this.setAttribute("data-status", isClosed ? "open" : "closed");\n});',
                "action": Return("third")
            },
            {
                "caption": 'document.querySelector("#door").addEventListener("click", function () {{\n  const isClosed = this.getAttribute("data-status") === "closed";\n  this.setAttribute("data-status", isClosed ? "open" : "closed");\n});',
                "action": Return("fourth")
            },
        ]
    })
    $ result = _return

    if result == "first":
        "Отлично! Тут мы используем правильный метод {i}addEventListener{/i}, удобный селектор {i}.door{/i} и обычную функцию, чтобы {i}this{/i} указывал на дверь."
    elif result == "second":
        "Этот код работает, но использует устаревший способ {i}onclick{/i}. Если нам нужно будет добавить ещё события, будет сложнее."
        call door_fix_game_js
    elif result == "third":
        "Использована стрелочная функция. В ней {i}this{/i} не будет указывать на дверь, и код не заработает как надо."
        call door_fix_game_js
    elif result == "fourth":
        "Используется селектор {i}#door{/i}, а у нас есть только {i}.door{/i}. Если элемента с таким {i}id{/i} нет, код не найдёт дверь."
        call door_fix_game_js

    return