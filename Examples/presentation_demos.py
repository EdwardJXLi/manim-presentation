from manimlib.imports import *
import manimlib.presentation

'''
Combination Of Some Default Demos
'''
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)


        self.play(ShowCreation(square))
        self.create_slide()
        self.play(Transform(square, circle))
        self.create_slide()

        c1 = Circle().shift(LEFT)
        s1 = Square().shift(RIGHT)
        g1 = Group(c1, s1)

        c2 = Circle().shift(RIGHT + 2 * DOWN)
        s2 = Square().shift(LEFT + 2 * DOWN)
        r2 = Rectangle(height=4, width=2) \
               .shift(2 * LEFT + 2 * DOWN)
        g2 = Group(r2, s2, c2)
        g2x = Group(r2, s2)

        
        self.play(ReplacementTransform(square, c1))
        self.create_slide()
        self.play(FadeIn(s1))
        self.create_slide()
        self.play(ReplacementTransform(g1, g2))
        self.create_slide()
        self.play(FadeOut(c2))
        self.create_slide()
        self.play(FadeOut(g2x))
        self.create_slide()
        #self.create_slide()

'''
Dragon Fractal Written By Alexander Vázquez
https://github.com/Elteoremadebeethoven/AnimationsWithManim
'''
class Dragon(MovingCameraScene):
    CONFIG = {
        "iterations":1,
        "angle":90*DEGREES,
        "border_proportion":1.25,
        "colors":[RED_A,RED_C,RED_E,BLUE_A,
                  BLUE_C,BLUE_E,YELLOW_A,YELLOW_C,
                  YELLOW_E,PURPLE_A,PURPLE_C,PURPLE_E]
    }
    def construct(self):
        self.color = it.cycle(self.colors)
        path = VGroup()
        first_line = Line(ORIGIN, UP / 5, color = next(self.color))
        path.add(first_line)

        self.camera_frame.set_height(first_line.get_height() * self.border_proportion)
        self.camera_frame.move_to(first_line)
        self.play(ShowCreation(first_line))
        self.add_foreground_mobject(path)
        self.create_slide()
        self.wait(0.5)

        self.target_path = self.get_all_paths(path,self.iterations)
        for i in range(self.iterations):
            self.duplicate_path(path,i)
        self.wait()

    def duplicate_path(self,path,i):
        set_paths = self.target_path[:2**(i + 1)]
        height = set_paths.get_height() * self.border_proportion
        new_path = path.copy()
        new_path.set_color(next(self.color))
        self.add(new_path)
        point = self.get_last_point(path)
        self.play(
            Rotating(
                new_path,
                radians=self.angle,
                about_point=path[-1].points[point],
                rate_func=linear
                ),
            self.camera_frame.move_to,set_paths,
            self.camera_frame.set_height,height,
            run_time=1, rate_func=smooth
            )
        self.add_foreground_mobject(new_path)
        post_path = reversed([*new_path])
        path.add(*post_path)
        self.create_slide()
        self.wait(0.5)

    def get_all_paths(self, path, iterations):
        target_path = path.copy()
        for _ in range(iterations):
            new_path = target_path.copy()
            point = self.get_last_point(new_path)
            new_path.rotate(
                        self.angle, 
                        about_point=target_path[-1].points[point],
                    )
            post_path = reversed([*new_path])
            target_path.add(*post_path)

        return target_path

    def get_last_point(self, path):
        return 0 if len(path) > 1 else -1