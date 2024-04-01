from manim import *
import itertools

class ColoredGrid(Scene):
    def construct(self):
        # Define the number of rows and columns in the initial grid
        rows, cols = 4, 4
        
        # Define a list of colors to use
        colors = [
            BLUE, TEAL, GREEN, YELLOW,
            GOLD, RED, MAROON, PURPLE
        ]
        
        # Create the initial grid of circles
        grid = VGroup(*[
            Circle(color=color).scale(0.3)
            for color in itertools.islice(itertools.cycle(colors), rows * cols)
        ])
        
        # Arrange the circles in the initial grid
        grid.arrange_in_grid(rows, cols, buff=0.5)
        
        # Animate the creation of the initial grid
        self.play(LaggedStartMap(GrowFromCenter, grid, lag_ratio=0.1), run_time=1.5)
        self.play(FadeOut(grid), run_time=1)
        
        # Transition to the number plane
        self.grid()
        
        # Create and display the 6x6 colored grid
        self.coloredSixGrid()
        
        # Add this line to call coloredThreeGrid
        self.coloredThreeGrid()
        
        # Ensure there's a wait time to view the last animation
        self.wait()  
    
    def grid(self):
        # Create the number plane
        numberplane = NumberPlane()
        
        # Fade in the number plane
        self.play(FadeIn(numberplane), run_time=1.5)

    def coloredSixGrid(self):
        # Define the number of rows and columns for the 6x6 grid
        rows, cols = 6, 6
        
        # Define a list of colors to use for the 6x6 grid
        colors = [
            BLUE, TEAL, GREEN, YELLOW,
            GOLD, RED, MAROON, PURPLE
        ]
        
        # Create the 6x6 grid of circles
        grid = VGroup(*[
            Circle(color=color).scale(0.3)
            for color in itertools.islice(itertools.cycle(colors), rows * cols)
        ])
        
        # Arrange the circles in the 6x6 grid
        grid.arrange_in_grid(rows, cols, buff=0.5)
        
        # Animate the creation of the 6x6 grid
        self.play(LaggedStartMap(GrowFromCenter, grid, lag_ratio=0.1), run_time=1.5)

    def coloredThreeGrid(self):
        # Define the number of rows and columns for the 3x3 grid
        rows, cols = 3, 3
        
        # Define a list of colors to use for the 3x3 grid
        colors = [
            BLUE, TEAL, GREEN, YELLOW,
            GOLD, RED, MAROON, PURPLE
        ]
        
        # Create the 3x3 grid of circles
        grid = VGroup(*[
            Circle(color=color).scale(0.3)
            for color in itertools.islice(itertools.cycle(colors), rows * cols)
        ])
        
        # Arrange the circles in the 3x3 grid
        grid.arrange_in_grid(rows, cols, buff=0.5)
        
        # Animate the creation of the 3x3 grid
        self.play(LaggedStartMap(GrowFromCenter, grid, lag_ratio=0.1), run_time=1.5)
