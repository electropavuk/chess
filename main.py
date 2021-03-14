import pygame

import pieces
import board
import ui
import config


b = board.Board()
s = ui.Scene(b)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit

        s.update()