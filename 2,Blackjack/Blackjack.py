'''
Blackjack Game
'''

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}
playing = True

class Card:
    '''
    Card class linking suits and rank together
    '''

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    '''
    Creating a deck from the cards class
    '''
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
        
    def __str__(self):
        comp_deck =''
        for d in self.deck:
            comp_deck += '\n' + d.__str__()
        return 'Here is my Deck: ' + comp_deck

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    '''
    Players hand
    '''
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    '''
    Class for holding chips and + - bets
    '''    

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Please enter your bet: '))
        except:
            print('Not a number')
            continue
        else:
            if chips.bet > chips.total:
                print('sorry your bet cant exceed:', chips.total)
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing

    while True:
        answer = input('Hit or stand. h or s: ')
        if answer.lower() == 'h':
            hit(deck,hand)
            break
        elif answer.lower() == 's':
            playing = False
            break
        else:
            print('Please enter h or s')

def show_some(player,dealer):
    print('Dealers hand: HIDDEN CARD,', dealer.cards[1])
    print('Players hand:', *player.cards, sep=' ')
    print('--------------------------------------')

def show_all(player,dealer):
    print('Dealers hand:', *dealer.cards, sep=' ')
    print(f'Dealers Value: {dealer.value}')
    print('Players hand:', *player.cards, sep=' ')
    print(f'Player Value: {player.value}')
    print('--------------------------------------')

def player_bust(chips):
    print('Player Bust')
    chips.lose_bet()

def player_wins(chips):
    print('Player Wins')
    chips.win_bet()

def dealer_bust(chips):
    print('Dealer Bust')
    chips.win_bet()

def dealer_wins(chips):
    print('Dealer Wins')
    chips.lose_bet()

def push():
    print('Tie game')

while True:
    print('Welcome to black jack')

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:

        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if (player_hand.value > 21):
            player_bust(player_chips)
            break
    
    if player_hand.value <= 21:

        show_all(player_hand, dealer_hand)

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
        
        if dealer_hand.value > 21:
            dealer_bust(player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)
        else:
            push()
    
    show_all(player_hand,dealer_hand)

    print(f'Player has {player_chips.total} chips')

    new_game = input('Would you like to play again y or n: ')

    if new_game.lower() == 'y':
        playing = True
        continue
    else:
        break

    
        






