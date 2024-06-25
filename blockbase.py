from colors import Colors
import pygame


class BlockBase:
    def __init__(self, id) -> None:
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.rotation_state = 0
        self.color = Colors.get_cell_colors()

    def draw(self, screen):
        tiles = self.cells[self.rotation_state]
        for tile in tiles:
            tile_rect = pygame.Rect(tile.col*self.cell_size + 1, tile.row*self.cell_size + 1,
                                    self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.color[self.id], tile_rect)
