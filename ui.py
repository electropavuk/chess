import pygame
import os
from time import time

from pprint import pprint

from config import *



class Scene(pygame.sprite.Sprite):
    piece_sprites = dict()
    board_sprite = None

    def __init__(self, board):
        super().__init__()
        self.screen = pygame.display.set_mode(resolution)
        self.board = BoardScene(board)
        self.components = [self.board]
        self.update()


    def update(self):
        self.screen.fill((10, 10, 10))
        for block in self.components:
            block.update()
            self.screen.blit(block.sprite, block.rect)
        # self.screen.blit

        pygame.display.update()



class BoardScene(pygame.sprite.Sprite):
    piece_sprites = dict()
    board_sprite = None

    def __init__(self, board):
        super().__init__()
        self.board = board
        self.size = resolution[1] - 2 * board_margin
        self.square_size = self.size // 8
        self.set_sprites()
        self.board.show()
        self.update()


    def update(self):
        self.sprite = self.board_sprite.copy()
        for i in range(8):
            for j in range(8):
                piece = self.board.board[i][j]
                if piece:
                    sprite = self.piece_sprites[piece.name]
                    rect = sprite.get_rect()
                    rect.center = ((j + 1/2) * self.square_size, 
                                    self.size - (i + 1/2) * self.square_size)
                    self.sprite.blit(sprite, rect)

    def set_sprites(self):
        board_path = os.path.join('ui', 'boards', board_name)
        # board_path = os.path.join('ui', 'pieces', curent_piece_set, 'bQ' + piece_names_ext)
        self.board_sprite = pygame.image.load(board_path)
        self.board_sprite = pygame.transform.scale(self.board_sprite, (self.size,) * 2)
        self.sprite = self.board_sprite.copy()
        self.rect = self.sprite.get_rect()
        self.rect.topleft = board_pos


        # self.sprite = pygame.Surface((1000,1000))
        # self.sprite.fill((22,222,222))
        # self.rect = self.sprite.get_rect()
        # self.rect.topleft = board_pos



        for piece in piece_names:
            piece_path = os.path.join('ui', 'pieces', curent_piece_set, piece + piece_names_ext)
            sprite = pygame.image.load(piece_path)
            size = (int(self.square_size * piece_to_square_ration),) * 2
            sprite = pygame.transform.scale(sprite, size)
            self.piece_sprites[piece] = sprite

            # sprite = pygame.Surface((50, 50))
            # sprite.fill((0,0,0))
            # self.piece_sprites[piece] = sprite
