#BlockClass
#21.01.2020
#Ole, Philippe

import sys, pygame

class block(object):
    def __init__(self, lenght, height, position, color):
        super(block, self).__init__()
        self.lenght = lenght*24
        self.height = height*24
        self.position = position
        self.color = color
        self.screen = pygame.display.get_surface()
        #self.hitbox = Hitbox(self, (self.lenght, self.height), True)
        pygame.draw.rect(self.screen, self.color, [self.position[0],self.position[1], self.lenght, self.height])
