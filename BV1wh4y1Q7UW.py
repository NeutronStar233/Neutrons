from manim import *
from math import *

config.background_color = WHITE
config.frame_width = 16
config.frame_height = 9
config.pixel_width = 1920
config.pixel_height = 1080

class Begin(Scene):
    def construct(self):
        Textset1 = VGroup(
            MathTex("\\vec z=(z_1,z_2)",color=BLACK),
            MathTex("\\vec w=(w_1,w_2)",color=BLACK),
            MathTex("\\vec z\cdot \\vec w=z_1w_1+z_2w_2",color=BLACK)
        ).arrange(DOWN)

        self.wait(2)

        self.play(Create(Textset1),run_time = 4)

        self.wait(1)

        Textset2 = VGroup(Textset1.copy(),MathTex("\overrightarrow{f(x)}\cdot\overrightarrow{g(x)}=???",color=RED)).arrange(DOWN)

        self.play(Transform(Textset1,Textset2),FadeIn(Text("实际并非写作这样，此处只作一引入",color=GRAY).to_corner(DR)),run_time = 1.5)

        self.wait(2)

        self.play(Transform(Textset1,VGroup(
            Text("本视频包括：",color = BLACK),
            Text("回顾向量",color = BLACK),
            Text("函数的内积",color = BLACK),
            Text("简单运用",color = BLACK)
        ).arrange(DOWN)),run_time = 1.5)

        self.wait(2)


class Chapter1_1(Scene):
    def construct(self):
        plane = NumberPlane(axis_config = {
            "color":BLACK
        })
        Text1 = Text("第一部分：回顾向量",color = BLACK)
        vectorE1 = Vector([1,0],color = BLACK)
        vectorE2 = Vector([0,1],color = BLACK)
        vectorQ1 = Vector([1,1],color = PURPLE)
        vectorQ2 = Vector([-1,1],color = PURPLE)

        ve1C = vectorE1.copy()
        ve2c = vectorE2.copy()

        vectorZ = Vector([2,3],color = RED)
        vectorW = Vector([4,1],color = GREEN)

        e1T = MathTex("\\overrightarrow {e_1}",color = BLACK).next_to(vectorE1,DOWN)
        e2T = MathTex("\\overrightarrow {e_2}",color = BLACK).next_to(vectorE2,LEFT)
        zT = MathTex("\\overrightarrow z",color=RED).next_to(vectorZ,UP+RIGHT)
        wT = MathTex("\\overrightarrow w",color=GREEN).next_to(vectorW,UP+RIGHT)
        q1T = MathTex("\\overrightarrow {q_1}",color = PURPLE).next_to(vectorQ1,UP + RIGHT)
        q2T = MathTex("\\overrightarrow {q_2}",color = PURPLE).next_to(vectorQ2,UP + LEFT)


        e1TC = e1T.copy()
        e2TC = e2T.copy()
        zTC = zT.copy()

        ZTWT = MathTex("\\overrightarrow z \\cdot \\overrightarrow w = z_1 w_1 + z_2 w_2  ",color = PURE_RED,font_size=88).next_to(vectorE2,DOWN)

        ZtWL = VGroup(
            Line((0,0,0),((11/sqrt(17)*(cos(atan(1/4)))),(11/sqrt(17))*(sin(atan(1/4))),0),color=PURE_RED,stroke_width=5),
            DashedLine((2,3,0),((11/sqrt(17)*(cos(atan(1/4)))),(11/sqrt(17))*(sin(atan(1/4))),0),color = RED_A),
            MathTex("The\ Length\ of\ Red\ Line = \\frac{\\overrightarrow z \\cdot \\overrightarrow w}{\\vert\\vert\\overrightarrow w\\vert\\vert}",color=PURE_RED).to_corner(UL)
        )
        E1tZL = VGroup(
            Line((0,0,0),(2,0,0),color=PURE_RED,stroke_width=5),
            DashedLine((2,3,0),(2,0,0),color = RED_A),
            MathTex("\\overrightarrow {e_1}\\cdot\\overrightarrow z = 1\cdot z_1 + 0\cdot z_2 = z_1",color=PURE_RED).to_corner(UL)
        )

        q1tzT = VGroup(
            Line((0,0,0),((5/sqrt(2))*(cos(atan(1))),(5/sqrt(2))*(sin(atan(1))),0),color = PURE_RED,stroke_width=5),
            DashedLine((2,3,0),((5/sqrt(2))*(cos(atan(1))),(5/sqrt(2))*(sin(atan(1))),0),color = RED_A),
            MathTex("The\ Length\ of\ Red\ Line  =\\frac{\\overrightarrow {q_1}\\cdot\\overrightarrow z}{\\vert\\vert\\overrightarrow {q_1}\\vert\\vert}",color=PURE_RED).to_corner(UL)
        )

        self.play(FadeIn(Text1))
        self.wait(1)
        self.play(FadeOut(Text1))

        self.wait(1)
        self.play(Create(plane))
        self.wait(1)
        self.play(Create(vectorE1),Create(vectorE2),
                  FadeIn(e1T),
                  FadeIn(e2T)
        )

        self.wait(1)
        self.play(Create(vectorZ),FadeIn(zT))
        self.play(Transform(vectorE1,Vector([2,0],color = RED_A)),
                  Transform(e1T,MathTex("z_1\\overrightarrow {e_1}",color = BLACK).next_to(vectorE1,DOWN)),
                  Transform(vectorE2,Vector([0,3],color = RED_A)),
                  Transform(e2T,MathTex("z_2\\overrightarrow {e_2}",color = BLACK).next_to(vectorE2,LEFT))
                  )
        self.play(vectorE2.animate.shift(2*RIGHT),e2T.animate.shift(2*RIGHT),Transform(zT,MathTex("\\overrightarrow z =z_1\\overrightarrow {e_1} + z_2\\overrightarrow {e_2} =(z_1,z_2)",color = RED).next_to(vectorZ,UP)))

        self.wait(2)

        self.play(FadeOut(e1T),
                  FadeOut(e2T),
                  Transform(zT,zTC),
                  FadeOut(vectorE1),
                  FadeOut(vectorE2)
                  )

        self.play(Create(vectorW),Create(wT))

        self.wait(1)

        self.play(
            Create(ZTWT),
            Write(ZtWL)
        )

        self.wait(3)

        self.play(FadeOut(vectorW,wT,ZtWL,ZTWT))

        self.wait(3)

        self.play(Create(vectorQ1),Create(vectorQ2),Write(q1T),Write(q2T))
        self.wait(2)
        self.play(Write(q1tzT))
        self.wait(2)
        self.play(Transform(q1tzT,VGroup(
            Line((0,0,0),((5/sqrt(2))*(cos(atan(1))),(5/sqrt(2))*(sin(atan(1))),0),color = PURE_RED,stroke_width=5),
            DashedLine((2,3,0),((5/sqrt(2))*(cos(atan(1))),(5/sqrt(2))*(sin(atan(1))),0),color = RED_A),
            MathTex("The\ Length\ of\ Red\ Line  =\\vert\\vert\\overrightarrow {q_1}}\\vert\\vert\\frac{\\overrightarrow {q_1}\\cdot\\overrightarrow z}{\\vert\\vert\\overrightarrow {q_1}\\vert\\vert\\vert\\vert\\overrightarrow {q_1}\\vert\\vert}",color=PURE_RED).to_corner(UL),
            MathTex("=\\vert\\vert\\overrightarrow {q_1}}\\vert\\vert\\frac{\\overrightarrow {q_1}\\cdot\\overrightarrow z}{\\overrightarrow {q_1}\\cdot\\overrightarrow {q_1}}",color = PURE_RED).to_corner(UR)
        )))
        self.wait(1)
        self.play(FadeOut(q1tzT))
        self.play(Transform(vectorQ1,Vector([(5/sqrt(2))*(cos(atan(1))),(5/sqrt(2))*(sin(atan(1)))],color=PURPLE)),
                  Transform(q1T, MathTex("\\frac{\\overrightarrow {q_1}\\cdot\\overrightarrow z}{\\overrightarrow {q_1}\\cdot\\overrightarrow {q_1}}\\overrightarrow {q_1}",color = PURPLE).next_to(Vector([(5/sqrt(2))*(cos(atan(1))),(5/sqrt(2))*(sin(atan(1)))],color=PURPLE),UP + RIGHT)))
        self.wait(1)
        self.play(Transform(vectorQ2,Vector([(-1/sqrt(2))*(cos(atan(-1))),(-1/sqrt(2))*(sin(atan(-1)))],color = PURPLE)),
                  Transform(q2T,MathTex("\\frac{\\overrightarrow {q_2}\\cdot\\overrightarrow z}{\\overrightarrow {q_2}\\cdot\\overrightarrow {q_2}}\\overrightarrow {q_2}",color = PURPLE).next_to(Vector([(-1/sqrt(2))*(cos(atan(-1))),(-1/sqrt(2))*(sin(atan(-1)))],color = PURPLE),DOWN+RIGHT)))
        self.play(vectorQ2.animate.shift(vectorQ1.get_vector()),q2T.animate.shift(vectorQ1.get_vector()))
        self.play(
            Write(MathTex("\\overrightarrow z = \\frac{\\overrightarrow {q_1}\\cdot\\overrightarrow z}{\\overrightarrow {q_1}\\cdot\\overrightarrow {q_1}}\\overrightarrow {q_1} +\\frac{\\overrightarrow {q_2}\\cdot\\overrightarrow z}{\\overrightarrow {q_2}\\cdot\\overrightarrow {q_2}}\\overrightarrow {q_2}",color=PURE_RED).to_corner(UL)
                  ))






        self.wait(3)


class Chapter2_1(Scene):
    def construct(self):
        def FOxTGOx(x):
            return 3*cos(x)+2*sin(2*x)+cos(3*x)+(x*x)/20



        Text1 = Text("第二部分：函数的内积", color=BLACK)

        FxT = MathTex("f(x)",color = BLACK)
        GxT = MathTex("g(x)",color = BLACK)
        FxtC = FxT.copy()


        ax = Axes(x_range=(-8,8),y_range=(-4.5,4.5),axis_config={
            "color":BLACK
        })
        labels = ax.get_axis_labels(x_label=MathTex("x",color=BLACK),y_label=MathTex("f(x)g(x)",color=BLACK))
        FGxCurve = ax.plot(lambda x:FOxTGOx(x),color = RED)

        Xunit = ax.x_length/16
        Yunit = ax.y_length/9

        FxGxL = Line((-3*Xunit,0,0),(-3*Xunit,FOxTGOx(-3)*Yunit,0),color=PURE_RED)
        Fx1Gx1Label = MathTex("f(x_1)g(x_1)",color=PURE_RED).next_to(FxGxL,UP)
        area = ax.get_area(FGxCurve,x_range=(-8,8),color=[RED,RED_E])

        VG1 = VGroup(
            MathTex("\\overrightarrow {f(x)} \cdot \\overrightarrow {g(x)} = f(x_1)g(x_1)+f(x_2)g(x_2)+f(x_3)g(x_3)...",color=RED),
            MathTex("=AREA",color=RED),
            MathTex("=\int_{-\infty}^{+\infty} f(x)g(x) dx",color=RED)).arrange(DOWN).next_to((0,0,0),DOWN)

        def CAni(v_line, t):
            v_line.put_start_and_end_on(((-8+16 * t) * Xunit, 0, 0),((-8 + 16 * t) * Xunit,FOxTGOx(-8+16 * t)*Yunit, 0))


        self.wait(1)
        self.play(FadeIn(Text1))
        self.wait(1)
        self.play(FadeOut(Text1))
        self.wait(2)

        self.play(Write(FxT))
        self.wait(1)
        self.play(Transform(FxT,MathTex("\\overrightarrow {f(x)} = (f(x_1),f(x_2),f(x_3)...)",color=BLACK)))
        self.wait(1)
        self.play(Transform(FxT,VGroup(FxtC,GxT,
            MathTex("\\overrightarrow {f(x)} \cdot \\overrightarrow {g(x)} = f(x_1)g(x_1)+f(x_2)g(x_2)+f(x_3)g(x_3)...",color=RED)
        ).arrange(DOWN)))
        self.play(Transform(FxT,MathTex("\\overrightarrow {f(x)} \cdot \\overrightarrow {g(x)} = f(x_1)g(x_1)+f(x_2)g(x_2)+f(x_3)g(x_3)...",color=RED)))
        self.wait(2)
        self.play(FadeOut(FxT))

        self.play(Create(ax),Create(FGxCurve),Write(labels))
        self.wait(1)
        self.play(Write(FxGxL),Write(Fx1Gx1Label))
        self.wait(1)
        Fx1Gx1Label.next_to((-8*Xunit,0,0),UP)
        self.play(UpdateFromAlphaFunc(FxGxL,CAni),Fx1Gx1Label.animate.shift(16*Xunit*RIGHT),FadeIn(area),run_time=3)
        self.wait(1)
        self.play(TransformFromCopy(area,VG1))
        self.wait(1)
        self.play(Transform(VG1,VGroup(
            MathTex("<f(x),g(x)>",color=RED),
            MathTex("=\int_{-\infty}^{+\infty} f(x)g(x) dx",color=PURE_RED)).arrange(DOWN).next_to((0,0,0),DOWN)))
        self.wait(2)
        self.play(Transform(VG1,VGroup(
            MathTex("<f(x),g(x)>",color=RED),
            MathTex("=\int_{a}^{b} f(x)g(x) dx",color=PURE_RED)).arrange(DOWN).next_to((0,0,0),DOWN)))


        self.wait(2)

class Chapter3_1(Scene):
    def construct(self):
        Text1 = Text("第三部分：简单运用", color=BLACK)

        FtT = MathTex("f(t)",color=BLACK)
        csNTT = MathTex("cos\ nt",color=BLACK).to_corner(UL)
        csPeqFT =MathTex("f(t) =  \sum_{n = 0}^{+\infty}  F(n)cos\ nt ",color=BLACK).to_corner(UL)
        FnT = MathTex("F(n) =\\frac{<f(t),cos\ nt>}{<cos\ nt,cos\ nt>}",color=BLACK).to_corner(UR)

        self.wait(1)
        self.play(FadeIn(Text1))
        self.wait(1)
        self.play(FadeOut(Text1))
        self.wait(2)


        self.play(Write(FtT))
        self.wait(1)
        self.play(Write(csNTT))
        self.wait(1)
        self.play(Transform(csNTT,VGroup(
            MathTex("cos\ nt", color=BLACK),
            MathTex("n\in N", color=BLACK)
        ).arrange(DOWN).to_corner(UL)))
        self.wait(1)
        self.play(Unwrite(csNTT),Unwrite(FtT))
        self.play(Write(csPeqFT))
        self.wait(2)


        self.play(Write(FnT))
        self.wait(1)
        self.play(Transform(FnT,VGroup(
            MathTex("F(n) =\\frac{\int_{-\pi}^{+\pi} f(t)cos\ nt\ dt}{\int_{-\pi}^{+\pi} {cos}^2 nt dt}",color=BLACK),
            MathTex("=\\frac{\int_{-\pi}^{+\pi} f(t)cos\ nt\ dt}{ \\frac{\pi}{2} + sin\pi cos\pi + \\frac{\pi}{2} - sin\pi cos\pi}", color=BLACK),
            MathTex("=\\frac{1}{\pi}\int_{-\pi}^{+\pi} f(t)cos\ nt\ dt",color=PURE_RED)
        ).arrange(DOWN).to_corner(UR)))
        self.wait(1)
        self.play(Unwrite(csPeqFT),Transform(FnT,MathTex("F(n)=\\frac{1}{\pi}\int_{-\pi}^{+\pi} f(t)cos\ nt\ dt",color=BLACK)))

        self.wait(2)
        self.play(Transform(FnT,VGroup(
            MathTex("f(t) = 2cos\ t + cos\ 2t",color=BLACK),
            MathTex("F(n)=\\frac{1}{\pi}\int_{-\pi}^{+\pi} (2cos\ t + cos\ 2t)cos\ nt\ dt", color=BLACK),
        ).arrange(DOWN)))
        self.wait(1)
        self.play(Transform(FnT,VGroup(
            MathTex("f(t) = 2cos\ t + cos\ 2t",color=BLACK),
            MathTex("F(1)=\\frac{1}{\pi}\int_{-\pi}^{+\pi} (2cos\ t + cos\ 2t)cos\ 1t\ dt", color=BLACK),
            MathTex("=2", color=BLACK),
        ).arrange(DOWN)))
        self.wait(1)
        self.play(Transform(FnT, VGroup(
            MathTex("f(t) = 2cos\ t + cos\ 2t", color=BLACK),
            MathTex("F(2)=\\frac{1}{\pi}\int_{-\pi}^{+\pi} (2cos\ t + cos\ 2t)cos\ 2t\ dt", color=BLACK),
            MathTex("=1", color=BLACK),
        ).arrange(DOWN)))
        self.wait(1)
        self.play(Transform(FnT, VGroup(
            MathTex("f(t) = 2cos\ t + cos\ 2t", color=BLACK),
            MathTex("F(3)=\\frac{1}{\pi}\int_{-\pi}^{+\pi} (2cos\ t + cos\ 2t)cos\ 3t\ dt", color=BLACK),
            MathTex("=0", color=BLACK),
        ).arrange(DOWN)))
        self.wait(2)

        self.play(FadeIn(Text("这不是真正的傅里叶变换",color=GRAY).to_corner(DR)))

        self.wait(3)

class TitlePage(Scene):
    def construct(self):
        self.add(VGroup(
            MathTex("\\vec z=(z_1,z_2)",color=BLACK),
            MathTex("\\vec w=(w_1,w_2)",color=BLACK),
            MathTex("\\vec z\cdot \\vec w=z_1w_1+z_2w_2",color=BLACK),
            MathTex("\\overrightarrow{f(x)}\cdot\\overrightarrow{g(x)} = ???",color=RED,font_size=100)
        ).arrange(DOWN))