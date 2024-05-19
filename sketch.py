from p5 import *

def setup():
  createCanvas(windowWidth, windowHeight)
  background(0)
x = 12
hue = 0

def draw():
  global x, hue
  # background(0)
  translate(width/2, height/2)
  # drawTickAxes()
  if mouseIsPressed:
    for i in range(x):
      stroke(hue, 100, 100)
      strokeWeight(5)
      point(mouseX - width/2, mouseY - height/2)
      rotate(360/x)
      hue += 18
      if hue > 360:
        hue = 0
  # text(keyCode, 0, 0)

def keyPressed():
  if keyCode == 76:
    save("hello, you have been spear phished ")
  if keyCode == 82:
    background(0)