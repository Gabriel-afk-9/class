import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        value_map = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
        value_str = value_map.get(self.value, str(self.value))

        return f'{value_str}{self.suit[0].upper()}'


class EmptyDeckError(Exception):
    pass

class Deck:
    def __init__(self):
        self.cards = []
        self.generate_deck()

    def generate_deck(self):
        suits = ['spades', 'clubs', 'hearts', 'diamonds']
        for suit in suits:
            for value in range(1, 14):
                self.cards.append(Card(suit, value))

    def shuffle(self):
        if not self.cards:
            raise EmptyDeckError("O baralho está vazio. Não é possível embaralhar.")
        random.shuffle(self.cards)

    def deal_card(self):
        if not self.cards:
            raise EmptyDeckError("O baralho está vazio. Não é possível distribuir cartas.")
        return self.cards.pop()

    def remaining_cards(self):
        return len(self.cards)

if __name__ == "__main__":
    deck = Deck()
    print(f'Número de cartas no baralho: {deck.remaining_cards()}')
    deck.shuffle()
    
    card = deck.deal_card()
    print(f'Carta distribuída: {card}')
    
    print(f'Número de cartas restantes no baralho: {deck.remaining_cards()}')
