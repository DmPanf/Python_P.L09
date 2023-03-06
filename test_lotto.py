import pytest
from game_lotto import Card

def test_card_contains():
    card = Card(0)
    assert 1 in card
    assert 25 in card
    assert 30 not in card

def test_card_cross_num():
    card = Card(0)
    card.cross_num(1)
    assert card.card_data[0] == -1
    with pytest.raises(ValueError):
        card.cross_num(30)

def test_card_closed():
    card = Card(0)
    assert not card.closed()
    for i in range(len(card.card_data)):
        card.cross_num(card.card_data[i])
    assert card.closed()
