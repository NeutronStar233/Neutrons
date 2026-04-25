from manim import *
import math
import numpy as np

config.background_color = ManimColor([250,250,230])
config.frame_width = 16
config.frame_height = 9
config.pixel_width = 1920
config.pixel_height = 1080

class s1(ThreeDScene):#NeutronStar233
    def construct(self):
        self.set_camera_orientation(phi=90*DEGREES)

        l = ValueTracker(2)
        h = ValueTracker(2.5)

        PLANE_A = always_redraw(lambda:Rectangle(height=h.get_value(),width=h.get_value()*2,color=RED,fill_opacity=0.37).rotate(axis=UP,angle=PI/2,about_point=ORIGIN).rotate(axis=RIGHT,angle=PI/2,about_point=ORIGIN).shift(LEFT*l.get_value()))
        t_A = always_redraw(lambda:MathTex("A",color=RED).move_to(PLANE_A.get_center()))
        m = Dot3D(color=BLACK)
        self.add_fixed_orientation_mobjects(t_A)
        self.play(FadeIn(PLANE_A,m,t_A))
        self.wait(1)

        t1 = Text("一张面密度\n处处相等的\n有限平面",color=DARK_GRAY,font_size=DEFAULT_FONT_SIZE/2).next_to(PLANE_A,IN)
        t2 = Text("某质点",color=DARK_GRAY,font_size=DEFAULT_FONT_SIZE/2).next_to(m,OUT+RIGHT)
        self.add_fixed_orientation_mobjects(t1,t2)
        self.play(Write(t1),Write(t2))
        self.wait(1)

        self.play(FadeOut(t1,t2))

        x = ValueTracker(0)
        y = ValueTracker(0)
        s = ValueTracker(0.5)

        r = always_redraw(lambda:Dot3D([x.get_value()*h.get_value(),y.get_value()*h.get_value()*0.5,0],color=RED).rotate(axis=UP,angle=PI/2,about_point=ORIGIN).rotate(axis=RIGHT,angle=PI/2,about_point=ORIGIN).shift(LEFT*l.get_value()))
        ds = always_redraw(lambda:Square(side_length=s.get_value(),color=RED_E,fill_opacity=0.37).move_to([x.get_value()*h.get_value(),y.get_value()*h.get_value()*0.5,0]).rotate(axis=UP,angle=PI/2,about_point=ORIGIN).rotate(axis=RIGHT,angle=PI/2,about_point=ORIGIN).shift(LEFT*l.get_value()))
        self.play(FadeIn(ds))
        t3 = Text("在A上取一块小区域\n显然\n这块区域越是小\n就越是可以将其近似为一个质点",color=DARK_GRAY,font_size=DEFAULT_FONT_SIZE/2).to_corner(DR)
        self.add_fixed_in_frame_mobjects(t3)
        self.move_camera(theta=-30*DEGREES,added_anims=[Write(t3),Succession(AnimationGroup(x.animate.set_value(0.75),y.animate.set_value(0.5)),
                                       AnimationGroup(x.animate.set_value(-0.5),y.animate.set_value(-0.75)))])
        self.wait(1)
        self.move_camera(theta=-60*DEGREES,added_anims=[x.animate.set_value(0.618),y.animate.set_value(0.37),FadeOut(t3)])
        def to_A(_x,_y):
            return Dot3D([_x*h.get_value(),_y*h.get_value()*0.5,0]).rotate(axis=UP,angle=PI/2,about_point=ORIGIN).rotate(axis=RIGHT,angle=PI/2,about_point=ORIGIN).shift(LEFT*l.get_value())
        def to_B(_x,_y):
            return Dot3D([-_x*h.get_value()*4/l.get_value(),-_y*h.get_value()*0.5*4/l.get_value(),0]).rotate(axis=UP,angle=PI/2,about_point=ORIGIN).rotate(axis=RIGHT,angle=PI/2,about_point=ORIGIN).shift(RIGHT*4)

        R = always_redraw(lambda:Dot3D(-4*r.get_center()/l.get_value()))
        dS = always_redraw(lambda:Square(side_length=4*s.get_value()/l.get_value(),color=BLUE_E,fill_opacity=0.37).move_to([-x.get_value()*h.get_value()*4/l.get_value(),-y.get_value()*h.get_value()*0.5*4/l.get_value(),0]).rotate(axis=UP,angle=PI/2,about_point=ORIGIN).rotate(axis=RIGHT,angle=PI/2,about_point=ORIGIN).shift(RIGHT*4))

        L1 =  always_redraw(lambda:DashedLine(start=ds.get_vertices()[1],end=dS.get_vertices()[3],color=BLACK,buff=0))
        L2 = always_redraw(
            lambda: DashedLine(start=ds.get_vertices()[2], end=dS.get_vertices()[0], color=BLACK, buff=0))

        self.play(FadeIn(dS,L1,L2))
        t4 = Text("在质点的另一侧\n作另一块与之面密度相等的小区域\n使之与原来的小区域\n关于给定质点位似",color=DARK_GRAY,font_size=DEFAULT_FONT_SIZE/2).to_corner(DR)
        self.add_fixed_in_frame_mobjects(t4)
        self.play(Write(t4))
        self.wait(2)
        self.play(FadeOut(t4))

        f = always_redraw(lambda:Arrow3D(start=ORIGIN,end=to_A(x.get_value(),y.get_value()).get_center()/math.sqrt(np.dot(to_A(x.get_value(),y.get_value()).get_center(),to_A(x.get_value(),y.get_value()).get_center())),color=PURE_RED))
        F = always_redraw(lambda: Arrow3D(start=ORIGIN, end=to_B(x.get_value(),y.get_value()).get_center()/math.sqrt(np.dot(to_B(x.get_value(),y.get_value()).get_center(),to_B(x.get_value(),y.get_value()).get_center())), color=PURE_BLUE))
        t5  = Text("这些区域越是小\n它们施加于质点的引力方向\n就越是近似于相反",color=DARK_GRAY,font_size=DEFAULT_FONT_SIZE/2).to_corner(DR)
        self.add_fixed_in_frame_mobjects(t5)
        self.play(Write(t5),GrowFromCenter(f),GrowFromCenter(F))
        self.wait(2)
        self.play(ShrinkToCenter(f),ShrinkToCenter(F),FadeOut(t5))
        self.remove(f,F)

        lr = Line3D(start=ORIGIN,end=ds.get_vertices()[2],color=RED)
        lR = Line3D(start=ORIGIN, end=dS.get_vertices()[0], color=BLUE)
        lr2 = Line3D(start=ORIGIN, end=ds.get_vertices()[1], color=MAROON_E)
        lR2 = Line3D(start=ORIGIN, end=dS.get_vertices()[3], color=TEAL_E)
        ls = Line3D(start=ds.get_vertices()[1],end=ds.get_vertices()[2],color=PURE_RED)
        lS = Line3D(start=dS.get_vertices()[3], end=dS.get_vertices()[0], color=PURE_BLUE)

        self.play(FadeIn(lr,lR,lr2,lR2,ls,lS),FadeOut(L1,L2))
        t_r = MathTex("r",color=RED).next_to(lr,IN)
        t_R = MathTex("R", color=BLUE).next_to(lR, OUT)
        t_s = MathTex("s",color=MAROON_E).next_to(ls,DOWN)
        t_S = MathTex("S", color=TEAL_E).next_to(lS, DOWN)
        self.add_fixed_orientation_mobjects(t_r,t_R,t_s,t_S)
        self.play(FadeIn(t_r,t_R,t_s,t_S))

        t6 = Text("根据相似\n我们可以得到这些关系...",color=DARK_GRAY,font_size=DEFAULT_FONT_SIZE/2).to_corner(DR)
        T1 = MathTex(r"r:R=s:S",color=BLACK).to_corner(UL)
        self.add_fixed_in_frame_mobjects(t6,T1)
        self.play(Write(t6),Write(T1))
        self.wait(2)
        self.play(FadeOut(t6))
        t7 = Text("现在设这些区域已经小到了可以视作质点的地步\n而我们知道，质点之间的引力\n正比于其质量\n反比于它们之间距离的平方",color=DARK_GRAY,font_size=DEFAULT_FONT_SIZE/2).to_corner(DR)
        T2 = MathTex(r"f:F=\left(m:M\right)\times \left(R^2:r^2\right)",color=BLACK).next_to(T1,DOWN,aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(t7,T2)
        self.play(Write(t7),Write(T2))
        self.wait(4)

        self.play(FadeOut(t7))
        t8 = Text("而由于它们的面密度相等\n它们的质量之比\n也就如同它们的面积之比\n即边长的平方之比\n也就如同它们到给定质点的距离的平方之比",color=DARK_GRAY,font_size=DEFAULT_FONT_SIZE/2).to_corner(DR)
        T3= MathTex(r"m:M=s^2:S^2=r^2:R^2",color=BLACK).next_to(T2,DOWN,aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(t8,T3)
        self.play(Write(t8),Write(T3))
        self.wait(4)
        self.play(FadeOut(t8))

        t9 = Text("于是可以得出\n这两个区域施加于该质点的引力大小之比为1\n即，相等",color=DARK_GRAY,font_size=DEFAULT_FONT_SIZE/2).to_corner(DR)
        T4 = MathTex(r"f:F=\left(r^2:R^2\right)\times\left(R^2:r^2\right)=1",color=BLACK).next_to(T3,DOWN,aligned_edge=LEFT)
        T5 = MathTex(r"f=F",color=BLACK).next_to(T4,DOWN,aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(t9,T4,T5)
        self.play(Write(t9),Write(T5),Write(T4))
        self.wait(4)
        self.play(FadeOut(t9))

        t10 = Text("而它们的方向相反\n因此，这对区域施加于给定质点的总引力为0",color=DARK_GRAY,font_size=DEFAULT_FONT_SIZE/2).to_corner(DR)
        T6 = MathTex(r"\vec{f}+\vec{F}=\vec{0}",color=BLACK).next_to(T5,DOWN,aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(t10,T6)
        self.play(Write(t10),Write(T6))
        self.wait(4)
        self.play(FadeOut(t10,T1,T2,T3,T4,T5,lr,lR,lr2,lR2,ls,lS,t_r,t_R,t_s,t_S),FadeIn(L2,f,F),T6.animate.to_corner(UL))
        t11 = Text("在原来的平面A上的每一个小区域\n显然都能通过位似\n作出与之对应的在另一侧的另一小区域\n而这样的每一对区域施加的总引力都为0",color=DARK_GRAY,font_size=DEFAULT_FONT_SIZE/2).to_corner(DR)
        self.add_fixed_in_frame_mobjects(t11)
        self.play(x.animate.set_value(0.37),Write(t11))
        self.play(y.animate.set_value(-0.618))
        self.play(x.animate.set_value(-0.37))
        self.play(y.animate.set_value(1))
        self.play(x.animate.set_value(-1),FadeOut(t11))
        t12 = Text("而与平面A上的每个小区域对应的那些小区域\n显然构成了另一个平面，即平面B",color=DARK_GRAY,font_size=DEFAULT_FONT_SIZE/2).to_corner(DR)
        B1 = ValueTracker(0)
        B2 = ValueTracker(0)
        B3 = ValueTracker(0)
        PLANE_B_ = always_redraw(lambda:Polygon(to_B(-1,1).get_center(),
                                                to_B(-1,1-B1.get_value()*2).get_center(),
                                                to_B(-1+B2.get_value()*2,1-B1.get_value()*2).get_center(),
                                                to_B(-1+B2.get_value()*2,1-B1.get_value()*2+B3.get_value()*2).get_center(),color=BLUE,fill_opacity=0.37))
        self.add_fixed_in_frame_mobjects(t12)
        self.play(Write(t12))
        self.add(PLANE_B_)
        self.play(y.animate.set_value(-1),B1.animate.set_value(1))
        self.play(x.animate.set_value(1),B2.animate.set_value(1))
        self.play(y.animate.set_value(1),B3.animate.set_value(1))
        self.play(x.animate.set_value(-1))
        t_B = MathTex("B",color=BLUE).move_to(PLANE_B_.get_center())
        self.add_fixed_orientation_mobjects(t_B)
        self.play(FadeIn(t_B))
        self.play(FadeOut(t12))
        t13 = Text("于是\n平面A和平面B对质点施加的总引力为0\n即平面A施加的引力的大小与平面B所施加的大小相等",color=DARK_GRAY,font_size=DEFAULT_FONT_SIZE/2).to_corner(DR)
        self.add_fixed_in_frame_mobjects(t13)
        self.play(Write(t13))
        self.wait(2)
        self.play(FadeOut(t13,f,F,ds,dS,L2))
        t14 = Text(
            "那么，如果平面B始终不变\n也就是平面A进行任何位似变换后\n得到的那个东西都是完全一样的\n那么，平面A施加于给定质点的引力\n也就与位置无关了",
            color=DARK_GRAY, font_size=DEFAULT_FONT_SIZE / 2).to_corner(DR)
        self.add_fixed_in_frame_mobjects(t14)
        self.play(Write(t14))
        self.play(l.animate.set_value(0.75))
        self.play(l.animate.set_value(4),run_time=2)
        self.play(l.animate.set_value(2),FadeOut(t14))
        t15= Text("所谓位似\n也就是把原来平面的边长乘上一个常数\n于是，如果这个边长乘上任何数所得的结果都一样\n那么这个平面施加于给定质点的引力就与其位置无关了",color=DARK_GRAY,font_size=DEFAULT_FONT_SIZE/2).to_corner(DR)
        T7 = MathTex(r"\forall x\in\left(0,+\infty\right),x\cdot \text{SideLength}_A=\text{Constant}",color=BLACK).next_to(T6,DOWN,aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(t15,T7)
        self.play(Write(t15),Write(T7))
        self.wait(2)
        self.play(FadeOut(t15))
        t16 = Text("这要求这个平面A的边长是0或者无穷大\n反过来，如果一个平面的边长是0或者无穷大\n那么它施加于其外任意一点的引力与其位置无关",color=DARK_GRAY,font_size=DEFAULT_FONT_SIZE/2).to_corner(DR)
        tt1 = Text("（显然引力方向是不变的，再加上引力大小不变，就可以说整个引力矢量不变了）",color=GRAY,font_size=DEFAULT_FONT_SIZE/2).to_corner(UR)
        T8 = MathTex(r"\Rightarrow \text{SideLength}_A =0\,\, \text{or}\,\,\infty",color=BLACK).next_to(T7,DOWN,aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(tt1,T8,t16)
        self.play(Write(t16),Write(T8),FadeIn(tt1))
        self.play(h.animate.set_value(0.25),run_time=2)
        self.play(h.animate.set_value(10),run_time=2)

        self.play(FadeOut(*self.mobjects))

        T_FINISH = Text("这就是所要证明的.",color=BLACK).to_corner(DR)
        self.add_fixed_in_frame_mobjects(T_FINISH)
        self.play(Write(T_FINISH))
        self.wait(2)
        self.play(FadeOut(T_FINISH))
        self.wait(1)#NeutronStar233

class bkg(Scene):
    def construct(self):
        pass
