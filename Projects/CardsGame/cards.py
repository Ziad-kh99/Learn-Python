class Card:

    FACES = ['ace', '2', '3', '4', '5', '6', '7',       # class-level attribute
             '8', '9', '10', 'jack', 'queen', 'king']      
    SUITS = ['hearts', 'diamonds', 'clubs', 'spades']

    def __init__(self, face, suit):
        '''Initialize a card with a face and suit.'''
        self._face = face
        self._suit = suit


    @property
    def face(self):
        '''Return the card's face value.'''
        return self._face
    
    @property
    def suit(self):
        '''Retrun the card's suit value.'''
        return self._suit 
    
    @property
    def image_name(self):
        '''Return the card's image file name.'''
        return str(self).replace(' ', '_') + '.png'
    
    def __repr__(self):
        '''Return string representation for repr().'''
        return f'{self._face} of {self._suit}'
    
    def __str__(self):
        '''Return string representaion for str().'''
        return f'{self._face} of {self._suit}'
    
    def __format__(self, format) -> str:
        '''Return formatted string representation.'''
        return f'{str(self):{format}}'
    
    