from manim import *

class demo(Scene): 
    def construct(self):
        # Create three rectangles with specific colors and positions
        rect1 = Rectangle(height=0.5, width=0.5, fill_opacity=1).shift(LEFT*5)
        rect2 = Rectangle(color=GRAY, height=0.5, width=0.5, fill_opacity=1).move_to([5, 0, 0])
        rect3 = Rectangle(color=BLUE, height=0.5, width=0.5, fill_opacity=1).move_to([5, 1, 0])

        # Create a series of rectangles with different colors
        r1 = Rectangle(height=0.5, width=0.5, fill_opacity=1, color=RED)
        r2 = Rectangle(height=0.5, width=0.5, fill_opacity=1, color=ORANGE)
        r3 = Rectangle(height=0.5, width=0.5, fill_opacity=1, color=YELLOW)
        r4 = Rectangle(height=0.5, width=0.5, fill_opacity=1, color=PURE_GREEN)
        r5 = Rectangle(height=0.5, width=0.5, fill_opacity=1, color=BLUE)
        
        # Group the rectangles and arrange them horizontally
        group = VGroup(r1, r2, r3, r4, r5)
        group.arrange()
        # Apply a gradient color effect to the group
        group.set_color_by_gradient(RED, ORANGE, YELLOW, PURE_GREEN, BLUE)

        # Animate the creation of the first three rectangles
        self.play(Write(rect1))
        self.play(Write(rect2))
        self.play(Write(rect3))

        # Group the first three rectangles and transform them into the grouped series of rectangles
        g2 = VGroup(rect1, rect2, rect3)
        self.play(rect2.animate.next_to(rect1, RIGHT))
        self.play(ReplacementTransform(g2, group))

        # Create surrounding rectangles around the group for visual effect
        s1 = SurroundingRectangle(group, color=WHITE)
        s2 = SurroundingRectangle(s1, color=WHITE)
        self.play(Write(s1), Write(s2, run_time=2.0))
        
        # Display numbers above the group of rectangles
        t = Text("1 2 3 4 5").next_to(s2, UP, buff=0.1).scale(1.5)
        self.play(Write(t))

        # Highlight each number and its corresponding rectangle
        self.play(Indicate(t[0], color=RED), Indicate(r1, color=RED), scale_factor=0.2)
        self.play(Indicate(t[1], color=ORANGE), Indicate(r2, color=ORANGE), scale_factor=0.2)
        self.play(Indicate(t[2], color=YELLOW), Indicate(r3, color=YELLOW), scale_factor=0.2)
        self.play(Indicate(t[3], color=PURE_GREEN), Indicate(r4, color=PURE_GREEN), scale_factor=0.2) 
        self.play(Indicate(t[4], color=BLUE), Indicate(r5, color=BLUE), scale_factor=0.2) 

        # Create a dot, then replace the group of rectangles and text with it
        d = Dot(color=GREY)
        g3 = VGroup(group, t, s1, s2)
        self.play(ReplacementTransform(g3, d))

        # Expand the dot dramatically, then fade it out
        self.play(d.animate.scale(150))
        self.play(FadeOut(d))
        
        # Wait at the end of the animation
        self.wait(3)
