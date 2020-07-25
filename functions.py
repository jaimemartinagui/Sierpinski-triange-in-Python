"""
    Module with auxiliar functions.
"""

class AuxiliarFunctions():
    """Class with auxiliar functions."""
    
    def draw_triangle(self, draw, size):
        draw.setheading(180)
        for _ in range(3):
            draw.rt(120)
            draw.fd(size)
    
    def draw_inverted_triangle(self, draw, size):
        draw.setheading(120)
        for _ in range(3):
            draw.fd(size)
            draw.rt(120)
    
    def set_pos(self, draw, pos):
        draw.pu()
        draw.setpos(pos)
        draw.pd()
    
    def get_mid_point(self, p1, p2):
        return p1 + (p2 - p1) / 2
