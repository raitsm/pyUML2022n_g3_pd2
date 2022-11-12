import turtle

def main():
    
    scr = turtle.getscreen()
    my_turtle = turtle.Turtle()
    
     
    my_turtle.forward(100)
    my_turtle.right(-90)    
    my_turtle.forward(100)
    my_turtle.home()
    my_turtle.goto(-50,50)
    my_turtle.color('blue','yellow')
    my_turtle.dot(50)
    
    turtle2 = turtle.Turtle()
    turtle2.color('red','green')
    turtle2.right(45)
    turtle2.forward(133)
    
    turtle.done()

if __name__ == "__main__":
    main()

