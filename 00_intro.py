import py5

def setup():
    py5.size(400,400)

def draw():
    py5.background(192, 64, 0)
    fun02()
    fun03()

def fun00():
    py5.stroke(255)
    py5.line(150, 25, 270, 350)

def fun01():
    py5.stroke(255) # sets the stroke color to white
    py5.stroke(255, 255, 255) # identical to stroke(255)
    py5.stroke(255, 128, 0) # bright orange (red 255, green 128, blue 0)
    py5.stroke('#FF8000') # bright orange as a web color
    py5.stroke(255, 128, 0, 128) # bright orange with 50% transparenc

def fun02():
    py5.stroke(255)
    py5.line(150, 25, py5.mouse_x, py5.mouse_y)

def fun03():
    py5.fill(255, 255, 0)
    py5.ellipse(py5.width/2, py5.height/2, 50,50)    

def mouse_pressed():
    py5.background(192, 64, 0)

py5.run_sketch()