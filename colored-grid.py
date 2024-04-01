from manim import *
import itertools

class ColoredGrid(Scene):
    def construct(self):
        # Define the number of rows and columns in the grid
        rows, cols = 4, 4
        
        # Define a list of colors to use
        colors = [
            BLUE, TEAL, GREEN, YELLOW,
            GOLD, RED, MAROON, PURPLE
        ]
        
        # Create a grid of circles
        grid = VGroup(*[
            Circle(color=color).scale(0.3)
            for color in itertools.islice(itertools.cycle(colors), rows * cols)
        ])
        
        # Arrange the circles in a grid
        grid.arrange_in_grid(rows, cols, buff=0.5)
        
        # Animate the creation of the grid
        self.play(LaggedStartMap(GrowFromCenter, grid, lag_ratio=0.1))
        self.wait()
