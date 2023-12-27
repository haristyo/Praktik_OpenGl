import pygame
from pygame.locals import *

from OpenGL.GL import * 
from OpenGL.GLU import *
from OpenGL.GLUT import *
def Cube ():
    glBegin (GL_QUADS)
    glVertex2f(-0.8, -0.8)
    glVertex2f(-0.8, 0.8); 
    glVertex2f(0.8, 0.8); 
    glVertex2f(0.8, -0.8); 
    glEnd ()
    
def Triangle ():
    glBegin (GL_TRIANGLES)
    glVertex2f(-0.8, -0.8)
    glVertex2f(-0.8, 0.8); 
    glVertex2f(0.8, 0.8); 
    # glVertex2f(0.8, -0.8); 
    glEnd ()

def TriangleStripe ():
    glBegin (GL_TRIANGLE_STRIP)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.0, 0.5); 
    glVertex2f(0.5, -0.5); 
    glVertex2f(1.0, 0.5); 
    glVertex2f(1.5, -0.5); 
    glVertex2f(2.0, 0.5); 
    glEnd ()
    
    
def Lines ():
    glBegin (GL_LINES)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.0, 0.5); 
    glVertex2f(0.0, 0.5); 
    glVertex2f(0.5, -0.5); 
    glVertex2f(0.5, -0.5); 
    glVertex2f(1.0, 0.5); 
    glVertex2f(1.0, 0.5); 
    glVertex2f(1.5, -0.5); 
    glVertex2f(1.5, -0.5); 
    glVertex2f(2.0, 0.5); 
    glEnd ()
    
def segiDelapan ():
    glBegin (GL_POLYGON)
    glVertex2f(-1, 0.4)
    glVertex2f(-0.4, 1); 
    glVertex2f(0.4, 1); 
    glVertex2f(1, 0.4); 
    glVertex2f(1, -0.4); 
    glVertex2f(0.4, -1); 
    glVertex2f(-0.4, -1); 
    glVertex2f(-1.0, -0.4); 
    glEnd ()
    
def init():
    glClearColor(0,0.0,0, 1); 
    glColor3f(1, 0.0, 0.0); 
    glMatrixMode(GL_PROJECTION); 
    glLoadIdentity(); 
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
    return 
   
def main():
    pygame.init()
    display = (750,750)
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
        Lines()
        # Cube()
        # Triangle()
        # TriangleStripe()
        # segiDelapan()
        pygame.display.flip()
        pygame.time.wait (10)
main()