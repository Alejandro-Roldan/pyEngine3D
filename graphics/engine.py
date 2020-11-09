import graphics.screen
import graphics.face
import graphics.vertex

import pygame
from pygame.locals import *
from functools import reduce


class Engine3D:
    def __resetDrag(self):
        self.__prev = []
    
    def __drag(self, x, y):
        if self.__prev:
            self.rotate('y', (x - self.__prev[0]) / 20)
            self.rotate('x', (y - self.__prev[1]) / 20)
        self.__prev = [x, y]

    def __zoomin(self):
        self.scale += 2.5

    def __zoomout(self):
        self.scale -= 2.5

    def __deselect(self, event):
        if self.__selected != None:
            self.__selected = None
            self.__axis = [self.screen.delete(line) for line in self.__axis]
            self.__moveaxis = None

    def __cameramove(self, u):
        self.screen.zeros[0] += u[0]
        self.screen.zeros[1] += u[1]
        
    def writePoints(self, points):
        self.points = []
        for point in points:
            self.points.append(graphics.vertex.Vertex(point))
            
    def writeTriangles(self, triangles):
        self.triangles = []
        for triangle in triangles:
            if len(triangle) != 4:
                triangle.append('gray')
            self.triangles.append(graphics.face.Face(triangle))
            
    def __init__(self, points, triangles, width=1000, height=700, distance=6, scale=100, title='3D', background='white'):
        #object parameters
        self.distance = distance
        self.scale = scale
        self.__prev = []

        # Dictionary with vector movement for the movement keys
        self.move_map = {K_w: ( 0, -5), K_s: ( 0,  5), K_a: (-5,  0), K_d: ( 5,  0)}
        
        #initialize display
        self.screen = Pygame_Screen(width, height, title, background)
        
        #store coordinates
        self.writePoints(points)
        self.flattened = []

        #store faces
        self.writeTriangles(triangles)

    def add(self, u, v):
        ''' Vector add '''
        return [u[i]+v[i] for i in range(len(u))]

    def events(self):
        ''' Event handling '''
        for event in pygame.event.get():
            # Control zoom with the mouse wheel
            if event.type == MOUSEBUTTONDOWN:
                # Mouse wheel forward
                if event.button == 4:
                    self.__zoomin()
                # Mouse wheel backward
                if event.button == 5:
                    self.__zoomout()

            # Reset drag when the left mouse button is unclicked
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    self.__resetDrag()

        # Get all pressed keys
        pressed_key = pygame.key.get_pressed()
        pressed_mouse = pygame.mouse.get_pressed()

        # Get all directions the camera should move
        move = [self.move_map[key] for key in self.move_map if pressed_key[key]]
        # Add all directions together to get the final direction
        reduced = reduce(self.add, move, (0, 0))
        # When the movement is non-zero update the camera position
        if reduced != (0, 0):
            self.__cameramove(reduced)

        # When the left click is pressed drag the model
        if pressed_mouse[0] is True:
            x, y = pygame.mouse.get_pos()
            self.__drag(x, y)

        # Move the event queue forward
        pygame.event.pump()

    def clear(self):
        #clear display
        self.screen.clear()

    def rotate(self, axis, angle):
        #rotate model around axis
        for point in self.points:
            point.rotate(axis, angle)

    def render(self):
        #calculate flattened coordinates (x, y)
        self.flattened = []
        for point in self.points:
            self.flattened.append(point.flatten(self.scale, self.distance))

        #get coordinates to draw triangles
        triangles = []
        for triangle in self.triangles:
            avgZ = -(self.points[triangle.a].z + self.points[triangle.b].z + self.points[triangle.c].z) / 3
            triangles.append((self.flattened[triangle.a], self.flattened[triangle.b], self.flattened[triangle.c], triangle.color, avgZ))

        #sort triangles from furthest back to closest
        triangles = sorted(triangles,key=lambda x: x[4])

        #draw triangles
        for triangle in triangles:
            self.screen.createTriangle(triangle[0:3], triangle[3])
