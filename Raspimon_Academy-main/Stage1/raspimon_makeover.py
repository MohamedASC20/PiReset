from sense_emu import SenseHat
from time import sleep

sense = SenseHat()

#makeover time! Here is a Python list. It holds  collection of string values.

names = ["Codey" , "Galbert" , "Freedy", "Voltria" , "Kat-Kat"]

names.append("Moe")

sense.show_message('hh')

#Colors:

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









#define another color. Use one letter variable names to make it easy later

raspimon = [
k, k, k, k, k, k, k, k,
k, r, r, r, r, r, r, k,
k, r, k, k, k, k, r, k,
k, r, r, k, r, k, r, k,
k, r, k, k, k, k, r, k,
k, r, r, r, r, r, r, k,
k, k, r, k, r, k, k, k,
k, k, r, k, r, k, k, k
]

rmon1 = [c, c, c, c, c, c, c, c,
         c, c, n, n, n, n, c, c,
         c, n, n, n, n, n, n, c,
         c, n, n, k, n, k, n, c,
         n, n, n, b, n, b, n, n,
         n, n, d, n, n, n, d, n,
         c, n, n, n, n, n, n, c,
         g, n, n, g, g, n, n, g
         ]
    
    
    
    
    
    
    
 
sense.set_pixels(rmon1)

#add a one-pixel mouth

 


