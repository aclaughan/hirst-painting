import logging
from random import randint, choice
from turtle import Turtle, Screen, colormode

logging.basicConfig(level = logging.DEBUG)

COLORS = \
    [
        "aliceblue", "antiquewhite", "antiquewhite1", "antiquewhite2",
        "antiquewhite3", "antiquewhite4", "aquamarine", "aquamarine2",
        "aquamarine4", "azure", "azure2", "azure3", "azure4", "beige",
        "bisque", "bisque2", "bisque3", "bisque4", "black", "blanchedalmond",
        "blue", "blue2", "blueviolet", "brown", "brown1", "brown2", "brown3",
        "brown4", "burlywood", "burlywood1", "burlywood2", "burlywood3",
        "burlywood4", "cadetblue", "cadetblue1", "cadetblue2", "cadetblue3",
        "cadetblue4", "chartreuse", "chartreuse2", "chartreuse3",
        "chartreuse4", "chocolate", "chocolate1", "chocolate2", "chocolate3",
        "coral", "coral1", "coral2", "coral3", "coral4", "cornflowerblue",
        "cornsilk", "cornsilk2", "cornsilk3", "cornsilk4", "crimson", "cyan",
        "cyan2", "cyan3", "darkblue", "darkcyan", "darkgoldenrod",
        "darkgoldenrod1", "darkgoldenrod2", "darkgoldenrod3",
        "darkgoldenrod4", "darkgreen", "darkgrey", "darkkhaki", "darkmagenta",
        "darkolivegreen", "darkolivegreen1", "darkolivegreen2",
        "darkolivegreen3", "darkolivegreen4", "darkorange", "darkorange1",
        "darkorange2", "darkorange3", "darkorange4", "darkorchid",
        "darkorchid1", "darkorchid2", "darkorchid3", "darkorchid4", "darkred",
        "darksalmon", "darkseagreen", "darkseagreen1", "darkseagreen2",
        "darkseagreen3", "darkseagreen4", "darkslateblue", "darkslategrey",
        "darkturquoise", "darkviolet", "deeppink", "deeppink2", "deeppink3",
        "deeppink4", "deepskyblue", "deepskyblue2", "deepskyblue3",
        "deepskyblue4", "dimgrey", "dodgerblue", "dodgerblue2", "dodgerblue3",
        "dodgerblue4", "firebrick", "firebrick1", "firebrick2", "firebrick3",
        "firebrick4", "floralwhite", "forestgreen", "gainsboro", "ghostwhite",
        "gold", "gold2", "gold3", "gold4", "goldenrod", "goldenrod1",
        "goldenrod2", "goldenrod3", "goldenrod4", "green", "green2", "green3",
        "green4", "greenyellow", "grey", "grey1", "grey10", "grey11",
        "grey12", "grey13", "grey14", "grey15", "grey16", "grey17", "grey18",
        "grey19", "grey2", "grey20", "grey21", "grey22", "grey23", "grey24",
        "grey25", "grey26", "grey27", "grey28", "grey29", "grey3", "grey30",
        "grey31", "grey32", "grey33", "grey34", "grey35", "grey36", "grey37",
        "grey38", "grey39", "grey4", "grey40", "grey42", "grey43", "grey44",
        "grey45", "grey46", "grey47", "grey48", "grey49", "grey5", "grey50",
        "grey51", "grey52", "grey53", "grey54", "grey55", "grey56", "grey57",
        "grey58", "grey59", "grey6", "grey60", "grey61", "grey62", "grey63",
        "grey64", "grey65", "grey66", "grey67", "grey68", "grey69", "grey7",
        "grey70", "grey71", "grey72", "grey73", "grey74", "grey75", "grey76",
        "grey77", "grey78", "grey79", "grey8", "grey80", "grey81", "grey82",
        "grey83", "grey84", "grey85", "grey86", "grey87", "grey88", "grey89",
        "grey9", "grey90", "grey91", "grey92", "grey93", "grey94", "grey95",
        "grey97", "grey98", "grey99", "honeydew", "honeydew2", "honeydew3",
        "honeydew4", "hotpink", "hotpink1", "hotpink2", "hotpink3",
        "hotpink4", "indianred", "indianred1", "indianred2", "indianred3",
        "indianred4", "indigo", "ivory", "ivory2", "ivory3", "ivory4",
        "khaki", "khaki1", "khaki2", "khaki3", "khaki4", "lavender",
        "lavenderblush", "lavenderblush2", "lavenderblush3", "lavenderblush4",
        "lawngreen", "lemonchiffon", "lemonchiffon2", "lemonchiffon3",
        "lemonchiffon4", "lightblue", "lightblue1", "lightblue2",
        "lightblue3", "lightblue4", "lightcoral", "lightcyan", "lightcyan2",
        "lightcyan3", "lightcyan4", "lightgoldenrod", "lightgoldenrod1",
        "lightgoldenrod2", "lightgoldenrod3", "lightgoldenrod4",
        "lightgoldenrodyellow", "lightgreen", "lightgrey", "lightpink",
        "lightpink1", "lightpink2", "lightpink3", "lightpink4", "lightsalmon",
        "lightsalmon2", "lightsalmon3", "lightsalmon4", "lightseagreen",
        "lightskyblue", "lightskyblue1", "lightskyblue2", "lightskyblue3",
        "lightskyblue4", "lightslateblue", "lightslategrey", "lightsteelblue",
        "lightsteelblue1", "lightsteelblue2", "lightsteelblue3",
        "lightsteelblue4", "lightyellow", "lightyellow2", "lightyellow3",
        "lightyellow4", "lime", "limegreen", "linen", "magenta", "magenta2",
        "magenta3", "maroon", "maroon1", "maroon2", "maroon3", "maroon4",
        "mediumaquamarine", "mediumblue", "mediumorchid", "mediumorchid1",
        "mediumorchid2", "mediumorchid3", "mediumorchid4", "mediumpurple",
        "mediumpurple1", "mediumpurple2", "mediumpurple3", "mediumpurple4",
        "mediumseagreen", "mediumslateblue", "mediumspringgreen",
        "mediumturquoise", "mediumvioletred", "midnightblue", "mintcream",
        "mistyrose", "mistyrose2", "mistyrose3", "mistyrose4", "moccasin",
        "navajowhite", "navajowhite2", "navajowhite3", "navajowhite4",
        "navyblue", "oldlace", "olive", "olivedrab", "olivedrab1",
        "olivedrab2", "olivedrab4", "orange", "orange2", "orange3", "orange4",
        "orangered", "orangered2", "orangered3", "orangered4", "orchid",
        "orchid1", "orchid2", "orchid3", "orchid4", "palegoldenrod",
        "palegreen", "palegreen1", "palegreen3", "palegreen4",
        "paleturquoise", "paleturquoise1", "paleturquoise2", "paleturquoise3",
        "paleturquoise4", "palevioletred", "palevioletred1", "palevioletred2",
        "palevioletred3", "palevioletred4", "papayawhip", "peachpuff",
        "peachpuff2", "peachpuff3", "peachpuff4", "peru", "pink", "pink1",
        "pink2", "pink3", "pink4", "plum", "plum1", "plum2", "plum3", "plum4",
        "powderblue", "purple", "purple1", "purple2", "purple3", "purple4",
        "red", "red2", "red3", "rosybrown", "rosybrown1", "rosybrown2",
        "rosybrown3", "rosybrown4", "royalblue", "royalblue1", "royalblue2",
        "royalblue3", "royalblue4", "saddlebrown", "salmon", "salmon1",
        "salmon2", "salmon3", "salmon4", "sandybrown", "seagreen",
        "seagreen1", "seagreen2", "seagreen3", "seashell", "seashell2",
        "seashell3", "seashell4", "sienna", "sienna1", "sienna2", "sienna3",
        "sienna4", "silver", "skyblue", "skyblue2", "skyblue3", "skyblue4",
        "slateblue", "slateblue1", "slateblue2", "slateblue3", "slateblue4",
        "slategrey", "snow", "snow2", "snow3", "snow4", "springgreen",
        "springgreen2", "springgreen3", "springgreen4", "steelblue",
        "steelblue1", "steelblue2", "steelblue3", "steelblue4", "tan", "tan1",
        "tan2", "tan4", "teal", "thistle", "thistle1", "thistle2", "thistle3",
        "thistle4", "tomato", "tomato2", "tomato3", "tomato4", "turquoise",
        "turquoise1", "turquoise2", "turquoise3", "turquoise4", "violet",
        "violetred", "violetred1", "violetred2", "violetred3", "violetred4",
        "wheat", "wheat1", "wheat2", "wheat3", "wheat4", "white",
        "whitesmoke", "yellow", "yellow2", "yellow3", "yellow4",
        "yellowgreen"
        ]

HIRST_COLORS = \
    [
        (238, 245, 241), (246, 238, 242), (132, 164, 202), (224, 151, 101),
        (29, 42, 62), (204, 135, 147), (162, 60, 48), (236, 213, 87),
        (44, 100, 145), (137, 181, 161), (148, 65, 75), (171, 24, 31),
        (157, 31, 26), (50, 40, 44), (55, 45, 42), (59, 114, 98),
        (233, 162, 168), (237, 165, 156), (215, 81, 68), (31, 59, 53),
        (15, 96, 71), (201, 89, 100), (171, 188, 220), (34, 60, 105)
        ]


def init_turtle( coordinates ):
    t, x_pos, y_pos = coordinates

    t.speed("fastest")

    t.penup()
    t.goto(x_pos, y_pos)

    t.shape('classic')
    t.shapesize(2)
    t.color('green4')
    t.pencolor('lawn green')
    t.pensize(2)
    t.pendown()
    colormode(255)


def draw_shape( info ):
    turtle, size, num_sides, x_pos, y_pos = info

    corner = 360 / num_sides

    init_turtle((turtle, x_pos, y_pos))
    for x in range(num_sides):
        turtle.forward(size)
        turtle.right(corner)
    turtle.penup()


def draw_dashed_line( info ):
    turtle, num_dash, x_pos, y_pos = info

    init_turtle((turtle, x_pos, y_pos))

    for x in range(num_dash):

        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()

    turtle.penup()


def random_walk( info ):
    turtle, pen_size, num_steps, x_pos, y_pos = info

    init_turtle((turtle, x_pos, y_pos))
    turtle.pensize(pen_size)
    for x in range(num_steps):
        pen_color = choice(COLORS)
        turtle.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        direction = choice([90, 180, 270, 360])
        turtle.forward(20)
        turtle.setheading(direction)

    turtle.penup()


def draw_circles( info ):
    turtle, pen_size, diameter, num_steps, x_pos, y_pos = info

    step = 0
    for x in range(num_steps):
        init_turtle((turtle, x_pos, y_pos))
        turtle.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
        turtle.circle(diameter)
        step += 360 / num_steps
        turtle.setheading(step)


def draw_hirst( info ):
    turtle, pen_size, diameter = info

    for y_pos in range(400, -400, -52):
        for x_pos in range(-600, 600, 52):
            init_turtle((turtle, x_pos, y_pos))
            random_color = choice(HIRST_COLORS)
            turtle.pencolor(random_color)
            turtle.fillcolor(random_color)
            turtle.begin_fill()
            turtle.circle(diameter)
            turtle.end_fill()


def main():
    bubbles = Turtle()

    # draw squares
    # for y in range(350, -260, -120):
    #     for x in range(-350, 260, 120):
    #
    # draw shapes
    # for num_sides in range(3,11):
    #     draw_shape((bubbles, 100, num_sides, 0, 0))
    #
    # draw_dashed_line((bubbles, 35, -350, 0))
    #
    # random_walk((bubbles, 15, 500, 0, 0))
    # draw_circles((bubbles, 10, 180, 80, 0, 0))

    draw_hirst((bubbles, 20, 12))
    bubbles.hideturtle()

    screen = Screen()
    screen.setup(width = 900, height = 820, startx = None, starty = None)

    print(f"height: {screen.window_height()}")
    print(f"width: {screen.window_width()}")

    screen.title('Bubbles')
    screen.exitonclick()


if __name__ == '__main__':
    main()

# logging.debug(stuff)
