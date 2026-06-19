"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

FACE_CARDS = ['J', 'Q', 'K']
ACE = 'A'

def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if card in FACE_CARDS:
        return 10
    elif card == ACE:
        return 1
    elif 2 <= int(card) <= 10:
        return int(card)
    else:
        return None


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    value_of_card_one = value_of_card(card_one)
    value_of_card_two = value_of_card(card_two)

    if value_of_card_one > value_of_card_two:
        return card_one
    elif value_of_card_one < value_of_card_two:
        return card_two
    else:
        return card_one, card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    if card_one == ACE or card_two == ACE:
        return 1
    elif value_of_card(card_one) + value_of_card(card_two) > 10:
        return 1
    else:
        return 11


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    is_21 = value_of_card(card_one) >= 10 or value_of_card(card_two) >= 10
    has_ace = card_one == ACE or card_two == ACE

    if is_21 and has_ace:
        return True
    else:
        return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    king_and_queen = ['K', 'Q']

    if card_one in king_and_queen or card_two in king_and_queen:
        return True

    value_of_card_one = value_of_card(card_one)
    value_of_card_two = value_of_card(card_two)

    if value_of_card_one == value_of_card_two and card_one == card_two:
        return True
    else:
        return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    double_down_rate = [9, 10, 11]

    if value_of_card(card_one) + value_of_card(card_two) in double_down_rate:
        return True
    else:
        return False
    
