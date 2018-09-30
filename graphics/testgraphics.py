'''
Created on Apr 17, 2014

@author: jerome boyer
'''
import graphics
import time
def main():
    win = graphics.GraphWin('Back and Forth', 300, 300)
    win.yUp() # make right side up coordinates!

    rect = graphics.Rectangle(graphics.Point(200, 90), graphics.Point(220, 100))
    rect.setFill("blue")
    rect.draw(win)

    cir1 = graphics.Circle(graphics.Point(40,100), 25)
    cir1.setFill("yellow")
    cir1.draw(win)

    cir2 =  graphics.Circle(graphics.Point(150,125), 25)
    cir2.setFill("red")
    cir2.draw(win)

    for i in range(46):
        cir1.move(5, 0)
        time.sleep(.05)

    for i in range(46):
        cir1.move(-5, 0)
        time.sleep(.05)

    win.promptClose(win.getWidth()/2, 20)

main()
