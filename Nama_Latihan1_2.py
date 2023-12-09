# from pygame.locals import *
# from OpenGL.GL import * 
# from OpenGL.GLU import *
# import pygame
# def Cube ():
#     glBegin (GL_QUADS)
#     glVertex2f(-0.8, -0.8); 
#     glVertex2f(-0.8, 0.8); 
#     glVertex2f(0.8, 0.8); 
#     glVertex2f(0.8, -0.8); 
#     glEnd ()
    
# def init():
#     glClearColor (1.0, 0.0, 0.0, 1.0); 
#     glColor3f (0.0, 1.0, 1.0); 
#     glMatrixMode (GL_PROJECTION); 
#     glLoadIdentity(); 
#     glOrtho(-1.0,1.0,-1.0,1.0,-1.0,1.0); 
    
    
# def main():
#     init()
#     display = (800,600)
#     pygame.display.set_caption ('Hello World..!!') 
#     pygame.display.set_mode (display, DOUBLEBUF | OPENGL)
#     gluPerspective (45, (display [0]/display [1]), 0.1, 50.0) 
#     glTranslatef (0.0,0.0, -5)
#     while True:
#         for event in pygame.event.get(): 
#             if event.type == pygame.QUIT: 
#                 pygame.quit()
#                 quit ()
#         glClear (GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT)
#         Cube()
#         pygame.display.flip()
#         pygame.time.wait (10)

# main()



import pygame
from pygame.locals import *

from OpenGL.GL import * 
from OpenGL.GLU import *
def Cube ():
    glBegin (GL_QUADS)
    glVertex2f(-0.8, -0.8); 
    glVertex2f(-0.8, 0.8); 
    glVertex2f(0.8, 0.8); 
    glVertex2f(0.8, -0.8); 
    glEnd ()
    
def init():
    glClearColor (1.0, 0.0, 0.0, 1.0); 
    glColor3f (0.0, 1.0, 1.0); 
    glMatrixMode (GL_PROJECTION); 
    glLoadIdentity(); 
    glOrtho(-1.0,1.0,-1.0,1.0,-1.0,1.0);     
    
def main():
    init()
    display = (800,600)
    pygame.display.set_caption ('Hello World..!!') 
    pygame.display.set_mode (display, DOUBLEBUF | OPENGL)
    gluPerspective (45, (display [0]/display [1]), 0.1, 50.0) 
    glTranslatef (0.0,0.0, -5)
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