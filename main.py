import pygame
from sys import exit
from game import Game



pygame.init()
pygame.display.set_caption("Hangman Spelling Game")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200, 700))
game = Game(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        else:
            if game.game_active:
                if event.type == pygame.KEYDOWN and event.unicode.isalpha():
                    game.guess_checker.check_guess(event.unicode)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game.letter_button_group.update(event.pos)
        if game.game_active:
            game.screen.game_active_update()
        else:
            game.screen.game_over_update()

    pygame.display.update()
    clock.tick(60)

