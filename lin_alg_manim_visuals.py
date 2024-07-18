from manim import *
import numpy as np

class LinearTransformationExample(LinearTransformationScene):
    def __init__(self, **kwargs):
        super().__init__(
            show_coordinates=True,
            leave_ghost_vectors=True,
            include_background_plane=True,
            show_basis_vectors=True,
            **kwargs
        )

    def construct(self):
        # Get user input for the transformation matrix
        a = float(input("Enter the element a11 of the matrix: "))
        b = float(input("Enter the element a12 of the matrix: "))
        c = float(input("Enter the element a21 of the matrix: "))
        d = float(input("Enter the element a22 of the matrix: "))
        matrix = [[a, b], [c, d]]

        # Create the transformation animation
        self.apply_matrix(matrix)
        
        # Add transformation matrix display
        matrix_tex = MathTex(f"\\begin{{pmatrix}} {a} & {b} \\\\ {c} & {d} \\end{{pmatrix}}")
        matrix_tex.to_corner(UL).scale(0.8)
        self.play(Write(matrix_tex))

        # Calculate and display determinant
        det_value = np.linalg.det(matrix)
        det_tex = MathTex(r"\text{Det} = ", str(round(det_value, 2)))
        det_tex.next_to(matrix_tex, DOWN)
        self.play(Write(det_tex))
        
        self.wait()

if __name__ == "__main__":
    config.frame_height = 6
    config.frame_width = 6
    scene = LinearTransformationExample()
    scene.render()
