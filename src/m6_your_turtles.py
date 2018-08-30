"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Matthew Rouse.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################
import rosegraphics as rg
window = rg.TurtleWindow

###############################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

chad = rg.SimpleTurtle('turtle')
chad.pen = rg.Pen('midnight blue', 5)
chad.speed = 5

for k in range(5):

    chad.draw_circle(60)
    chad.right(72)

lela = rg.SimpleTurtle('turtle')
lela.pen = rg.Pen('red', 6)
lela.speed = 6

for l in range(5):

    lela.draw_square(70)
    lela.left(72)

window.close_on_mouse_click()