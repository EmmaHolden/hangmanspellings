import pygame
from game_variables import letter_font

class LetterButton(pygame.sprite.Sprite):
    def __init__(self, game, name, coordinates):
        self.game = game
        super().__init__()
        self.name = name
        self.coordinates = coordinates
        self.image = letter_font.render(name, False, "white")
        self.rect = self.image.get_rect(topleft = self.coordinates)
    def check_collision(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.game.guess_checker.check_guess(self.name)

    def update(self, mouse_pos):
        self.check_collision(mouse_pos)