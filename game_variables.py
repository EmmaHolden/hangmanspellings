import pygame

pygame.init()

spelling_words = ["camel", "otter", "octopus", "sealion", "tiger"]

game_font = pygame.font.Font('font/chalk.otf', 120)

letter_font = pygame.font.Font('font/chalk.otf', 60)

instruction_font = pygame.font.Font('font/Pixeltype.ttf', 40)

word_font = pygame.font.Font('font/Pixeltype.ttf', 80)

timer_font = pygame.font.Font('font/Pixeltype.ttf', 120)

game_colours = {
    "green": '#00DFA2',
    "blue": '#0079FF',
    "yellow": '#F6FA70',
    "orange": '#FF9526',
    "red": '#FF0060',
    "purple": '#2A3492',
}

coordinates = [
    (120, 280), (200, 280), (280, 280), (360, 280), (440, 280), (520, 280), (600, 280),
    (120, 350), (200, 350), (280, 350), (360, 350), (440, 350), (520, 350), (600, 350),
    (120, 420), (200, 420), (280, 420), (360, 420), (440, 420), (520, 420), (600, 420),
                (200, 490), (280, 490), (360, 490), (440, 490), (520, 490),
               ]