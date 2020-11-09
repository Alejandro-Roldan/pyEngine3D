### Cube ###

import graphics.engine
import pygame

points = [[-1,-1,-1],[-1,-1,1],[-1,1,1],[-1,1,-1],[1,-1,-1],[1,-1,1],[1,1,1],[1,1,-1]]
triangles = [[0,1,2],[0,2,3],[2,3,7],[2,7,6],[1,2,5],[2,5,6],[0,1,4],[1,4,5],[4,5,6],[4,6,7],[3,7,4],[4,3,0]]

test = graphics.engine.Engine3D(points, triangles, title='Cube')

def animation():
    test.clear()
    test.rotate('y', 0.2)
    test.rotate('x', 0.2)
    test.render()

# Create a pygame Clock object
clock = pygame.time.Clock()

running = True
# Mainloop
while running:
    # Limit fps to 60
    clock.tick(60)
    print('FPS: {:.2f}'.format(clock.get_fps()), end='\r')

    # Check the event queue
    test.events()
    # Draw the image
    animation()

pygame.quit()

############
