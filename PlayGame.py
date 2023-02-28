import DeckClass
import PlayerClass


player1 = PlayerClass.Player('One')
player2 = PlayerClass.Player('Two')

new_deck = DeckClass.Deck()
new_deck.deck_shuffle()


for x in range(26):
    player1.adding_cards(new_deck.deal_one())
    player2.adding_cards(new_deck.deal_one())

game_on = True

round_num = 0

while game_on:

    round_num += 1
    print(f'Round {round_num}')

    if len(player1.all_cards) == 0:
        print('Player 1 out of cards! Player two wins!')
        game_on = False


    elif len(player2.all_cards) == 0:
        print('Player 2 out of cards! Player one wins!')
        game_on = False


    else:
        player_one_cards = []
        player_one_cards.append(player1.remove_one())

        player_two_cards = []
        player_two_cards.append(player2.remove_one())

        at_war = True
        while at_war:

            if player_one_cards[-1].value > player_two_cards[-1].value:

                player1.adding_cards(player_one_cards)
                player1.adding_cards(player_two_cards)

                at_war = False

            elif player_one_cards[-1].value < player_two_cards[-1].value:
                player2.adding_cards(player_one_cards)
                player2.adding_cards(player_two_cards)

                at_war = False

            else:
                print('WAR!')

                if len(player1.all_cards) < 3:
                    print('Player one unable to declare war')
                    print('Player two wins!')
                    game_on = False
                    break

                elif len(player2.all_cards) < 3:
                    print('Player two unable to declare war')
                    print('Player one wins!')
                    game_on = False
                    break

                else:
                    for num in range(3):
                        player_one_cards.append(player1.remove_one())
                        player_two_cards.append(player2.remove_one())




