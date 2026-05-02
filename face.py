from turtle import*
class Face():
    def __init__(self, xpos, ypos):
        self.size = 90
        self.coord(xpos,ypos)
        self.noseSize ='small'
    def SetSize(self,radius):
        self.size = radius
    def draw(self):
        self.goHome()
        pensize(3)
        speed(0)
        self.drawOutline()
        self.drawEye(135)
        self.drawEye(45)
        self.drawMouth()
        self.drawNose()
#After drawing each part, turtle position
#returns to the centre, Parts can be drawn in any order
    def goHome(self):
        penup()
        goto(self.coord)
        setheading(0)
    def drawOutline(self):
        penup()
        #move turtle pen in forward direction
        forward(self.size)
        left(90)
        #Draw a circle of given radius
        pendown()
        circle(self.size)
        #return back to center