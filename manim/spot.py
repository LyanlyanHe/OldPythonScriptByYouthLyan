from manimlib import *
import numpy as np

def f(x):
    return np.exp(2 * x) - 3 * np.exp(x) + 2 * x

def f_prime(x):
    return 2 * np.exp(2 * x) - 3 * np.exp(x) + 2


class A_Quadratic(Scene):
    def construct(self):
        t2c = { 
            "x": BLUE_C,
        }
        kw = {
            "t2c": t2c,
            "font_size": 36
        }
        
        quadratic = VGroup(
            Tex("f(x)=e^{2x}-3e^x+2x+c", **kw),
            Tex("f'(x)=2e^{2x}-3e^x+2", **kw),
            VGroup(Text("Setting ", **kw), Tex("f'(x)=0", **kw)),
            Tex("2e^{2x}-3e^x+2=0", **kw),
            Tex("2(e^x)^2-3e^x+2=0", **kw),
            VGroup(Tex(r"e^x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}", **kw),
            Tex(r"e^x=\frac{-(-3)\pm\sqrt{(-3)^2-4\cdot2\cdot2}}{2\cdot2}", **kw)),
            Tex(r"e^x=\frac{3\pm\sqrt{9-16}}{4}", **kw),
            Tex(r"e^x=\frac{3\pm\sqrt{-7}}{4}", **kw)
        )
        quadratic[2].arrange(RIGHT, buff=MED_SMALL_BUFF)
        quadratic.arrange(DOWN, buff=MED_SMALL_BUFF)
        
        self.add(quadratic[0])
        self.play(TransformMatchingTex(quadratic[0].copy(), quadratic[1], path_arc=15 * DEGREES))
        self.wait()
        self.play(Write(quadratic[2][0]), TransformMatchingTex(quadratic[1].copy(), quadratic[2][1], key_map={r"2e^{2x}-3e^x+2": "f'(x)"}, path_arc=15 * DEGREES))
        self.wait()
        self.play(TransformMatchingTex(quadratic[2][1].copy(), quadratic[3], key_map={"f'(x)": "2e^{2x}-3e^x+2"}, path_arc=15 * DEGREES))
        self.wait()
        self.play(TransformMatchingTex(quadratic[3].copy(), quadratic[4]))
        self.wait()
        self.play(TransformMatchingTex(quadratic[4].copy(), quadratic[5][0], matched_keys=["e^x"], path_arc=15 * DEGREES)),
        self.wait()
        self.play(TransformMatchingTex(quadratic[5][0], quadratic[5][1], key_map={"b": "-3", "a": "2", "c": 2}, path_arc=15 * DEGREES))
        self.wait()
        self.play(TransformMatchingTex(quadratic[5][1].copy(), quadratic[6], key_map={"(-3)^2": "9", r"4\cdot2\cdot2": "16", r"2\cdot2": "4"}, path_arc=15 * DEGREES))
        self.wait()
        self.play(TransformMatchingTex(quadratic[6].copy(), quadratic[7], key_map={"9-16": "-7"}, path_arc=15 * DEGREES))
        
class A_Discriment(Scene):
    def construct(self):
        discriment = VGroup(
            Tex("b^2-4ac>0", t2c={"b^2-4ac>0": BLUE_D}),
            Tex("b^2-4ac=0",),
            Tex("b^2-4ac<0", t2c={"b^2-4ac<0": RED_D}),
        )
        
        self.play(Write(discriment[0]))
        self.wait()
        self.play(TransformMatchingTex(discriment[0], discriment[1], key_map={">": "="}))
        self.wait()
        self.play(TransformMatchingTex(discriment[1], discriment[2], key_map={"=": "<"}))
        self.wait()
        self.play(FadeOut(discriment[2]))
        
        d_work = VGroup(
            Tex("f'(x)=2 e^{2x}-3e^x+2", t2c={"2 ": BLUE_C, "-3": TEAL_C, "+2": YELLOW}),
            Tex(r"a=2,b=-3,c=2", t2c={"a=2": BLUE_C, "b=-3": TEAL_C, "c=2": YELLOW}),
            Tex("b^2-4ac"),
            Tex("(-3)^2-4\cdot2\cdot2"),
            Tex("=9-16"),
            Tex("=-7"),
        )
        d_work.arrange(DOWN)
        self.play(Write(d_work[0]))
        self.wait()
        self.play(TransformMatchingTex(d_work[0].copy(), d_work[1], path_arc=90 * DEGREES))
        self.wait()
        self.play(Write(d_work[2]))
        self.wait()
        self.play(TransformMatchingTex(d_work[2], d_work[3], key_map={"b": "-3", "a": "2", "c": "2"}, path_arc=15 * DEGREES))
        self.wait()
        self.play(TransformMatchingTex(d_work[3].copy(), d_work[4], key_map={"(-3)^2": "9", "4\cdot2\cdot2": "16"}, path_arc=15 * DEGREES))
        self.wait()
        self.play(TransformMatchingTex(d_work[4].copy(), d_work[5], key_map={"9-16": "-7"}, path_arc=15 * DEGREES))
        self.wait()
        self.play(d_work[5]["-7"].animate.set_color(RED_D))


class B_Table(Scene):
    def construct(self):
        font_size = 22
        
        # Why didn't anyone tell me there is such thing call TexText
        sign_tpl = VGroup(Text("Sign of ", font_size=font_size), Tex("f'(x)=2e^{2x}-3e^x+2", font_size=font_size))
        sign_tpl.arrange(RIGHT, buff=MED_SMALL_BUFF)
        
        values_tpl = VGroup(VGroup(Text("Values of ", font_size=font_size), Tex("f(x)", font_size=font_size)), Text("increasing or decreasing", font_size=font_size))
        values_tpl[0].arrange(RIGHT, buff=SMALL_BUFF)
        values_tpl.arrange(DOWN, buff=SMALL_BUFF)
        # I am such an idiot D:
        
        table = Group(
            Text("Value of x", font_size=font_size), Tex("x<0", font_size=font_size), Tex("x=0", font_size=font_size), Tex("x>0", font_size=font_size),
            sign_tpl, *[Tex("f'(x)>0", t2c={"f'(x)>0": BLUE_D}, font_size=font_size) for _ in range(3)],
            Text("Slope of tangents", font_size=font_size), *[Text("Positive", t2c={"Positive": BLUE_D}, font_size=font_size) for _ in range(3)],
            values_tpl, *[Text("Increasing", t2c={"Increasing": BLUE_D}, font_size=font_size) for _ in range(3)]
        )
        table.arrange_in_grid(4, 4, buff=SMALL_BUFF)
        
        self.play(
            *[Write(line) for line in table[0: 5]],
            Write(table[8]),
            Write(table[12]),
            run_time=3
        )
        self.wait()
        
        for x in range(3):
            self.play(
                *[Write(line) for line in table[5 + x::4]],
                run_time=1
            )
            self.wait()

class B_Graph(Scene):
    def construct(self):
        axes = Axes(
            x_range=(-9, 9),
            y_range=(-6, 7),
            height=8,
            width=16 / 9 * 8,
        )
        
        axes.add_coordinate_labels(
            font_size=16,
            num_decimal_places=1
        )
        
        graph = axes.get_graph(f, color=BLUE_E)
        graph.set_stroke(width=6)
        self.add(axes)
        self.play(ShowCreation(graph), run_time=3)
        self.wait()
        
        
        dot = Dot(point=axes.i2gp(0, graph))
        x_tracker = ValueTracker(0)
        line = always_redraw(lambda: axes.get_tangent_line(x=x_tracker.get_value(), length=2.5 ,graph=graph))
        
        gradient = DecimalNumber(0.00)
        # gradient.set_color(BLUE_E)
        crocodile = Tex(">0", t2c={">0": BLUE_E})
        label = VGroup(Text("Gradient=", font_size=36), gradient)
        # label[0].set_color(BLUE_E)
        label.arrange(RIGHT, buff=SMALL_BUFF)

        f_always(dot.move_to, lambda: axes.i2gp(x_tracker.get_value(), graph))
        v_line = always_redraw(lambda: axes.get_v_line(dot.get_bottom()))
        always(label.next_to, dot, UP)
        f_always(gradient.set_value, lambda: f_prime(x_tracker.get_value()))
        
        
        
        self.play(FadeIn(dot), ShowCreation(v_line), Write(label), ShowCreation(line))
        for i in [-1.5, 0, 1]:
            self.play(x_tracker.animate.set_value(i), run_time=3)
            self.wait()
            crocodile.next_to(label, RIGHT)
            self.play(FadeIn(crocodile))
            self.wait()
            self.play(FadeOut(crocodile))
            
class B_SolutionInterval(Scene):
    def construct(self):
        axes = Axes(x_range=(-15, 15), y_range=(0, 0.1))
        negative = Line(axes.c2p(-15,0), axes.c2p(0, 0))
        negative.set_color(BLUE)
        positive = Line(axes.c2p(0,0), axes.c2p(15, 0))
        positive.set_color(BLUE)
        
        dot = Dot(axes.c2p(0,0))
        dot.set_color(BLUE)
        
        # nvm TexText is not working D:
        interval = VGroup(Text("Increasing interval ="), Tex("[-\\infty, +\\infty]"))
        interval.arrange(RIGHT, buff=SMALL_BUFF)
        interval.move_to(axes.c2p(0, -2.6))
        negative_label = VGroup(Text("(+)", t2c={"(+)": BLUE}), Tex("x<0"))
        zero_label = VGroup(Text("(+)", t2c={"(+)": BLUE}), Tex("x=0"))
        positive_label = VGroup(Text("(+)", t2c={"(+)": BLUE}), Tex("x>0"))
        negative_label.arrange(DOWN, buff=LARGE_BUFF)
        negative_label.move_to(axes.c2p(-4, 0))
        positive_label.arrange(DOWN, buff=LARGE_BUFF)
        positive_label.move_to(axes.c2p(4, 0))
        zero_label.arrange(DOWN, buff=LARGE_BUFF)
        zero_label.move_to(axes.c2p(0, 0))
        
     
        self.add(axes)
        self.play(ShowCreation(negative))
        self.wait()
        self.play(Write(negative_label))
        self.wait()
        self.play(FadeIn(dot))
        self.wait()
        self.play(Write(zero_label))
        self.wait()
        self.play(ShowCreation(positive))
        self.wait()
        self.play(Write(positive_label))
        self.wait()
        self.play(Write(interval))
     
class C_Derivatives(Scene):
    def construct(self):
        t2c = { 
            "x": BLUE_C,
            "c": YELLOW,
        }
        
        kw = {
            "t2c": t2c,
            "font_size": 36
        }
        
        derivatives = VGroup(
            Tex("f(x)=e^{2x}-3e^x+2x+c", **kw),
            Tex("f'(x)=2e^{2x}-3e^x+2", **kw),
            Tex(r'f^{\prime\prime} (x)=4e^{2x}-3e^x', **kw)
        )
        derivatives.arrange(DOWN, buff=LARGE_BUFF)
        
        self.add(derivatives[0])
        self.wait()
        self.play(TransformMatchingTex(derivatives[0].copy(), derivatives[1], matched_keys=["2x"], key_map={"2x": "2"}, path_arc=90*DEGREES))
        self.wait()
        self.play(TransformMatchingTex(derivatives[1].copy(), derivatives[2], key_map={"2": "4", r"'": r"\prime \prime"}, path_arc=90*DEGREES))

class C_Graph(Scene):
    def construct(self):
        axes = Axes(x_range=(-5, 5),
                    y_range=(-2, 3),
        )
        labels = VGroup(
            VGroup(Tex(r"f^{\prime\prime}(x)>0"), Text(" Local Minimum")),
            VGroup(Tex(r"f^{\prime\prime}(x)<0"), Text(" Local Maximum")),
            VGroup(Tex(r"f^{\prime\prime}(x)=0"), Text(" others method is required")),
        )
        labels[0][0].set_color(RED)
        labels[1][0].set_color(BLUE)
        for x in labels:
            x.arrange(RIGHT, buff=MED_LARGE_BUFF)
        
        whole = VGroup(labels, axes)
        whole.arrange(DOWN, buff=MED_LARGE_BUFF)
        
        minimum = axes.get_graph(lambda x: x ** 2 * .75 - 1, color=RED, x_range=(-2, 2))
        maximum = axes.get_graph(lambda x: -x ** 2 * .75 + 1.5,color=BLUE, x_range=(-2, 2))

        self.play(Write(labels[0]), ShowCreation(minimum))
        self.wait()
        self.play(TransformMatchingTex(labels[0][0], labels[1][0], key_map={">": "<"}),
                  ReplacementTransform(labels[0][1], labels[1][1]),
                  ReplacementTransform(minimum, maximum))
        self.wait()
        self.play(TransformMatchingTex(labels[1][0], labels[2][0], key_map={">": "<"}),
                  ReplacementTransform(labels[1][1], labels[2][1]),
                  FadeOut(maximum))

class D_Algebra1(Scene):
    def construct(self):
        t2c = { 
            "x": BLUE_C,
        }
        kw = {
            "t2c": t2c,
            "font_size": 36
        }
        
        algebra = VGroup(
            Tex(r"f^{\prime\prime(x)}=0", **kw),
            Tex("4e^{2x}-3e^x=0", **kw),
            Tex("e^x(4e^x-3)=0", **kw),
            Tex(r"x\in \mathds{R},e^x>0", **kw),
            Tex("4e^x-3=0", **kw),
            Tex("4e^x=3", **kw),
            Tex(r"e^x=\frac{3}{4}", **kw),
            VGroup(Tex(r"\ln{e^x}=\ln{\frac{3}{4}}", **kw), Tex(r"x=\ln{\frac{3}{4}}", **kw)),
        )
        algebra.arrange(DOWN, buff=MED_SMALL_BUFF)
        
        self.add(algebra[0])
        self.wait()
        self.play(TransformMatchingTex(algebra[0].copy(), algebra[1], key_map={"f\"(x)": "4e^{2x}-3e^x"}))
        self.wait()
        self.play(TransformMatchingTex(algebra[1].copy(), algebra[2], matched_keys=["e^x", "4e^x", "-3"]))
        self.wait()
        self.play(Write(algebra[3]))
        self.wait()
        self.play(TransformMatchingTex(algebra[2].copy(), algebra[4], matched_keys=["4e^x-3"]))
        self.wait()
        self.play(TransformMatchingTex(algebra[4].copy(), algebra[5], key_map={"-3": "3"}))
        self.wait()
        self.play(TransformMatchingTex(algebra[5].copy(), algebra[6], matched_keys=["4"])),
        self.wait()
        self.play(TransformMatchingTex(algebra[6].copy(), algebra[7][0])),
        self.wait() 
        self.play(TransformMatchingTex(algebra[7][0], algebra[7][1], key_map={"\ln{e^x}": "x"}))

class D_Algebra2(Scene):
    def construct(self):
        t2c = { 
            "x": BLUE_C,
        }
        kw = {
            "t2c": t2c,
            "font_size": 36
        }
        
        ughh = VGroup(
            Tex("f(x)=e^{2x}-3e^x+2x+c", **kw),
            VGroup(Text("Setting c = 0, ", **kw), Tex("f(x)=e^{2x}-3e^x+2x", **kw)),
            Tex(r"f(\ln{\frac{3}{4}})=e^{2(\ln{\frac{3}{4}})}-3e^{\ln{\frac{3}{4}}}+2\cdot\ln{\frac{3}{4}}", **kw),
            Tex(r"\approx -2.2629 (4d.p.)", **kw),
            Text("The inflection point of the function is ", **kw),
            Tex(r"(\ln{\frac{3}{4}}, -2.2629) \approx       (-0.2877, -2.2629)", **kw)
        )
        ughh[1].arrange(RIGHT, buff=MED_SMALL_BUFF)
        ughh.arrange(DOWN, buff=MED_SMALL_BUFF)
        
        self.play(Write(ughh[0]))
        self.wait()
        self.play(Write(ughh[1][0]))
        self.wait()
        self.play(TransformMatchingTex(ughh[0].copy(), ughh[1][1], path_arc=45 * DEGREES))
        self.wait()
        self.play(TransformMatchingTex(ughh[1][1].copy(), ughh[2], key_map={"x": r"\ln{\frac{3}{4}}"}))
        self.wait()
        self.play(TransformMatchingTex(ughh[2].copy(), ughh[3], key_map={r"e^{2(\ln{\frac{3}{4}})}-3e^{\ln{\frac{3}{4}}}+2\cdot\ln{\frac{3}{4}}": "-2.2629 (4d.p.)",
                                                                         "=": r"\approx"}))
        self.wait()
        self.play(Write(ughh[4]), Write(ughh[5]))
        
class D_Table(Scene):
    def construct(self):
        t2c = { 
            "x": BLUE_C,
            "Concave Down": BLUE,
            "Point of Inflection": TEAL,
            "Concave Up": RED
        }
         
        kw = {
            "t2c": t2c,
            "font_size": 18
        }
        
        sign_tpl = VGroup(Text("Sign of ", **kw), Tex("f^{\prime\prime}(x)=4e^{2x}-3e^x", **kw))
        sign_tpl.arrange(DOWN, buff=SMALL_BUFF)
        graph_tpl = VGroup(Text("Graph of ", **kw), Tex("f(x)", **kw))
        graph_tpl.arrange(DOWN, buff=SMALL_BUFF)
        sketch_tpl = VGroup(Text("Sketch of ", **kw), Tex("f(x)", **kw))
        sketch_tpl.arrange(DOWN, buff=SMALL_BUFF)
        
        axes_n = Axes(width=2.5, height=1.5)
        axes_saddle = Axes(width=2.5, height=1.5)
        axes_U = Axes(width=2.5, height=1.5)
        
        table = VGroup(
            Text("Interval", **kw), Tex(r"x<\ln{\frac{3}{4}}", **kw), Tex(r"x=\ln{\frac{3}{4}}", **kw), Tex(r"x>\ln{\frac{3}{4}}", **kw),
            sign_tpl, Tex(r"f^{\prime\prime}(x)<0", **kw), Tex(r"f^{\prime\prime}(x)=0", **kw), Tex(r"f^{\prime\prime}(x)>0", **kw),
            graph_tpl, Text("Concave Down", **kw), Text("Point of Inflection", **kw), Text("Concave Up", **kw),
            sketch_tpl, axes_n, axes_saddle, axes_U
        )
        table.arrange_in_grid(4 , 4)
        graph_n = axes_n.get_graph(lambda x: -x ** 2 * .2 + 1.5, x_range=(-4.5, 4.5),color=BLUE)
        graph_saddle = axes_saddle.get_graph(lambda x: x ** 3 * .2, x_range=(-2.5, 2.5),color=TEAL)
        graph_U = axes_U.get_graph(lambda x: x ** 2 * .2 - 1.5, x_range=(-4.5, 4.5),color=RED)
        
        graphs = [graph_n, graph_saddle, graph_U]
        self.play(
            *[Write(x) for x in table[:5]],
            Write(table[8]),
            Write(table[12])
        )
        self.wait()
        for x in range(5, 8):
            self.play(
                *[Write(table[x: x + (4 + 1): 4])],
            )
            self.play(ShowCreation(graphs[x - 5]))
            self.wait()

class E(Scene):
    def construct(self):
        t2c = { 
            "x": BLUE_C,
            "Concave Down": BLUE,
            "Point of Inflection": TEAL,
            "Concave Up": RED
        }
         
        kw = {
            "t2c": t2c,
            "font_size": 12
        }
        
        sign_tpl = VGroup(Text("Sign of ", **kw), Tex("f^{\prime\prime}(x)=4e^{2x}-3e^x", **kw))
        sign_tpl.arrange(DOWN, buff=SMALL_BUFF)
        graph_tpl = VGroup(Text("Graph of ", **kw), Tex("f(x)", **kw))
        graph_tpl.arrange(DOWN, buff=SMALL_BUFF)
        sketch_tpl = VGroup(Text("Sketch of ", **kw), Tex("f(x)", **kw))
        sketch_tpl.arrange(DOWN, buff=SMALL_BUFF)
        
        axes_n = Axes(width=1, height=1.25)
        axes_saddle = Axes(width=1, height=1.25)
        axes_U = Axes(width=1, height=1.25)
        
        table = VGroup(
            Text("Interval", **kw), Tex(r"x<\ln{\frac{3}{4}}", **kw), Tex(r"x=\ln{\frac{3}{4}}", **kw), Tex(r"x>\ln{\frac{3}{4}}", **kw),
            sign_tpl, Tex(r"f^{\prime\prime}(x)<0", **kw), Tex(r"f^{\prime\prime}(x)=0", **kw), Tex(r"f^{\prime\prime}(x)>0", **kw),
            graph_tpl, Text("Concave Down", **kw), Text("Point of Inflection", **kw), Text("Concave Up", **kw),
            sketch_tpl, axes_n, axes_saddle, axes_U
        )
        table.arrange_in_grid(4 , 4)
        graph_n = axes_n.get_graph(lambda x: -x ** 2 * .2 + 1.5 + 4, x_range=(-4.5, 4.5),color=BLUE)
        graph_saddle = axes_saddle.get_graph(lambda x: x ** 3 * .2 + 4, x_range=(-2.5, 2.5),color=TEAL)
        graph_U = axes_U.get_graph(lambda x: x ** 2 * .2 - 1.5 + 4, x_range=(-4.5, 4.5),color=RED)
        
        # I totally didn't recopy this whole thing from D Table :D
        conclution = VGroup(
            table, 
            VGroup(Text("Interval of upward concavity (concave up) = ", font_size=18), Tex(r"(\ln{\frac{3}{4}}, \infty)", font_size=18)),
            VGroup(Text("Interval of downward concavity (concave down) = ", font_size=18), Tex(r"(-\infty, \ln{\frac{3}{4}})", font_size=18))
        )
        [x.arrange(RIGHT, buff=MED_SMALL_BUFF) for x in conclution[1:3]]
        conclution.arrange(DOWN, SMALL_BUFF)
        
        self.add(table[:13])
        self.add(graph_n, graph_saddle, graph_U)
        self.play(*[Write(conclution[1:3])], run_time=4)
        
        


    
class F_Algebra(Scene):
    def construct(self):
        t2c = { 
            "x": BLUE_C,
            r"+\infty": BLUE_D,
            r"\infty": BLUE_D,
            r"-\infty": RED_D,
            # "c": YELLOW
        }
        kw = {
            "t2c": t2c,
            "font_size": 36
        }
        
        more_algebra = VGroup(
            VGroup(Tex("f(x)=e^{2x}-3e^x+2x+c", **kw),
                   Tex("f(x)=e^{2x}-3e^x+2x", **kw))
            ,
            VGroup(
                VGroup(
                    Tex(r"1.\lim_{x\rightarrow+\infty}{f(x)}", **kw),
                    Tex(r"=\lim_{x\rightarrow+\infty}{(e^{2x}-3e^x+2x)}", **kw),
                    Tex(r"=e^{2\infty}-3e^\infty+2\cdot\infty", **kw),
                    Tex(r"=\infty-\infty+\infty", **kw),
                    Tex(r"=+\infty", **kw)
                ),
                VGroup(
                    Tex(r"2.\lim_{x\rightarrow-\infty}{f(x)}", **kw),
                    Tex(r"=\lim_{x\rightarrow-\infty}{(e^{2x}-3e^x+2x)}", **kw),
                    Tex(r"=e^{2 \cdot -\infty}-3e^-\infty+2 \cdot -\infty", **kw),
                    Tex(r"=0-0-\infty", **kw),
                    Tex(r"=-\infty", **kw)
                )
            ),
            Tex(r"\lim_{x\rightarrow+\infty}{f(x)} \neq \lim_{x\rightarrow-\infty}{f(x)}", **kw)
        )
    
        for x in more_algebra[1]:
            x.arrange(DOWN, buff=MED_LARGE_BUFF, center=False, aligned_edge=LEFT)
        more_algebra[1].arrange(RIGHT, buff=LARGE_BUFF)
        more_algebra.arrange(DOWN, buff=MED_SMALL_BUFF)
        
        
        self.add(more_algebra[0][0])
        self.wait()
        self.play(TransformMatchingTex(more_algebra[0][0], more_algebra[0][1]))
        self.wait()
        
        # Positive infinity
        self.play(Write(more_algebra[1][0][0]))
        self.wait()
        self.play(TransformMatchingTex(more_algebra[1][0][0].copy(), more_algebra[1][0][1], key_map={"f(x)": r"(e^{2x}-3e^x+2x)"}))
        self.wait()
        self.play(TransformMatchingTex(more_algebra[1][0][1].copy(), more_algebra[1][0][2], key_map={"x": r"\infty"}))
        self.wait()
        self.play(TransformMatchingTex(more_algebra[1][0][2].copy(), more_algebra[1][0][3], key_map={r"e^{2\cdot\infty}": r"\infty",
                                                                                                     r"-3e^\infty}": r"-infty",
                                                                                                     r"2\cdot\infty": r"\infty"}))
        self.wait()
        self.play(TransformMatchingTex(more_algebra[1][0][3].copy(), more_algebra[1][0][4], key_map={r"\infty-\infty+\infty": r"\infty"}))
        self.wait() 
        
        # Negative infinity
        self.play(Write(more_algebra[1][1][0]))
        self.wait()
        self.play(TransformMatchingTex(more_algebra[1][1][0].copy(), more_algebra[1][1][1], key_map={"f(x)": r"(e^{2x}-3e^x+2x)"}))
        self.wait()
        self.play(TransformMatchingTex(more_algebra[1][1][1].copy(), more_algebra[1][1][2], key_map={"x": r"-\infty"}))
        self.wait()
        self.play(TransformMatchingTex(more_algebra[1][1][2].copy(), more_algebra[1][1][3], key_map={r"e^{2\cdot-\infty}": r"0",
                                                                                                     r"3e^-\infty}": r"0",
                                                                                                     r"2\cdot-\infty": r"-\infty"}))
        self.wait()
        self.play(TransformMatchingTex(more_algebra[1][1][3].copy(), more_algebra[1][1][4], key_map={r"0-0-\infty": r"-\infty"}))
        self.wait()
        
        # Conclusion
        self.play(Write(more_algebra[-1]))
        
class G_Algebra(Scene):
    def construct(self):
        t2c = { 
            "x": BLUE_C,
        }
        kw = {
            "t2c": t2c,
            "font_size": 32
        }
        
        
        a_lot_of_algebra = VGroup(
            Tex("f(x)=e^{2x}-3e^x+2x+c", **kw),
            Text("Setting c = 0,", **kw),
            Tex("f(x)=e^{2x}-3e^x+2x", **kw),
            
            Text("To find y-intercept", **kw),
            Tex("f(0)=e^2\cdot0-3e^0+2\cdot0", **kw),
            Tex("=1-3+0", **kw),
            Tex("=-2", **kw),
            Tex(r"\therefore y-intercept=(0, -2)", **kw),
            
            Text("To find x-intercept", **kw),
            Tex("f(x)=0", **kw),
            Tex("e^{2x}-3e^x+2x=0", **kw),
            Tex(r"x\approx 0.823 (3d.p.)", **kw),
            Tex(r"\therefore x-intercept=(0.823, 0)", **kw),
        )
        a_lot_of_algebra.arrange(DOWN, buff=MED_SMALL_BUFF)
        
        self.play(Write(a_lot_of_algebra[0]))
        self.wait()
        self.play(Write(a_lot_of_algebra[1]))
        self.play(TransformMatchingTex(a_lot_of_algebra[0].copy(), a_lot_of_algebra[2]))
        self.wait()
        
        self.play(Write(a_lot_of_algebra[3]))
        self.wait()
        self.play(Write(a_lot_of_algebra[4]))
        self.wait()
        self.play(TransformMatchingTex(a_lot_of_algebra[4].copy(), a_lot_of_algebra[5], key_map={r"e^2\cdot0": "1", r"3e^0": "3", r"2\cdot0": "0"}))
        self.wait()
        self.play(TransformMatchingTex(a_lot_of_algebra[5].copy(), a_lot_of_algebra[6], key_map={"1-3+0": "-2"}))
        self.wait()
        
        self.play(Write(a_lot_of_algebra[7]))
        self.wait()
        self.play(Write(a_lot_of_algebra[8]))
        self.wait()
        self.play(Write(a_lot_of_algebra[9]))
        self.wait()
        self.play(TransformMatchingTex(a_lot_of_algebra[9].copy(), a_lot_of_algebra[10], key_map={"f(x)": "e^{2x}-3e^x+2x"}))
        self.wait()
        self.play(TransformMatchingTex(a_lot_of_algebra[10].copy(), a_lot_of_algebra[11], key_map={"e^{2x}-3e^x+2x": "x"}, path_arc=30 * DEGREES))
        self.wait()
        self.play(Write(a_lot_of_algebra[-1]))

class Finalle(Scene):
    def construct(self):
        axes = Axes(
            x_range=(-20, 20),
            y_range=(-11, 10), 
            unit_size=.5
        )
        
        
        graph = axes.get_graph(f, color=BLUE)
        graph.set_stroke(width=3)
        self.add(axes)
        self.play(ShowCreation(graph), run_time=5)
        self.wait()

        def taylor_f(x, j):
            n = 4
            y = 0
            
            
            a = j()
            
            if n >= 1:
                y += f(a)
            if n >= 2:
                y += f_prime(a) * (x - a)
            if n >= 3:
                for i in range(2, n + 1):
                    y += (((2 ** i * math.exp(2 * a) - 3 * np.exp(a))) / math.factorial(i)) * (x - a) ** i
            
            return y
            
        # curve = axes.get_graph(lambda x: taylor_f(x, math.log(3 / 4)), color=YELLOW)
        # self.play(ShowCreation(curve))
        # x_tracker = ValueTracker(0)
        # curvature = axes.get_graph(lambda x: taylor_f(x, x_tracker.get_value), color=YELLOW)
        # curvature.add_updater(lambda m: m.become(axes.get_graph(lambda x: taylor_f(x, x_tracker.get_value), color=YELLOW)))
        # self.play(ShowCreation(curvature, run_time=5))
        
        # G
        x_intercept = Dot(axes.c2p(0.823, 0), .05)
        y_intercept = Dot(axes.c2p(0, -2), .05)
        xi_label = Tex("(0.823, 0)")
        yi_label = Tex("(0, -2)")
        xi_label.next_to(x_intercept, UP + RIGHT)
        yi_label.next_to(y_intercept, DOWN + RIGHT) 
        
        self.play(
            FadeIn(x_intercept),
            FadeIn(y_intercept)
        )
        self.wait()
        self.play(
            Write(yi_label),
            Write(xi_label)
        )
        self.wait()
        self.play(
            FadeOut(x_intercept),
            FadeOut(y_intercept),
            FadeOut(yi_label),
            FadeOut(xi_label)
        )
        
        
        # F
        f_x_tracker = ValueTracker(1.04)
        straight_line = axes.get_graph(lambda x: 1.5, color=YELLOW)
        straight_line.add_updater(lambda m: m.become(axes.get_graph(lambda x: f(f_x_tracker.get_value()))))
        self.play(ShowCreation(straight_line))
        self.wait()
        intersect = Dot(axes.c2p(1.04, 1.5), 0.05)
        intersect.set_color(RED)
        f_always(intersect.move_to, lambda : axes.c2p(f_x_tracker.get_value(), f(f_x_tracker.get_value())))
        
        self.play(FadeIn(intersect))
        self.wait()
        self.play(f_x_tracker.animate.set_value(3), run_time=2)
        self.play(f_x_tracker.animate.set_value(-5), run_time=4)
        self.wait()
        # E
        e_x_tracker = ValueTracker(0.2)
        curvature = axes.get_graph(lambda x: taylor_f(x, e_x_tracker.get_value), color=WHITE)
        curvature.add_updater(lambda m: m.become(axes.get_graph(lambda x: taylor_f(x, e_x_tracker.get_value))))
        
        e_label = Text("Concave down")
        e_label_1 = Text("Concave up")
        e_label.set_color(RED)
        e_label_1.set_color(TEAL)
        self.play(ShowCreation(curvature), run_time=3)
        self.play(e_x_tracker.animate.set_value(-2), run_time=3)
        self.play(FadeIn(e_label))
        self.wait()
        self.play(FadeOut(e_label))
        self.play(e_x_tracker.animate.set_value(1), run_time=3)
        self.play(FadeIn(e_label_1))
        self.wait()
        self.play(FadeOut(e_label_1))
        self.play(e_x_tracker.animate.set_value(3), run_time=3)
        
        # D 
        d_label = VGroup(Text("Point of inflection = "), Tex("(-0.2877, -2.2629)"))
        d_label.arrange(RIGHT, buff=SMALL_BUFF)
        inflection_point = Dot(axes.c2p(-0.2877, -2.2629), 0.06)
        inflection_point.set_color(RED)
        
        self.play(FadeIn(inflection_point))
        self.wait()
        self.play(Write(d_label))
        self.wait()
        self.play(FadeOut(d_label), FadeOut(inflection_point))
        self.wait()
        # C
        cd = axes.get_graph(f_prime, color=RED)
        cdd = axes.get_graph(lambda x: 4 * math.exp(2 * x) - 3 * math.exp(x), color=YELLOW)
        self.play(ReplacementTransform(graph, cd))
        self.wait()
        self.play(ReplacementTransform(cd, cdd))
        self.wait()
        self.play(ReplacementTransform(cdd, axes.get_graph(f, color=BLUE)))
        graph = axes.get_graph(f, color=BLUE)
        
        # B
        b_x_tracker = ValueTracker(-5)
        b_dot = Dot(axes.c2p(-5, f(-5)))
        b_dot.set_color(RED)
        b_line = always_redraw(lambda : axes.get_tangent_line(b_x_tracker.get_value(), length=2.5, graph=graph))
        self.add(b_dot)
        self.add(b_line)
        self.play(b_x_tracker.animate.set_value(3.5), run_time=5)
        self.wait()
        
        # A
        # GG
        self.play(FadeOut(axes))
        self.play(FadeOut(graph))
        self.play(Write(Text("Thank you for your attention"), run_time=3))