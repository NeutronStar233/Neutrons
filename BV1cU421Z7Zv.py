import random
import math
import numpy
from manim import*

config.background_color = WHITE
config.frame_width = 16
config.frame_height = 9
config.pixel_width = 1920
config.pixel_height = 1080

class s1(Scene):
    def construct(self):
        self.wait(1)

        t1 = Text("神经网络",color=BLACK)
        tidk = Tex(r"$$\text{Neural Network}$$",color=BLACK).next_to(t1,DOWN)
        self.wait(1)
        self.play(FadeIn(t1,tidk))
        self.wait(1)
        t4 = Tex("ChatGPT",color=BLACK)
        self.play(Transform(t1,t4),FadeOut(tidk))
        self.wait(1)
        t2 = Text("\"为什么陨石总是落在陨石坑上\"", font_size=25 ,color=RED).next_to(t1,LEFT,buff = 1)
        at2 = Text("\"为什么陨石总是落在陨石坑上\"", font_size=25 ,color=RED).next_to(t1,LEFT,buff = 1)
        self.play(FadeIn(t2))
        self.add(at2)
        self.wait(1)
        t3 = Text("\"事实上，这是因为陨石坑是由陨石撞击形成的...\"",font_size=18,color=RED).next_to(t1,RIGHT,buff = 0.5)
        self.play(Transform(t2,t3))
        self.wait(1)
        t5 = Text("某能从图片识别出数字0~9的神经网络",font_size=25,color=BLACK)
        self.play(FadeOut(t2),FadeOut(at2),Transform(t1,t5))
        self.wait(1)
        t6 = Text("7",font="High Tower Text",font_size=200,color= BLACK).next_to(t1,LEFT,buff = 1)
        at6 = Text("7",font="High Tower Text",font_size=200,color= BLACK).next_to(t1,LEFT,buff = 1)
        self.play(FadeIn(t6))
        self.add(at6)
        self.wait(1)
        t7 = Tex("7",color=RED).next_to(t1,RIGHT,buff = 1)
        self.play(Transform(t6,t7))
        self.wait(1)
        t8 = Text("神经网络",color= BLACK)
        self.play(Transform(t1,t8))
        self.wait(1)
        t9 = Tex("f",color=RED,font_size=200)
        self.play(Transform(t1,t9))
        self.wait(1)
        t10 = Text("7",font="High Tower Text",font_size=200,color= BLACK).next_to(t1,LEFT,buff = 1)
        t11 = Tex("f",color=RED,font_size=200)
        t12 = Tex("(",color=RED)
        t13 = Tex(") =",color=RED)
        t14 = Tex("7",color=RED).next_to(t1,RIGHT,buff = 1)
        g1 = VGroup(t11,t12,t10,t13,t14).arrange(RIGHT)
        self.play(Transform(t1,t11),Transform(at6,t10),Transform(t6,t14),FadeIn(t12),FadeIn(t13))
        self.wait(1)
        t15 = Tex(r"$$\left[ \begin{array}{l}0.001\\0.012\\0.002\\0.001\\0.001\\0.002\\0.001\\0.997\\0.001\\0.001\\\end{array} \right] $$",color=RED)
        t16 = Tex("(",color=RED)
        t17 = Tex(") =",color=RED)
        g2 = VGroup(t11,t16,t10,t17,t15).arrange(RIGHT)
        self.play(Transform(t1,t11),Transform(at6,t10),Transform(t6,t15),Transform(t12,t16),Transform(t13,t17))
        self.wait(1)
        t18 = Tex("(",color=RED)
        t19 = Tex(") =",color=RED)
        t20 = Tex(r"$$\begin{matrix}0&		1&		1&    0\\0&		0&		1&0\\0&0&1&0\\0& 0& 1& 0\\\end{matrix}$$",color=BLACK)
        t21 = Tex(r"$$\left[ \begin{array}{l}0.001\\0.012\\0.002\\0.001\\0.001\\0.002\\0.001\\0.997\\0.001\\0.001\\\end{array} \right] $$",color=RED)
        g3 = VGroup(t11,t18,t20,t19,t21).arrange(RIGHT)
        bt1 = Text("虽然但是，这里没有16*16个值，因为我懒（bushi）",color=GRAY,font_size=25).to_corner(RIGHT+DOWN)
        self.play(Transform(t1,t11),Transform(at6,t20),Transform(t6,t21),Transform(t12,t18),Transform(t13,t19),FadeIn(bt1))
        self.wait(1)
        t22 = Tex("(",color=RED)
        t23 = Tex(") =",color=RED)
        t24 = Tex(r"$$\left[\begin{array}{l}0\\		1\\		1\\    0\\0\\		0\\		1\\0\\0\\0\\1\\0\\0\\ 0\\ 1\\ 0\\\end{array}\right]$$",color=BLACK)
        t25 = Tex(r"$$\left[ \begin{array}{l}0.001\\0.012\\0.002\\0.001\\0.001\\0.002\\0.001\\0.997\\0.001\\0.001\\\end{array} \right] $$",color=RED)
        g3 = VGroup(t11, t22, t24, t23, t25).arrange(RIGHT)
        self.play(Transform(t1, t11), Transform(at6, t24), Transform(t6, t25), Transform(t12, t22), Transform(t13, t23),FadeOut(bt1))
        self.wait(1)


def EF(x):
    return  float(0.5*(x) * (x) - 2 * (x) - 4)
def D_EF(x):
       return float(x-2)

class NBOBJECT:
    def __init__(self,value):
        self.value = value
    def GetValue(self):
        return self.value
    def ChangeValue(self,newValue):
        self.value = newValue
class ALLTHEGD2(Animation):
    def __init__(self,mobject,function,Dfunction,axes:Axes,backingX,start_x=float(-1),**kwargs):
        super().__init__(mobject,**kwargs)
        self.LX = start_x
        self.LT = 0
        self.FUNCTION = function
        self.DFUNCTION = Dfunction
        self.AXES = axes
        self.MOBJECT = backingX
    def begin(self):
        V_NDOF = Arrow(start=self.AXES.coords_to_point(self.LX,self.FUNCTION(self.LX)),end=self.AXES.coords_to_point(-self.DFUNCTION(self.LX)+self.LX,self.FUNCTION(self.LX)),color=BLUE,buff=0)
        dot = Dot(self.AXES.coords_to_point(self.LX,self.FUNCTION(self.LX)),color=PURE_RED)

        self.mobject.add(V_NDOF)
        self.V_NDOF = V_NDOF
        self.mobject.add(dot)
        self.dot = dot

        super().begin()
    def clean_up_from_scene(self, scene: Scene) -> None:
        super().clean_up_from_scene(scene)
        scene.remove(self.V_NDOF)
        scene.remove(self.dot)

    def interpolate_mobject(self, alpha):
        if alpha-self.LT >= 0.1:
            self.LT += 0.1
            NEWX = float(self.LX-(0.2*self.DFUNCTION(self.LX)))
            self.dot.move_to(self.AXES.coords_to_point(NEWX,self.FUNCTION(NEWX)))
            self.MOBJECT[0] = NEWX
            self.V_NDOF.put_start_and_end_on(self.AXES.coords_to_point(NEWX,self.FUNCTION(NEWX)),self.AXES.coords_to_point(NEWX-self.DFUNCTION(NEWX),self.FUNCTION(NEWX)))
            self.LX = NEWX


class s2(Scene):
    def construct(self):
        t1 = Tex("f(",color=BLACK)
        t2 = Tex("·",color=BLACK)
        t3 = Tex(")",color=BLACK)
        g1 = VGroup(t1,t2,t3).arrange(RIGHT)
        self.wait(1)
        self.play(Write(g1))
        self.wait(1)
        t4 = Tex("$$x$$",color=RED)
        t5 = Tex("f(",color=BLACK)
        t6 = Tex(")",color=BLACK)
        g2 = VGroup(t5,t4,t6).arrange(RIGHT)
        self.play(Transform(t1,t5),Transform(t2,t4),Transform(t3,t6))
        self.wait(1)
        t7 = Tex("5",color=RED)
        t8 = Tex("=",color=BLACK)
        t9 = Tex("11",color=RED)
        g3 = VGroup(t5,t7,t6,t8,t9).arrange(RIGHT)
        self.play(Transform(t1,t5),Transform(t2,t7),Transform(t3,t6),Write(t8),Write(t9))
        self.wait(1)
        t10 = Tex("$$kx+b$$",color=RED)
        at8 = Tex("=",color=BLACK)
        g4 = VGroup(t5, t4, t6,at8,t10).arrange(RIGHT)
        self.play(Transform(t1,t5),Transform(t2,t4),Transform(t3,t6),Transform(t8,at8),Transform(t9,t10))
        self.wait(1)
        t19 = Tex("$$5k+b$$",color=RED)
        t20 = Tex("$$=11$$",color=RED)
        g5 = VGroup(t5,t7,t6,at8,t19,t20).arrange(RIGHT)
        self.play(Transform(t1, t5), Transform(t2, t7), Transform(t3, t6), Transform(t8, at8), Transform(t9, t19),Write(t20))
        self.wait(1)
        t21 = Tex(r"$$k=\frac{11-b}{5}$$",color=BLACK)
        at20 = Tex("$$=11$$",color=RED)
        at5 = Tex("f(",color=BLACK)
        at7 = Tex("5",color=RED)
        at6 = Tex(")",color=BLACK)
        bt8 = Tex("=",color=BLACK)
        at19 = Tex("$$5k+b$$",color=RED)
        ag5 = VGroup(at5,at7,at6,bt8,at19,at20).arrange(RIGHT)
        g6 = VGroup(ag5,t21).arrange(DOWN)
        self.play(Transform(t1, at5), Transform(t2, at7), Transform(t3, at6), Transform(t8, bt8), Transform(t9, at19),Transform(t20,at20),FadeIn(t21))
        self.wait(1)
        at_5 = Tex("$$5$$",color=BLACK)
        t_5 = Tex("$$5$$",color=BLACK)
        t_k = Tex("$$k$$",color=RED)
        t_b = Tex("$$b$$",color=RED)
        t_PLUS = Tex("$$+$$",color=BLACK)
        t_CDOT = Tex(r"$$\cdot$$",color=BLACK)
        g7 = VGroup(t5,at_5,at6,at8,t_5,t_CDOT,t_k,t_PLUS,t_b,at20).arrange(RIGHT)
        self.play(Transform(t1, t5), Transform(t2, at_5), Transform(t3, at6), Transform(t8, at8), Transform(t9, t_5),Transform(t20, at20),FadeOut(t21),
                  FadeIn(t_k,t_PLUS,t_b,t_CDOT))
        self.wait(1)
        t_1 = Tex("$$1$$",color=RED)
        at_1 = Tex("$$1$$",color=RED)
        at_PLUS = Tex("$$+$$", color=BLACK)
        at_CDOT = Tex(r"$$\cdot$$", color=BLACK)
        t_EQUALTO6 = Tex("$$=6$$",color=RED)
        g7 = VGroup(t5, at_5, at6, at8, t_5, at_CDOT, t_1, at_PLUS, at_1, t_EQUALTO6).arrange(RIGHT)
        self.play(Transform(t1, t5), Transform(t2, at_5), Transform(t3, at6), Transform(t8, at8), Transform(t9, t_5),
                  Transform(t20, t_EQUALTO6),Transform(t_k,t_1),Transform(t_b,at_1),Transform(t_PLUS,at_PLUS),Transform(t_CDOT,at_CDOT))
        self.wait(1)
        g7.to_corner(UP)
        self.play(Transform(t1, t5), Transform(t2, at_5), Transform(t3, at6), Transform(t8, at8), Transform(t9, t_5),
                  Transform(t20, t_EQUALTO6), Transform(t_k, t_1), Transform(t_b, at_1), Transform(t_PLUS, at_PLUS),
                  Transform(t_CDOT, at_CDOT))
        self.wait(1)
        T1 = Tex("$$C$$",color=RED)
        T2 = Tex("$$=$$",color=BLACK)
        T3 = Tex("$$6$$",color=RED)
        T4 = Tex("$$-$$",color=BLACK)
        T5 = Tex("$$11$$",color=RED)
        G1 = VGroup(T1,T2,T3,T4,T5).arrange(RIGHT).next_to(g7,DOWN).to_edge(LEFT)
        self.play(FadeIn(T1,T2,T3,T4,T5))
        self.wait(1)
        aT1 = Tex("$$C$$", color=RED)
        aT2 = Tex("$$=$$", color=BLACK)
        aT3 = Tex("$$6$$", color=RED)
        aT4 = Tex("$$-$$", color=BLACK)
        aT5 = Tex("$$11$$", color=RED)
        T6 = Tex("$$=$$",color=BLACK)
        T7 = Tex("$$-5$$",color=RED)
        G2 = VGroup(aT1,aT2,aT3,aT4,aT5,T6,T7).arrange(RIGHT).next_to(g7,DOWN).to_edge(LEFT)
        self.play(Transform(T1,aT1),Transform(T2,aT2),Transform(T3,aT3),Transform(T4,aT4),Transform(T5,aT5),FadeIn(T6,T7))
        self.wait(1)
        aT6 = Tex("$$=$$",color=BLACK)
        AT1 = Tex("$$($$",color=BLACK)
        AT2 = Tex("$$)^2$$",color=BLACK)
        aT7 = Tex("$$25$$",color=RED)
        G3 = VGroup(aT1,aT2,AT1,aT3,aT4,aT5,AT2,aT6,aT7).arrange(RIGHT).next_to(g7,DOWN).to_edge(LEFT)
        self.play(Transform(T1, aT1), Transform(T2, aT2), Transform(T3, aT3), Transform(T4, aT4), Transform(T5, aT5),
                  FadeIn(AT1, AT2),Transform(T6,aT6),Transform(T7,aT7))
        self.wait(1)
        AX = Axes(
            x_range = [-10,10,2],
            y_range = [-10, 10, 2],
            x_length = 8,
            y_length = 8,
            axis_config={"color":BLACK,"include_numbers":True}
        )
        for number in AX.x_axis.numbers:
            number.set_color(BLACK)
        for number in AX.y_axis.numbers:
            number.set_color(BLACK)
        AX.next_to(g7,DOWN).to_edge(RIGHT)
        graph = AX.plot(lambda x:EF(x),color=RED)
        _666T = VGroup(Text("梯度下降",color=BLACK),Tex(r"$$\text{Gradient Descent}$$",color=BLACK)).arrange(DOWN).to_edge(DOWN)
        self.play(Write(AX))
        self.play(Write(graph),Write(_666T))
        self.wait(1)
        dot = Dot(color=PURE_RED)
        dot.move_to(AX.coords_to_point(-1,EF(-1)))
        T_POSITION_OF_DOT = Tex(r"$$\left(x_0,f(x_0)\right)$$",color=RED).next_to(dot,LEFT+UP)
        T_TIPS = Text("这里的f是一个单独的例子，并非上面的f",color=GRAY,font_size=25).to_corner(RIGHT+DOWN)
        self.play(FadeIn(dot),Write(T_POSITION_OF_DOT),FadeIn(T_TIPS),FadeOut(_666T))
        self.wait(1)
        T_DELTA_OF_F = Tex(r"$$\nabla f=\left[ f' \right] $$",color=RED).to_edge(LEFT)
        V_DOF = Arrow(start=AX.coords_to_point(-1,EF(-1)),end=AX.coords_to_point(D_EF(-1)-1,EF(-1)),color=RED,buff=0)
        self.play(Write(T_DELTA_OF_F),Write(V_DOF),FadeOut(T_TIPS))
        self.wait(1)
        T_NDELTA_OF_F = Tex(r"$$-\nabla f=-\left[ f' \right] $$",color=BLUE).next_to(T_DELTA_OF_F,DOWN,aligned_edge=LEFT)
        V_NDOF = Arrow(start=AX.coords_to_point(-1,EF(-1)),end=AX.coords_to_point(-D_EF(-1)-1,EF(-1)),color=BLUE,buff=0)
        self.play(Write(V_NDOF),Write(T_NDELTA_OF_F))
        self.wait(1)
        T_NEWXZERO = Tex(r"$$x_{0}^{'}$$",color=RED)
        T_E = Tex("$$=$$",color=BLACK)
        T_XZERO = Tex(r"$$x_0$$",color=RED)
        T_MINUS = Tex("$$-$$",color=BLUE)
        T_DEOF = Tex("$$f'$$",color=BLUE)
        gG1 = VGroup(T_NEWXZERO,T_E,T_XZERO,T_MINUS,T_DEOF).arrange(RIGHT).next_to(T_NDELTA_OF_F,DOWN,aligned_edge=LEFT)
        self.play(Write(T_NEWXZERO),Write(T_E),Write(T_XZERO),Write(T_MINUS),Write(T_DEOF))
        self.wait(1)
        aT_NEWXZERO = Tex(r"$$x_{0}^{'}$$", color=RED)
        aT_E = Tex("$$=$$", color=BLACK)
        aT_XZERO = Tex(r"$$x_0$$", color=RED)
        aT_MINUS = Tex("$$-$$", color=BLUE)
        aT_DEOF = Tex("$$f'$$", color=BLUE)
        T_RATE = Tex("$$r$$",color=RED)
        gG2 = VGroup(aT_NEWXZERO, aT_E, aT_XZERO, aT_MINUS,T_RATE, aT_DEOF).arrange(RIGHT).next_to(T_NDELTA_OF_F, DOWN,
                                                                                       aligned_edge=LEFT)
        self.play(Transform(T_NEWXZERO,aT_NEWXZERO),Transform(T_E,aT_E),Transform(T_XZERO,aT_XZERO),Transform(T_MINUS,aT_MINUS),Transform(T_DEOF,aT_DEOF),Write(T_RATE))
        self.wait(1)
        self.remove(V_DOF,V_NDOF,dot,T_POSITION_OF_DOT)
        backingX = [random.random()]
        self.play(ALLTHEGD2(Mobject(),EF,D_EF,AX,backingX,-1),runtime=3,rate_functions=lambda t:t)
        dot.move_to(AX.coords_to_point(backingX[0],EF(backingX[0])))
        self.add(dot)
        self.wait(1)
        def HHF(x):
            return (0.1*(x*x*x))-x
        def D_HHF(x):
            return 0.3*(x*x)-1
        graph2holes = AX.plot(HHF,color= BLUE)
        self.play(Unwrite(graph),Write(graph2holes))
        self.wait(1)
        self.play(dot.animate.move_to(AX.coords_to_point(4,HHF(4))))
        self.wait(1)
        self.remove(dot)
        backingX = [random.random()]
        self.play(ALLTHEGD2(Mobject(),HHF,D_HHF,AX,backingX,4),runtime=3,rate_functions=lambda t:t)
        dot.move_to(AX.coords_to_point(backingX[0],HHF(backingX[0])))
        self.add(dot)
        self.wait(1)
        self.play(dot.animate.move_to(AX.coords_to_point(-1.826,HHF(-1.826))))
        T_DEZ = Tex(r"$$\nabla f=\vec{0}$$",color=RED).next_to(dot,LEFT+UP)
        self.play(Write(T_DEZ))
        self.wait(3)
        self.wait(1)
        self.play(FadeOut(T_DELTA_OF_F,T_NDELTA_OF_F,AX,graph2holes,dot,T_DEZ),FadeOut(T_NEWXZERO),FadeOut(T_E),FadeOut(T_XZERO),FadeOut(T_MINUS),FadeOut(T_DEOF,T_RATE))
        self.wait(1)
        T_F = Tex(r"$$\text{f}$$",color=RED)
        aAT1 = Tex("$$($$", color=BLACK)
        aAT2 = Tex("$$)^2$$", color=BLACK)
        aaT6 = Tex("$$=$$", color=BLACK)
        aaT7 = Tex("$$25$$",color=RED)
        G4 = VGroup(aT1,aT2,aAT1,T_F,aT4,aT5,aAT2,aaT6,aaT7).arrange(RIGHT).next_to(g7,DOWN).to_edge(LEFT)
        self.play(Transform(T1, aT1), Transform(T2, aT2), Transform(T3, T_F), Transform(T4, aT4), Transform(T5, aT5),
                  Transform(AT1,aAT1),Transform(AT2,aAT2),Transform(T6,aaT6),Transform(T7,aaT7))
        self.wait(1)
        T_DELTA_OF_C = Tex(r"$$\nabla C=\left[ \begin{array}{l}\frac{\partial C}{\partial k} \\ \frac{\partial C}{\partial b}\\\end{array} \right] $$",color=RED).next_to(G4,DOWN,aligned_edge=LEFT)
        self.play(Write(T_DELTA_OF_C))
        self.wait(1)
        T_W = Tex(r"$$W=\left[\begin{array}{l}k\\b \end{array} \right] $$",color=RED).next_to(T_DELTA_OF_C,DOWN,aligned_edge=LEFT)
        T_NEWW = Tex(r"$$W'=W-r\nabla C$$",color=BLUE).next_to(T_W,DOWN,aligned_edge=LEFT)
        self.play(Write(T_W),Write(T_NEWW))
        self.wait(1)
        T_CDK = Tex(r"$$\frac{\partial C}{\partial k}$$",color=RED).next_to(T_NEWW,DOWN,aligned_edge=LEFT)
        self.play(Write(T_CDK))
        self.wait(1)
        aT_CDK = Tex(r"$$\frac{\partial C}{\partial k}$$",color=RED).next_to(T_NEWW,DOWN,aligned_edge=LEFT)
        T_EEE = Tex(r"$$=$$",color=BLACK)
        T_CDF = Tex(r"$$\frac{\partial C}{\partial \text{f}}$$",color=RED)
        T_FDK = Tex(r"$$\frac{\partial \text{f}}{\partial k}$$",color=BLUE)
        G_CDK = VGroup(aT_CDK,T_EEE,T_CDF,T_FDK).arrange(RIGHT).next_to(T_NEWW,DOWN,aligned_edge=LEFT)
        self.play(Transform(T_CDK,aT_CDK),Write(T_EEE),Write(T_CDF),Write(T_FDK))
        self.wait(1)
        TTT_21 = Tex(r"$$\frac{1}{2}$$",color=RED)
        aT_F = Tex(r"$$\text{f}$$",color=RED)
        aaaT7 = Tex("$$12.5$$", color=RED)
        G5 = VGroup(aT1, aT2,TTT_21, aAT1, aT_F, aT4, aT5, aAT2,aaT6,aaaT7).arrange(RIGHT).next_to(g7, DOWN).to_edge(LEFT)
        self.play(Transform(T1, aT1), Transform(T2, aT2), Transform(T3, aT_F), Transform(T4, aT4), Transform(T5, aT5),
                  Transform(AT1, aAT1), Transform(AT2, aAT2),Write(TTT_21),Transform(T6,aaT6),Transform(T7,aaaT7))
        self.wait(1)
        T_EE2 = Tex(r"$$=$$",color=BLACK)
        T_TCDF = Tex(r"$$(\text{f}-11)$$",color=RED)
        T_TFDK = Tex(r"$$5$$",color=BLUE)
        aG_CDK = VGroup(aT_CDK,T_EEE,T_CDF,T_FDK,T_EE2,T_TCDF,T_TFDK).arrange(RIGHT).next_to(T_NEWW,DOWN,aligned_edge=LEFT)
        self.play(Write(T_EE2),Write(T_TCDF),Write(T_TFDK))
        self.wait(1)
        T_CDB = Tex(r"$$\frac{\partial C}{\partial b}$$",color=RED)
        T_EE3 = Tex("$$=$$",color=BLACK)
        T_CDF2 = Tex(r"$$\frac{\partial C}{\partial \text{f}}$$",color=RED)
        T_FDB = Tex(r"$$\frac{\partial \text{f}}{\partial b}$$",color=BLUE)
        T_EE4 = Tex("$$=$$", color=BLACK)
        T_TCDF2 = Tex(r"$$(\text{f}-11)$$",color=RED)
        T_TFDB = Tex(r"$$1$$",color=BLUE)
        G_CDB = VGroup(T_CDB,T_EE3,T_CDF2,T_FDB,T_EE4,T_TCDF2,T_TFDB).arrange(RIGHT).next_to(G_CDK,DOWN,aligned_edge=LEFT)
        self.play(FadeIn(T_CDB,T_EE3,T_CDF2,T_FDB,T_EE4,T_TCDF2,T_TFDB))
        self.wait(1)
        T_RCDK = Tex(r"$$=-25$$",color=BLACK)
        T_RCDB = Tex(r"$$=-5$$", color=BLACK)
        aG_CDK = VGroup(aT_CDK, T_EEE, T_CDF, T_FDK, T_EE2, T_TCDF, T_TFDK,T_RCDK).arrange(RIGHT).next_to(T_NEWW, DOWN,
                                                                                                   aligned_edge=LEFT)
        aG_CDB = VGroup(T_CDB, T_EE3, T_CDF2, T_FDB, T_EE4, T_TCDF2, T_TFDB,T_RCDB).arrange(RIGHT).next_to(G_CDK, DOWN,
                                                                                                   aligned_edge=LEFT)
        self.play(Write(T_RCDK),Write(T_RCDB))
        self.wait(1)
        T_RDC = Tex(r"$$=\left[ \begin{array}{l}-25\\-5\\\end{array} \right] $$",color=BLACK).next_to(T_DELTA_OF_C,RIGHT)
        self.play(Write(T_RDC))
        self.remove(T_CDB,T_EE3,T_CDF2,T_FDB,T_EE4,T_TCDF2,T_TFDB,T_EE2,T_TCDF,T_TFDK,T_CDK,T_CDK,T_CDF,T_FDK)
        self.add(aG_CDK,aG_CDB)
        self.wait(1)
        T_R_E_ZZO = Tex(r"$$r=0.01$$",color=RED).next_to(g7,DOWN).to_edge(RIGHT)
        aT_NEWW = Tex(r"$$W'=W-r\nabla C$$",color=BLUE).next_to(T_W,DOWN,aligned_edge=LEFT)
        T_RNEWW = Tex(r"$$=\left[\begin{array}{l}k\\b \end{array} \right]-0.01\left[\begin{array}{l}-25\\-5 \end{array} \right]=\left[\begin{array}{l}1.25\\1.05 \end{array} \right]$$",color=BLACK)
        G_RNEWWW = VGroup(aT_NEWW,T_RNEWW).arrange(RIGHT).next_to(T_W,DOWN,aligned_edge=LEFT)
        self.play(Transform(T_NEWW,aT_NEWW),Write(T_RNEWW),Write(T_R_E_ZZO),aG_CDK.animate.next_to(G_RNEWWW,DOWN,aligned_edge=LEFT))
        self.play(aG_CDB.animate.next_to(aG_CDK,DOWN,aligned_edge=LEFT))
        self.wait(1)
        T_NK = Tex(r"$$1.25$$",color=RED)
        T_NB = Tex(r"$$1.05$$", color=RED)
        t_EQUALTO73 = Tex(r"$$=7.3$$",color=RED)
        aaT7 = Tex(r"$$6.845$$",color=RED).next_to(T6,RIGHT)
        g7 = VGroup(t5, at_5, at6, at8, t_5, at_CDOT, T_NK, at_PLUS, T_NB, t_EQUALTO73).arrange(RIGHT).to_corner(UP)

        self.play(Transform(t1, t5), Transform(t2, at_5), Transform(t3, at6), Transform(t8, at8), Transform(t9, t_5),
                  Transform(t20, t_EQUALTO73), Transform(t_k, T_NK), Transform(t_b, T_NB), Transform(t_PLUS, at_PLUS),
                  Transform(t_CDOT, at_CDOT),Transform(T6,aaT6),Transform(T7,aaT7))
        self.wait(1)

def param_surface(u, v):
    x = u
    y = v
    z = 0.1*((5*x+y-11)**2)
    return z
def pf(k,b):
    return 5*k+b
def C(k,b):
    return 0.5*((5*k+b-11)**2)
def DC_DK(f):
    return (f-11)*5
def DC_DB(f):
    return (f-11)
class s2_3d(ThreeDScene):
    def construct(self):
        resolution_fa = 8
        self.set_camera_orientation(phi=60 * DEGREES, theta=(60-140) * DEGREES)
        axes = ThreeDAxes(x_range=(-10, 10, 20), y_range=(-10, 10, 20), z_range=(-100, 100, 20),axis_config={"color":BLACK})
        label = axes.get_axis_labels(x_label=Tex("$$k$$",color=RED),y_label=Tex("$$b$$",color=DARK_BLUE),z_label=Tex("$$C$$",color=BLACK))

        surface_plane = Surface(
            lambda u, v: axes.c2p(u, v, param_surface(u,v)),
            resolution=(resolution_fa, resolution_fa),
            v_range=[-10, 10],
            u_range=[-10, 10],
            )
        surface_plane.set_style(fill_opacity=0.5)

        k = 1
        b = 1
        DOT = Dot3D(axes.coords_to_point(k,b,param_surface(k,b)),color=PURE_RED)
        NV_K = Arrow(start=axes.coords_to_point(k,b,param_surface(k,b)),end=axes.coords_to_point(k-(0.2*DC_DK(pf(k,b))),b,param_surface(k,b)),color=RED,buff=0)
        NV_B = Arrow(start=axes.coords_to_point(k,b,param_surface(k,b)),end=axes.coords_to_point(k,b-(0.2*DC_DB(pf(k,b))),param_surface(k,b)),color=DARK_BLUE,buff=0)
        NV_ALL = Arrow(start=axes.coords_to_point(k,b,param_surface(k,b)),end=axes.coords_to_point(k-(0.2*DC_DK(pf(k,b))),b-(0.2*DC_DB(pf(k,b))),param_surface(k,b)),color=BLACK,buff=0)
        line = axes.plot(lambda x:11-(5*x),color=PURE_RED)
        lineK = Arrow(start=axes.coords_to_point(k,b,0),end=axes.coords_to_point(k,0,0),color=BLACK,buff=0)
        lineB = Arrow(start=axes.coords_to_point(k,b,0),end=axes.coords_to_point(0,b,0),color=BLACK,buff=0)
        dotk = Dot3D(axes.coords_to_point(k,0,0),color=BLACK)
        dotb = Dot3D(axes.coords_to_point(0, b, 0), color=BLACK)
        T_K = Tex(r"$$k=1$$",color=RED).next_to(dotk,DOWN)
        T_B = Tex(r"$$b=1$$", color=DARK_BLUE).next_to(dotb,LEFT)
        T_C = Tex(r"$$C=12.5$$",color=PURE_RED).next_to(DOT,RIGHT+UP)

        self.add(axes, surface_plane,label,NV_K,NV_B,DOT,NV_ALL,line,lineB,lineK,dotb,dotk,T_K,T_B,T_C)
        self.wait()
        dt = 1/15
        THETA = (60-140)
        THETA_T = (60-130)
        DTHETA = (THETA_T-THETA)/60

        for i in range(60):
            THETA += DTHETA
            if i%10 == 0:
                F = pf(k,b)
                k = k - (0.01 * DC_DK(F))
                b = b - (0.01 * DC_DB(F))
                NV_K.put_start_and_end_on(start=axes.coords_to_point(k,b,param_surface(k,b)),end=axes.coords_to_point(k-(0.2*DC_DK(pf(k,b))),b,param_surface(k,b)))
                NV_B.put_start_and_end_on(start=axes.coords_to_point(k,b,param_surface(k,b)),end=axes.coords_to_point(k,b-(0.2*DC_DB(pf(k,b))),param_surface(k,b)))
                NV_ALL.put_start_and_end_on(start=axes.coords_to_point(k,b,param_surface(k,b)),end=axes.coords_to_point(k-(0.2*DC_DK(pf(k,b))),b-(0.2*DC_DB(pf(k,b))),param_surface(k,b)))

                lineK.put_start_and_end_on(start=axes.coords_to_point(k, b, 0), end=axes.coords_to_point(k, 0, 0))
                lineB.put_start_and_end_on(start=axes.coords_to_point(k, b, 0), end=axes.coords_to_point(0, b, 0))

                DOT.move_to(axes.coords_to_point(k,b,param_surface(k,b)))

                dotk.move_to(axes.coords_to_point(k, 0, 0))
                dotb.move_to(axes.coords_to_point(0, b, 0))

                self.remove(T_B,T_K,T_C)
                T_C = Tex(r"$$C="+str(C(k,b))+"$$", color=PURE_RED).next_to(DOT, RIGHT + UP)
                T_K = Tex("$$k="+str(k)+"$$", color=RED).next_to(dotk, DOWN)
                T_B = Tex("$$b="+str(b)+"$$", color=DARK_BLUE).next_to(dotb, LEFT)
                self.add(T_B,T_K,T_C)

            self.set_camera_orientation(phi=60 * DEGREES, theta=THETA * DEGREES)
            self.wait(dt)
        self.wait(1)

class s2_f(Scene):
    def construct(self):
        T_F = Tex(r"$$\text{f}(5)$$",color=BLACK)
        T_E5 = Tex(r"$$=5$$",color=BLACK)
        T_KK = Tex(r"$$k$$",color=RED)
        T_PLUS = Tex(r"$$+$$",color=BLACK)
        T_BB = Tex(r"$$b$$", color=BLUE)
        V_F = VGroup(T_F,T_E5,T_KK,T_PLUS,T_BB).arrange(RIGHT)
        T_5 = Tex("$$=5$$",color=BLACK)
        T_TIMES = Tex(r"$$\cdot$$",color=BLACK)
        T_K = Tex("$$1.8036476056$$",color=RED)
        T_ADD = Tex("$$+$$",color=BLACK)
        T_B = Tex("$$1.16072952112$$",color=BLUE)
        T_R = Tex("$$=10.17896754912$$",color=BLACK)
        V1 = VGroup(T_5,T_TIMES,T_K).arrange(RIGHT)
        V2 = VGroup(T_ADD,T_B).arrange(RIGHT)
        V3 = VGroup(V_F,V1,V2,T_R).arrange(DOWN)
        self.wait(1)
        self.play(Write(V3))
        self.wait(1)

class Neuron:
    def __init__(self,lightness):
        self.lightness = lightness
        self.graph = Circle(radius=0.25,color=BLACK,fill_color=BLACK,fill_opacity=lightness)
class Layer:
    def __init__(self,neuronsNumber):
        self.neurons = [Neuron(0) for i in range(neuronsNumber)]
        self.neuronsNumber = neuronsNumber
class CNN:
    def __init__(self,numbers):
        self.numbers = numbers
        self.layers = [Layer(i) for i in numbers]
        NeuronGraphs = VGroup(*[VGroup(*[j.graph for j in i.neurons]).arrange(DOWN) for i in self.layers]).arrange(RIGHT,buff=1)
        self.Lines = []
        is_first_layer = True
        lastLayer = self.layers[0]
        self.layersNumber = 0
        for i in self.layers:
            if is_first_layer:
                is_first_layer = False
                lastLayer = i
                self.layersNumber += 1
            else:
                for j in i.neurons:
                    for k in lastLayer.neurons:
                        R =random.random()
                        self.Lines.append(Line(start=j.graph.get_corner(LEFT),end=k.graph.get_corner(RIGHT),color=BLACK))
                lastLayer = i
                self.layersNumber += 1
        LINE = VGroup(*self.Lines)
        self.graph = VGroup(NeuronGraphs,LINE)
    def forward(self,whereLayer,whereNeuron):
        weight = [[[float(0) for k in range(self.layers[i-1].neuronsNumber)]for j in range(self.layers[i].neuronsNumber)]for i in range(1,self.layersNumber)]
        for layer in range(whereLayer+1,self.layersNumber):
            for i in range(self.layers[layer].neuronsNumber):
                if layer == whereLayer+1:
                    weight[layer-1][i][whereNeuron] = 1
                else:
                    for j in range(self.layers[layer-1].neuronsNumber):
                        weight[layer - 1][i][j] = 1


        NeuronGraphs = VGroup(*[VGroup(*[j.graph for j in i.neurons]).arrange(DOWN) for i in self.layers]).arrange(
            RIGHT, buff=1)
        self.Lines = []
        is_first_layer = True
        lastLayer = self.layers[0]
        self.layersNumber = 0
        for i in self.layers:
            if is_first_layer:
                is_first_layer = False
                lastLayer = i
                self.layersNumber += 1
            else:
                for j in i.neurons:
                    for k in lastLayer.neurons:
                        self.Lines.append(
                            Line(start=j.graph.get_corner(LEFT), end=k.graph.get_corner(RIGHT), color=ManimColor([float(weight[self.layers.index(i)-1][i.neurons.index(j)][lastLayer.neurons.index(k)]),float(0),float(0)])))
                lastLayer = i
                self.layersNumber += 1
        LINE = VGroup(*self.Lines)
        self.graph = VGroup(NeuronGraphs, LINE)

    def accept(self,whereLayer,whereNeuron):
        weight = [[[float(0) for k in range(self.layers[i-1].neuronsNumber)]for j in range(self.layers[i].neuronsNumber)]for i in range(1,self.layersNumber)]
        for i in range(self.layers[whereLayer+1].neuronsNumber):
            weight[whereLayer][i][whereNeuron] = float(1)
        for i in range(self.layers[whereLayer-1].neuronsNumber):
            weight[whereLayer-1][whereNeuron][i] = float(1)

        NeuronGraphs = VGroup(*[VGroup(*[j.graph for j in i.neurons]).arrange(DOWN) for i in self.layers]).arrange(
            RIGHT, buff=1)
        self.Lines = []
        is_first_layer = True
        lastLayer = self.layers[0]
        self.layersNumber = 0
        for i in self.layers:
            if is_first_layer:
                is_first_layer = False
                lastLayer = i
                self.layersNumber += 1
            else:
                for j in i.neurons:
                    for k in lastLayer.neurons:
                        self.Lines.append(
                            Line(start=j.graph.get_corner(LEFT), end=k.graph.get_corner(RIGHT), color=ManimColor([float(weight[self.layers.index(i)-1][i.neurons.index(j)][lastLayer.neurons.index(k)]),float(0),float(0)])))
                lastLayer = i
                self.layersNumber += 1
        LINE = VGroup(*self.Lines)
        self.graph = VGroup(NeuronGraphs, LINE)

    def backward(self,whereLayer,whereNeuron):
        weight = [[[float(0) for k in range(self.layers[i-1].neuronsNumber)]for j in range(self.layers[i].neuronsNumber)]for i in range(1,self.layersNumber)]
        for i in range(self.layers[whereLayer-1].neuronsNumber):
            weight[whereLayer-1][whereNeuron][i] = float(1)

        NeuronGraphs = VGroup(*[VGroup(*[j.graph for j in i.neurons]).arrange(DOWN) for i in self.layers]).arrange(
            RIGHT, buff=1)
        self.Lines = []
        is_first_layer = True
        lastLayer = self.layers[0]
        self.layersNumber = 0
        for i in self.layers:
            if is_first_layer:
                is_first_layer = False
                lastLayer = i
                self.layersNumber += 1
            else:
                for j in i.neurons:
                    for k in lastLayer.neurons:
                        self.Lines.append(
                            Line(start=j.graph.get_corner(LEFT), end=k.graph.get_corner(RIGHT), color=ManimColor([float(weight[self.layers.index(i)-1][i.neurons.index(j)][lastLayer.neurons.index(k)]),float(0),float(0)])))
                lastLayer = i
                self.layersNumber += 1
        LINE = VGroup(*self.Lines)
        self.graph = VGroup(NeuronGraphs, LINE)



class s3__(Scene):
    def construct(self):
        NImage = ImageMobject("1.png")
        self.wait(1)
        self.play(FadeIn(NImage))
        self.wait(1)
        cnn = CNN(numbers=[5,1,3])
        Gcnn = cnn.graph
        self.play(FadeOut(NImage),FadeIn(Gcnn))
        self.wait(1)
        cnn = CNN(numbers=[6,3,5,4,2])
        aGcnn = cnn.graph
        self.play(Transform(Gcnn,aGcnn))
        self.wait(1)
        cnn = CNN(numbers=[3,2])
        aGcnn = cnn.graph
        self.play(Transform(Gcnn, aGcnn))
        self.wait(1)
        G1 = VGroup(*[Tex("$$a_"+str(i)+"$$",color=BLACK)for i in range(1,3)],Tex("$$...$$",color=BLACK),Tex("$$a_i$$",color=BLACK),Tex("$$...$$",color=BLACK),Tex("$$a_n$$",color=BLACK)).arrange(DOWN)
        G2 = VGroup(*[Tex("$$a'_"+str(i)+"$$",color=BLACK)for i in range(1,2)],Tex("$$...$$",color=BLACK),Tex("$$a'_j$$",color=BLACK),Tex("$$...$$",color=BLACK),Tex("$$a'_m$$",color=BLACK)).arrange(DOWN)
        GF = VGroup(G1,G2).arrange(RIGHT,buff=1)
        self.play(Transform(Gcnn,GF))
        self.wait(1)
        aGF = VGroup(Tex(r"$$\mathbf{a}$$",color=BLACK),Tex(r"$$\mathbf{a'}$$",color=BLACK)).arrange(RIGHT,buff=1)
        self.play(Transform(Gcnn,aGF))
        self.wait(1)
        aGF = Tex(r"$$\mathbf{a'}_j=\sum{\mathbf{a}_i}$$",color=BLACK)
        self.play(Transform(Gcnn,aGF))
        self.wait(1)
        T_WEIGHT = VGroup(Text("权重", color=BLACK), Tex(r"$$\text{Weight}$$", color=BLACK)).arrange(
            DOWN).to_edge(DOWN)
        aGF = Tex(r"$$\mathbf{a'}_j=\sum{\mathbf{W}_{ij}\mathbf{a}_i}$$",color=BLACK)
        self.play(Transform(Gcnn, aGF),Write(T_WEIGHT))
        self.wait(1)
        aGF = Tex(r"$$\mathbf{a'}_j=\mathbf{W}_{j}\cdot\mathbf{a}$$",color=BLACK)
        self.play(Transform(Gcnn, aGF),FadeOut(T_WEIGHT))
        self.wait(1)
        aGF = Tex(r"$$\mathbf{a'}=\mathbf{W}\mathbf{a}$$", color=BLACK)
        self.play(Transform(Gcnn, aGF))
        self.wait(1)

        self.play(Gcnn.animate.to_edge(UP))
        T_WHATMEANA = Tex(r"$$\mathbf{a}=\begin{bmatrix}\mathbf{a}_1\\\mathbf{a}_2\\\end{bmatrix}$$",
                         color=BLACK).next_to(Gcnn,DOWN).to_edge(LEFT)
        self.play(Write(T_WHATMEANA))
        self.wait(1)
        T_WHATMEANA2 = Tex(r"$$\mathbf{a'}=\begin{bmatrix}\mathbf{a'}_1\\\mathbf{a'}_2\\\mathbf{a'}_3\\\end{bmatrix}$$",color=BLACK).next_to(T_WHATMEANA,DOWN,aligned_edge=LEFT)
        self.play(Write(T_WHATMEANA2))
        self.wait(1)
        T_WHATMEANW = Tex(r"$$\mathbf{W}=\begin{bmatrix}\mathbf{W}_{11},\mathbf{W}_{12}\\\mathbf{W}_{21},\mathbf{W}_{22}\\\mathbf{W}_{31},\mathbf{W}_{32}\\\end{bmatrix}$$",color=BLACK).next_to(T_WHATMEANA2,DOWN,aligned_edge=LEFT)
        self.play(Write(T_WHATMEANW))
        self.wait(1)
        T_WHATMEAN = Tex(r"$$\mathbf{Wa}=\begin{bmatrix}\mathbf{W}_{11},\mathbf{W}_{12}\\\mathbf{W}_{21},\mathbf{W}_{22}\\\mathbf{W}_{31},\mathbf{W}_{32}\\\end{bmatrix}\begin{bmatrix}\mathbf{a}_1\\\mathbf{a}_2\\\end{bmatrix}=\left[ \begin{array}{c}\mathbf{W}_{11}\mathbf{a}_1+\mathbf{W}_{12}\mathbf{a}_2\\\mathbf{W}_{21}\mathbf{a}_1+\mathbf{W}_{22}\mathbf{a}_2\\\mathbf{W}_{31}\mathbf{a}_1+\mathbf{W}_{32}\mathbf{a}_2\\\end{array} \right] $$",color=RED).next_to(T_WHATMEANW,DOWN,aligned_edge=LEFT)
        self.play(Write(T_WHATMEAN))
        self.wait(1)

        aGF = Tex(r"$$\mathbf{a'}_j=\sum{\mathbf{W}_{ij}\mathbf{a}_i}$$", color=BLACK)
        self.play(Transform(Gcnn, aGF),FadeOut(T_WHATMEANW,T_WHATMEAN,T_WHATMEANA,T_WHATMEANA2))
        self.wait(1)
        aGF = Tex(r"$$\mathbf{a'}=\mathbf{W}\mathbf{a}$$", color=BLACK)
        self.play(Transform(Gcnn, aGF))
        self.wait(1)
        aGF = Tex(r"$$\mathbf{a'}_j=\sum{\mathbf{W}_{ij}\mathbf{a}_i}$$", color=BLACK)
        self.play(Transform(Gcnn, aGF))
        self.wait(1)
        aGF = Tex(r"$$\mathbf{a'}_j=\sum{\mathbf{W}_{ij}\mathbf{a}_i}+\mathbf{b}_j$$", color=BLACK)
        T_BIAS = VGroup(Text("偏置",color=BLACK),Tex(r"$$\text{Bias}$$",color=BLACK)).arrange(DOWN).to_edge(DOWN)
        self.play(Transform(Gcnn, aGF),Write(T_BIAS))
        self.wait(1)
        aT1 = Tex(r"$$\mathbf{a'}_j=$$", color=BLACK)
        aT2 = Tex(r"$$\sigma$$", color=RED)
        aT3 = Tex(r"$$($$",color=BLACK)
        aT4 = Tex(r"$$\sum{\mathbf{W}_{ij}\mathbf{a}_i}+\mathbf{b}_j$$", color=BLACK)
        aT5 = Tex(r"$$)$$",color=BLACK)
        aV = VGroup(aT1,aT4).arrange(RIGHT)
        self.add(aT1,aT4)
        self.remove(Gcnn)
        axes = Axes(x_range=[-2,2,1],y_range=[-2,2,1],x_length=5,y_length=5,axis_config={"color":BLACK,"include_numbers":True}).to_corner(RIGHT+UP)
        for number in axes.x_axis.numbers:
            number.set_color(BLACK)
        for number in axes.y_axis.numbers:
            number.set_color(BLACK)
        graph_sigmoid = axes.plot(lambda x:1/(1+math.exp(-x)),color=RED)
        AaT1 = Tex(r"$$\mathbf{a'}_j=$$", color=BLACK)
        AaT2 = Tex(r"$$\sigma$$", color=RED)
        AaT3 = Tex(r"$$($$", color=BLACK)
        AaT4 = Tex(r"$$\sum{\mathbf{W}_{ij}\mathbf{a}_i}+\mathbf{b}_j$$", color=BLACK)
        AaT5 = Tex(r"$$)$$", color=BLACK)
        aV = VGroup(AaT1,aT2,aT3, AaT4,aT5).arrange(RIGHT)
        T_FES = Tex(r"$$\sigma \left( x \right) =\frac{1}{1+e^{-x}},\sigma \left( x \right) \in \left( 0,1 \right) $$",color=RED).to_corner(LEFT+UP)
        self.play(Transform(aT1,AaT1),Transform(aT4,AaT4),FadeIn(aT2,aT3,aT5),Write(T_FES),Create(graph_sigmoid),Create(axes),FadeOut(T_BIAS))
        self.wait(1)
        graph_tanh = axes.plot(lambda x: math.tanh(x), color=BLUE)
        AaT2 = Tex(r"$$\text{tanh}$$", color=BLUE)
        aV = VGroup(AaT1, AaT2, AaT3, AaT4, AaT5).arrange(RIGHT)
        T_FET = Tex(r"$$\text{tanh} \left( x \right) =\frac{e^{x}-e^{-x}}{e^{x}+e^{-x}},\text{tanh} \left( x \right) \in \left( -1,1 \right) $$",
                    color=BLUE).to_corner(LEFT + UP)
        self.play(Transform(aT1, AaT1), Transform(aT4, AaT4), Transform(aT2,AaT2),Transform(aT3,AaT3),Transform(aT5,AaT5), Transform(T_FES,T_FET),
                  Uncreate(graph_sigmoid),Create(graph_tanh))
        self.wait(1)
        def ReLU(x):
            if x > 0:
                return x
            else:
                return 0
        graph_relu = axes.plot(lambda x:ReLU(x), color=PURE_RED)
        AaT2 = Tex(r"$$\text{ReLU}$$", color=PURE_RED)
        aV = VGroup(AaT1, AaT2, AaT3, AaT4, AaT5).arrange(RIGHT)
        T_FER = Tex(
            r"$$\text{ReLU} \left( x \right) =MAX(0,x)$$",
            color=PURE_RED).to_corner(LEFT + UP)
        self.play(Transform(aT1, AaT1), Transform(aT4, AaT4), Transform(aT2, AaT2), Transform(aT3, AaT3),
                  Transform(aT5, AaT5), Transform(T_FES, T_FER),
                  Uncreate(graph_tanh), Create(graph_relu))
        self.wait(1)
        T_AFNOTICE = VGroup(Text("激活函数",color=BLACK),Tex(r"$$\text{Activation Function}$$",color=BLACK)).arrange(DOWN).to_edge(DOWN)
        AaT2 = Tex(r"$$\text{f}$$",color=RED)
        aV = VGroup(AaT1, AaT2, AaT3, AaT4, AaT5).arrange(RIGHT)
        self.play(Transform(aT1, AaT1), Transform(aT4, AaT4), Transform(aT2, AaT2), Transform(aT3, AaT3),
                  Transform(aT5, AaT5), Transform(T_FES, T_FER),
                  FadeOut(graph_relu,axes,T_FES),Write(T_AFNOTICE))
        self.wait(1)
        AaT1 = Tex(r"$$\mathbf{a}_{(l)j}=$$", color=BLACK)
        AaT4 = Tex(r"$$\sum{\mathbf{W}_{(l)ij}\mathbf{a}_{(l-1)i}+\mathbf{b}_{(l)j}}$$", color=BLACK)
        aV = VGroup(AaT1, AaT2, AaT3, AaT4, AaT5).arrange(RIGHT)
        self.play(Transform(aT1, AaT1), Transform(aT4, AaT4), Transform(aT2, AaT2), Transform(aT3, AaT3),
                  Transform(aT5, AaT5),FadeOut(T_AFNOTICE))
        self.wait(1)
        AaT1 = Tex(r"$$\mathbf{a}_{(l)j}=$$", color=BLACK,fill_opacity=0.2)
        AaT2 = Tex(r"$$\text{f}$$",color=RED,fill_opacity=0.2)
        AaT3 = Tex(r"$$($$", color=BLACK,fill_opacity=0.2)
        AaT4 = Tex(r"$$\sum{\mathbf{W}_{(l)ij}\mathbf{a}_{(l-1)i}+\mathbf{b}_{(l)j}}$$", color=BLACK,fill_opacity=0.2)
        AaT5 = Tex(r"$$)$$", color=BLACK,fill_opacity=0.2)
        aV = VGroup(AaT1, AaT2, AaT3, AaT4, AaT5).arrange(RIGHT)
        CGNN = CNN(numbers=[6,4,5,2,3]).graph
        T_INPUT = VGroup(Text("输入",color=RED),Tex(r"$$\text{Input Layer}$$",color=RED)).arrange(DOWN).next_to(CGNN,LEFT)
        T_HIDEN = VGroup(Text("隐层",color=BLUE),Tex(r"$$\text{Hiden Layer}$$",color=BLUE)).arrange(DOWN).next_to(CGNN,DOWN)
        T_OUTPUT = VGroup(Text("输出",color=RED),Tex(r"$$\text{Output Layer}$$",color=RED)).arrange(DOWN).next_to(CGNN,RIGHT)
        self.play(Transform(aT1, AaT1), Transform(aT4, AaT4), Transform(aT2, AaT2), Transform(aT3, AaT3),
                  Transform(aT5, AaT5),Create(CGNN),Write(T_INPUT),Write(T_HIDEN),Write(T_OUTPUT))
        self.wait(1)
        AaT4 = VGroup(Tex(r"$$\mathbf{W}$$", color=PURE_RED,font_size=100),Tex(r"$$\mathbf{b}$$", color=BLUE,font_size=100)).arrange(RIGHT,buff=1).to_edge(UP)
        self.play(Transform(aT4, AaT4))
        self.wait(1)
        AaT1 = Tex(r"$$\mathbf{a}_{(l)}=$$", color=BLACK)
        AaT2 = Tex(r"$$\text{f}$$", color=RED)
        AaT3 = Tex(r"$$($$", color=BLACK)
        AaT4 = Tex(r"$$\mathbf{W}_{(l)}\mathbf{a}_{(l-1)}+\mathbf{b}_{(l)}$$", color=BLACK)
        AaT5 = Tex(r"$$)$$", color=BLACK)
        aV = VGroup(AaT1, AaT2, AaT3, AaT4, AaT5).arrange(RIGHT)
        self.play(Transform(aT1, AaT1), Transform(aT4, AaT4), Transform(aT2, AaT2), Transform(aT3, AaT3),
                  Transform(aT5, AaT5),FadeOut(CGNN,T_INPUT,T_HIDEN,T_OUTPUT))
        self.wait(1)
        AaT4 = VGroup(Tex(r"$$\mathbf{W}$$", color=PURE_RED,font_size=100),Tex(r"$$\mathbf{b}$$", color=BLUE,font_size=100)).arrange(RIGHT,buff=1).to_edge(UP)
        self.play(Transform(aT4, AaT4), FadeOut(aT1,aT2,aT3,aT5))
        self.wait(1)
        self.play(FadeOut(aT4))
        T__L2 = Tex(r"$$\mathbf{a}_{(2)}$$",color=BLACK)
        T__E = Tex(r"$$=$$",color=BLACK)
        T__R = Tex(r"$$\mathbf{W}_{(2)}\mathbf{a}_{(1)}$$",color=BLACK)
        V__E = VGroup(T__L2,T__E,T__R).arrange(RIGHT)
        self.play(Write(T__L2),Write(T__E),Write(T__R))
        self.wait(1)
        aT__R = Tex(r"$$\mathbf{W}_{(2)}\mathbf{a}_{(1)}$$", color=BLACK)
        aT__E = Tex(r"$$=$$", color=BLACK)
        aT__L2 = Tex(r"$$a_{(" + str(2) + ")}$$", color=BLACK)
        for i in range(3,8):
            aT__L2 = Tex(r"$$a_{("+str(i)+")}$$", color=BLACK)
            aT__R = VGroup(Tex(r"$$\mathbf{W}_{("+str(i)+")}$$",color=BLACK),aT__R).arrange(RIGHT)
            aV__E = VGroup(aT__L2, aT__E, aT__R).arrange(RIGHT)
            self.play(Transform(T__L2,aT__L2),Transform(T__E,aT__E),Transform(T__R,aT__R))
            self.wait(1)
        V__E = VGroup(aT__L2,aT__E,aT__R)
        self.add(V__E)
        self.remove(T__L2,T__E,T__R)
        T__FINAL = Tex(r"$$\mathbf{a}_{(L)}=\mathbf{W}_{(L)}\mathbf{W}_{(L-1)}...\mathbf{W}_{(2)}\mathbf{a}_{(1)}$$",color=BLACK)
        self.play(Transform(V__E,T__FINAL))
        self.wait(1)
        T_F1 = Tex(r"$$\mathbf{a}_{(L)}=$$",color=BLACK)
        T_F2 = Tex(r"$$\left(\mathbf{W}_{(L)}\mathbf{W}_{(L-1)}...\mathbf{W}_{(2)}\right)$$",color=BLACK)
        T_F3 = Tex(r"$$\mathbf{a}_{(1)}$$",color=BLACK)
        self.play(Transform(V__E, VGroup(T_F1,T_F2,T_F3).arrange(RIGHT)))
        self.wait(1)
        self.remove(V__E)
        self.add(T_F1,T_F2,T_F3)
        aT_F1 = Tex(r"$$\mathbf{a}_{(L)}=$$", color=BLACK)
        aT_F2 = Tex(r"$$\mathbf{W}_{OVERALL}$$", color=BLACK)
        aT_F3 = Tex(r"$$\mathbf{a}_{(1)}$$", color=BLACK)
        VGroup(aT_F1, aT_F2, aT_F3).arrange(RIGHT)
        self.play(Transform(T_F1,aT_F1),Transform(T_F2,aT_F2),Transform(T_F3,aT_F3))
        self.wait(1)
        self.play(FadeOut(T_F1,T_F2,T_F3))
        self.wait(1)

class s3_part_2(Scene):
    def construct(self):
        numberplane = NumberPlane(axis_config={"color":BLACK})
        self.wait(1)
        self.play(FadeIn(numberplane))
        self.wait(1)
        VEC_A = Vector([1,2],color=RED)
        T_VEC_A = Tex(r"$$\mathbf{a}$$",color=RED).next_to(VEC_A,RIGHT+UP)
        self.play(Create(VEC_A),Write(T_VEC_A))
        self.wait(1)
        ARRAY_A = numpy.array([1,2])
        ARRAY_W = numpy.array([[2,1],[1,1.5]])
        aVEC_A = Vector(numpy.dot(ARRAY_W,ARRAY_A), color=RED)
        aT_VEC_A = Tex(r"$$\mathbf{W}\mathbf{a}$$", color=RED).next_to(aVEC_A, RIGHT,aligned_edge=UP)
        self.play(Transform(VEC_A,aVEC_A),Transform(T_VEC_A,aT_VEC_A))
        self.wait(1)
        self.play(FadeOut(VEC_A,T_VEC_A))
        self.wait(1)
        VEC_A = Vector([1, 2], color=RED)
        T_VEC_A = Tex(r"$$\mathbf{a}$$", color=RED).next_to(VEC_A, RIGHT + UP)
        self.play(Create(VEC_A), Write(T_VEC_A))
        self.wait(1)

        VEC_I = Vector([1, 0], color=BLACK)
        VEC_J = Vector([0, 1], color=BLACK)
        self.play(Create(VEC_I),Create(VEC_J))
        self.wait(1)

        aVEC_A = Vector(numpy.dot(ARRAY_W, ARRAY_A), color=RED)
        aT_VEC_A = Tex(r"$$\mathbf{W}\mathbf{a}$$", color=RED).next_to(aVEC_A,  RIGHT,aligned_edge=UP)

        nPPP = NumberPlane(axis_config={"color": GRAY},background_line_style={"stroke_color":YELLOW_D},x_axis_config={"unit_size":math.sqrt(ARRAY_W[0][0]**2+ARRAY_W[0][1]**2),"rotation":math.atan(ARRAY_W[0][1]/ARRAY_W[0][0])},y_axis_config={"unit_size":math.sqrt(ARRAY_W[1][0]**2+ARRAY_W[1][1]**2),"rotation":math.atan(ARRAY_W[1][1]/ARRAY_W[1][0])})
        aRNP = numberplane.copy()
        self.play(Transform(VEC_A, aVEC_A), Transform(T_VEC_A, aT_VEC_A),Transform(aRNP,nPPP),Transform(VEC_I,Vector([2, 1], color=BLACK)),Transform(VEC_J,Vector([1, 1.5], color=BLACK)))

        self.wait(1)
        self.play(FadeOut(VEC_A,T_VEC_A,aRNP,VEC_I,VEC_J))
        self.wait(1)

        V_WANT = Vector([4,4],color=PURE_RED)
        T_WANT = Tex(r"$$\mathbf{T}_a$$", color=PURE_RED).next_to(V_WANT, RIGHT, aligned_edge=UP)
        T_NOTES = Text("此处\"T\"是目标Target的缩写，常用于表示目标值",color=GRAY,font_size=25).to_corner(RIGHT+DOWN)
        VEC_A = Vector([1, 2], color=RED)
        T_VEC_A = Tex(r"$$\mathbf{a}$$", color=RED).next_to(VEC_A, RIGHT + UP)
        VEC_I = Vector([1, 0], color=BLACK)
        VEC_J = Vector([0, 1], color=BLACK)
        V_A_C = Vector([1, 2], color=RED_A)
        self.add(V_A_C)
        self.play(AnimationGroup(Create(VEC_A),Create(V_WANT)),Create(VEC_I),Create(VEC_J),Write(T_VEC_A),Write(T_NOTES),Write(T_WANT))
        self.wait(1)

        aVEC_A = Vector(numpy.dot(ARRAY_W, ARRAY_A), color=RED)
        aT_VEC_A = Tex(r"$$\mathbf{W}_a\mathbf{a}$$", color=RED).next_to(T_WANT,DOWN)

        nPPP = NumberPlane(axis_config={"color": GRAY}, background_line_style={"stroke_color": YELLOW_D},
                           x_axis_config={"unit_size": math.sqrt(ARRAY_W[0][0] ** 2 + ARRAY_W[0][1] ** 2),
                                          "rotation": math.atan(ARRAY_W[0][1] / ARRAY_W[0][0])},
                           y_axis_config={"unit_size": math.sqrt(ARRAY_W[1][0] ** 2 + ARRAY_W[1][1] ** 2),
                                          "rotation": math.atan(ARRAY_W[1][1] / ARRAY_W[1][0])})
        aRNP = numberplane.copy()
        self.play(Transform(VEC_A, aVEC_A), Transform(T_VEC_A, aT_VEC_A), Transform(aRNP, nPPP),
                  Transform(VEC_I, Vector([2, 1], color=BLACK)), Transform(VEC_J, Vector([1, 1.5], color=BLACK)),FadeOut(T_NOTES))
        self.wait(1)
        V_WANT_B = Vector([3,-2],color=PURE_BLUE)
        V_B = Vector([-2, 1], color=BLUE)
        V_B_C = Vector([-2, 1], color=BLUE_A)
        T_WANT_B = Tex(r"$$\mathbf{T}_b$$", color=PURE_BLUE).next_to(V_WANT_B, RIGHT+DOWN)
        T_V_B = Tex(r"$$\mathbf{b}$$", color=BLUE).next_to(V_B, RIGHT + DOWN)
        self.add(V_B_C)
        self.play(AnimationGroup(Create(V_B), Create(V_WANT_B)), Write(T_V_B),Write(T_WANT_B))
        self.wait(1)
        aVEC_B = Vector(numpy.dot(ARRAY_W, numpy.array([-2,1])), color=BLUE)
        aT_VEC_B = Tex(r"$$\mathbf{W}_a\mathbf{b}$$", color=BLUE).next_to(aVEC_B, LEFT+DOWN)

        aVEC_A = Vector([1,2],color=RED)
        aT_VEC_A = Tex(r"$$\mathbf{W}_a\mathbf{a}$$", color=RED).next_to(aVEC_A, RIGHT+UP)
        self.play(Transform(V_B,aVEC_B),Transform(T_V_B,aT_VEC_B))
        self.wait(1)

        self.play(FadeOut(aRNP),Transform(V_B,Vector([-2, 1], color=BLUE)),Transform(VEC_A,aVEC_A),Transform(T_VEC_A,Tex(r"$$\mathbf{a}$$", color=RED).next_to(V_A_C, RIGHT + UP)),Transform(T_V_B,Tex(r"$$\mathbf{b}$$", color=BLUE).next_to(V_B_C, RIGHT + DOWN)),Transform(VEC_I,Vector([1, 0], color=BLACK)),Transform(VEC_J,Vector([0, 1], color=BLACK)))
        self.wait(1)

        ARRAY_WB = [[-0.4,2.2],[1.6,1.2]]

        aRNP = numberplane.copy()
        nPPP = NumberPlane(axis_config={"color": GRAY}, background_line_style={"stroke_color": YELLOW_D},
                           x_axis_config={"unit_size": math.sqrt(ARRAY_WB[0][0] ** 2 + ARRAY_WB[1][0] ** 2),
                                          "rotation": math.atan(ARRAY_WB[1][0] / ARRAY_WB[0][0])},
                           y_axis_config={"unit_size": math.sqrt(ARRAY_WB[0][1] ** 2 + ARRAY_WB[1][1] ** 2),
                                          "rotation": math.atan(ARRAY_WB[1][1] / ARRAY_WB[0][1])})
        aVEC_B = Vector(numpy.dot(ARRAY_WB, numpy.array([-2, 1])), color=BLUE)
        aT_VEC_B = Tex(r"$$\mathbf{W}\mathbf{b}$$", color=BLUE).next_to(T_WANT_B,UP)
        aVEC_A = Vector(numpy.dot(ARRAY_WB, ARRAY_A), color=RED)
        aT_VEC_A = Tex(r"$$\mathbf{W}\mathbf{a}$$", color=RED).next_to(T_WANT, DOWN)
        self.play(Transform(VEC_A, aVEC_A), Transform(T_VEC_A, aT_VEC_A), Transform(V_B, aVEC_B), Transform(T_V_B, aT_VEC_B),Transform(aRNP,nPPP),Transform(VEC_I,Vector([-1, -1], color=BLACK)),Transform(VEC_J,Vector([1, -4], color=BLACK)))
        self.wait(1)
        VEC_C = Vector([-1,2],color=GREEN)
        T_VEC_C_C = Tex(r"$$\mathbf{c}$$",color=GREEN).next_to(VEC_C,LEFT+DOWN)
        VEC_CC = Vector([-1,2],color=GREEN_A)
        V_WANT_C = Vector([4.1889,1.5487],color=PURE_GREEN)
        T_WANT_C = Tex(r"$$\mathbf{T}_c$$", color=PURE_GREEN).next_to(V_WANT_C, RIGHT + UP)
        self.play(Create(VEC_CC),Write(T_VEC_C_C),Create(V_WANT_C),Write(T_WANT_C))
        self.wait(1)
        self.play(Transform(VEC_C,Vector([4.8,0.8],color=GREEN)),Transform(T_VEC_C_C,Tex(r"$$\mathbf{W}\mathbf{c}$$",color=GREEN).next_to(Vector([4.8,0.8],color=GREEN),RIGHT+UP)))
        self.wait(1)

        self.play(FadeOut(aRNP),
                  Transform(T_VEC_A, Tex(r"$$\mathbf{a}$$", color=RED).next_to(V_A_C, RIGHT + UP)),
                  Transform(T_V_B, Tex(r"$$\mathbf{b}$$", color=BLUE).next_to(V_B_C, LEFT + UP)),
                  Transform(T_VEC_C_C, Tex(r"$$\mathbf{c}$$", color=GREEN).next_to(VEC_C, LEFT + UP)),
                  Transform(VEC_I, Vector([1, 0], color=BLACK)), Transform(VEC_J, Vector([0, 1], color=BLACK))
                  ,Transform(V_B,Vector([-2, 1], color=BLUE)),Transform(VEC_A,Vector([1, 2], color=RED)),Transform(VEC_C,Vector([-1, 2], color=GREEN)))

        _T_ALR = Tex(r"$$\mathbf{a}_{(L)}=\mathbf{W}_{(L)}\mathbf{W}_{(L-1)}...\mathbf{W}_{1}\mathbf{a}_{0}=(\mathbf{W}_{(L)}\mathbf{W}_{(L-1)}...\mathbf{W}_{1})\mathbf{a}_{0}$$",color=BLACK).to_corner(LEFT+UP)
        self.play(Write(_T_ALR))
        self.wait(1)
        self.play(Transform(_T_ALR,Tex(r"$$\mathbf{a}_{(2)}=\mathbf{W}_{(2)}\mathbf{W}_{(1)}\mathbf{a}_{(0)}$$",color=BLACK).to_corner(LEFT+UP)))
        self.wait(1)
        _T_F = Tex(r"$$\text{f}\left(x\right)=x$$",color=BLACK).to_corner(RIGHT+UP)
        self.play(Transform(_T_ALR,Tex(r"$$\mathbf{a}_{(2)}=\mathbf{W}_{(2)}\text{f}\left(\mathbf{W}_{(1)}\mathbf{a}_{(0)}\right)$$",color=BLACK).to_corner(LEFT+UP)),Write(_T_F))
        self.wait(1)
        _T_FONV = Tex(r"$$f\left(\left[ \begin{array}{c}v_1\\v_2\\...\\v_n\\\end{array} \right]\right)=\left[ \begin{array}{c}f\left( v_1 \right)\\f\left( v_2 \right)\\...\\f\left( v_n \right)\\\end{array} \right] $$",color=BLACK).next_to(_T_ALR,DOWN,aligned_edge=LEFT)
        self.play(Write(_T_FONV))
        self.wait(1)
        self.play(Transform(_T_ALR,
                            Tex(r"$$\mathbf{a}_{(2)}=\text{f}\left(\mathbf{W}_{(2)}\text{f}\left(\mathbf{W}_{(1)}\mathbf{a}_{(0)}\right)\right)$$",
                                color=BLACK).to_corner(LEFT + UP)),FadeOut(_T_FONV))
        self.wait(1)
        _T_2 = Tex(r"$$=\text{f}\left(\text{f}\left(\mathbf{W}_{(2)}\mathbf{W}_{(1)}\mathbf{a}_{(0)}\right)\right)$$",color=BLACK).next_to(_T_ALR,DOWN,aligned_edge=LEFT)
        _T_3 = Tex(r"$$=\text{f}^{(2)}\left(\mathbf{W}_{(2)}\mathbf{W}_{(1)}\mathbf{a}_{(0)}\right)$$",color=BLACK).next_to(_T_2,DOWN,aligned_edge=LEFT)
        self.play(Write(_T_2),Write(_T_3))
        self.wait(1)

        _T_ATTENTION = Tex(r"$$\mathbf{W}_{(2)}\text{f}\left(\mathbf{W}_{(1)}\mathbf{a}_{(0)}\right)=\text{f}\left(\mathbf{W}_{(2)}\mathbf{W}_{(1)}\mathbf{a}_{(0)}\right)$$",color=BLACK).next_to(_T_3,DOWN,aligned_edge=LEFT)
        self.play(Write(_T_ATTENTION))
        self.wait(1)
        self.play(Transform(_T_ATTENTION,_T_ATTENTION.copy().to_edge(UP)),FadeOut(_T_ALR,_T_2,_T_3),Transform(_T_F,Tex(r"$$\text{f}\left(a+b\right)=\text{f}\left(a\right)+\text{f}\left(b\right)$$$$\text{f}\left(kx\right)=k\text{f}\left(x\right)$$",color=PURE_RED).to_edge(LEFT)))
        self.wait(1)

        self.remove(_T_ATTENTION,_T_F,VEC_I,VEC_J)
        self.wait(1)

        _ARRAY_NBW = [[-0.1151,1.1561],[0.7784,0.7094]]

        def sigmoid(x):
            return 1 / (1 + math.exp(-x))
        def tenS(x):
            return 10 * (-0.5 + sigmoid(x))

        aRNP = NumberPlane(axis_config={"color": GRAY}, background_line_style={"stroke_color": YELLOW_D})
        aRNP.prepare_for_nonlinear_transform()
        self.play(aRNP.animate.apply_complex_function(
            lambda x: tenS(numpy.dot(_ARRAY_NBW, [x.real, x.imag])[0]) + (tenS(numpy.dot(_ARRAY_NBW, [x.real, x.imag])[1]) * 1j)
        ),Transform(T_VEC_C_C,Tex(r"$$\text{f}\left(\mathbf{W}\mathbf{c}\right)$$",color=GREEN).next_to(T_WANT_C,DOWN)),Transform(T_V_B,Tex(r"$$\text{f}\left(\mathbf{W}\mathbf{b}\right)$$",color=BLUE).next_to(T_WANT_B,UP)),Transform(T_VEC_A,Tex(r"$$\text{f}\left(\mathbf{W}\mathbf{a}\right)$$",color=RED).next_to(T_WANT,DOWN)), Transform(VEC_A,Vector([4,4],color=RED)), Transform(V_B,Vector([3,-2],color=BLUE)), Transform(VEC_C,Vector([4.1889,1.5487],color=GREEN)),run_time=3, rate_functions=rush_from)
        self.wait(1)

        self.remove(numberplane,aRNP,T_VEC_C_C,T_VEC_A,T_V_B,VEC_A,V_B,VEC_C,VEC_CC,V_WANT,V_WANT_B,V_WANT_C,T_WANT,T_WANT_B,T_WANT_C,V_A_C,V_B_C)
        self.wait(1)
        T_FINAL_NN = Tex(r"$$\mathbf{a}_{(l)j}=\text{f}\left(\sum_i{\mathbf{W}_{(l)ij}\mathbf{a}_{(l-1)i}}+\mathbf{b}_{(l)j}\right)$$", color=RED)
        self.play(Write(T_FINAL_NN))
        self.wait(1)
        self.play(T_FINAL_NN.animate.scale(0.5).to_edge(UP))
        self.wait(1)
        FS = 20
        TT_C = Tex(r"$$C=\sum_n{\left( a_{\left( L \right) n}-T_n \right) ^2}$$",color=BLACK,font_size=FS).next_to(T_FINAL_NN,DOWN).to_edge(LEFT)
        self.play(Write(TT_C))
        self.wait(1)
        self.play(Transform(TT_C,Tex(r"$$C=\frac{1}{2}\sum_n{\left( a_{\left( L \right) n}-T_n \right) ^2}$$",color=BLACK,font_size=FS).next_to(T_FINAL_NN,DOWN).to_edge(LEFT)))
        self.wait(1)
        TT_C_D_WL = Tex(r"$$\frac{\partial C}{\partial \boldsymbol{W}_{\left( L \right) ij}}$$",color=BLACK,font_size=FS).next_to(TT_C,DOWN,aligned_edge=LEFT)
        TT_C_D_BL = Tex(r"$$\frac{\partial C}{\partial \boldsymbol{b}_{\left( L \right) j}}$$", color=BLACK,font_size=FS).next_to(TT_C_D_WL,DOWN,aligned_edge=LEFT)
        self.play(Write(TT_C_D_WL),Write(TT_C_D_BL))
        self.wait(1)
        aTT_C_D_WL = Tex(r"$$\frac{\partial C}{\partial \boldsymbol{W}_{\left( L \right) ij}}=\frac{\partial C}{\partial \boldsymbol{a}_{\left( L \right) j}}\frac{\partial \boldsymbol{a}_{\left( L \right) j}}{\partial \boldsymbol{W}_{\left( L \right) ij}}=\left( \boldsymbol{a}_{\left( L \right) j}-\boldsymbol{T}_j \right) \text{f}’\left( \sum_i{\boldsymbol{W}_{\left( L \right) ij}\boldsymbol{a}_{\left( L-1 \right) i}+\boldsymbol{b}_{\left( L \right) j}} \right) \boldsymbol{a}_{\left( L-1 \right) i}$$", color=BLACK,font_size=FS).next_to(
            TT_C, DOWN, aligned_edge=LEFT)
        aTT_C_D_BL = Tex(r"$$\frac{\partial C}{\partial \boldsymbol{b}_{\left( L \right) j}}=\frac{\partial C}{\partial \boldsymbol{a}_{\left( L \right) j}}\frac{\partial \boldsymbol{a}_{\left( L \right) j}}{\partial \boldsymbol{b}_{\left( L \right) j}}=\left( \boldsymbol{a}_{\left( L \right) j}-\boldsymbol{T}_j \right) \text{f}’\left( \sum_i{\boldsymbol{W}_{\left( L \right) ij}\boldsymbol{a}_{\left( L-1 \right) i}+\boldsymbol{b}_{\left( L \right) j}} \right) $$", color=BLACK,font_size=FS).next_to(
            TT_C_D_WL, DOWN, aligned_edge=LEFT)
        self.play(Transform(TT_C_D_WL,aTT_C_D_WL),Transform(TT_C_D_BL,aTT_C_D_BL))
        self.wait(1)
        TT_C_D_A_A_D_WB = Tex(r"$$\frac{\partial C}{\partial \boldsymbol{a}_{\left( L \right) j}}=\left( \boldsymbol{a}_{\left( \boldsymbol{L} \right) \boldsymbol{j}}-\boldsymbol{T}_j \right) $$$$\frac{\partial \boldsymbol{a}_{\left( L \right) j}}{\partial \boldsymbol{W}_{\left( L \right) ij}}=\text{f}’\left( \sum_i{\boldsymbol{W}_{\left( L \right) ij}\boldsymbol{a}_{\left( L-1 \right) i}+\boldsymbol{b}_{\left( L \right) j}} \right) \boldsymbol{a}_{\left( L-1 \right) i}$$$$\frac{\partial \boldsymbol{a}_{\left( L \right) j}}{\partial \boldsymbol{b}_{\left( L \right) j}}=\text{f}’\left( \sum_i{\boldsymbol{W}_{\left( L \right) ij}\boldsymbol{a}_{\left( L-1 \right) i}+\boldsymbol{b}_{\left( L \right) j}} \right) $$",color=BLACK,font_size=FS).next_to(TT_C,DOWN,aligned_edge=LEFT)
        aTT_C_D_WL.next_to(TT_C_D_A_A_D_WB,DOWN,aligned_edge=LEFT)
        aTT_C_D_BL.next_to(aTT_C_D_WL, DOWN, aligned_edge=LEFT)
        self.play(Transform(TT_C_D_WL,aTT_C_D_WL),Transform(TT_C_D_BL,aTT_C_D_BL),Write(TT_C_D_A_A_D_WB))
        self.wait(1)
        TT_C_D_ALM1 = Tex(r"$$\frac{\partial C}{\partial \boldsymbol{W}_{\left( L-1 \right) ki}}=\frac{\partial C}{\partial \boldsymbol{a}_{\left( L-1 \right) i}}\frac{\partial \boldsymbol{a}_{\left( L-1 \right) i}}{\partial \boldsymbol{W}_{\left( L-1 \right) ki}}=\frac{\partial C}{\partial \boldsymbol{a}_{\left( L \right) j}}\frac{\partial \boldsymbol{a}_{\left( L \right) j}}{\partial \boldsymbol{a}_{\left( L-1 \right) i}}\frac{\partial \boldsymbol{a}_{\left( L-1 \right) i}}{\partial \boldsymbol{W}_{\left( L-1 \right) ki}}$$$$\frac{\partial C}{\partial \boldsymbol{b}_{\left( L-1 \right) i}}=\frac{\partial C}{\partial \boldsymbol{a}_{\left( L-1 \right) i}}\frac{\partial \boldsymbol{a}_{\left( L-1 \right) i}}{\partial \boldsymbol{b}_{\left( L-1 \right) i}}=\frac{\partial C}{\partial \boldsymbol{a}_{\left( L \right) j}}\frac{\partial \boldsymbol{a}_{\left( L \right) j}}{\partial \boldsymbol{a}_{\left( L-1 \right) i}}\frac{\partial \boldsymbol{a}_{\left( L-1 \right) i}}{\partial \boldsymbol{b}_{\left( L-1 \right) i}}$$",color=BLACK,font_size=FS).next_to(TT_C_D_BL,DOWN,aligned_edge=LEFT)
        self.play(Write(TT_C_D_ALM1))
        self.wait(1)
        aTT_C_D_ALM1 = Tex(r"$$\frac{\partial C}{\partial \boldsymbol{W}_{\left( L-1 \right) ki}}=\frac{\partial C}{\partial \boldsymbol{a}_{\left( L-1 \right) i}}\frac{\partial \boldsymbol{a}_{\left( L-1 \right) i}}{\partial \boldsymbol{W}_{\left( L-1 \right) ki}}=\sum_j{\frac{\partial C}{\partial \boldsymbol{a}_{\left( L \right) j}}\frac{\partial \boldsymbol{a}_{\left( L \right) j}}{\partial \boldsymbol{a}_{\left( L-1 \right) i}}\frac{\partial \boldsymbol{a}_{\left( L-1 \right) i}}{\partial \boldsymbol{W}_{\left( L-1 \right) ki}}}$$$$\frac{\partial C}{\partial \boldsymbol{b}_{\left( L-1 \right) i}}=\frac{\partial C}{\partial \boldsymbol{a}_{\left( L-1 \right) i}}\frac{\partial \boldsymbol{a}_{\left( L-1 \right) i}}{\partial \boldsymbol{b}_{\left( L-1 \right) i}}=\sum_j{\frac{\partial C}{\partial \boldsymbol{a}_{\left( L \right) j}}\frac{\partial \boldsymbol{a}_{\left( L \right) j}}{\partial \boldsymbol{a}_{\left( L-1 \right) i}}\frac{\partial \boldsymbol{a}_{\left( L-1 \right) i}}{\partial \boldsymbol{b}_{\left( L-1 \right) i}}}$$",color=PURE_RED,font_size=FS).next_to(TT_C_D_BL,DOWN,aligned_edge=LEFT)
        self.play(Transform(TT_C_D_ALM1,aTT_C_D_ALM1))
        self.wait(1)
        aTT_C_D_A_A_D_WB = Tex(r"$$\frac{\partial C}{\partial \boldsymbol{a}_{\left( L \right) j}}=\left( \boldsymbol{a}_{\left( \boldsymbol{L} \right) \boldsymbol{j}}-\boldsymbol{T}_j \right) $$$$\frac{\partial \boldsymbol{a}_{\left( L-n+1 \right) k}}{\partial \boldsymbol{a}_{\left( L-n \right) j}}=\text{f}’\left( \sum_j{\boldsymbol{W}_{\left( L-n+1 \right) jk}\boldsymbol{a}_{\left( L-n \right) j}+\boldsymbol{b}_{\left( L-n+1 \right) k}} \right) \boldsymbol{W}_{\left( L-n+1 \right) jk}$$$$\frac{\partial \boldsymbol{a}_{\left( L-n \right) j}}{\partial \boldsymbol{W}_{\left( L-n \right) ij}}=\text{f}’\left( \sum_i{\boldsymbol{W}_{\left( L-n \right) ij}\boldsymbol{a}_{\left( L-n-1 \right) i}+\boldsymbol{b}_{\left( L-n \right) j}} \right) \boldsymbol{a}_{\left( L-n-1 \right) i}$$$$\frac{\partial \boldsymbol{a}_{\left( L-n \right) j}}{\partial \boldsymbol{b}_{\left( L-n \right) j}}=\text{f}’\left( \sum_i{\boldsymbol{W}_{\left( L-n \right) ij}\boldsymbol{a}_{\left( L-n-1 \right) i}+\boldsymbol{b}_{\left( L-n \right) j}} \right) $$",color=PURE_BLUE,font_size=FS).next_to(TT_C,DOWN,aligned_edge=LEFT)
        aTT_C_D_ALM1 = Tex(
            r"$$\frac{\partial C}{\partial \boldsymbol{W}_{\left( L-n \right) ij}}=\frac{\partial C}{\partial \boldsymbol{a}_{\left( L-n \right) j}}\frac{\partial \boldsymbol{a}_{\left( L-n \right) j}}{\partial \boldsymbol{W}_{\left( L-n \right) ij}}=\sum_k{\frac{\partial C}{\partial \boldsymbol{a}_{\left( L-n+1 \right) k}}\frac{\partial \boldsymbol{a}_{\left( L-n+1 \right) k}}{\partial \boldsymbol{a}_{\left( L-n \right) j}}\frac{\partial \boldsymbol{a}_{\left( L-n \right) j}}{\partial \boldsymbol{W}_{\left( L-n \right) ij}}}$$$$\frac{\partial C}{\partial \boldsymbol{b}_{\left( L-n \right) j}}=\frac{\partial C}{\partial \boldsymbol{a}_{\left( L-n \right) j}}\frac{\partial \boldsymbol{a}_{\left( L-n \right) j}}{\partial \boldsymbol{b}_{\left( L-n \right) j}}=\sum_k{\frac{\partial C}{\partial \boldsymbol{a}_{\left( L-n+1 \right) k}}\frac{\partial \boldsymbol{a}_{\left( L-n+1 \right) k}}{\partial \boldsymbol{a}_{\left( L-n \right) j}}\frac{\partial \boldsymbol{a}_{\left( L-n \right) j}}{\partial \boldsymbol{b}_{\left( L-n \right) j}}}$$",
            color=PURE_RED, font_size=FS).next_to(aTT_C_D_A_A_D_WB, DOWN, aligned_edge=LEFT)
        self.play(Transform(TT_C_D_ALM1,aTT_C_D_ALM1),FadeOut(TT_C_D_BL),FadeOut(TT_C_D_WL),Transform(TT_C_D_A_A_D_WB,aTT_C_D_A_A_D_WB))
        self.wait(1)
        TT_NEW_W_B = Tex(r"$$\boldsymbol{W'}=\boldsymbol{W}-r\frac{\partial C}{\partial \boldsymbol{W}}$$$$\boldsymbol{b'}=\boldsymbol{b}-r\frac{\partial C}{\partial \boldsymbol{b}}$$",color=PURE_GREEN,font_size=1.5*FS).next_to(TT_C_D_ALM1,DOWN,aligned_edge=LEFT)
        TT_BPT = VGroup(Text("反向传播",color=BLACK),Tex(r"$$Backpropagation$$",color=BLACK)).arrange(DOWN).to_edge(DOWN)
        self.play(Write(TT_NEW_W_B),Write(TT_BPT))
        self.wait(1)
        aTT_BPT = VGroup(Text("B.P.神经网络",color=BLACK),VGroup(Tex(r"$$\mathbf{B}$$",color=PURE_RED),Tex(r"$$ack$$",color=PURE_RED,font_size=FS),
                                                                 Tex(r"$$\mathbf{P}$$",color=PURE_BLUE),Tex(r"$$ropagation$$",color=PURE_BLUE,font_size=FS),Tex(r"$$\mathbf{N}$$",color=BLACK),Tex(r"$$\mathbf{eural}$$",color=BLACK,font_size=FS),Tex(r"$$\mathbf{N}$$",color=BLACK),Tex(r"$$\mathbf{etwork}$$",font_size=FS,color=BLACK)).arrange(RIGHT,buff=0)).arrange(DOWN).to_edge(DOWN)
        self.play(Transform(TT_BPT,aTT_BPT))
        self.wait(1)
        

class s3__2_G(Scene):
    def construct(self):
        T = Tex(r"$$\mathbf{W}_{(2)}\text{f}\left(\mathbf{W}_{(1)}\mathbf{a}_{(0)}\right)=\text{f}\left(\mathbf{W}_{(2)}\mathbf{W}_{(1)}\mathbf{a}_{(0)}\right)$$",color=BLACK).to_corner(LEFT+UP)
        self.add(T)


class s3_Graphs(Scene):
    def construct(self):
        cnn = CNN(numbers=[6, 3, 5, 4, 2])
        g = cnn.graph
        self.add(g)
        self.wait(1)
        cnn.backward(1,0)
        self.play(Transform(g,cnn.graph))
        self.wait(1)
        for i in range(6):
            cnn = CNN(numbers=[6, 3, 5, 4, 2])
            cnn.forward(0, i)
            self.play(Transform(g, cnn.graph))
            self.wait(1)

class s2_Graphs(Scene):
    def construct(self):
        T = Tex(r"$$\frac{\partial C}{\partial \text{f}}\frac{\partial \text{f}}{\partial k}$$",color=BLACK)
        aT = Tex(r"$$\frac{\partial C}{\partial \text{f}}\frac{\partial \text{f}}{\partial k}$$",color=BLACK)
        T2 = Tex(r"$$\cos\text{45°}=\frac{\sqrt{2}}{2}=\sqrt{\enspace}$$",color=BLACK)
        V = VGroup(aT,T2).arrange(DOWN)
        self.add(V)