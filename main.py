"""
    Two ways of generating Sierpinski Triangle: Recursion and Iteration.
"""

import turtle
from fractions import Fraction

import numpy as np

from functions import draw_triangle, draw_inverted_triangle, set_pos, get_mid_point


def recursive_sierpinski(size, n, draw=None, first_call=True):
    """Function that generates a sierpinski triangle through recursion"""
    
    if first_call:
        draw = turtle.Turtle()
        draw.hideturtle()
        draw.speed(0)
        turtle.Screen().setup(1000, 1000)
        # Set the initial position in order to center the triangle
        total_size = size * 2 ** (n - 1)
        h = np.sqrt(total_size ** 2 - (total_size/2) ** 2)
        set_pos(draw, (-total_size/2, -h/2))
    
    if n == 1:
        draw_triangle(draw, size)
    else:
        recursive_sierpinski(size, n-1, draw, first_call=False)
        draw.rt(120)
        draw.fd(size * 2 ** (n - 2))
        recursive_sierpinski(size, n-1, draw, first_call=False)
        draw.lt(120)
        draw.fd(size * 2 ** (n - 2))
        recursive_sierpinski(size, n-1, draw, first_call=False)
        draw.fd(size * 2 ** (n - 2))


def iterative_sierpinski(n, size_factor=50):
    """Function that generates a sierpinski triangle through iteration"""
    
    draw = turtle.Turtle()
    draw.hideturtle()
    draw.speed(0)
    turtle.Screen().setup(1000, 1000)
    
    # Set the size of the external triangle and calculate its height
    size = size_factor * 2 ** (n - 1)
    h = np.sqrt(size ** 2 - (size/2) ** 2)
    
    # Set the initial position in order to center the triangle
    init_pos = (- size/2, -h/2)
    set_pos(draw, init_pos)
    
    for n in range(n+1):
        # Set the new size of the triangles to draw
        new_size = size * (1 / (2 ** n))
        if n == 0:
            draw_triangle(draw, size)
        elif n == 1:
            pos = {'0': [Fraction(1, 2)]}
            set_pos(draw, (init_pos[0] + Fraction(1, 2) * size, init_pos[1] + 0))
            draw_inverted_triangle(draw, new_size)
        else:
            # Vertical levels of each dimension (n)
            levels = []
            for i in range(2**(n-1)):
                levels.append(Fraction(i, 2**(n-1)))
            pos_aux = {}
            for level in levels:
                if str(level) in pos:
                    den = pos['0'][0].denominator * 2
                    pos_aux[str(level)] = sorted([x - Fraction(1, den) for x in pos[str(level)]] + 
                                                [x + Fraction(1, den) for x in pos[str(level)]])
                else:
                    key = list(pos_aux.keys())[-1]
                    pos_aux[str(level)] = [get_mid_point(pos_aux[key][i], pos_aux[key][i+1]) for i in range(0, len(pos_aux[key]), 2)]
            # Transform the dictionary to a list of points
            points = [(init_pos[0] + size * x, init_pos[1] + h * int(y)) if y == '0' else \
                      (init_pos[0] + size * x, init_pos[1] + h * Fraction(int(y.split('/')[0]), int(y.split('/')[1]))) \
                      for y in pos_aux for x in pos_aux[y]]
            for point in points:
                set_pos(draw, point)
                draw_inverted_triangle(draw, new_size)
            
            pos = pos_aux

recursive_sierpinski(10, 6)