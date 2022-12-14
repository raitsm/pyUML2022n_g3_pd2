import turtle
import math

POINTS = 8         
FULL_CIRCLE = 360       
# jo lielāka starpība starp RADIUS_DIFFERENCE un CENTER_RADIUS_BASE, jo izteiktāki stari zvaigznei
# ja abi būs vienādi, tad, 3-staru zvaigzne izskatīsies līdzīga vienādmalu trijstūrim
CENTER_RADIUS_BASE = 30     # zvaigznes iekšējais rādiuss
RADIUS_DIFFERENCE = 60      # starpība starp zvaigznes iekšējo un ārējo rādiusu (faktiski stara garums)
RAY_LENGTH_BASE = CENTER_RADIUS_BASE + RADIUS_DIFFERENCE     # garums no stara virsotnes līdz bāzes riņķa līnijas centram
MARGIN = 40

# risinājums, kurā zvaigzne tiek zīmēta no leņķiem, kas tiek secīgi grozīti
# 3- un 4-staru gadījumā vai nu paliek nelielas atstarpes starp staru pamatnēm,
# vai arī, ja edge_length aprēķina tikai pēc height, stari turpinās zvaigznes centra iekšienē
# izmanto palīgfunkciju draw_angle

def use_angles(num_points: int=POINTS):
    increment_angle = 360 / num_points
    star_angle = increment_angle/5
    for i in range(num_points):
        draw_angle(increment_angle * i, star_angle, RAY_LENGTH_BASE)

def draw_angle(direction: int, star_angle: int, height: int):
# draw_angle zīmē leņķi norādītajā virzienā (virzienu norāda grādos)
# parametri: leņķa bisektrises virziens grādos, leņķa platums grādos, leņķa bisektrises garums

    t = turtle.Turtle()
    # aprēķina stara malas garumu
    edge_length = (height - CENTER_RADIUS_BASE)/math.cos(math.radians(star_angle))

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
    
    calculated_radius = CENTER_RADIUS_BASE + num_points/2
    calculated_ray_length = RAY_LENGTH_BASE + num_points
    turtle.penup()
    turtle.speed("fastest")
    turtle.color("red")                  
    for i in range(num_points):
        # formulas punktu izvietošanai uz riņķa līnijas aizgūtas no stackoverflow.com
        angle_center = 2 * math.pi * i / num_points
        angle_points = angle_center + math.pi / num_points
        turtle.goto(calculated_radius * math.sin(angle_center), calculated_radius * math.cos(angle_center))
        turtle.pendown()
        turtle.goto(calculated_ray_length * math.sin(angle_points), calculated_ray_length * math.cos(angle_points))
  
    # savienot pēdējo virsotni ar starta pozīciju  
    turtle.goto(calculated_radius * math.sin(0), calculated_radius * math.cos(0))
    
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

# ekrāna konfigurācija: izmērs un fona krāsa
def setup_screen(size: float,bg_color: str="white"):
    turtle.setup(width=size, height=size, startx=MARGIN, starty=MARGIN)
    turtle.screensize(canvwidth=size*2, canvheight=size*2,bg=bg_color) #  
    return


def main():
    # num_points = POINTS
    num_points = num_points_wrapper()

    setup_screen((RAY_LENGTH_BASE + num_points) + MARGIN*2, bg_color="grey")

    use_lines(num_points)
    # use_angles(num_points)
        
    turtle.done()

if __name__ == "__main__":
    main()

