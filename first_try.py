from visual import *
from my_visual.my_display import MyDisplay
from my_visual.my_box import MyBox


x = MyDisplay()

'''
x = MyBox(None, color.gray(0.8), 2)
x.set_front(color.red)
x.set_back(color.orange)
x.set_top(color.yellow)
x.set_bottom(color.white)
x.set_left(color.green)
x.set_right(color.blue)



side = Side(4,0)
for x in xrange(4):
    for y in xrange(4):
        side.set_part(x,y, str(y+1)+" "+str(x+1))

side._array = zip(*side._array[::1])
print(side.my_print())

'''

'''
def random():
    top = box()
    top.size = vector(8, 1, 8)
    top.pos = vector(0, 4.5, 0)
    top.color = color.green

#x=VisualSide(5,color.red,vector(0,0,0))
x=VisualCube()

main_window = display()
main_window.background = color.blue
'''

#main_window.add_renderable(random())

#this.add_renderable(x.side)
'''
top = box()
top.size = vector(8, 1, 8)
top.pos = vector(0, 4.5, 0)
top.color = color.green
edge = box()
edge.size = vector(8, 1, 1)
edge.pos = vector(0, 4.5, 4.5)
edge.color = color.black
front = box()
front.size = vector(8, 8, 1)
front.pos = vector(0, 0, 4.5)
left = box()
left.size = vector(1, 8, 8)
left.pos = vector(4.5, 0, 0)
'''



#my_num = raw_input("Enter something: ")
#print(my_num)
#x._array_block[0][0].color = color.black
#x._array_block[1][3].rotate(angle=5, axis=2)

