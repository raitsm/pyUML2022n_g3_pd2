import turtle
import math

POINTS = 11
FULL_CIRCLE = 360
CENTER_RADIUS = 20
RADIUS_DIFFERENCE = 60
RAY_LENGTH = CENTER_RADIUS + RADIUS_DIFFERENCE

# risinājums, kurā zvaigzne tiek zīmēta no leņķiem, kas tiek secīgi grozīti
# 3- un 4-staru gadījumā vai nu paliek nelielas atstarpes starp staru pamatnēm,
# vai arī, ja edge_length aprēķina tikai pēc height, stari turpinās zvaigznes centra iekšienē
# izmanto palīgfunkciju draw_angle

def use_angles(num_points: int=POINTS):
    increment_angle = 360 / num_points
    star_angle = increment_angle/5
    for i in range(num_points):
        draw_angle(increment_angle * i, star_angle, RAY_LENGTH)

def draw_angle(direction: int, star_angle: int, height: int):
# draw_angle zīmē leņķi norādītajā virzienā (virzienu norāda grādos)
# parametri: leņķa bisektrises virziens grādos, leņķa platums grādos, leņķa bisektrises garums

    t = turtle.Turtle()
    # aprēķina stara malas garumu
    edge_length = (height - CENTER_RADIUS)/math.cos(math.radians(star_angle))

    # atrod leņķa virsotnes koordinātes un nopozicionējas tajās
    t.home()    
    t.left(direction)
    t.penup()   
    t.forward(height)
    tmp = t.pos()       # virsotnes koordinātes saglabā

    # zīmē vienu leņķa malu
    t.left(180-star_angle)
    t.pendown()
    t.forward(edge_length)
    
    # atgriežas leņķa virsotnē, zīmē otru malu
    t.setpos(tmp)       
    t.right(-2*star_angle)
    t.forward(edge_length)

    t.hideturtle()      # novāc marķieri
    return

# use_lines izmanto divas riņķa līnijas: iekšējo, uz kuras tiek vienmērīgi izvietoti punkti, 
# kas atbilst uz zvaigznes iekšpusi vērsto leņķu virsotnēm (leņķis starp zvaigznes divām virsotnēm)
# un ārējo, uz kā vienmērīgi tiek izvietoti punkti, kas atbilst zvaigznes virsotnēm 
# Ciklā tiek vilkta lauzta līnija no punkta uz punktu.
def use_lines(num_points: int=POINTS):
    
    turtle.penup()                  
    for i in range(num_points):
        # formulas punktu izvietošanai uz riņķa līnijas aizgūtas no stackoverflow.com
        angle_center = 2 * math.pi * i / num_points
        angle_points = angle_center + math.pi / num_points
        turtle.goto(CENTER_RADIUS * math.sin(angle_center), CENTER_RADIUS * math.cos(angle_center))
        turtle.pendown()
        turtle.goto(RAY_LENGTH * math.sin(angle_points), RAY_LENGTH * math.cos(angle_points))
  
    # savienot pēdējo virsotni ar starta pozīciju  
    turtle.goto(CENTER_RADIUS * math.sin(0), CENTER_RADIUS * math.cos(0))
    
    turtle.hideturtle()
    return

# virsotņu skaita ievads. nodrošina prasību, ka virsotņu skaitam jābūt nepāra.
def num_points_wrapper() -> int:
    # abas zvaigznes zīmēšanas funkcijas (use_angles un use_lines) darbojas neatkarīgi no tā, vai virsotņu skaits ir pāra vai nepāra skaitlis.
    # num_points_wrapper() izmantota tikai, lai nodrošinātu atbilstību uzdevuma prasībām.
    while True:
        n = input("\nIevadiet virsotņu skaitu (nepāra skaitlis >= 1): ")
        try:
            num = int(n)
            num = num // 1  # atmetam decimāldaļas
            if num % 2 == 1 and num > 0:
                return num
        except:
            pass
    return

def main():
    # num_points = POINTS
    num_points = num_points_wrapper()

    use_lines(num_points)
    # use_angles(num_points)
        
    turtle.done()

if __name__ == "__main__":
    main()

