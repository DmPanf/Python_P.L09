def test_clear_screen():
    # Проверяем, что функция clear_screen() работает без ошибок
    clear_screen()

def test_random_list():
    # Проверяем, что функция random_list() возвращает список указанной длины без повторений
    r_list = random_list(10)
    assert len(r_list) == 10
    assert len(set(r_list)) == 10

def test_emoji_digits():
    # Проверяем, что функция emoji_digits() заменяет числа на соответствующие emoji
    assert emoji_digits(0) == '⬜️0️⃣'
    assert emoji_digits(9) == '⬜️9️⃣'
    assert emoji_digits(10) == '1️⃣0️⃣'
    assert emoji_digits(99) == '9️⃣9️⃣'
