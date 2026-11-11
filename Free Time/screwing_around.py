import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")

t.speed(0)
t.width(50)

distance = 0

while True:
    for c in ('maroon', 'darkred', 'brown', 'firebrick', 'rosybrown', 'indianred', 'lightcoral', 'red', 'mistyrose', 'salmon', 'tomato', 'darksalmon', 'coral', 'orangered', 'lightsalmon', 'sienna', 'seashell', 'saddlebrown', 'chocolate', 'sandybrown', 'peachpuff', 'peru', 'linen', 'bisque', 'darkorange', 'burlywood', 'antiquewhite', 'tan', 'navajowhite', 'blanchedalmond', 'papayawhip', 'moccasin', 'orange', 'wheat', 'oldlace', 'floralwhite', 'darkgoldenrod', 'goldenrod', 'cornsilk', 'gold', 'lemonchiffon', 'khaki', 'palegoldenrod', 'darkkhaki', 'olive', 'beige', 'lightgoldenrodyellow', 'ivory', 'lightyellow', 'yellow', 'olivedrab', 'yellowgreen', 'darkolivegreen', 'greenyellow', 'chartreuse', 'lawngreen', 'darkgreen', 'green', 'forestgreen', 'darkseagreen', 'limegreen', 'lightgreen', 'palegreen', 'honeydew', 'lime', 'seagreen', 'mediumseagreen', 'springgreen', 'mediumspringgreen', 'mediumaquamarine', 'aquamarine', 'turquoise', 'lightseagreen', 'mediumturquoise', 'darkslategray', 'darkslategrey', 'teal', 'darkcyan', 'paleturquoise', 'azure', 'lightcyan', 'aqua', 'cyan', 'darkturquoise', 'cadetblue', 'powderblue', 'lightblue', 'deepskyblue', 'skyblue', 'lightskyblue', 'steelblue', 'aliceblue', 'dodgerblue', 'slategray', 'slategrey', 'lightslategray', 'lightslategrey', 'lightsteelblue', 'cornflowerblue', 'royalblue', 'midnightblue', 'navy', 'darkblue', 'mediumblue', 'lavender', 'blue', 'slateblue', 'darkslateblue', 'mediumslateblue', 'mediumpurple', 'blueviolet', 'indigo', 'darkorchid', 'darkviolet', 'mediumorchid', 'purple', 'darkmagenta', 'thistle', 'plum', 'violet', 'fuchsia', 'magenta', 'orchid', 'mediumvioletred', 'deeppink', 'hotpink', 'lavenderblush', 'palevioletred', 'crimson', 'pink', 'lightpink',):
        t.color(c)
        t.fd(distance)
        t.left(2.43243243243)
    distance += 0.1