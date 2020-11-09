### Shark ###

import graphics.engine

points = []
triangles = []

with open('coords/SharkV.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        coords = line[:-2].split(' ')
        points.append([float(coords[0]), float(coords[1]), float(coords[2])])
    f.close()

with open('coords/SharkT.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        coords = line[:-2].split(' ')
        newCoords = []
        for coord in coords[1:4]:
            newCoords.append(int(coord))
        triangles.append(newCoords)
    f.close()

test = graphics.engine.Engine3D(points, triangles, scale=100, title='Shark')

def animation():
    test.clear()
    test.rotate('y', 0.1)
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
    game.events()
    # Draw the image
    animation()

pygame.quit()

##############
