import turtle
XMIN = -100
XMAX = 60
MARGIN = 40

# funkcijas vērtību aprēķināšana
def calculate_fn(x: float) -> float:
    y = x/2 + 5
    return y

# parādīt koordinātu asis un apzīmējumus
def draw_axis(l: float, axis_color: str="black"):
    t1 = turtle.Turtle(visible=False)
    t1.width(2)
    t1.color(axis_color)
    # draw y axis
    t1.penup()
    t1.goto(0,l + 20)
    t1.pendown()
    t1.goto(0,-l - 20)
    # draw x axis
    t1.penup()
    t1.goto(l+20,0)
    t1.pendown()
    t1.goto(-l-20,0)
    # add labels
    t1.penup()
    t1.setpos(4,0)
    t1.pendown()
    t1.write("0",font=("Arial", 10, "bold"))
    t1.penup()
    t1.setpos(4,l)
    t1.pendown()
    t1.write("Y",font=("Arial", 10, "bold"))
    t1.penup()
    t1.setpos(l,0)
    t1.pendown()
    t1.write("X",font=("Arial", 10, "bold"))
    
    return

# funkcijas grafika zīmēšana. Tā kā funkcija ir lineāra, pietiek aprēķināt y vērtību intervāla sākumā un beigās
# un savienot šos punktus
def plot_function(xmin: float, xmax: float, plot_color: str="red"):
    t = turtle.Turtle(visible=False)
    t.speed("fastest")
    t.color(plot_color)
    t.penup()
    t.goto(xmin,calculate_fn(xmin))
    t.pendown()
    t.goto(xmax,calculate_fn(xmax))
    turtle.done()

# funkcija x vērtību intervāla robežu ievadei
# intervāla garumam jābūt vismaz 150 vienību.
def get_interval() -> tuple:
    MININT = 150        # intervāla minimālais garums
    print("Ievadiet x vērtību intervāla robežas x1 un x2. Intervāla garumam jābūt vismaz 150.\n")
    while True:
        x1 = get_value("\nIevadiet x1: ")
        x2 = get_value("\nIevadiet x2: ")
        if x1 > x2:
            x1, x2 = x2, x1
        if x2 - x1 >= MININT:
            return(x1, x2)
    return

# funkcija veselu skaitļu ievadīšanai
def get_value(prompt: str) -> int:
    while True:
        tmp = input(prompt)
        try:
            t = int(tmp)
            t = t // 1
            return t
        except:
            pass
    return

# ekrāna konfigurēšana: laukums un fona krāsa
def setup_screen(interval: float,bg_color: str="white"):
    canvas_size = 2*interval + MARGIN*4
    turtle.setup(width=canvas_size, height=canvas_size,startx=MARGIN,starty=MARGIN)
    turtle.screensize(canvwidth=canvas_size, canvheight=canvas_size, bg=bg_color)
    return


def main():
    # get x range
    # x_values = (XMIN,XMAX)
    x_values = get_interval()
    x_interval = x_values[1] - x_values[0]
    setup_screen(x_interval,"gray")
    draw_axis(x_interval,axis_color="black")
    plot_function(x_values[0], x_values[1],plot_color="red")
    return
    
if __name__ == "__main__":
    main()
