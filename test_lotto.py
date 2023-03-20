import pytest
from lotto_game import Card, Game

# Для каждого класса в программе добавить магический метод __str__;

@pytest.fixture
def game():
    return Game(2)  # количество игроков

  
def test_game_init(game):
    """
    Тест проверяет, что списки имеют правильную длину после инициализации.
    """
    assert len(game.player_cards) == 2
    assert len(game.game_barrels) == 90
    assert len(game.card_colors) == 8
    assert len(game.user_icons) == 8



    
 
