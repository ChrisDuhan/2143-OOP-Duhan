"""
Name: Chris Duhan
Email: chris.m.duhan@gmail.com
Assignment: Homework 2 - War card game
Due: 17 Feb @ 11:59 p.m.
"""
"""
So this was a fun program, it's still got a few things that could be implimented more effectivly, plus it goes on till the last card, meaning that the game could possibly end during war.
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

"""
@Class Card 
@Description:
    This class represents a single card. 
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
    join_lines() - desciption below
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
        you can uncomment the commands below that ask for input and that pause
""" 
class Game(object):
    def __init__(self,player_name):
        self.D = Deck()
        self.D.shuffle()

        self.CH = Hand()
        self.PH = Hand()
        self.war_stack = []
        self.winner = None
        self.rounds = 0
        self.deal()
        self.play()
        
    def deal(self):
        for i in range(26):
            self.CH.add(self.D.pop_card())
            self.PH.add(self.D.pop_card())
            
    def play(self):
        while(len(self.CH._list) and len(self.PH._list)):
            os.system('cls')
            os.system('clear')
            PC = self.PH.play_card()
            CC = self.CH.play_card()
            
            if PC.__lt__(CC):
                print("Computer")
                print(CC)
                print(PC)
                print(player_name)
                print()
                print("You lost")
                #input("Press enter to play a round")
                self.CH.add(PC)
                self.CH.add(CC)
                for i in self.war_stack:
                  self.CH.add(self.war_stack.pop())
                  
            elif CC.__lt__(PC):
                print("Computer")
                print(CC)
                print(PC)
                print(player_name)
                print()
                print("You won")
                #input("Press enter to play a round")
                self.PH.add(PC)
                self.PH.add(CC)
                for i in self.war_stack:
                  self.PH.add(self.war_stack.pop())
                  
            else:
                print("Computer")
                print(CC)
                print(PC)
                print(player_name)
                print()
                print("War!")
                self.war_stack.append(self.PH.play_card())
                self.war_stack.append(self.CH.play_card())
                #time.sleep(2)
                #input("Press enter to play a war round")
                os.system('cls')
                self.play()

            self.rounds = self.rounds + 1
            if (self.rounds % 26 == 0):
                self.PH.shuffle()
                self.CH.shuffle()
                
            if len(self.CH._list) == 0:
                self.winner = "You"
            if len(self.PH._list) == 0:
                self.winner = "The computer"
            
            # time.sleep(.5)

print("Welcome to the game of")
print(" _    _   ___  ______  _\n| |  | | / _ \ | ___ \| |\n| |  | |/ /_\ \| |_/ /| |\n| |/\| ||  _  ||    / | |\n\  /\  /| | | || |\ \ |_|\n \/  \/ \_| |_/\_| \_|(_)")
print()
input("Press enter to begin")
os.system('cls')
os.system('clear')
player_name = input("Please type your name: ")
new_game = Game(player_name)

os.system('cls')
os.system('clear')
print('%s won' % new_game.winner)
print('Game finished after %d rounds'% new_game.rounds)
