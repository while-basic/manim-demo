from manim import *

class DotGridTransformation(Scene):
    def construct(self):
        # Create a sequence of dot grids increasing in size
        dot_grids = VGroup(
            *[
                VGroup(
                    *[
                        Dot(point=np.array([x, y, 0]), color=WHITE)
                        for x in np.linspace(-0.5, 0.5, width)
                        for y in np.linspace(-0.5, 0.5, height)
                    ]
                ).move_to(np.array([index - 2, 0, 0]))
                for index, (width, height) in enumerate(
                    [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)]
                )
            ]
        )

        # Position the dot grids to match the image layout
        dot_grids.arrange_submobjects(RIGHT, buff=1)

        # Animate the dot grids sequentially appearing
        for grid in dot_grids:
            self.play(FadeIn(grid, shift=0.5 * UP, scale=0.5), run_time=0.5)
            self.wait(0.1)

        # Hold the final image
        self.wait(2)
