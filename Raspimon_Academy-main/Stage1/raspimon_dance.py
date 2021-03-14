from sense_emu import SenseHat
from time import sleep


sense = SenseHat()
sense.low_light = True

#load the Raspimons you want to animate
r = (255, 0, 0 ) # RED color, stored in an another data structure called a tuple.
k = (0, 0, 0) # black means zero amounts of red, green and blue
r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)
k = (0, 0, 0)
w = (255, 255, 255)
c = (0, 255, 255)
y = (255, 255, 0)
o = (255, 128, 0)
n = (255, 128, 128)
p = (128, 0, 128)
d = (255, 0, 128)
l = (128, 255, 128)

rmon1 = [c, c, c, c, c, c, c, c,
         c, c, n, n, n, n, c, c,
         c, n, n, n, n, n, n, c,
         c, n, n, k, n, k, n, c,
         n, n, n, b, n, b, n, n,
         n, n, d, n, n, n, d, n,
         c, n, n, n, n, n, n, c,
         g, n, n, g, g, n, n, g
         ]

rmon2 = [c, c, n, n, n, n, c, c,
         c, n, n, n, n, n, n, c,
         c, n, n, k, n, k, n, c,
         n, n, n, b, n, b, n, n,
         n, n, d, n, n, n, d, n,
         c, n, n, n, n, n, n, c,
         c, n, n, c, c, n, n, c,
         g, g, g, g, g, g, g, g
         ]
    
    
    
    
    
    
    

for i in range(20):
  #animate your raspimon!
    sense.set_pixels(rmon1)
    sleep(1)
    sense.set_pixels(rmon2)
    sleep(1)
#while True:
  #dance forever!