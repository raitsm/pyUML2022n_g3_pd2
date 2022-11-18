import turtle
XMIN = -100
XMAX = 60
APMALE = 40

def calculate_fn(x: float) -> float:
    y = x/2 + 5
    return y

# draws axis and axis labels
def draw_axis(l: float, axis_color: str="black"):
    t1 = turtle.Turtle(visible=False)
    t1.width(2)
    t1.color(axis_color)
    # draw y axis
    t1.penup()
    t1.goto(0,l/2 + 20)
    t1.pendown()
    t1.goto(0,-l/2 - 20)
    # draw x axis
    t1.penup()
    t1.goto(l/2+20,0)
    t1.pendown()
    t1.goto(-l/2-20,0)
    # add labels
    t1.penup()
    t1.setpos(4,0)
    t1.pendown()
    t1.write("0",font=("Arial", 10, "bold"))
    t1.penup()
    t1.setpos(4,l/2)
    t1.pendown()
    t1.write("Y",font=("Arial", 10, "bold"))
    t1.penup()
    t1.setpos(l/2,0)
    t1.pendown()
    t1.write("X",font=("Arial", 10, "bold"))
    
    return

# plots the function
def plot_function(xmin: float, xmax: float, plot_color: str="red"):
    t = turtle.Turtle(visible=False)
    t.speed("fastest")
    t.color(plot_color)
    t.penup()
    t.goto(xmin,calculate_fn(xmin))
    t.pendown()
    t.goto(xmax,calculate_fn(xmax))
    turtle.done()

# takes user input with minimum and maximum values for x
# nb, the range between min and max x must exceed 150.
def get_interval() -> tuple:
    pass

# initial setup of turtle canvas
def setup_screen(interval: float,bg_color: str="white"):
    canvas_size = interval + APMALE*2
    turtle.setup(width=canvas_size, height=canvas_size)
    turtle.screensize(canvwidth=interval, canvheight=interval, bg=bg_color)
    return

def main():
    # get x range
    xmin = XMIN
    xmax = XMAX
    x_interval = xmax - xmin
    setup_screen(x_interval,"gray")
    draw_axis(x_interval,axis_color="black")
    plot_function(xmin, xmax,plot_color="red")
    
if __name__ == "__main__":
    main()
