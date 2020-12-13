from graphics import*
from time import*
from random import*
from math import sqrt

def Distance(cir1, cir2):
	center1 = cir1.getCenter()
	center2= cir2.getCenter()
	x1 = center1.getX()
	y1 = center1.getY()
	x2 = center2.getX()
	y2 = center2.getY()
	dist = sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
	return dist
win = GraphWin("Invaders",1000,500)

r1 = Rectangle(Point(500,450),Point(550, 490))
r1.setFill("blue")
r1.draw(win)
c1 = Circle(Point(100,100),30)
c1.setFill("red")
c1.draw(win)
c2 = Circle(Point(200,100),30)
c2.setFill("red")
c2.draw(win)
c3 = Circle(Point(300,100),30)
c3.setFill("red")
c3.draw(win)
c4 = Circle(Point(400,100),30)
c4.setFill("red")
c4.draw(win)
c5 = Circle(Point(500,100),30)
c5.setFill("red")
c5.draw(win)
won = False
shoot = False
x_velocity = 2
y_velocity = 0
keyPress = ""
circles = [c1,c2,c3,c4,c5]
score = 0
while won == False:
	y_velocity = 0
	center1 = c1.getCenter()
	center2 = c2.getCenter()
	center3 = c3.getCenter()
	center4 = c4.getCenter()
	center5 = c5.getCenter()
	c1x = center1.getX()
	c2x = center2.getX()
	c3x = center3.getX()
	c4x = center4.getX()
	c5x = center5.getX()
	c1y = center1.getY()
	c2y = center2.getY()
	c3y = center3.getY()
	c4y = center4.getY()
	c5y = center5.getY()
	keyPress = win.checkKey()
	rCenter = r1.getCenter()
	rx = rCenter.getX()
	ry = rCenter.getY()
	if score == 5:
		won = True
		message = Text(Point(100,20), "Congrats you won!")
		message.draw(win)
		sleep(5)
	if shoot == True:
		shot_center = shot.getCenter()
		shot_y = shot_center.getY()
		for x in circles:
			if Distance(x,shot) <= 30:
				x.setOutline("white")
				x.setFill("white")
				circles.remove(x)
				score = score + 1
				shot.undraw()
				shoot = False
		if shot_y <= 0 and shoot == True:
			shot.undraw()
			shoot = False
	if keyPress == "d" and rx + 50 != 1000:
		r1.move(5,0)
	if keyPress == "a" and rx - 50 != 0:
		r1.move(-5,0)
	if keyPress == "w" and shoot == False:
		shot = Rectangle(Point(rx - 3, ry - 3),Point(rx + 3, ry + 3))
		shot.setFill("green")
		shot.draw(win)
		shoot = True
	if c1y + 30 == 430 or c2y + 30 == 430 or c3y + 30 == 430 or c4y + 30 == 430 or c5y + 30 == 430:
		won = True
		message = Text(Point(100,20), "Game Over")
		message.draw(win)
		sleep(5)
	if c1x + 30 == 1000 or c2x + 30 == 1000 or c3x + 30 == 1000 or c4x + 30 == 1000 or c5x + 30 == 1000:
		x_velocity = x_velocity*-1
		y_velocity = 50
		c1.move(x_velocity, y_velocity)
		c2.move(x_velocity, y_velocity)
		c3.move(x_velocity, y_velocity)
		c4.move(x_velocity, y_velocity)
		c5.move(x_velocity, y_velocity)
		sleep(0.001)
	elif c1x - 30 == 0 or c2x - 30 == 0 or c3x - 30 == 0 or c4x - 30 == 0 or c5x - 30 == 0:
		x_velocity = x_velocity*-1
		y_velocity = 50
		c1.move(x_velocity, y_velocity)
		c2.move(x_velocity, y_velocity)
		c3.move(x_velocity, y_velocity)
		c4.move(x_velocity, y_velocity)
		c5.move(x_velocity, y_velocity)
		sleep(0.001)
	else:
		if shoot == True:
			shot.move(0,-10)
		c1.move(x_velocity, y_velocity)
		c2.move(x_velocity, y_velocity)
		c3.move(x_velocity, y_velocity)
		c4.move(x_velocity, y_velocity)
		c5.move(x_velocity, y_velocity)
		sleep(0.001)
