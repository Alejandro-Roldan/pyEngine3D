import pygame

class Screen:
    def __init__(self, width, height, title, background):
        #calculate center of screen
        self.zeros = [int(width/2), int(height/2)]

        # self variables
        self.title = title
        self.background = background

        # Initialize Pygame window
        pygame.init()
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(self.title)
        self.window.fill(background)
        pygame.display.update()
    
    def createTriangle(self, points, color):
        a, b, c = points[0], points[1], points[2]
        # Create coordinates starting in center of screen
        coords = ((a[0] + self.zeros[0], a[1] + self.zeros[1]), (b[0] + self.zeros[0], b[1] + self.zeros[1]), (c[0] + self.zeros[0], c[1] + self.zeros[1]))
        # Draw triangle on screen
        return pygame.draw.polygon(self.window, color, coords, 1)

    def createLine(self, points, color):
        a, b = points[-2], points[-1]
        return pygame.draw.line(self.window, color, a, b, 1)

    def createLines(self, points, color):
        return pygame.draw.lines(self.window, color, True, points, 1)

    def clear(self):
        #clear display
        self.window.fill(self.background)
