from manim import *

class NeuralNetwork(Scene):
    def construct(self):
        # Define neural network sizes
        input_size = 8
        hidden_size = 14
        output_size = 4

        # Create neural network layers
        input_layer = VGroup(*[Circle(radius=0.15, color=BLUE) for _ in range(input_size)])
        input_layer.arrange(DOWN, buff=0.5)
        
        hidden_layer = VGroup(*[Circle(radius=0.15, color=GREEN) for _ in range(hidden_size)])
        hidden_layer.arrange(DOWN, buff=0.3)

        output_layer = VGroup(*[Circle(radius=0.15, color=RED) for _ in range(output_size)])
        output_layer.arrange(DOWN, buff=0.7)

        # Position layers
        input_layer.to_edge(LEFT, buff=1.5)
        hidden_layer.to_edge(LEFT, buff=3.0)
        output_layer.to_edge(RIGHT, buff=1.5)

        # Create neural network connections
        connections = VGroup()
        for input_node in input_layer:
            for hidden_node in hidden_layer:
                connections.add(Line(input_node.get_center(), hidden_node.get_center(), stroke_width=0.5, color=WHITE))
        
        for hidden_node in hidden_layer:
            for output_node in output_layer:
                connections.add(Line(hidden_node.get_center(), output_node.get_center(), stroke_width=0.5, color=WHITE))

        # Add everything to the scene
        self.play(ShowCreation(connections), run_time=3)
        self.play(LaggedStartMap(GrowFromCenter, input_layer),
                  LaggedStartMap(GrowFromCenter, hidden_layer),
                  LaggedStartMap(GrowFromCenter, output_layer),
                  run_time=2)

        self.wait(1)
