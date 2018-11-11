import turtle
import numpy as np
import vtolParam as P

class vtolAnimationTurtle():

    def __init__(self):

		turtle.register_shape("quad.GIF")
		self.vtol = turtle.Turtle()
		self.vtol.shape("quad.GIF")
		self.vtol.shapesize(.25,.25)
		self.vtol.speed(0)
		self.vtol.color('red')
		self.vtol.penup()
		self.vtol.setheading(0)
		self.vtol.setposition(0,0)
		
		self.ref = turtle.Turtle()
		self.ref.shape('circle')
		self.ref.shapesize(.2,.2)
		self.ref.speed(0)
		self.ref.color('black')
		self.ref.penup()
		
		
		self.scale = 50.0

        


    def drawVtol(self,u,reference):
        state = u[0]
        zv = state[0]
        h = state[1]
        theta = state[2]
        self.ref.setposition((reference[0]-3)*self.scale, (reference[1]-2)*self.scale)
        self.vtol.setposition((zv-3)*self.scale,(h-2)*self.scale)
        self.vtol.setheading(theta*180.0/np.pi+90)
