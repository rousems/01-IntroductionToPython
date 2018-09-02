"""
An exercise that summarizes what you have learned in this Session.

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Matthew Rouse.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()
#chad = rg.SimpleTurtle('circle')
#chad.pen = rg.Pen('blue', 4)
#chad.speed = 4

#chad.left(90)
#chad.forward(200)
#chad.pen_up()
#chad.go_to(rg.Point(100, -40))
#chad.pen_down()
#chad.pen = rg.Pen('green', 10)
#chad.right(180)
#chad.forward(150)
chad = rg.SimpleTurtle('turtle')
chad.pen = rg.Pen('blue', 4)
chad.speed = 4
chad.pen_up()
chad.left(90)
chad.forward(50)
chad.left(90)
chad.forward(175)
chad.right(90)
chad.pen_down()
chad.forward(100)
chad.pen_up()
chad.right(90)
chad.forward(250)
chad.right(90)
chad.pen_down()
chad.forward(100)
chad.left(90)
chad.pen_up()
chad.forward(50)
chad.pen_down()
chad.left(90)
chad.forward(100)
chad.pen_up()
chad.backward(250)
chad.left(90)
chad.pen_down()
chad.backward(100)
chad.pen_up()
chad.forward(150)
chad.pen_down()
chad.right(90)
chad.forward(100)
chad.left(90)
chad.pen_up()
chad.forward(200)
chad.pen_down()
chad.left(90)
chad.forward(100)
chad.pen_up()
chad.right(90)
chad.forward(50)
chad.right(90)
chad.pen_down()
chad.forward(100)
chad.left(90)
chad.pen_up()
chad.forward(500)

########################################################################
# DONE: 2.
#   Write code that accomplishes the following:
#     - Constructs a SimpleTurtle with a  blue  Pen.
#     - Makes the SimpleTurtle go straight UP 200 pixels.
#     - Tells the SimpleTurtle to make its pen go UP
#          (so that the next movements do NOT leave a "trail")
#          HINT: Use the "dot trick" to figure out how to do this.
#     - Tells the SimpleTurtle to go to (100, -40).
#     - Tells the SimpleTurtle to make its pen go DOWN
#          (so that the next movements will return to leaving a "trail")
#     - Makes the SimpleTurtle's pen have color "green" and thickness 10.
#     - Tells the SimpleTurtle to go 150 pixels straight DOWN.
#
# Don't forget to:
#     - import rosegraphics and construct a TurtleWindow
#          at the BEGINNING of your code, and to
#     - ask your TurtleWindow to   close_on_mouse_click
#          as the LAST line of your code.
#   See the beginning and end of m4e_loopy_turtles for an example.
#
#      ** Nothing fancy is required. **
#      ** The NEXT exercise will let you show your creativity. **
#
#   As always, test by running the module.
#
#   As always, COMMIT-and-PUSH when you are done with this module.
#
###############################################################################

window.close_on_mouse_click()