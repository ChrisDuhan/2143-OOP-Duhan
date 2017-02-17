"""
Name: Chris Duhan
Email: chris.m.duhan@gmail.com
Assignment: Homework 2 - War card game
Due: 14 Feb @ 11:00 a.m.
"""

import os
import time
import random

#Source for cards and card class: http://codereview.stackexchange.com/questions/82103/ascii-fication-of-playing-cards
CARD = """\
┌───────┐
│{}     │
│       │
│   {}  │
│       │
│     {}│
└───────┘
""".format('{trank:^2}', '{suit: <2}', '{brank:^2}')
TEN = """\
┌───────┐
│{}    │
│       │
│   {}  │
│       │
│    {}│
└───────┘
""".format('{trank:^3}', '{suit: <2}', '{brank:^3}')
FACECARD = """\
┌───────┐
│{}│
│       │
│   {}  │
│       │
│{}│
└───────┘
""".format('{trank:<7}', '{suit: <2}', '{brank:>7}')
HIDDEN_CARD = """\
┌───────┐
│░░░░░░░│
│░░░░░░░│
│░░░░░░░│
│░░░░░░░│
│░░░░░░░│
└───────┘
"""

class Card(object):
    
    def __init__(self, suit, rank):
        """
        :param suit: The face of the card, e.g. Spade or Diamond
        :param rank: The value of the card, e.g 3 or King
        """
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King","Ace"]
        self.card_values = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'Jack': 10,
            'Queen': 10,
            'King': 10,
            'Ace': 11,  # value of the ace is high until it needs to be low
        }
        self.str_values = {
            '2': CARD,
            '3': CARD,
            '4': CARD,
            '5': CARD,
            '6': CARD,
            '7': CARD,
            '8': CARD,
            '9': CARD,
            '10': TEN,
            'Jack': FACECARD,
            'Queen': FACECARD,
            'King': FACECARD,
            'Ace': FACECARD,  # value of the ace is high until it needs to be low
        }
        self.suits = ['Spades','Hearts','Diamonds','Clubs']
        self.symbols = {
            'Spades':   '♠',
            'Diamonds': '♦',
            'Hearts':   '♥',
            'Clubs':    '♣',
        }
        
        if type(suit) is int:
            self.suit = self.suits[suit]
        else:
            self.suit = suit.capitalize()
        self.rank = str(rank)
        self.symbol = self.symbols[self.suit]
        self.points = self.card_values[str(rank)]
        self.ascii = self.__str__()
    
    def __str__(self):
        symbol = self.symbols[self.suit]
        trank = self.rank+symbol
        brank = symbol+self.rank
        return self.str_values[self.rank].format(trank=trank, suit=symbol,brank=brank)
           
    def __cmp__(self,other):
        return self.ranks.index(self.rank) < self.ranks.index(other.rank) 
    
    def __lt__(self,other):
        return self.__cmp__(other)
        
    def stringy(self):
        self.ascii = self.__str__()

"""
@Class Deck 
@Description:
    This class represents a deck of cards. 
@Methods:
    pop_cards() - removes a card from top of deck
    add_card(card) - adds a card to bottom of deck
    shuffle() - shuffles deck
    sort() - sorts the deck based on value, not suit (could probaly be improved based on need)
"""       
class Deck(object):
    def __init__(self):
        #assume top of deck = 0th element
        self.cards = []
        for suit in range(4):
            for rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King","Ace"]:
                self.cards.append(Card(suit,rank))
                
    def __str__(self):
        cards_on_screen = []
        for card in self.cards:
            cards_on_screen.append(str(card))
        return "".join(cards_on_screen)
    
    def pop_card(self):
        return self.cards.pop(0)
        
    def add_card(self,card):
        self.cards.append(card)
        
    def shuffle(self):
        random.shuffle(self.cards)
    
    def sort(self):
        self.cards = sorted(self.cards)

"""
@Class Hand 
@Description:
    This class represents a players' hand of cards. 
@Methods:
    play_card() - removes a card from top of deck
    add(card) - adds a card to bottom of deck
    shuffle() - shuffles the hand
""" 
class Hand(list):
    def __init__(self, cards=None):
        """Initialize the class"""
        super().__init__()
        if (cards is not None):
            self._list = list(cards)
        else:
            self._list = []
    
    def __str__(self):
        return self.join_lines()

    def join_lines(self):
        """
        Stack strings horizontally.
        This doesn't keep lines aligned unless the preceding lines have the same length.
        :param strings: Strings to stack
        :return: String consisting of the horizontally stacked input
        """
        liness = [card.ascii.splitlines() for card in self._list]
        return '\n'.join(''.join(lines) for lines in zip(*liness))
    
    def add(self,card):
        self._list.append(card)
    
    def play_card(self):
        return self._list.pop(0)
    
    def shuffle(self):
        random.shuffle(self._list)

"""
@Class Game 
@Description:
    This class represents a game of War
@Methods:
    game_start() - prepares the players hands
    play() - a card from each palyer is compared and the winner takes both,
        if war occurs it makes a war stack and plays again
    
    play() is currently set up to auto-play the whole game, if you want to play each round yourself
        you can uncomment the commands below that ask for input
""" 
class Game(object):
    def __init__(self,player_name):
        self.D = Deck()
        self.D.shuffle()

        self.C = player("Computer")
        self.P = player(player_name)

        self.winner = None
        self.rounds = 0
        self.cards_in_play = Hand()
        self.deal()
        self.play()
        
    def deal(self):
        for i in range(26):
            self.C.H.add(self.D.pop_card())
            self.P.H.add(self.D.pop_card())

    # def compare(self, playerCard, computerCard):
    #     if(playerCard > computerCard):
    #         self.win = self.P
    #     elif (playerCard < computerCard):
    #         self.win = self.C
    #     else:
    #         self.win = "tie"
    #     return self.win

    def emptyPot(self, winningPlayer):
        while(len(self.cards_in_play._list)):
            winningPlayer.H.add(self.cards_in_play.play_card())
        while(len(self.P.war._list)):
            self.P.war.play_card()
        while(len(self.C.war._list)):
            self.C.war.play_card()

    def tie(self, p, c):
        os.system('cls')
        os.system('clear')
        
        # only if there is more than one card in a player's hand
        
        # exits after popping two cards in to each players war hand and the main pot

        # game continues as normal in main game loop
        
        if(len(c.H._list) > 1):
            c.war.add(c.H._list[0])
            self.cards_in_play.add(c.H.play_card())
        if(len(c.H._list) > 1):
            self.temp = c.H._list[0]
        
        # set cards string method to print hidden

            self.temp.ascii = HIDDEN_CARD
            c.war.add(self.temp)
            self.cards_in_play.add(c.H.play_card())

        if(len(p.H._list) > 1):
            p.war.add(p.H._list[0])
            self.cards_in_play.add(p.H.play_card())
            
        if(len(p.H._list) > 1):
            self.temp = p.H._list[0]

        # set cards string method to print hidden

            self.temp.ascii = HIDDEN_CARD
            p.war.add(self.temp)
            self.cards_in_play.add(p.H.play_card())

        print(c.name + "'s hand:\n")
        print(c.war)
        print()
        print(p.war)
        print()
        print(p.name + "'s hand:")
        print()

        # time.sleep(.5)


    def play(self):
        while(len(self.C.H._list) and len(self.P.H._list)):
            os.system('cls')
            os.system('clear')
            print(self.C.name)
            print(self.C.H._list[0])
            print(self.P.H._list[0])
            print(self.P.name)
            print()
            
            if (self.P.H._list[0].rank == self.C.H._list[0].rank):
                self.tie(self.P, self.C)
                
            else:
                self.cards_in_play.add(self.P.H.play_card())
                self.cards_in_play.add(self.C.H.play_card())
                self.emptyPot(self.winner)
                print(self.winner.name + " wins")
                
                for card in self.P.H._list:
                    card.stringy()
                    
                for card in self.C.H._list:
                    card.stringy()

            self.rounds = 0
            self.rounds = self.rounds + 1

            if (self.rounds % 26 == 0):
                self.P.H.shuffle()
                self.C.H.shuffle()
            
            # time.sleep(.5)

            
class player(object):
    def __init__(self,name):
        self.name = name
        self.H = Hand()
        self.war = Hand()

player_name = input("Please type your name: ")
new_game = Game(player_name)
os.system('cls')
os.system('clear')
print ("Game finished after " + str(new_game.rounds) + " rounds")
