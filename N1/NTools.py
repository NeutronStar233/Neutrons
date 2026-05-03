#N1

from manim import *
import numpy as np
import math

config.background_color = ManimColor([250,250,230])
config.frame_width = 16
config.frame_height = 9
config.pixel_width = 1920
config.pixel_height = 1080

class NScene(Scene):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.saying = Text("")
        self.formulae = list()
        self.space = 3
    def say(self,text,*k):
        self.play(FadeOut(self.saying))
        self.saying = Text(text,color=BLACK,font_size=DEFAULT_FONT_SIZE/2).to_edge(DR)
        self.play(Write(self.saying),*k)
        self.wait(self.space)
    def ending(self,text):
        self.play(FadeOut(*self.mobjects))
        t = Text(text,color=BLACK).to_edge(DR)
        self.play(Write(t))
        self.wait(self.space)


def equal_line_notes(l,n=1,c=BLACK):
    l=l.copy()
    p = l.get_center()[:2]
    x1 = np.array([l.get_length(),0])
    x2 = np.array([0,l.get_length()])
    y1 = l.get_start()[:2]-p
    y2 = l.rotate(PI/2,about_point=l.get_center()).get_start()[:2]-p
    W = np.column_stack((y1,y2))@np.linalg.inv(np.column_stack((x1,x2)))
    def f(x):
        return W@x + p
    return VGroup(Line([*f([-0.37*0.5*n+0.37*i,-0.37]),0],[*f([-0.37*0.5*n+0.37*i,0.37]),0],color=c)for i in range(n))

def parallel_line_notes(l,n=1,c=BLACK):
    l = l.copy()
    p = l.get_center()[:2]
    x1 = np.array([l.get_length(), 0])
    x2 = np.array([0, l.get_length()])
    y1 = l.get_start()[:2] - p
    y2 = l.rotate(PI / 2, about_point=l.get_center()).get_start()[:2] - p
    W = np.column_stack((y1, y2)) @ np.linalg.inv(np.column_stack((x1, x2)))
    def f(x):
        return [*(W @ x + p),0]
    def arr(x):
        return VGroup(Line(f([x,0]),f([x+0.37*math.cos(36*DEGREES),0.37*math.sin(36*DEGREES)]),color=c),
                      Line(f([x,0]),f([x+0.37*math.cos(-36*DEGREES),0.37*math.sin(-36*DEGREES)]),color=c))
    return VGroup(arr(-0.37*0.5*n+0.37*i) for i in range(n))

def instant_position_function_of_straight_line(k,o):
    return lambda x:x*k+o

def parallel_line_cross_point_meet_line(l_to_parallel,p_to_cross,l_to_meet,**kwargs):
    k_ltp = (l_to_parallel.get_end()-l_to_parallel.get_start())[:2]
    k_ltm = (l_to_meet.get_end()-l_to_meet.get_start())[:2]
    o_ltm = l_to_meet.get_center()[:2]
    p = p_to_cross.get_center()[:2]
    f = instant_position_function_of_straight_line(k_ltp,p)
    t = (np.linalg.inv(np.column_stack((k_ltp,-k_ltm)))@(o_ltm-p))[0]
    return Line([*p,0],[*f(t),0],**kwargs)
