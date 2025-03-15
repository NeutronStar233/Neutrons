import numpy as np
from manim import *
from math import *

config.background_color = ManimColor([250,250,230])
config.frame_width = 16
config.frame_height = 9
config.pixel_width = 1920
config.pixel_height = 1080

BACKGROUNDCOLOR = ManimColor([250,250,230])

class s1(Scene):
    def construct(self):
        self.wait(1)
        nbp = NumberPlane(axis_config={"color":BLACK})
        circle = Circle(radius=2)
        self.play(Write(nbp))
        self.play(Write(circle))
        self.wait(1)
        t1 = MathTex(r"\mathbf{f}\left(t\right)=\begin{bmatrix}\sin t\\\cos t\end{bmatrix},t\in\left[0,2\pi)",color=BLACK).to_corner(UL)
        def f(t):
            return 2*np.array([cos(t),sin(t),0])
        tr = ValueTracker(0)
        Q_F = always_redraw(lambda:Arrow([0,0,0],f(tr.get_value()),color=RED_E,buff=0))
        Q_F_P = always_redraw(lambda:Dot(f(tr.get_value()),color=RED_E))
        t_change = True
        Q_T_F = always_redraw(lambda:MathTex(r"\mathbf{f}\left("+r"{:.2f}".format(tr.get_value())+r"\right)",color=RED_E).next_to(Q_F_P,UR)
        if t_change else MathTex(r"\mathbf{f}\left(t\right)",color=RED_E).next_to(Q_F_P,UR))
        self.play(Write(Q_F),Write(Q_F_P),Write(t1),FadeIn(Q_T_F))
        self.play(tr.animate.set_value(2*PI),run_time=2)
        self.remove(Q_T_F)
        t_change = False
        Q_T_F = always_redraw(lambda:MathTex(r"\mathbf{f}\left("+r"{:.2f}".format(tr.get_value())+r"\right)",color=RED_E).next_to(Q_F_P,UR)
        if t_change else MathTex(r"\mathbf{f}\left(t\right)",color=RED_E).next_to(Q_F_P,UR))
        self.add(Q_T_F)
        self.wait(1)
        def f_prime(t):
            return 2*np.array([-sin(t),cos(t),0])
        Q_F_Prime = always_redraw(lambda:Arrow(f(tr.get_value()),f(tr.get_value())+f_prime(tr.get_value()),color=BLUE_E,buff=0))
        Q_T_F_Prime = always_redraw(lambda:MathTex(r"\mathbf{f}'\left(t\right)",color=BLUE_E).next_to(Dot(f(tr.get_value())+f_prime(tr.get_value())),UP))
        self.play(Write(Q_F_Prime),Write(Q_T_F_Prime))
        self.play(tr.animate.set_value(30*DEGREES+2*PI))
        self.wait(1)
        Q_R = always_redraw(lambda:Line([0,0,0],f(tr.get_value()),color=RED))
        self.play(Write(Q_R))
        self.wait(1)
        Q_TANGENT_LINE = always_redraw(lambda:Line(f(tr.get_value())+f_prime(tr.get_value())*10,f(tr.get_value())-f_prime(tr.get_value())*10,color=BLUE))
        self.play(Write(Q_TANGENT_LINE))
        self.wait(1)
        Q_ANGLE = always_redraw(lambda:RightAngle(Line(f(tr.get_value())-f_prime(tr.get_value())*10,f(tr.get_value())+f_prime(tr.get_value())*10,color=BLUE),Line(f(tr.get_value()),[0,0,0],color=RED)
                             ,stroke_width=10,color=GREEN))
        self.play(Write(Q_ANGLE))
        self.wait(1)
        t2 = MathTex(r"\mathbf{f}\perp\mathbf{f}'",color=BLACK).next_to(t1,DOWN,aligned_edge=LEFT)
        self.play(Write(t2))
        self.wait(1)

        Q_Nagetive_F_Prime = Arrow(f(tr.get_value()),f(tr.get_value())-f_prime(tr.get_value()),color=GRAY,buff=0)
        self.play(Write(Q_Nagetive_F_Prime))
        self.wait(1)

        self.play(FadeOut(Q_Nagetive_F_Prime))
        self.wait(1)

        Q_F_OD = always_redraw(lambda:VGroup(Line([0,0,0],[2*cos(tr.get_value()),0,0],color=RED,stroke_width=5),Line(f(tr.get_value()),f(tr.get_value())+np.array([0,-2*sin(tr.get_value()),0]),color=BLUE,stroke_width=5)))
        Q_F_Prime_OD = always_redraw(lambda:VGroup(Line(f(tr.get_value())+f_prime(tr.get_value()), f(tr.get_value())+f_prime(tr.get_value())+np.array([2 * sin(tr.get_value()), 0, 0]), color=BLUE_E,stroke_width=5),
                        Line(f(tr.get_value()),f(tr.get_value()) + np.array([0, 2 * cos(tr.get_value()), 0]),
                             color=RED_E,stroke_width=5)))
        self.play(Write(Q_F_OD))
        self.play(Write(Q_F_Prime_OD))
        self.wait(1)

        Q_Triangle_F = always_redraw(lambda:Polygon([0,0,0],f(tr.get_value()),[2*cos(tr.get_value()),0,0],color=RED,fill_opacity=0.2,stroke_opacity=0.2))
        Q_Triangle_F_Prime = always_redraw(lambda :Polygon(f(tr.get_value()),f(tr.get_value())+f_prime(tr.get_value()),f(tr.get_value())+f_prime(tr.get_value())[1]*UP,color=BLUE,fill_opacity=0.2,stroke_opacity=0.2))
        self.play(FadeIn(Q_Triangle_F,Q_Triangle_F_Prime))
        ##Q_Triangle_F_Copy = always_redraw(lambda:Q_Triangle_F.copy().scale(0.5).set_opacity(0.5))
        ##Q_Triangle_F_Prime_Copy = always_redraw(lambda :Q_Triangle_F_Prime.copy().scale(0.5).set_opacity(0.5))
        t_relation = MathTex(r"\sim",color=BLACK)
        VGroup(Q_Triangle_F.copy().scale(0.5).set_opacity(0.5), t_relation,
               Q_Triangle_F_Prime.copy().scale(0.5).set_opacity(0.5)).arrange(RIGHT).next_to(t2, DOWN,
                                                                                             aligned_edge=LEFT)
        t2_p_5 = always_redraw(lambda:VGroup(Q_Triangle_F.copy().scale(0.5).set_opacity(0.5),MathTex(r"\sim",color=BLACK),Q_Triangle_F_Prime.copy().scale(0.5).set_opacity(0.5)).arrange(RIGHT).next_to(t2,DOWN,aligned_edge=LEFT))
        self.play(ReplacementTransform(Q_Triangle_F.copy(),t2_p_5[0]))
        self.play(Write(t_relation))
        self.play(ReplacementTransform(Q_Triangle_F_Prime.copy(), t2_p_5[2]))
        self.wait(1)
        self.remove(t_relation,t2_p_5[0],t2_p_5[2])
        self.add(t2_p_5)

        t3 = MathTex(r"\mathbf{f}=\begin{bmatrix}|XXX|\\|YYY|\end{bmatrix},\mathbf{f}'=\begin{bmatrix}-|YYY|\\|XXX|\end{bmatrix}",color=BLACK).scale(0.75).next_to(t2_p_5,DOWN,aligned_edge=LEFT)
        XXX1 = t3[0][4:7]
        YYY1 = t3[0][9:12]
        XXX2 = t3[0][21:24]
        YYY2 = t3[0][26:29]
        XXX1.fade(1)
        YYY1.fade(1)
        XXX2.fade(1)
        YYY2.fade(1)
        Q_F_1 = always_redraw(lambda:Q_F_OD[0].copy().scale(0.5*0.75).move_to(XXX1.get_center()))
        Q_F_2 = always_redraw(lambda:Q_F_OD[1].copy().scale(0.5*0.75).move_to(YYY1.get_center()))
        Q_F_Prime_1 = always_redraw(lambda:Q_F_Prime_OD[0].copy().scale(0.5*0.75).move_to(XXX2.get_center()))
        Q_F_Prime_2 = always_redraw(lambda:Q_F_Prime_OD[1].copy().scale(0.5*0.75).move_to(YYY2.get_center()))
        self.play(Write(t3),ReplacementTransform(Q_F_OD[0].copy(),Q_F_1)
                  ,ReplacementTransform(Q_F_OD[1].copy(),Q_F_2)
                  ,ReplacementTransform(Q_F_OD[0].copy(),Q_F_Prime_1)
                  ,ReplacementTransform(Q_F_OD[1].copy(),Q_F_Prime_2))
        t4 = MathTex(r"|XX2|=k|XX1|,|YY2|=k|YY1|",color=BLACK).scale(0.75).next_to(t3,DOWN,aligned_edge=LEFT)
        XX1 = t4[0][1:4]
        XX2 = t4[0][8:11]
        YY1 = t4[0][14:17]
        YY2 = t4[0][21:24]
        YY1.fade(1)
        YY2.fade(1)
        XX1.fade(1)
        XX2.fade(1)
        Q_F_1_ = always_redraw(lambda:Q_F_OD[0].copy().scale(0.5 * 0.75).move_to(XX1.get_center()))
        Q_F_2_ = always_redraw(lambda:Q_F_OD[1].copy().scale(0.5 * 0.75).move_to(YY1.get_center()))
        Q_F_Prime_1_ = always_redraw(lambda:Q_F_Prime_OD[0].copy().scale(0.5 * 0.75).move_to(YY2.get_center()))
        Q_F_Prime_2_ = always_redraw(lambda:Q_F_Prime_OD[1].copy().scale(0.5 * 0.75).move_to(XX2.get_center()))
        self.play(Write(t4),ReplacementTransform(Q_F_OD[0].copy(),Q_F_1_)
                  ,ReplacementTransform(Q_F_OD[1].copy(),Q_F_2_)
                  ,ReplacementTransform(Q_F_OD[0].copy(),Q_F_Prime_1_)
                  ,ReplacementTransform(Q_F_OD[1].copy(),Q_F_Prime_2_))
        t5 = MathTex(r"\cos' t=-k\sin t,\sin't = k\cos t",color=BLACK).next_to(t4,DOWN,aligned_edge=LEFT)
        self.play(Write(t5))
        self.wait(1)
        t6 = MathTex(r"k=\frac{|\mathbf{f}'|}{|\mathbf{f}|}",color=BLACK).next_to(t5,DOWN,aligned_edge=LEFT)
        self.play(Write(t6))
        self.wait(1)
        Q_Path = always_redraw(lambda:ParametricFunction(f,t_range=[30*DEGREES+2*PI,tr.get_value()],color=RED_E,stroke_width=10))
        Q_Time = always_redraw(
            lambda: ParametricFunction(lambda t:0.125*f(t), t_range=[30 * DEGREES + 2 * PI, tr.get_value()], color=GREEN_E,
                                       stroke_width=10))
        self.add((Q_Path),Q_Time)
        self.play(tr.animate.set_value(30*DEGREES+4*PI),run_time=4)
        self.wait(1)
        t7 = MathTex(r"\bar{|\mathbf{f}'|}=\frac{2\pi}{2\pi}=1",color=BLACK).to_corner(UR)
        self.play(Write(t7))
        self.wait(1)
        t8 = MathTex(r"\forall a,b,\,|\mathbf{f}'\left(a\right)|=|\mathbf{f}'\left(b\right)|",color=BLACK).next_to(t7,DOWN,aligned_edge=RIGHT)
        self.play(Write(t8))
        self.wait(1)
        t9 = MathTex(r"|\mathbf{f}'|=\bar{|\mathbf{f}'|}=1",color=BLACK).next_to(t8,DOWN,aligned_edge=RIGHT)
        self.play(Write(t9))
        self.wait(1)
        t10 = MathTex(r"k=\frac{|\mathbf{f}'|}{|\mathbf{f}|}=\frac{1}{1}=1",color=BLACK).next_to(t9,DOWN,aligned_edge=RIGHT)
        self.play(Write(t10))
        self.wait(1)
        t11 = MathTex(r"\cos' t=-\sin t,\sin't = \cos t",color=PURE_RED).next_to(t10,DOWN,aligned_edge=RIGHT)
        self.play(Write(t11))
        self.wait(1)

class s1_1(Scene):
    def construct(self):
        self.wait(1)
        t1 = MathTex(r"\tan‘ t=\left(\frac{\sin t}{\cos t}\right)'=\frac{\sin't\cos t-\sin t\cos't}{\cos^2t}",color=BLACK).to_corner(UL)
        self.play(Write(t1))
        t2 = MathTex(r"=\frac{1}{\cos^2t}",color=BLACK).next_to(t1,DOWN,aligned_edge=LEFT)
        self.play(Write(t2))
        self.wait(1)
