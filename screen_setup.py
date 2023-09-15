import pygame
from game_variables import game_font, letter_font
class ScreenSetup():
    def __init__(self, game, screen):
        self.game = game
        self.screen = screen
        self.background = pygame.image.load('graphics/chalkboard.jpg').convert_alpha()
        self.background = pygame.transform.scale(self.background, (1200, 700))
        self.line_horizontal_surface = pygame.image.load('graphics/line.png').convert_alpha()
        self.line_horizontal_surface = pygame.transform.scale(self.line_horizontal_surface, (620, 50))
        self.line_vertical_surface = pygame.image.load('graphics/line.png').convert_alpha()
        self.line_vertical_surface = pygame.transform.scale(self.line_vertical_surface, (300, 50))
        self.line_vertical_surface = pygame.transform.rotate(self.line_vertical_surface, 90)
        self.word_was_label = letter_font.render('The  word  was :', False, "white")

    def draw_background(self):
        self.screen.blit(self.background, (0, 0))

    def draw_letter_grid(self):
        self.game.letter_button_group.draw(self.screen)
        self.screen.blit(self.line_horizontal_surface, (60, 320))
        self.screen.blit(self.line_horizontal_surface, (60, 390))
        self.screen.blit(self.line_horizontal_surface, (60, 460))
        self.screen.blit(self.line_vertical_surface, (145, 260))
        self.screen.blit(self.line_vertical_surface, (225, 260))
        self.screen.blit(self.line_vertical_surface, (305, 260))
        self.screen.blit(self.line_vertical_surface, (385, 260))
        self.screen.blit(self.line_vertical_surface, (465, 260))
        self.screen.blit(self.line_vertical_surface, (545, 260))

    def get_current_word_state(self):
        word = ""
        for object in self.game.letter_objects:
            if object.revealed:
                word += object.name
            else:
                word += "_"
            word += " "
        return game_font.render(word, False, "white")

    def get_hangman_picture(self):
        self.hangman_surface = pygame.image.load(f'graphics/washingman{self.game.lives}.png').convert_alpha()
        return pygame.transform.scale(self.hangman_surface, (400, 400))

    def get_spelling_word(self):
        return game_font.render(self.game.spelling_word, False, "white")

    def draw_current_word_state(self):
        self.screen.blit(self.get_current_word_state(), (300, 100))

    def draw_hangman_picture(self, coordinates):
        self.screen.blit(self.get_hangman_picture(), coordinates)


    def game_active_update(self):
        self.draw_background()
        self.draw_letter_grid()
        self.draw_current_word_state()
        self.draw_hangman_picture((700, 200))

    def get_win_lose_message(self):
        if self.game.lives == 9:
            message = 'Y O U     L O S E!'
        else:
            message = 'Y O U     W I N!'
        return game_font.render(message, False, "white")


    def game_over_update(self):
        self.draw_background()
        self.draw_hangman_picture((700, 200))
        self.screen.blit(self.get_win_lose_message(), (300, 100))
        self.screen.blit(self.word_was_label, (200, 300))
        self.screen.blit(self.get_spelling_word(), (200, 400))

