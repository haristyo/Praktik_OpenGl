from OpenGL.GL import *
from OpenGL.GLUT import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    
    glBegin(GL_POLYGON)
    glVertex2f(-0.5, -0.5)
    glVertex2f(-0.5, 0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(0.5, -0.5)
    glEnd()

    glFlush()

# def main():
glutInit(sys.argv)
glutInitWindowSize(800, 600)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Contoh Jendela GLUT")
glutDisplayFunc(display)
glutMainLoop()

# if __name__ == "__main__":
# main()
