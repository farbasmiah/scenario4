import math
import matplotlib.pyplot as plt

def equation (x1,y1,x2,y2):
    if x1==x2:
        return (y1,0)
    x1 += 0.0
    grad = (y2-y1)/(x2-x1)
    cons = y1 - (x1 * grad)
    return (grad,cons)

def intersection (fst,snd):
    if fst[0] == snd[0]:
        print "erro"
        return False
    x = fst[0] - snd[0]
    c = snd[1] - fst[1] + 0.0
    c = c/x
    return c

#xs = (0, 0), (2, 0), (2, 1), (1, 1), (1, 2), (3, 2), (3, 3), (0, 3)
xs = (8, 18), (20, 18), (20, 16), (21, 16), (21, 18), (24, 18), (24, 20), (25, 20), (25, 16), (26, 16), (26, 20), (29, 20), (29, 11), (17, 11), (17, 8), (35, 8), (35, 20), (36, 20), (36, 22), (23, 22), (23, 50), (9, 50), (9, 22), (8, 22), (8, 28), (6, 28), (6, 16), (2, 16), (2, 4), (0, 4), (0, 1), (-1, 1), (-1, 4), (-2, 4), (-2, 1), (-5, 1), (-5, 0), (9, 0), (9, -3), (7, -3), (7, -1), (6, -1), (6, -3), (5, -3), (5, -4), (6, -4), (6, -5), (-6, -5), (-6, -7), (-2, -7), (-2, -23), (2, -23), (2, -7), (6, -7), (6, -13), (4, -13), (4, -14), (7, -14), (7, -16), (8, -16), (8, -4), (9, -4), (9, -10), (10, -10), (10, -9), (17, -9), (17, -13), (18, -13), (18, -9), (20, -9), (20, -15), (23, -15), (23, -9), (25, -9), (25, -4), (10, -4), (10, -3), (16, -3), (16, -2), (10, -2), (10, 0), (12, 0), (12, 3), (15, 3), (15, 4), (6, 4), (6, 6), (14, 6), (14, 8), (6, 8), (6, 10), (16, 10), (16, 12), (6, 12), (6, 13), (8, 13), (8, 14), (6, 14), (6, 15), (9, 15), (9, 13), (10, 13), (10, 16), (8, 16)
x = []
y=[]


for q in range(0,2):
    if q==0:
        toAdd = x
    else:
        toAdd = y
    for h in xs:
        toAdd.append(h[q])

print x, " ", y
x.append(xs[0][0])
y.append(xs[0][1])
#x+=[2,4]
#y+=[2,4]

#plt.figure(1)
#plt.subplot(211)
plt.plot(x, y)
xs = (8, -16), (35, 8), (23, 50), (20, 18), (-2, 4), (6, -13), (36, 22), (18, -9), (6, -5), (-5, 0), (9, -10), (17, -13), (6, -3), (16, 12), (23, -9), (2, -23), (24, 18), (9, 15), (8, 16), (26, 16), (6, 28), (9, -3), (10, -9), (2, 4), (9, 22), (20, -15), (10, -3), (10, 0), (15, 4), (7, -1), (17, 11), (8, 14)
x=[]
y=[]
for q in range(0,2):
    if q==0:
        toAdd = x
    else:
        toAdd = y
    for h in xs:
        toAdd.append(h[q])
plt.plot(x,y,'ro')
#plt.axis([-10, 30, 60, 40])
plt.show()
#print intersection((2,-3),(7,28))

#print intersection ((equation(3,2.5,3,2)),(equation(3,2.5,3,3)))

#(0, 0), (2, 0), (2, 1), (1, 1), (1, 2), (3, 2), (3, 3), (0, 3); (2, 0), (3, 2.5)

