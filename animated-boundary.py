from manim import * 
import numpy as np

class AllAnimations(Scene):
    def construct(self):
        text = Text("Animations").shift(UP*2.5)
        self.play(Write(text))
        self.wait(1)

        self.play(Transform(text,Text("Create a circle, shift up, run for 2.5 seconds").shift(UP*2.5)), run_time=0.5)
        start = Circle()
        self.play(Create(start))
        
        self.play(Transform(text,Text("Uncreate").shift(UP*2.5)), run_time=1.5)
        self.play(Uncreate(start))
        
        self.play(Transform(text,Text("AnimatedBoundary").shift(UP*2.5)), run_time=1.5)
        circle = Circle()
        animated_boundary = AnimatedBoundary(circle, cycle_rate=3, colors=[RED, GREEN, BLUE])
        self.add(circle, animated_boundary)
        self.wait(2)
        self.remove(circle, animated_boundary)