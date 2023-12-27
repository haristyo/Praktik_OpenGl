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
def CubeGlut():
    glClear(GL_COLOR_BUFFER_BIT)
    # ... (tambahkan kode untuk merender objek atau apapun yang diinginkan)
    glBegin (GL_QUADS)
    glVertex2f(-0.8, -0.8)
    glVertex2f(-0.8, 0.8); 
    glVertex2f(0.8, 0.8); 
    glVertex2f(0.8, -0.8); 
    glEnd ()
    glutSwapBuffers()
    
def init():
    glClearColor(0,0,0, 1); 
    glColor3f(0.5, 0.5, 0.5); 
    glMatrixMode(GL_PROJECTION); 
    glLoadIdentity(); 
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
    return    
    
def mainGlut():
    glutInit(sys.argv)
    glutInitWindowSize(800, 600)  # Lebar dan tinggi jendela

    # Mengatur posisi jendela
    glutInitWindowPosition(500, 300)
    glutCreateWindow(b"Contoh Jendela GLUT")

    glutDisplayFunc(CubeGlut)  # Daftarkan fungsi display

    glutMainLoop()  # Mulai loop utama GLUT
def main():
    pygame.init()
    display = (600,900)
    pygame.display.set_caption ('Hello World..!!') 
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
        Cube()
        pygame.display.flip()
        pygame.time.wait (10)
# main()
mainGlut()