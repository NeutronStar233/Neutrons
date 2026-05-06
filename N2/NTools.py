###Which N2.py used###
from manim import *
import numpy as np
from manim.utils.color.BS381 import LEAF_BROWN

###NeutronStar233
config.background_color = ManimColor([250,250,230])
config.frame_width = 16
config.frame_height = 9
config.pixel_width = 1920
config.pixel_height = 1080
config.max_files_cached = 370

LEAF_RED = ManimColor([165,42,42])
LEAF_YELLOW =ManimColor([211,177,125])

class NScene(Scene):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.saying = Text("")
        self.formulae = list()
        self.space = 3

    def say(self,text,*k,is_wait=True,is_sequencing=False):
        self.play(FadeOut(self.saying))
        self.saying = VGroup(Text(i,color=BLACK,font_size=DEFAULT_FONT_SIZE/2)for i in text)
        for i in range(len(self.saying)):
            if i == 0:
                self.saying[len(self.saying)-1].to_corner(DR)
            else:
                self.saying[len(self.saying)-1-i].next_to(self.saying[len(self.saying)-i],UP,aligned_edge=RIGHT)
        if not is_sequencing:
            self.play(Write(self.saying),*k)
        else:
            self.play(Write(self.saying), k[0])
            for i in k:
                if i != k[0]:
                    self.play(i)
        if is_wait:
            self.wait(self.space)

    def ending(self,text):
        self.play(FadeOut(*self.mobjects))
        t = Text(text,color=BLACK).to_edge(DR)
        self.play(Write(t))
        self.wait(self.space)


def equal_line_notes(l,n=1,c=BLACK,size=1):
    l=l.copy()
    p = l.get_center()[:2]
    x1 = np.array([l.get_length(),0])
    x2 = np.array([0,l.get_length()])
    y1 = l.get_start()[:2]-p
    y2 = l.rotate(PI/2,about_point=l.get_center()).get_start()[:2]-p
    W = np.column_stack((y1,y2))@np.linalg.inv(np.column_stack((x1,x2)))
    def f(x):
        return W@x + p
    return VGroup(Line([*f([-0.37*0.5*n+0.37*i,-0.37*size]),0],[*f([-0.37*0.5*n+0.37*i,0.37*size]),0],color=c)for i in range(n))

def parallel_line_notes(l,n=1,c=BLACK,size=1):
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
        return VGroup(Line(f([x,0]),f([x+0.37*math.cos(36*DEGREES)*size,0.37*math.sin(36*DEGREES)*size]),color=c),
                      Line(f([x,0]),f([x+0.37*math.cos(-36*DEGREES)*size,0.37*math.sin(-36*DEGREES)*size]),color=c))
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

###Lines
def k_of_(l):
    return (l.get_end()-l.get_start())[:2]
def o_of_(l):
    return l.get_center()[:2]
def ex(p) -> tuple[float,float,float]:
    return [*p,0]
def cross_l(l1,l2):
    k1 = (l1.get_end()-l1.get_start())[:2]
    k2 = (l2.get_end()-l2.get_start())[:2]
    o1 = l1.get_center()[:2]
    o2 = l2.get_center()[:2]
    f1 = instant_position_function_of_straight_line(k1,o1)
    #k1t1 + o1 = k2t2 + o2
    #k1t1 - k2t2 = o2-o1
    #[k1,-k2][t1,t2] =
    #print(k1,k2,o1,o2)
    t1 = (np.linalg.inv(np.column_stack((k1,k2)))@(o2-o1))[0]
    return f1(t1)
def parallel_line_cross_point(l,p,**kwargs):
    return Line(start=p.get_center(),end=p.get_center()+ex(k_of_(l)),**kwargs)
def perpendicular_line_cross_point(l,p,**kwargs):
    return Line(start=p.get_center(),end=p.get_center()+ex(np.column_stack(([0,1],[-1,0]))@k_of_(l)),**kwargs)
###Cercles
import math
from typing import List, Tuple

def circle_intersection(r1: float, r2: float, o1: Tuple[float, float], o2: Tuple[float, float]) -> List[Tuple[float, float]]:#DeepSeek
    """
    返回两个圆的交点列表。
    - 相离 / 内含（无交点）：返回 []
    - 相切：返回包含一个交点的列表
    - 相交于两点：返回两个交点的列表
    - 重合（无限交点）：返回 [] （可根据需求改为抛出异常）
    """
    eps = 1e-12
    dx = o2[0] - o1[0]
    dy = o2[1] - o1[1]
    d = math.hypot(dx, dy)          # 圆心距

    # 重合（无限交点）→ 按需求返回空列表
    if d < eps and abs(r1 - r2) < eps:
        return []                   # 或 raise ValueError("重合")

    # 无交点：相离 或 内含且不切
    if d > r1 + r2 + eps or d < abs(r1 - r2) - eps:
        return []

    # 计算交点（通用公式，h=0 时自动退化为切点）
    a = (r1 * r1 - r2 * r2 + d * d) / (2 * d)
    h_sq = r1 * r1 - a * a
    if h_sq < 0:
        # 由于浮点误差可能为微小负数，置零
        h_sq = 0.0
    h = math.sqrt(h_sq)

    # 圆心连线上的中点
    xm = o1[0] + (a / d) * dx
    ym = o1[1] + (a / d) * dy

    # 垂直方向单位向量
    perp_x = -dy / d
    perp_y = dx / d

    # 交点
    if h < eps:                     # 相切，一个交点
        return [(xm, ym)]
    else:
        x1 = xm + h * perp_x
        y1 = ym + h * perp_y
        x2 = xm - h * perp_x
        y2 = ym - h * perp_y
        return [(x1, y1), (x2, y2)]

def cross_c(c1:Circle,c2:Circle):
    r1 = c1.radius
    r2 = c2.radius
    o1 = c1.get_center()[:2]
    o2 = c2.get_center()[:2]
    return [ex(i)for i in circle_intersection(r1,r2,o1,o2)]

def cross_cl(c:Circle,l:Line):
    r = c.radius
    o = Dot(c.get_center())
    k = k_of_(l)
    m = cross_l(perpendicular_line_cross_point(l,o),l)
    d = Line(o.get_center(),ex(m)).get_length()
    s = math.sqrt((r*r)-(d*d))
    return [ex(i)for i in [m+k*(s/np.linalg.norm(k)),m-k*(s/np.linalg.norm(k))]]
###
def distance(A,B):
    return Line(A.get_center(),B.get_center()).get_length()
def infinity_straight_line_cross_points(A,B,length=37,**kwargs):
    a = A.get_center()
    b = B.get_center()
    k = 0.5*length*(a-b)/np.linalg.norm(a-b)
    return Line(a-k,a+k,**kwargs)
def line_via_dot(A,B,c=BLACK,**kwargs):
    return Line(A.get_center(),B.get_center(),color=c,**kwargs)
def equal_lines_notes_group(*lines,n=1,c=BLACK,size=1):
    return VGroup(*[equal_line_notes(i,n,c,size)for i in lines])
def polygon_via_dot(*dots,**kwargs):
    return Polygon(*[i.get_center()for i in dots],**kwargs)
###
def perpendicular_bisector(x1,x2):
    a = x1.get_center()
    b = x2.get_center()
    c = Dot((a+b)/2)
    return perpendicular_line_cross_point(Line(a,b),c)
def circumcircle_of_triangle(x1,x2,x3,**kwargs):
    o = Dot(ex(cross_l(perpendicular_bisector(x1,x2),perpendicular_bisector(x2,x3))))
    return Circle(radius = distance(o,x2),**kwargs).move_to(o.get_center())
###
def falling_maple(*x):
    return polygon_via_dot(*x,color=LEAF_RED, fill_opacity=0.37)
def withered_leaf(*x):
    return polygon_via_dot(*x, color=LEAF_YELLOW, fill_opacity=0.37)
###
def perpendicular_bisector_notes(l,n,c=BLACK,size=0.5,**kwargs):
    bisector = perpendicular_bisector(Dot(l.get_start()),Dot(l.get_end()))
    M = Dot(ex(cross_l(l,bisector)))
    A = Dot(l.get_start())
    B = Dot(l.get_end())
    AM = line_via_dot(A,M)
    MB = line_via_dot(M,B)
    return VGroup(equal_lines_notes_group(AM,MB,n=n,c=c,size=size,**kwargs),
                  RightAngle(l,bisector,color=c,length=size*0.37,**kwargs))
###
def right_aligned_text(t):
    saying = VGroup(Text(i, color=BLACK, font_size=DEFAULT_FONT_SIZE / 2) for i in t)
    for i in range(len(saying)):
        if i == 0:
            pass
        else:
            saying[len(saying) - 1 - i].next_to(saying[len(saying) - i], UP, aligned_edge=RIGHT)
    return saying
###NeutronStar233
