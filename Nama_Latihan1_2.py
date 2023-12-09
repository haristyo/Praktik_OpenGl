import pygame
from pygame.locals import *

from OpenGL.GL import * 
from OpenGL.GLU import *
def Cube ():
    glBegin (GL_TRIANGLES)
    # suriken
    glVertex2f(0, 1); 
    glVertex2f(1, 1.25); 
    glVertex2f(1, 2); 
    glVertex2f(1.25, 1.25); 
    glVertex2f(2, 1); 
    # glVertex2f(0.25, -0.25); 
    glVertex2f(1, 0); 
    # glVertex2f(-0.25, -0.25); 
    # glVertex2f(-1, 0); 
    # glVertex2f(0, -1); 
    # glVertex2f(1, 0); 
    
    # glVertex2f(-0.4, -0.4); 
    # glVertex2f(-1.8, 1.8); 
    # glVertex2f(0.3, 0.3); 
    # glVertex2f(1.8, -1.8);
    
    # segi 8
    # glVertex2f(0, 1)
    # glVertex2f(0.5, 0.5)
    # glVertex2f(1, 0)
    # glVertex2f(0.8, -0.8)
    # glVertex2f(0, -1)
    # glVertex2f(-0.8, -0.8)
    # glVertex2f(-1, 0)
    # glVertex2f(-0.8, 0.8)
     
    glEnd ()
    
def init():
    glClearColor(0.7, 0.3, 0.22, 1.0); 
    glColor3f(0.22, 0.9, 0.5); 
    glMatrixMode(GL_PROJECTION); 
    glLoadIdentity(); 
    glOrtho(-1.0,1.0,-1.0,1.0,-1.0,1.0)
    return     
    
def main():
    
    pygame.init()
    display = (1600,1000)
    pygame.display.set_caption ('0102523717 - Haris Prasetyo') 
    pygame.display.set_mode (display, DOUBLEBUF | OPENGL)
    gluPerspective (45, (display [0]/display [1]), 0.1, 50.0) 
    glTranslatef (0.0,0.0, -5)
    
    init()
    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit ()
        glClear (GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait (10)
        
main()
## background colour ## object colour
##load identity ##projection