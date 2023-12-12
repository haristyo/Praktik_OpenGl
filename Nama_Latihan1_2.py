import pygame
from pygame.locals import *

from OpenGL.GL import * 
from OpenGL.GLU import *
def suriken(indexX=0,indexY=0,scale=1):
    glBegin(GL_POLYGON)
    # suriken
    # glVertex2f(0, 1) #klo ini pertama jadi rusak
    glVertex2f(indexX+( 0.25 * scale),indexY +(0.25 * scale))
    glVertex2f(indexX+( 1 * scale),indexY +( 0 * scale))
    glVertex2f(indexX+( 0.25 * scale),indexY +( (-0.25) * scale))
    glVertex2f(indexX+(0 * scale),indexY +( (-1) * scale))
    glVertex2f(indexX+(-0.25 * scale),indexY +( (-0.25) * scale))
    glVertex2f(indexX+(-1 * scale),indexY +( 0 * scale))
    glVertex2f(indexX+(-0.25 * scale),indexY +( 0.25 * scale))
    
    glVertex2f(indexX+(0* scale),indexY + (1* scale)) #klo ini terakhir jadi bisa
    glEnd ()

def demokrat(indexX=0,indexY=0,scale=1):
    glBegin(GL_POLYGON)
    # demokrat
    glVertex2f(indexX+(0.4*scale),indexY +((0.4)*scale))
    glVertex2f(indexX+(1.1*scale),indexY +((-0.3)*scale))
    glVertex2f(indexX+(0*scale),indexY +((-0.1)*scale))
    glVertex2f(indexX+((-1.1)*scale),indexY +((-0.3)*scale))
    glVertex2f(indexX+((-0.4)*scale),indexY +((0.4)*scale))
    glVertex2f(indexX+(0*scale),indexY +((1.4)*scale))
    glEnd ()

def init():
    glClearColor(0, 0, 1, 1.0); 
    glColor3f(1, 0,0); 
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
        suriken(1.05,1.05,0.75)
        suriken(-1.05,1.05,0.75)
        suriken(1.05,-1.05,0.75)
        suriken(-1.05,-1.05,0.75)
        demokrat(0,0,0.5)
        pygame.display.flip()
        pygame.time.wait (10)
        
main()
## background colour ## object colour
##load identity ##projection