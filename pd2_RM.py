import turtle
import math

POINTS = 3
FULL_CIRCLE = 360
HEIGHT = 100

# funkcija zīmē vienādsānu trijstūri norādītajā virzienā (virzienu norāda grādos)
# parametri: virziens grādos (atbilstoši Turtle), trijstūra augstums pikseļos un pamata garums pikseļos
def draw_triangle(direction: int, star_angle: int, height: int):

    STRAIGHT_ANGLE = 90
    t = turtle.Turtle()
    edge_length = height/math.cos(math.radians(star_angle))
    print(direction, height, star_angle, edge_length)
    t.home()    # pozicionēties uz 0,0
    t.left(direction + STRAIGHT_ANGLE)
    t.penup()   
    t.forward(height)
    
    tmp = t.pos()
    t.left(180-star_angle)
    t.pendown()
    t.forward(edge_length)
    t.penup()
    t.setpos(tmp)
    t.right(-2*star_angle)     # TODO - FIX THIS
    t.pendown()
    t.forward(edge_length)
    t.penup()
    t.home()
    t.hideturtle()
    return

def test_star(points: int):
    
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    while True:
        turtle.forward(200)
        turtle.left(160)
        print(turtle.pos(),abs(turtle.pos()))
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()
    turtle.done()



def main():
    num_points = POINTS
    increment_angle = 360 / num_points
    base = HEIGHT       # aprēķināt
    star_angle = increment_angle/6
    # my_turtle = turtle.Turtle()
    
    for i in range(num_points):
        print(increment_angle * i)
        draw_triangle(increment_angle * i, star_angle, HEIGHT)
        
    
    # scr = turtle.getscreen()
    # test_star(POINTS)
     
    # my_turtle.forward(100)
    # my_turtle.right(-90)    
    # my_turtle.forward(100)
    # my_turtle.home()
    # my_turtle.goto(-50,50)
    # my_turtle.color('blue','yellow')
    # my_turtle.dot(50)
    
    # turtle2 = turtle.Turtle()
    # turtle2.color('red','green')
    # turtle2.right(45)
    # turtle2.forward(133)
    
    turtle.done()

if __name__ == "__main__":
    main()

