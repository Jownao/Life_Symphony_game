import pygame

class Element:
    def __init__(self, position, size, color):
        self.position = position
        self.size = size
        self.color = color

    def draw(self, screen):
        pass  # Será implementado nas subclasses


class Tree(Element):
    def __init__(self, position, size, color):
        super().__init__(position, size, color)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position[0], self.position[1], self.size, self.size))


class River(Element):
    def __init__(self, position, size, color):
        super().__init__(position, size, color)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position[0], self.position[1], self.size, self.size))


class Building(Element):
    def __init__(self, position, size, color):
        super().__init__(position, size, color)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.position[0], self.position[1], self.size, self.size))
