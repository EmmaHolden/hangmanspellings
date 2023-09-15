import pygame
class GuessChecker():
    def __init__(self, game):
        self.game = game
        self.guessed_letters = []

    def check_guess(self, event_key):
        guess = event_key.upper()
        if guess not in self.guessed_letters:
            self.guessed_letters.append(guess)
            for i in self.game.letter_button_group:
                if i.name == guess:
                    i.kill()
            if guess in self.game.spelling_word:
                for letter in self.game.letter_objects:
                    if guess == letter.name:
                        letter.revealed = True
                        revealed = [letter.revealed for letter in self.game.letter_objects]
                        if False not in revealed:
                            self.game.game_active = False
            else:
                self.game.lives += 1
                if self.game.lives == 9:
                    self.game.game_active = False


