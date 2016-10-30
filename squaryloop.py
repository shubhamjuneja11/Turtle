#!/usr/bin/env python
import turtle
import time
def drawsquare(b):
	for i in range (1,5):
		b.forward(100)
		b.right(90)
	
def drawart():
	window=turtle.Screen()
	window.bgcolor("green")
	b=turtle.Turtle()
	b.shape("turtle")
	b.color("yellow")

	for i in range (1,37):
		drawsquare(b)
		b.right(10)

drawart()

turtle.getscreen()._root.mainloop() 
