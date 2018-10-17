'''
Created on Apr 21, 2014

curve of y=log x
@author: boyerje
'''

from graphics import *
import math
def main():
    win = GraphWin('y=log(x)', 300, 300)
    win.yUp() # 0,0 is in left lower corner - right side up coordinates
    # 0,0 is not visible
    yaxis=Line(Point(3,3), Point(3,win.getHeight()))
    yaxis.setWidth(2)
    yaxis.draw(win)
    xaxis=Line(Point(0,win.getHeight()/2), Point(win.getWidth(),win.getHeight()/2))
    xaxis.setWidth(2)
    xaxis.draw(win)
    # a unit on x is 1/10 of the length of x axis
    xscale=win.getWidth()/10
    # while y is at 1/8 
    yscale=win.getHeight()/8
    # draw a little vertical part at (1,0)  
    unit=Line(Point(xscale,win.getHeight()/2-5),Point(xscale,win.getHeight()/2+5))
    unit.draw(win)
    
    # draw log
    x=0.0001     # log 0 = -infinity
    y=math.log(x)
    step=0.2  # make a step small enough to have nice curve
    while x < 10 :
        x2=x+step
        y2=math.log(x2)
        # x axis moves of height/2 homothety
        l=Line(Point(x*xscale,win.getHeight()/2+y*yscale),Point(x2*xscale,win.getHeight()/2+y2*yscale))
        l.draw(win)
        y=y2
        x=x2
        

    # text is centered over the point specified
    message = Text(Point(win.getWidth()/2, 30),'Click anywhere to quit')
    message.setStyle('italic')
    message.setSize(10)
    message.draw(win)
    win.getMouse()
    win.close() 
        
    
main()
    