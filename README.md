# Cat-And-Mouse
LEGO Mindstorms Robot Project of a mouse running from a cat


Goal: To develop a robot "mouse" that moves around and says a phrase until it sees a "cat". Then, it will run back to its home and hide.

Project Requirements - 
1) "Mouse" is a LEGO EV3 robot, programmed with Micropython and Pybricks (https://pybricks.com/ev3-micropython/)
2) "Mouse" is built to the EV3D4 format
3) "Mouse" must move semi-randomly
4) "Mouse" must search for a "cat" using color sensor (Cat will be Yellow for this project)
5) Upon seeing the "cat", "mouse" will return to its starting point ("home") and quit program ("hiding")
6) While moving, mouse will say "while the cat is out the mice come out to dance", and upon seeing the cat the mouse will say "the cat has returned" (Phrases will be in French for client)
7) Movement area is a 50cm x 50cm square with no demarcating lines or hard walls
8) Robot will be placed in the bottom-leftmost square in the "grid" (see below)


I decided to implement a coordinate grid system to make keeping track of current position and walls easily and to make odometry simpler for returning to starting point.
It is essentially Quadrant I of an (x,y) coordinate grid, with North being up the Y axis, etc.
For the tracking, etc. to work, robot must be placed in the bottom-leftmost square (0,0) and facing North (ie. facing straight up the y-axis). 


Future changes/expansions:
1) Fixing odometry - As with all situations involving counting wheel rotations and adding lots of small changes, this is not very accurate and error is very high.
2) Color sensor - The color sensors are not optimal for seeing the cat as the distance for an accurate color sense is very close. Another sensor may be preferable.
3) Communication/Multiple Robots - It would be interesting to put this on multiple robots and have them all running around, then run home if ANY sees the cat. Could be a fun extension project for a future class, etc.
