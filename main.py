from tabulate import tabulate
from src.Deck import Deck
from src.Player import Player

# This function displays the number of wins for each player during the game
def wins_count(p1_wins, p2_wins):

    print("\n     STATISTICS!")
    print("="*21)
    print(tabulate([["One", p1_wins],["Two", p2_wins]],
                   headers=["Player", "Wins"],
                   tablefmt='orgtbl'))
    print("=" * 21)

'''
Game Setup
'''
# Wins
player_one_wins = 0
player_two_wins = 0

# Players
player_one = Player("One")
player_two = Player("Two")
# Deck
new_deck = Deck()
new_deck.shuffle()
# Split the deck into two parts
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

'''
Game Logic
'''
round_num = 0
while game_on:

    round_num += 1
    print(f"Round {round_num}")

    # Check to see if a player is out of cards:
    if len(player_one.all_cards) == 0:
        print("\nPlayer One out of cards! Game Over.")
        print("Player Two Wins!")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("\nPlayer Two out of cards! Game Over.")
        print("Player One Wins!")
        game_on = False
        break

    # Otherwise, the game is still on!
    # Start a new round and reset current cards on the table
    player_one_cards = []   # Player 1's cards on the table
    player_one_cards.append(player_one.remove_one())    # Player 1 put one card on the table
    print(f"    => Player One's card: {player_one_cards[-1]}")


    player_two_cards = []   # Player 2's cards on the table
    player_two_cards.append(player_two.remove_one())    # Player 2 put one card on the table
    print(f"    => Player Two's card: {player_two_cards[-1]}")

    at_war = True

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:

            # Player One wins this round
            player_one_wins += 1

            # Player One gets the cards
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            # No longer at "war", time for next round
            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:

            # Player Two wins this round
            player_two_wins += 1

            # Player Two gets the cards
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            # No longer at "war", time for next round
            at_war = False

        else:
            print("\n========")
            print(" WAR!!! ")
            print("========\n")
            # This occurs when the cards are equal.
            # We'll grab another card each and continue the current war.

            # First check to see if player has enough cards

            # Check to see if a player is out of cards:
            if len(player_one.all_cards) < 5:
                print("\nPlayer One unable to play war! Game Over at War.")
                print("Player Two wins! Player One loses.")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("\nPlayer Two unable to play war! Game Over at War.")
                print("Player One wins! Player Two loses.")
                game_on = False
                break
            # Otherwise, we're still at war, so we'll add the next cards
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())


    # Check if number of rounds is equal to 1000
    if round_num == 1000:
        print("\n\n" + "="*29)
        print("END OF GAME, TOO MUCH ROUNDS!")
        print("=" * 29)
        game_on = False
        break

# Display the statistics about the game
wins_count(player_one_wins, player_two_wins)