from manim import *

class ImpressiveAnimation(Scene):
    def construct(self):
        # Create a square and circle
        square = Square(color=BLUE, fill_opacity=1)
        circle = Circle(color=YELLOW, fill_opacity=1)
        
        # Create a text label
        text = Text("C-Cel Tech", font_size=36, color=WHITE).move_to(UP*2)
        
        # Animation 1: Show the square
        self.play(Create(square))
        self.wait(1)
        
        # Animation 2: Transform the square into a circle
        self.play(Transform(square, circle))
        self.wait(1)
        
        # Animation 3: Move the circle upwards while fading in the text
        self.play(
            FadeIn(text)
        )
        self.wait(1)
        
        # Animation 4: Rotate and then fade out
        self.play(Rotate(square, angle=PI/4))
        self.wait(1)
        self.play(FadeOut(square), FadeOut(text))

# To run this, use the command line:
# manim -pql your_script_name.py ImpressiveAnimation
