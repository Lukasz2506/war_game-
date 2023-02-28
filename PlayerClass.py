import DeckClass
import CardClass


class Player:

    def __init__(self, name):

        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop()

    def adding_cards(self, new_cards):
        # List of a multiple card objects
        if type(new_cards) == type([]):
            return self.all_cards.extend(new_cards)
        # Single card object
        else:
            return self.all_cards.append((new_cards))
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'


# new_player = Player('Jose')
# print(new_player)
# new_card = CardClass.Card('Heart', 'Two')
# print(new_card)
#
# new_player.adding_cards(new_card)
# print(new_player)
# print(new_player.all_cards[0])
# new_player.adding_cards([new_card, new_card, new_card])
# print(new_player)
# new_player.remove_one()
# print(new_player)

