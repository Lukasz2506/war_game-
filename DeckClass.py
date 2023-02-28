import CardClass
import random


class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in CardClass.suits:
            for rank in CardClass.ranks:
                # Create a Card object
                created_card = CardClass.Card(suit, rank)
                self.all_cards.append(created_card)

    def deck_shuffle(self):

        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


# deck = Deck()
# print(deck.all_cards)
# first_card = deck.all_cards[0]
# print(first_card)
# last_card = deck.all_cards[-1]
# print(last_card)
#
# for card_object in deck.all_cards:
#     print(card_object)
#
# print(deck.all_cards[0])
# deck.deck_shuffle()
# print(deck.all_cards[0])
# print(len(deck.all_cards))
# print(deck.deal_one())
# print(len(deck.all_cards))