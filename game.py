import pygame
import string
import random
from game_variables import spelling_words, game_colours, game_font, letter_font, coordinates
from screen_setup import ScreenSetup
from guess_checker import GuessChecker
from letter import Letter
from letter_button import LetterButton

class Game():
    def __init__(self, screen):
        self.coordinates = coordinates
        self.screen = ScreenSetup(self, screen)
        self.guess_checker = GuessChecker(self)
        self.lives = 0
        self.letters = list(string.ascii_uppercase)
        self.spelling_word = random.choice(spelling_words).upper()
        self.game_active = True
        self.letter_objects = [Letter(char) for char in self.spelling_word]
        self.letter_button_group = pygame.sprite.Group()
        self.add_letter_objects()

    def add_letter_objects(self):
        for i in range(0, 26):
            self.letter_button_group.add(LetterButton(game = self, name=self.letters[i], coordinates=self.coordinates[i]))