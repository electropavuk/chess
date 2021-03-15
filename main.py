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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

        s.update()
        b.make_move_from_uci(input())

        s.update()
