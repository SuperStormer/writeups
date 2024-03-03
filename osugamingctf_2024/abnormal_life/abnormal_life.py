#!/usr/bin/env python3
import turtle

from osrparse import Replay

r = Replay.from_path("abnormal.osr")

prev = (0, 0)
turtle.setworldcoordinates(0, -6, 300, 1)
turtle.pendown()
for l in [(l.time, l.life) for l in r.life_bar_graph]:
	dist = (prev[0] - l[0])**2 + (prev[1] - l[1])**2
	if dist > 150:
		turtle.penup()
	turtle.goto(l)
	if dist > 150:
		turtle.pendown()
	prev = l
turtle.exitonclick()
