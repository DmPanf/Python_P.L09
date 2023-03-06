import pytest
from lotto_game import Card, Game

def test_card_contains():
    """
    Тест проверяет работу метода __contains__(), который проверяет, 
    содержится ли указанный элемент в карточке игрока. 
    В данном случае, тест проверяет, что в карточке игрока содержатся числа 1 и 25, 
    и что число 30 не содержится в карточке.
    """
    card = Card(0)
    assert 1 in card
    assert 25 in card
    assert 30 not in card

"""    
def test_card_cross_num():
    """
    Тест проверяет работу метода cross_num(), который "зачеркивает" число на карточке 
    при совпадении с вытащенным числом. В данном случае, тест проверяет, что после 
    "зачеркивания" числа 1 на карточке, оно стало равно -1, а при попытке "зачеркнуть" число, 
    которого нет на карточке, возникает ошибка ValueError.
    """
    card = Card(0)
    card.cross_num(1)
    assert card.card_data[0] == -1
    with pytest.raises(ValueError):
        card.cross_num(30)
"""
        
def test_card_closed():
    """
    Тест проверяет работу метода closed(), который проверяет, заполнены ли все ячейки 
    на карточке игрока. В данном случае, тест проверяет,     что изначально все ячейки на карточке 
    не заполнены, а после "зачеркивания" всех чисел на карточке, она становится заполненной.
    """
    card = Card(0)
    assert not card.closed()
    for i in range(len(card.card_data)):
        card.cross_num(card.card_data[i])
    assert card.closed()

    
def test_game_init(game):
    """
    Тест проверяет, что списки имеют правильную длину после инициализации.
    """
    assert len(game.player_cards) == 2
    assert len(game.game_barrels) == 90
    assert len(game.card_colors) == 8
    assert len(game.user_icons) == 8



    
 
