import pygame
from pygame.locals import *
import numpy as np
import math

from OpenGL.GL import * 
from OpenGL.GLU import *
from OpenGL.GLUT import *
    
def init():
    glClearColor(0,1,0, 1); 

def plotFunc1() :
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(1.0)
    for x in np.arange(-5.0, 5.0, 0.01):
        y = x*x - 2
        glColor3f(0.0, 0.0, 0.0)
        glBegin(GL_POINTS)
        glVertex2f(x,y)
        glEnd()
        for a in np.arange(-5.0, 5.0, 0.01):
            if a < ((x*x) - 2):
                glColor3f(0.50,0.50,0.50)
                glBegin(GL_POINTS)
                glVertex2f(x,a)
                glEnd()
                glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(-5.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, -5.0)
    glEnd()
    glFlush()
    
def main():
    pygame.init()
    display = (600,600)
    pygame.display.set_caption ('Haris Prasetyo - 0102523717') 
    pygame.display.set_mode (display, DOUBLEBUF | OPENGL)
    gluPerspective (45, (display [0]/display [1]), 0.1, 50.0) 
    # glutInitWindowSize(800, 600);  # Set dimensi jendela
    glTranslatef (0.0,0.0, -5)
    init()
    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit ()
        glClear (GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT)
        plotFunc1()
        pygame.display.flip()
        pygame.time.wait (10)

main()