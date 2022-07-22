from manim import *
import math

class PlotParametricFunction(Scene):
    def func(self, t):
        return np.array((np.sin(2 * t), np.sin(3 * t), 0))

    def construct(self):
        func = ParametricFunction(self.func, t_range = np.array([0, TAU]), fill_opacity=0).set_color(RED)
        self.add(func.scale(3))
class NumberLineTest(Scene):
    def construct(self):
        # a = Axes(
        #     x_min=-3,
        #     x_max=3,
        #     y_min=-3,
        #     y_max=3,
        #     axis_config={
        #         "include_tip": False,
        #     }
        # )
        a = Axes().add_coordinates()
        # f = ParametricFunction(self.func,t_range = np.array([-1, 1]),
        #                        color=BLUE)
        f = ParametricFunction(self.func,t_range = np.array([-math.sqrt(3), math.sqrt(3)]),
                             color=BLUE)
        self.add(a, f)

    def func(self, t):
        return [math.sin(t), math.cos(t), 0]