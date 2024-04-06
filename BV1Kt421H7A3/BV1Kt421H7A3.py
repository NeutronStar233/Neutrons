from math import *
from manim import *
import numpy as np

config.background_color = WHITE
config.frame_width = 16
config.frame_height = 9
config.pixel_width = 1920
config.pixel_height = 1080

class s1(ThreeDScene):
    def construct(self):
        self.wait(1)

        screen = Rectangle(stroke_color=PURE_RED,width=16/4,height=9/4)#
        screen.rotate_about_origin(-60 * DEGREES, RIGHT, ORIGIN)
        screen.rotate_about_origin(-60 * DEGREES, OUT, ORIGIN)
        _L = sin(60 * DEGREES)
        screen.shift([3 * _L * cos(30 * DEGREES), 3 * _L * sin(30 * DEGREES), 3 * cos(60 * DEGREES)])
        self.add(screen)
        cube = Cube(fill_opacity=0,stroke_width=3,stroke_color=BLACK,side_length=1)
        self.set_camera_orientation(phi=60*DEGREES,theta=30*DEGREES,focal_distance=4)
        axes = ThreeDAxes(axis_config={"color":BLACK})
        self.add(axes)
        self.play(Create(cube))
        self.wait(1)
        # screen = ImageMobject("s1_ManimCE_v0.18.0.png")#Square(stroke_color=GREEN,fill_color=PURE_GREEN,fill_opacity=0.75)#
        # screen.rotate_about_origin(-60*DEGREES,RIGHT,ORIGIN)
        # screen.rotate_about_origin(-60*DEGREES,OUT,ORIGIN)
        # _L = sin(60*DEGREES)
        # screen.shift([3*_L*cos(30*DEGREES),3*_L*sin(30*DEGREES),3*cos(60*DEGREES)])
        self.wait(1)
        self.play(screen.animate.fade_to(PURE_RED,0.5))
        self.move_camera(focal_distance=20)
        self.move_camera(theta=80*DEGREES)
        self.wait(1)
        P1 = Dot3D([0.5,0.5,0.5],color=RED)
        P2 = Dot3D(screen.get_center(),color=PURE_BLUE)
        P1_2 = Line3D(P1,P2,color=GRAY)
        self.play(Create(P1))
        self.play(Write(P1_2))
        self.play(Create(P2))
        self.wait(1)
        imgCamera = SVGMobject("pcamera.svg")
        imgCamera.move_to(screen.get_center().copy())
        imgCamera.scale(0.5)
        self.add_fixed_orientation_mobjects(imgCamera)
        self.play(FadeIn(imgCamera),FadeOut(screen,P1,P2,P1_2))
        self.wait(1)
        self.move_camera(theta=120*DEGREES)
        self.wait(1)

class s1_2(Scene):
    def construct(self):
        e_photo = VGroup(Vector([1,0,0],color=RED),Vector([0,1,0],color=BLUE))
        point_photo = Dot([2,2,0],color=PURE_RED,radius=0.25)
        e_point_photo = VGroup(Line([2,2,0],[0,2,0],color=RED),Line([2,2,0],[2,0,0],color=BLUE),DashedLine([0,2,0],[0,0,0],color=BLUE_A),DashedLine([2,0,0],[0,0,0],color=RED_A))
        edge_photo = Rectangle(width=16,height=9,stroke_color=PURE_RED,stroke_width=10)
        photo = VGroup(e_photo,point_photo,e_point_photo,edge_photo)
        photo.scale(0.4)
        photo.to_edge(LEFT)
        e_screen = VGroup(Vector([1,0,0],color=RED),Vector([0,-1,0],color=BLUE)).shift(LEFT*8,UP*4.5)
        point_screen = Dot([2, 2, 0], color=PURE_BLUE, radius=0.25)
        e_point_screen = VGroup(Line([2, 2, 0], [-8, 2, 0], color=RED), Line([2, 2, 0], [2, 4.5, 0], color=BLUE),
                               DashedLine([-8, 2, 0], [-8, 4.5, 0], color=BLUE_A),
                               DashedLine([2, 4.5, 0], [-8, 4.5, 0], color=RED_A))
        edge_screen = Rectangle(width=16, height=9, stroke_color=BLACK, stroke_width=10)
        screen = VGroup(edge_screen,e_screen,point_screen,e_point_screen)
        screen.scale(0.4)
        screen.to_edge(RIGHT)
        text = VGroup(Text(r"“相片”",color=BLACK).next_to(photo,DOWN),Text(r"屏幕",color=BLACK).next_to(screen,DOWN))
        self.add(photo,screen,text)
        self.wait(1)
        trans = Arrow(point_photo,point_screen,color=GRAY,buff=0)
        self.play(Write(trans))
        self.wait(1)
        t_P = Tex(r"$$\text{P}$$",color=PURE_RED).next_to(point_photo,RIGHT+UP)
        t_Q = Tex(r"$$\text{Q}$$",color=PURE_BLUE).next_to(point_screen,RIGHT+DOWN)
        math_trans = VGroup(Tex(r"$$Q_x = k P_x + \frac{\text{width}}{2}$$",color=BLACK).scale(0.75),Tex(r"$$Q_y = - k P_y + \frac{\text{height}}{2}$$",color=BLACK).scale(0.75)).arrange(DOWN).to_edge(DOWN)
        self.play(Write(math_trans),Write(t_P),Write(t_Q))
        self.wait(1)

def specailly322(P:Dot3D,h):
    return [h*P.get_x()/P.get_z(),0,-h*P.get_y()/P.get_z()]

class s2(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60*DEGREES,theta=30*DEGREES)
        M = SVGMobject("pcamera.svg").scale(0.20)
        M_label = Tex(r"$$\text{M}$$",color=GRAY).move_to([0,0,-0.25])
        self.add_fixed_orientation_mobjects(M_label,M)
        self.play(Create(M_label),Create(M))
        self.wait(1)
        EZ = Vector([0, 1, 0], color=GREEN)
        e_camera = VGroup(Vector([-1,0,0],color=RED),Vector([0,0,1],color=BLUE))
        label_x = Tex(r"$$x$$",color=RED).move_to([-1,0,0])
        label_y = Tex(r"$$y$$",color=BLUE).move_to([0,0,1])
        label_z = Tex(r"$$z$$",color=GREEN).move_to([0,1,0])
        self.play(Create(e_camera),Create(EZ),M.animate.scale(0.5))
        self.add_fixed_orientation_mobjects(label_x,label_y,label_z)
        x_y_plane = Square(color=GRAY,fill_opacity=0.125,side_length=1)
        x_y_plane.rotate(90*DEGREES,RIGHT)
        tracker = ValueTracker(0)
        x_y_plane.add_updater(lambda m:m.fade(tracker.get_value()))
        self.wait(1)
        self.play((Create(x_y_plane)))
        self.play(x_y_plane.animate.scale(7))
        # ax_y_plane = NumberPlane(axis_config={"color":BLACK})
        # ax_y_plane.rotate(90*DEGREES,RIGHT)
        # self.remove(x_y_plane)
        # self.play(FadeIn(ax_y_plane))
        self.wait(1)
        Q_X_T = ValueTracker(-0.5)
        Q_Y_T = ValueTracker(0.5)
        QYT = ValueTracker(0)

        PXT = ValueTracker(-1)
        PYT = ValueTracker(-2)
        PZT = ValueTracker(1)
        DotP = Dot3D([-1,-2,1],color=PURE_RED)
        DotQ = Dot3D([-0.5,0,0.5],color=PURE_BLUE)
        DotP.add_updater(lambda m:m.move_to([PXT.get_value(),PYT.get_value(),PZT.get_value()]))
        DotQ.add_updater(lambda m:m.move_to([Q_X_T.get_value(),QYT.get_value(),Q_Y_T.get_value()]))
        PQ = Arrow(DotP,DotQ,color=GRAY,buff=0)
        PQ.add_updater(lambda m:m.put_start_and_end_on([PXT.get_value(), PYT.get_value(),PZT.get_value()], [Q_X_T.get_value(), 0, Q_Y_T.get_value()]))
        PE_Y = DashedLine([-1,-2,1],[-1,-2,0],color=BLUE)
        PE_X = DashedLine([-1,-2,0],[0,-2,0],color=RED)
        PE_Z = DashedLine([0,-2,0],[0,0,0],color=GREEN)
        PE_Y.add_updater(lambda m:m.put_start_and_end_on([PXT.get_value(),PYT.get_value(),PZT.get_value()],[PXT.get_value(),PYT.get_value(),0]))
        PE_X.add_updater(lambda m: m.put_start_and_end_on([PXT.get_value(), PYT.get_value(), 0],
                                                          [0, PYT.get_value(), 0]))
        PE_Z.add_updater(lambda m: m.put_start_and_end_on([0, PYT.get_value(),0],
                                                          [0, 0, 0]))

        QE_X = DashedLine([-0.5,QYT.get_value(),0.5], [0, QYT.get_value(), 0.5], color=RED)
        QE_Y = DashedLine([-0.5,QYT.get_value(),0.5], [-0.5, QYT.get_value(), 0], color=BLUE)
        QE_X.add_updater(lambda m:m.put_start_and_end_on([Q_X_T.get_value(),QYT.get_value(),Q_Y_T.get_value()],[0,QYT.get_value(),Q_Y_T.get_value()]))
        QE_Y.add_updater(lambda m:m.put_start_and_end_on([Q_X_T.get_value(), QYT.get_value(), Q_Y_T.get_value()], [Q_X_T.get_value(), QYT.get_value(), 0]))
        P_label = Tex(r"$$\text{P}$$",color=PURE_RED).move_to(DotP)
        Q_label = Tex(r"$$\text{Q}$$",color=PURE_BLUE).move_to(DotQ)
        P_label.add_updater(lambda m:m.move_to([PXT.get_value(),PYT.get_value(),PZT.get_value()+0.25]))
        Q_label.add_updater(lambda m:m.move_to([Q_X_T.get_value(),QYT.get_value(),Q_Y_T.get_value()+0.25]))
        self.add_fixed_orientation_mobjects(P_label)
        self.move_camera(theta=-30*DEGREES,added_anims=[Create(DotP),Write(PE_X),Write(PE_Y),Write(PE_Z),Write(P_label)])
        self.wait(1)
        self.play(Write(PQ))
        self.add_fixed_orientation_mobjects(Q_label)
        self.play(Create(DotQ),Write(QE_X),Write(QE_Y),Write(Q_label))
        self.wait(1)
        t_trans_PQ = Tex(r"$$Q_x = P_x$$$$Q_y = P_y$$",color=BLACK).to_corner(UL)
        self.add_fixed_in_frame_mobjects(t_trans_PQ)
        self.play(Q_X_T.animate.set_value(-1),Q_Y_T.animate.set_value(1),Write(t_trans_PQ))
        self.wait(1)
        t_tracker = ValueTracker(45*DEGREES)
        ok = True
        def PXFUNC(m:Mobject):
            if ok:
                return m.set_value(-sqrt(2)*cos(t_tracker.get_value()))
            else:
                return m
        def PYFUNC(m:Mobject):
            if ok:
                return m.set_value(sqrt(2) * sin(t_tracker.get_value()))
            else:
                return m
        PXT.add_updater(lambda m:PXFUNC(m))
        PZT.add_updater(lambda m:PYFUNC(m))
        Q_X_T.add_updater(lambda m: m.set_value(-sqrt(2) * cos(t_tracker.get_value())))
        Q_Y_T.add_updater(lambda m: m.set_value(sqrt(2) * sin(t_tracker.get_value())))
        self.play(t_tracker.animate.set_value(155*DEGREES),PXT.animate.get_value(),PZT.animate.get_value(),PYT.animate.get_value(),DotP.animate.get_center(),Q_X_T.animate.get_center(),
                  Q_Y_T.animate.get_center(),DotQ.animate.get_center(),QE_Y.animate.get_center(),QE_X.animate.get_center())
        self.wait(1)
        t1_tracker = ValueTracker(0)
        PYT.add_updater(lambda m:m.set_value(-2-sin(t1_tracker.get_value())))
        self.play(t1_tracker.animate.set_value((360+90)*DEGREES),PYT.animate.get_value())
        self.wait(1)
        #self.move_camera(theta=0)
        #self.move_camera(phi=90*DEGREES)
        MP = Line3D(M.get_center(),[3,-3,3],color=RED)
        ok = False
        self.move_camera(theta=-22.5*DEGREES,added_anims=[Write(MP),FadeOut(PQ),PXT.animate.set_value(3),PZT.animate.set_value(3),DotP.animate.get_center(),PE_X.animate.get_center()
                  ,PE_Y.animate.get_center()
                  ,PE_Z.animate.get_center(),FadeOut(t_trans_PQ)])
        # self.play(Write(MP),FadeOut(PQ),PXT.animate.set_value(3),PZT.animate.set_value(3),DotP.animate.get_center(),PE_X.animate.get_center()
        #           ,PE_Y.animate.get_center()
        #           ,PE_Z.animate.get_center(),FadeOut(t_trans_PQ))
        self.wait(1)
        ESight = e_camera.copy()
        DotO = Dot3D(M.get_center(),color=BLACK)
        O_label = Tex(r"$$\text{O}$$",color=BLACK).move_to(DotO.get_center())
        h = ValueTracker(0.01)
        x_y_plane.add_updater(lambda m:m.move_to([0,-h.get_value(),0]))
        Q_X_T.add_updater(lambda m:m.set_value(-h.get_value()*PXT.get_value()/PYT.get_value()))
        Q_Y_T.add_updater(lambda m:m.set_value(-h.get_value()*PZT.get_value()/PYT.get_value()))
        QYT.add_updater(lambda m:m.set_value(-h.get_value()))
        ESight.add_updater(lambda m:m.move_to([-0.5,-h.get_value(),0.5]))
        DotO.add_updater(lambda m:m.move_to([0,-h.get_value(),0]))
        O_label.add_updater(lambda m:m.move_to([0,-h.get_value(),-0.25]))
        self.add_fixed_orientation_mobjects(O_label)
        self.play(h.animate.set_value(1.5),QYT.animate.get_value(),Q_X_T.animate.get_value(),Q_Y_T.animate.get_value(),QE_X.animate.get_center(),QE_Y.animate.get_center(),
                  DotO.animate.get_center(),ESight.animate.get_center(),O_label.animate.get_center())
        self.wait(1)
        t_h = Tex(r"$$\text{MO}=h$$",color=BLACK).to_corner(UL)
        self.add_fixed_in_frame_mobjects(t_h)
        self.play(Write(t_h))
        self.wait(1)

        DotA = Dot3D([0,DotQ.get_y(),DotQ.get_z()],color=BLACK)
        DotB = Dot3D([DotQ.get_x(), DotQ.get_y(), 0], color=BLACK)
        AO = DashedLine(DotA,DotO,color=BLACK)
        BO = DashedLine(DotB, DotO, color=BLACK)
        DotC = Dot3D([0,DotP.get_y(),DotP.get_z()],color=BLACK)
        DotD = Dot3D([0,DotP.get_y(),0],color=BLACK)
        DotE = Dot3D([DotP.get_x(), DotP.get_y(), 0], color=BLACK)
        CD = DashedLine(DotC,DotD,color=BLACK)
        CP = DashedLine(DotC,DotP,color=BLACK)
        ME = DashedLine(M.get_center(),DotE,color=BLACK)
        MC = DashedLine(M.get_center(),DotC,color=BLACK)

        A_label = Tex(r"$$\text{A}$$",color=BLACK).move_to([0,DotQ.get_y(),DotQ.get_z()+0.25])
        B_label = Tex(r"$$\text{B}$$", color=BLACK).move_to([DotQ.get_x(), DotQ.get_y(), -0.25])
        C_label = Tex(r"$$\text{C}$$", color=BLACK).move_to([0,DotP.get_y(),DotP.get_z()+0.25])
        D_label = Tex(r"$$\text{D}$$", color=BLACK).move_to([0,DotP.get_y(),-0.25])
        E_label = Tex(r"$$\text{E}$$", color=BLACK).move_to([DotP.get_x(), DotP.get_y(), -0.25])

        t_s_piremid = Tex(r"$$\text{M-CDEP} \sim \text{M-AOBQ}$$$$\text{Q}_x=\text{AQ}=\text{CP} \cdot \frac{MO}{MD}=h \frac{\text{P}_x}{-\text{P}_z}$$$$\text{Q}_y=\text{BQ}=\text{EP} \cdot \frac{MO}{MD}=h \frac{\text{P}_y}{-\text{P}_z}$$",color=BLACK).to_corner(UR)

        self.add_fixed_in_frame_mobjects(t_s_piremid)
        self.add_fixed_orientation_mobjects(A_label,B_label,C_label,D_label,E_label)
        self.play(FadeIn(A_label,B_label,C_label,D_label,E_label,DotA,DotB,DotC,DotD,DotE,AO,BO,CD,CP,ME,MC),Write(t_s_piremid))
        self.wait(1)
        lightScreen = Square(side_length=7,color=GRAY,fill_opacity=0.125)
        lightScreen.shift(1.5*UP)
        lightScreen.rotate(90*DEGREES,RIGHT)
        PLight = Line3D(DotP,-10*DotP.get_center(),color=RED)
        self.play(FadeOut(t_s_piremid,A_label,B_label,C_label,D_label,E_label,DotA,DotB,DotC,DotD,DotE,AO,BO,CD,CP,ME,MC,x_y_plane,DotQ,QE_X,QE_Y,Q_label,ESight,DotO,MP,O_label))
        self.wait(1)
        DotQ_ = Dot3D([-DotQ.get_x(),-DotQ.get_y(),-DotQ.get_z()],color=BLUE)
        Q__label = Tex(r"$$\text{Q}'$$",color=BLUE).move_to([-DotQ.get_x(),-DotQ.get_y(),-DotQ.get_z()-0.25])
        DotO_ = Dot3D([0,1.5,0],color=BLACK)
        O__label = Tex(r"$$\text{O}'$$",color=BLACK).move_to([0,1.5,-0.25])
        self.add_fixed_orientation_mobjects(Q__label,O__label)
        self.move_camera(theta=-10*DEGREES,added_anims=[Write(PLight),Write(Q__label),Create(DotQ_),Create(lightScreen),Create(DotO_),Write(O__label)])
        self.wait(1)
        QQ_ = DashedLine(DotQ,DotQ_,color=BLACK)
        t_exra = Tex(r"$$\text{Q}=-\text{Q}'$$",color=BLACK).to_corner(UR)
        self.add_fixed_in_frame_mobjects(t_exra)
        self.play(FadeIn(x_y_plane,DotO,DotQ,QQ_,O_label,Q_label),Write(t_exra))
        self.wait(1)
        self.play(FadeOut(lightScreen,QQ_,DotQ_,DotQ,O__label,Q__label,PLight,DotP,P_label,DotO_,Q_label,t_exra,PE_X,PE_Y,PE_Z))
        screen = Rectangle(width=0.02,height=0.01,color=RED,fill_opacity=0.25)
        screen.move_to(x_y_plane.get_center())
        screen.rotate(90*DEGREES,RIGHT)
        self.add(screen)
        self.move_camera(theta=-20*DEGREES,added_anims=[screen.animate.scale(100)])
        self.wait(1)
        side1 = DashedLine([0, 0, 0], [-1, -1.5, 0.5], color=BLACK)
        side2 = DashedLine([0, 0, 0], [1, -1.5, 0.5], color=BLACK)
        side3 = DashedLine([0, 0, 0], [-1, -1.5, -0.5], color=BLACK)
        side4 = DashedLine([0, 0, 0], [1, -1.5, -0.5], color=BLACK)

        self.play(Write(side1),Write(side2),Write(side3),Write(side4))

        nbvt = ValueTracker(1)

        key = True

        side1.add_updater(lambda m:m.put_start_and_end_on([0,0,0],[-nbvt.get_value()*1, -nbvt.get_value()*1.5, nbvt.get_value()*0.5]) if key else m)
        side2.add_updater(lambda m: m.put_start_and_end_on([0, 0, 0], [nbvt.get_value() * 1, -nbvt.get_value() * 1.5, nbvt.get_value() * 0.5]) if key else m)
        side3.add_updater(lambda m: m.put_start_and_end_on([0, 0, 0], [-nbvt.get_value() * 1, -nbvt.get_value() * 1.5, -nbvt.get_value() * 0.5]) if key else m)
        side4.add_updater(lambda m: m.put_start_and_end_on([0, 0, 0], [nbvt.get_value() * 1, -nbvt.get_value() * 1.5, -nbvt.get_value() * 0.5]) if key else m)

        topR = Rectangle(width=2,height=1,color=GRAY,fill_opacity=0)
        topR.move_to(x_y_plane.get_center())
        topR.rotate(90 * DEGREES, RIGHT)
        topR.add_updater(lambda m:m.move_to([0,-nbvt.get_value()*1.5,0]) if key else m)

        self.add(topR)
        self.play(nbvt.animate.set_value(4),topR.animate.scale(4))
        self.wait(1)

        key = False

        side1.add_updater(lambda m:m.put_start_and_end_on([0,0,0],[-4,-4*h.get_value(),2]))
        side2.add_updater(lambda m: m.put_start_and_end_on([0, 0, 0], [4, -4*h.get_value(), 2]))
        side3.add_updater(lambda m: m.put_start_and_end_on([0, 0, 0], [-4, -4*h.get_value(), -2]))
        side4.add_updater(lambda m: m.put_start_and_end_on([0, 0, 0], [4, -4*h.get_value(), -2]))

        topR.add_updater(lambda m: m.move_to([0, -4*h.get_value(), 0]))

        screen.add_updater(lambda m:m.move_to([0,-h.get_value(),0]))

        self.play(h.animate.set_value(0.5),topR.animate.get_center())
        self.play(h.animate.set_value(1.5),topR.animate.get_center())
        self.wait(1)

        DotPP = Dot3D([-2,3,1],color=PURE_RED)
        PP_label = Tex(r"$$\text{P}$$",color=PURE_RED).move_to([-3,2.75,1])

        self.add_fixed_orientation_mobjects(PP_label)
        self.move_camera(theta=10*DEGREES,added_anims=[Create(DotPP),Write(PP_label)])
        self.wait(1)

        DotQQ = Dot3D([2*1.5/3,-1.5,-1.5/3],color=PURE_BLUE)
        QQ_label = Tex(r"$$\text{Q}$$",color=PURE_BLUE).move_to([2*1.5/3,-1.5,0.25-1.5/3])

        PPQQ = Line3D([-2,3,1],[2*1.5/3,-1.5,-1.5/3],color=GRAY)

        self.play(Write(PPQQ))
        self.add_fixed_orientation_mobjects(QQ_label)
        self.play(Create(DotQQ),Write(QQ_label))

        self.wait(1)

        cancel = SVGMobject("cancel.svg")
        cancel.move_to(DotQQ.get_center())
        self.add_fixed_orientation_mobjects(cancel)
        self.play(Create(cancel))
        self.wait(1)

        code_false = '''if(z >= 0){
    VISIBLE = false;
}
        '''

        t_code = Code(code=code_false,language="C++",font="Consolas").to_corner(UR)

        self.add_fixed_in_frame_mobjects(t_code)
        self.play(FadeOut(cancel,PPQQ,DotQQ,QQ_label),Write(t_code))
        self.wait(1)

        self.play(FadeOut(e_camera,EZ,DotPP,PP_label,M,M_label,x_y_plane,topR,side1,side2,side3,side4,DotO,O_label,screen,t_h,t_code,label_x,label_y,label_z))
        self.wait(1)

        t_final = Tex(r"$$Q_x = h \frac{P_x}{P_z}$$$$Q_y = h \frac{P_y}{P_z}$$$$\text{VISIBLE}=! (P_z >= 0)$$",color=BLACK)
        self.add_fixed_in_frame_mobjects(t_final)
        self.play(Write(t_final))
        self.wait(1)

class s2_algebra(Scene):
    def construct(self):
        t_trans_PQ = Tex(r"$$Q_x = P_x$$$$Q_y = P_y$$",color=BLACK)
        self.wait(1)
        self.play(Write(t_trans_PQ))
        self.wait(1)
        self.play(Transform(t_trans_PQ,Tex(r"$$Q_x = \frac{P_x}{-P_z}$$$$Q_y = \frac{P_y}{-P_z}$$",color=BLACK)),Write(Text("或者|z|",color=GRAY).to_corner(DR)))
        self.wait(1)

class s3(ThreeDScene):
    def construct(self):
        E_C_X = Arrow([0,0,0],[1,0,0],buff=0,color=RED)
        E_C_Y = Arrow([0, 0, 0], [0, 1, 0], buff=0, color=BLUE)
        E_C_Z = Arrow([0, 0, 0], [0, 0 ,1], buff=0, color=GREEN)
        label_x_ = Tex(r"$$x'$$",color=RED).move_to([1,0,-0.25])
        label_y_ = Tex(r"$$y'$$", color=BLUE).move_to([0,1,-0.25])
        label_z_ = Tex(r"$$z'$$", color=GREEN).move_to([0,0,1.25])
        camera = SVGMobject("pcamera.svg").scale(0.20).move_to([0,0,0])
        DotP = Dot3D([2,-1.5,1],color=PURE_RED)
        DP_label = Tex(r"$$\text{P}$$",color=PURE_RED).move_to([2,-1.5,1.25])
        self.set_camera_orientation(phi=60 * DEGREES, theta=30 * DEGREES)
        self.add_fixed_orientation_mobjects(camera,DP_label)
        self.play(Create(camera),Write(E_C_X),Write(E_C_Y),Write(E_C_Z),Create(DotP),Write(DP_label))
        self.wait(1)

        E_W_X = Arrow([0, 0, 0], [1, 0, 0], buff=0, color=RED)
        E_W_Y = Arrow([0, 0, 0], [0, 1, 0], buff=0, color=BLUE)
        E_W_Z = Arrow([0, 0, 0], [0, 0, 1], buff=0, color=GREEN)
        label_x = Tex(r"$$x$$", color=RED).move_to([1, 0, -0.25])
        label_y = Tex(r"$$y$$", color=BLUE).move_to([0, 1, -0.25])
        label_z = Tex(r"$$z$$", color=GREEN).move_to([0, 0, 1.25])
        DotO = Dot3D([0,0,0],color=BLACK)
        O_label = Tex(r"$$\text{O}$$",color=BLACK).move_to([0,0,-0.25])
        self.add_fixed_orientation_mobjects(O_label)
        #self.move_camera(added_anims=[Create(DotO),Write(E_W_X),Write(E_W_Y),Write(E_W_Z),Create(DotO),Write(O_label)])
        label_x_.shift([-2,2,1])
        label_y_.shift([-2,2,1])
        label_z_.shift([-2,2,1])
        self.add_fixed_orientation_mobjects(label_x_,label_y_,label_z_,label_x,label_y,label_z)
        self.play(Create(DotO),Write(E_W_X),Write(E_W_Y),Write(E_W_Z),Create(DotO),Write(O_label),E_C_X.animate.shift([-2,2,1]),E_C_Y.animate.shift([-2,2,1]),E_C_Z.animate.shift([-2,2,1]),
                 camera.animate.shift([-2,2,1]),DotP.animate.shift([-2,2,1]),DP_label.animate.shift([-2,2,1]),Write(label_x_),Write(label_y_),Write(label_z_)
                  ,Write(label_x),Write(label_y),Write(label_z))
        self.wait(1)

        OP = Arrow([0,0,0],DotP,color=YELLOW_E,buff=0)
        OP_label = Tex(r"$$\text{p}'$$",color=YELLOW_E).next_to(OP,DOWN)
        self.play(Write(OP))
        self.wait(1)
        OM = Arrow([0,0,0],[-2,2,1],color=ORANGE,buff=0)
        OM_label = Tex(r"$$\text{m}'$$",color=ORANGE).next_to(OM,RIGHT)
        self.play(Write(OM))

        t_tracker = ValueTracker(0)
        isable = True
        E_C_X.add_updater(lambda m:m.put_start_and_end_on([-2,2,1],[-2+cos(t_tracker.get_value()),2,1+sin(t_tracker.get_value())]) if isable else m)
        E_C_Z.add_updater(lambda m: m.put_start_and_end_on([-2, 2, 1], [-2 - sin(t_tracker.get_value()), 2,
                                                                        1 + cos(t_tracker.get_value())]) if isable else m)
        label_x_.add_updater(lambda m:m.move_to([-2+cos(t_tracker.get_value()),2,1+sin(t_tracker.get_value()-0.25)]) if isable else m)
        label_z_.add_updater(
            lambda m: m.move_to([-2 - sin(t_tracker.get_value()), 2,
                                                                        1 + cos(t_tracker.get_value())+0.25]) if isable else m)

        self.play(t_tracker.animate.set_value(360*DEGREES))
        self.wait(1)
        isable = False

        self.add_fixed_orientation_mobjects(OM_label)
        self.play(Write(OM_label))
        self.wait(1)

        MP = Arrow([-2,2,1],DotP,color=PURE_GREEN,buff=0)
        MP_label = Tex(r"$$\text{p}$$",color=PURE_GREEN).next_to(MP,OUT)
        self.add_fixed_orientation_mobjects(MP_label,OP_label)
        self.play(Write(OP_label),Write(MP_label),Write(MP))
        self.wait(1)

        t_same_e = Tex(r"$$\begin{bmatrix}  x'&y'  &z'\end{bmatrix}=\begin{bmatrix}  x&y  &z\end{bmatrix}=\begin{bmatrix}  1&  0& 0\\ 0&  1& 0\\ 0&  0&1\end{bmatrix}$$",color=BLACK).to_corner(UL)
        t_ZM =  Text("注明：此处x、y、z、x'、y'、z'皆是向量，后同",color=GRAY,font_size=25).to_corner(DR)
        self.add_fixed_in_frame_mobjects(t_same_e,t_ZM)
        self.play(Write(t_same_e),Write(t_ZM))
        self.wait(1)

        t_example = Tex(r"$$\begin{bmatrix}  \hat{i}&\hat{j}\end{bmatrix}$$",color=BLACK).next_to(t_same_e,DOWN,aligned_edge=LEFT)
        E_T = VGroup(Vector([1,0.5,0],color=RED),Tex(r"$$\hat{i}$$",color=RED).move_to([1.25,0.5,0]),
                     Vector([-0.2,0.8,0],color=BLUE),Tex(r"$$\hat{j}$$",color=BLUE).move_to([-0.2,1.05,0]),Dot([0,0,0],color=BLACK)).next_to(t_example,DOWN,aligned_edge=LEFT)
        t_iyje = Text(r"注明：此处将坐标系指向量空间，后同",color=GRAY,font_size=20).to_corner(DR)

        self.add_fixed_in_frame_mobjects(E_T,t_example,t_iyje)
        self.play(Create(E_T),Write(t_example),Write(t_iyje),FadeOut(t_ZM))
        self.wait(1)
        at_example = Tex(r"$$\begin{bmatrix}\hat{i}_x  & \hat{j}_x\\ \hat{i}_y &\hat{j}_y\end{bmatrix}$$",color=BLACK).next_to(t_same_e,DOWN,aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(at_example)
        self.play(FadeOut(t_example,t_iyje),FadeIn(at_example),E_T.animate.next_to(at_example,DOWN,aligned_edge=LEFT))
        self.wait(1)
        self.play(FadeOut(at_example,E_T))
        self.wait(1)
        at_same_e = Tex(r"$$\begin{bmatrix}  x'&y'  &z'\end{bmatrix}=\begin{bmatrix}  x&y  &z\end{bmatrix}=\mathbf{\text{E}}_3$$",color=BLACK).to_corner(UL)
        self.add_fixed_in_frame_mobjects(at_same_e)
        self.play(FadeOut(t_same_e),FadeIn(at_same_e))
        self.wait(1)

        t_p_ = Tex(r"$$\mathbf{\text{p}}'=\mathbf{\text{p}}+\mathbf{\text{m}}$$",color=BLACK).next_to(at_same_e,DOWN,aligned_edge=LEFT)
        t_p = Tex(r"$$\mathbf{\text{p}}=\mathbf{\text{p}}'-\mathbf{\text{m}}$$", color=BLACK).next_to(t_p_, DOWN,
                                                                                    aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(t_p_)
        self.play(Write(t_p_))
        self.wait(1)
        self.add_fixed_in_frame_mobjects(t_p)
        self.play(Write(t_p))
        self.wait(1)

        self.play(FadeOut(t_p,t_p_,at_same_e))
        self.wait(1)

        CXT = ValueTracker(0)
        CYT = ValueTracker(0)
        CZT = ValueTracker(0.01)

        RYT = ValueTracker(0)

        isable2 = True
        isable3 = True

        E_C_X.add_updater(lambda m:m.put_start_and_end_on([CXT.get_value(),CYT.get_value(),CZT.get_value()],[CXT.get_value()+cos(RYT.get_value()),CYT.get_value(),CZT.get_value()+sin(RYT.get_value())]) if isable2 else m)
        E_C_Y.add_updater(lambda m: m.put_start_and_end_on([CXT.get_value(), CYT.get_value(), CZT.get_value()],
                                                           [CXT.get_value(), CYT.get_value()+1,
                                                            CZT.get_value()]) if isable2 else m)
        E_C_Z.add_updater(lambda m: m.put_start_and_end_on([CXT.get_value(), CYT.get_value(), CZT.get_value()],
                                                           [CXT.get_value() - sin(RYT.get_value()), CYT.get_value(),
                                                            CZT.get_value() + cos(RYT.get_value())]) if isable2 else m)
        OM.add_updater(lambda m:m.put_start_and_end_on([0,0,0],[CXT.get_value(),CYT.get_value(),CZT.get_value()]) if isable3 else m)
        MP.add_updater(lambda m:m.put_start_and_end_on([CXT.get_value(),CYT.get_value(),CZT.get_value()],DotP.get_center()) if isable3 else m)
        camera.add_updater(lambda m:m.move_to([CXT.get_value(),CYT.get_value(),CZT.get_value()]))
        label_x_.add_updater(lambda m:m.move_to([CXT.get_value()+cos(RYT.get_value()),CYT.get_value(),CZT.get_value()+sin(RYT.get_value())-0.25]))
        label_y_.add_updater(
            lambda m: m.move_to([CXT.get_value(), CYT.get_value()+1, CZT.get_value()-0.25]))
        label_z_.add_updater(
            lambda m: m.move_to([CXT.get_value() - sin(RYT.get_value()), CYT.get_value(), CZT.get_value()+cos(RYT.get_value())-0.25]))

        self.remove(MP_label)
        self.play(RYT.animate.set_value((360+60)*DEGREES))
        self.play(CXT.animate.set_value(-1),CYT.animate.set_value(3),CZT.animate.set_value(2))
        self.wait(1)
        isable3 = False
        self.play(CXT.animate.set_value(0),CYT.animate.set_value(0),CZT.animate.set_value(0),DotP.animate.move_to([1,2,3]),DP_label.animate.move_to([1,2,3.25]),OP.animate.put_start_and_end_on([0,0,0],[1,2,3]),FadeOut(MP,OM,OM_label,label_x_,label_y_,label_z_,OP_label))
        self.play(RYT.animate.set_value(0))
        self.wait(1)
        t1 = Tex(r"$$p’=Ap$$",color=BLACK).to_corner(UR)
        self.add_fixed_in_frame_mobjects(t1)
        self.play(Write(t1))
        self.wait(1)
        t2 = Tex(r"$$p=A^{-1}p'$$",color=BLACK).next_to(t1,DOWN,aligned_edge=RIGHT)
        self.add_fixed_in_frame_mobjects(t2)
        self.play(Write(t2))
        self.wait(1)

class s3_part2(Scene):
    def construct(self):
        numberplane = NumberPlane(axis_config={"color":BLACK})
        EI = Vector([1,0],color=RED)
        EJ = Vector([0,1],color=BLUE)
        I_label = Tex(r"$$\hat{i}$$",color=RED).next_to(EI,UR)
        J_label = Tex(r"$$\hat{j}$$", color=BLUE).next_to(EJ, UR)
        self.wait(1)
        self.play(Create(numberplane),Write(EI),Write(EJ),Write(I_label),Write(J_label))
        self.wait(1)
        t1 = Tex(r"$$\begin{bmatrix}  \hat{i}_x& \hat{j}_x\\  \hat{i}_y&\hat{j}_y\end{bmatrix}$$",color=BLACK).to_corner(UL)
        self.play(Write(t1))
        self.wait(1)
        aEI = Vector([2,1],color=RED)
        aEJ = Vector([0.5,2.5], color=BLUE)
        aI_label = Tex(r"$$\hat{i}$$", color=RED).next_to(aEI, UR)
        aJ_label = Tex(r"$$\hat{j}$$", color=BLUE).next_to(aEJ, UR)
        sq = [[2,0.5],[1,2.5]]
        newnp = numberplane.copy()
        anewnp = NumberPlane(axis_config={"color": GRAY}, background_line_style={"stroke_color": YELLOW_D},
                            x_axis_config={"unit_size":sqrt(sq[0][0]**2+sq[1][0]**2),"rotation":atan(sq[1][0]/sq[0][0])},
                            y_axis_config={"unit_size":sqrt(sq[0][1]**2+sq[1][1]**2),"rotation":atan(sq[1][1]/sq[0][1])})
        self.play(Transform(EI,aEI),Transform(EJ,aEJ),Transform(I_label,aI_label),Transform(J_label,aJ_label),Transform(newnp,anewnp))
        self.wait(1)
        aEI = Vector([1, 0], color=RED)
        aEJ = Vector([0, 1], color=BLUE)
        aI_label = Tex(r"$$\hat{i}$$", color=RED).next_to(aEI, UR)
        aJ_label = Tex(r"$$\hat{j}$$", color=BLUE).next_to(aEJ, UR)
        self.play(FadeOut(newnp,t1),Transform(EI,aEI),Transform(EJ,aEJ),Transform(I_label,aI_label),Transform(J_label,aJ_label))
        self.wait(1)

        v = Vector([1,1],color=PURE_GREEN)
        v_label = Tex(r"$$\mathbf{v}$$",color=PURE_GREEN).next_to(v,UR)
        self.play(Write(v),Write(v_label))
        self.wait(1)

        self.play(Write(t1))
        self.wait(1)

        t_axis = Text("原本坐标系",color=BLACK).to_edge(DOWN)
        self.play(Write(t_axis))
        self.wait(1)
        aEI = Vector([2, 1], color=RED)
        aEJ = Vector([0.5, 2.5], color=BLUE)
        aI_label = Tex(r"$$\hat{i}$$", color=RED).next_to(aEI, UR)
        aJ_label = Tex(r"$$\hat{j}$$", color=BLUE).next_to(aEJ, UR)
        newnp = numberplane.copy()

        EIx = Line([2,0,0],[0,0,0],color=RED,stroke_width=10)
        EIy = Line([2, 1,0], [2, 0,0], color=PURPLE,stroke_width=10)
        EJx = Line([0.5, 2.5,0], [0, 2.5,0], color=RED,stroke_width=10)
        EJy = Line([0, 2.5,0], [0, 0,0], color=PURPLE,stroke_width=10)
        EIx_label = Tex(r"$$\hat{i}_x$$",color=RED).next_to(EIx,DOWN)
        EIy_label = Tex(r"$$\hat{i}_y$$", color=PURPLE).next_to(EIy, RIGHT)
        EJx_label = Tex(r"$$\hat{j}_x$$", color=RED).next_to(EJx, UP)
        EJy_label = Tex(r"$$\hat{j}_y$$", color=PURPLE).next_to(EJy, LEFT)
        av = Vector([2.5, 3.5], color=PURE_GREEN)
        av_label = Tex(r"$$\mathbf{v}$$", color=PURE_GREEN).next_to(av, UR)
        self.play(Transform(EI,aEI),Transform(EJ,aEJ),Transform(I_label,aI_label),Transform(J_label,aJ_label),
                  Transform(newnp,anewnp),Transform(t_axis,Text("转换到的坐标系",color=BLACK).to_edge(DOWN)),
                  FadeIn(EIx,EIy,EJx,EJy,EIx_label,EIy_label,EJx_label,EJy_label),Transform(v,av),Transform(v_label,av_label))
        self.wait(1)

        aEI = Vector([1, 0], color=RED)
        aEJ = Vector([0, 1], color=BLUE)
        aI_label = Tex(r"$$\hat{i}$$", color=RED).next_to(aEI, UR)
        aJ_label = Tex(r"$$\hat{j}$$", color=BLUE).next_to(aEJ, UR)
        av = Vector([1, 1], color=PURE_GREEN)
        av_label = Tex(r"$$\mathbf{v}$$", color=PURE_GREEN).next_to(av, UR)
        self.play(FadeOut(newnp, t_axis,EIx,EIy,EJx,EJy,EIx_label,EIy_label,EJx_label,EJy_label), Transform(EI, aEI), Transform(EJ, aEJ), Transform(I_label, aI_label),
                  Transform(J_label, aJ_label),Transform(v,av),Transform(v_label,av_label))

        tt = Text("一键三连",color=BLACK).to_corner(UR)
        self.play(Write(tt))
        self.wait(1)
        self.play(Transform(tt,Text("2*Coin",t2c={'2':PURE_RED},color=BLACK).to_corner(UR)))
        self.wait(1)
        self.play(FadeOut(tt))
        self.wait(1)



        newnp = numberplane.copy()
        t_v_xy = Tex(r"$$\begin{bmatrix} x\\y\end{bmatrix}$$",color=BLACK).next_to(t1,RIGHT)
        aEI = Vector([2, 1], color=RED)
        aEJ = Vector([0.5, 2.5], color=BLUE)
        aI_label = Tex(r"$$\hat{i}$$", color=RED).next_to(aEI, UR)
        aJ_label = Tex(r"$$\hat{j}$$", color=BLUE).next_to(aEJ, UR)
        av = Vector([2.5,3.5],color=PURE_GREEN)
        av_label = Tex(r"$$\mathbf{v}$$",color=PURE_GREEN).next_to(av,UR)
        self.play(Write(t_v_xy),Transform(newnp,anewnp),Transform(EI,aEI),Transform(EJ,aEJ),Transform(I_label,aI_label),Transform(J_label,aJ_label)
                  ,Transform(v,av),Transform(v_label,av_label))
        self.wait(1)


        tt2 = Tex(r"$$=x\begin{bmatrix}  \hat{i}_x \\\hat{i}_y\end{bmatrix}+y\begin{bmatrix}  \hat{j}_x \\\hat{j}_y\end{bmatrix}$$$$=\begin{bmatrix} x \hat{i}_x+y \hat{j}_x \\x \hat{i}_y+y \hat{j}_y \ \end{bmatrix}$$",color=BLACK).next_to(t1,DOWN,aligned_edge=LEFT)
        self.play(Write(tt2),EJ.animate.shift([2,1,0]),J_label.animate.move_to([3,2,0]))
        self.wait(1)

        TTT = Tex(
            r"$$\begin{bmatrix} \hat{k}_x& \hat{l}_x\\ \hat{k}_y &\hat{l}_y\end{bmatrix}\begin{bmatrix}  \hat{i}_x& \hat{j}_x\\ \hat{i}_y &\hat{j}_y\end{bmatrix}$$",
            color=BLACK).to_corner(UR)
        TTT2 = Tex(
            r"$$=\begin{bmatrix}\begin{bmatrix}  \hat{k}_x& \hat{l}_x\\ \hat{k}_y &\hat{l}_y\end{bmatrix}\hat{i}& \begin{bmatrix}  \hat{k}_x& \hat{l}_x\\ \hat{k}_y &\hat{l}_y\end{bmatrix}\hat{j}\end{bmatrix} $$",
            color=BLACK).next_to(TTT, DOWN, aligned_edge=RIGHT)
        self.play(Write(TTT), Write(TTT2))
        self.wait(1)
        self.play(FadeOut(TTT,TTT2))

        aEI = Vector([1, 0], color=RED)
        aEJ = Vector([0, 1], color=BLUE)
        aI_label = Tex(r"$$\hat{i}$$", color=RED).next_to(aEI, UR)
        aJ_label = Tex(r"$$\hat{j}$$", color=BLUE).next_to(aEJ, UR)
        av = Vector([1, 1], color=PURE_GREEN)
        av_label = Tex(r"$$\mathbf{v}$$", color=PURE_GREEN).next_to(av, UR)
        swq2 = np.array(np.linalg.inv(np.matrix(np.array([[2, 0.5], [1, 2.5]]))))
        bnewnp = NumberPlane(axis_config={"color": GRAY}, background_line_style={"stroke_color": YELLOW_D},
                             x_axis_config={"unit_size": sqrt(swq2[0][0] ** 2 + swq2[1][0] ** 2),
                                            "rotation": atan(swq2[1][0] / swq2[0][0])},
                             y_axis_config={"unit_size": sqrt(swq2[0][1] ** 2 + swq2[1][1] ** 2),
                                            "rotation": atan(swq2[1][1] / swq2[0][1])})

        self.play(Transform(newnp, numberplane), Transform(numberplane, bnewnp),Transform(EI, aEI), Transform(EJ, aEJ), Transform(I_label, aI_label),
                  Transform(J_label, aJ_label),Transform(v,av),Transform(v_label,av_label))
        self.wait(1)
        aEI = Vector([2, 1], color=RED)
        aEJ = Vector([0.5, 2.5], color=BLUE)
        aI_label = Tex(r"$$\hat{i}$$", color=RED).next_to(aEI, UR)
        aJ_label = Tex(r"$$\hat{j}$$", color=BLUE).next_to(aEJ, UR)
        av = Vector([2.5, 3.5], color=PURE_GREEN)
        av_label = Tex(r"$$\mathbf{v}$$", color=PURE_GREEN).next_to(av, UR)
        self.play(Transform(newnp, anewnp), Transform(numberplane, newnp.copy()), Transform(EI, aEI), Transform(EJ, aEJ),
                  Transform(I_label, aI_label),
                  Transform(J_label, aJ_label), Transform(v, av), Transform(v_label, av_label))
        self.wait(1)
        aEI = Vector([1, 0], color=RED)
        aEJ = Vector([0, 1], color=BLUE)
        aI_label = Tex(r"$$\hat{i}$$", color=RED).next_to(aEI, UR)
        aJ_label = Tex(r"$$\hat{j}$$", color=BLUE).next_to(aEJ, UR)
        av = Vector([1, 1], color=PURE_GREEN)
        av_label = Tex(r"$$\mathbf{v}$$", color=PURE_GREEN).next_to(av, UR)
        self.play(FadeOut(t1,tt2,t_v_xy,newnp),Transform(EI, aEI), Transform(EJ, aEJ), Transform(I_label, aI_label),
                  Transform(J_label, aJ_label),Transform(v,av),Transform(v_label,av_label))
        self.wait(1)

        T_V = Tex(r"$$\mathbf{v}$$",color=PURE_RED).to_corner(UL)
        self.play(Write(T_V))
        self.wait(1)

        T_W = Tex(r"$$\mathbf{W}$$",color=PURE_BLUE)
        aT_V = T_V.copy().set_color(PURE_BLUE)
        vg = VGroup(T_W,aT_V).arrange(RIGHT).to_corner(UL)
        newnp = numberplane.copy()
        aEI = Vector([2, 1], color=RED)
        aEJ = Vector([0.5, 2.5], color=BLUE)
        aI_label = Tex(r"$$\hat{i}$$", color=RED).next_to(aEI, UR)
        aJ_label = Tex(r"$$\hat{j}$$", color=BLUE).next_to(aEJ, UR)
        av = Vector([2.5, 3.5], color=PURE_GREEN)
        av_label = Tex(r"$$\mathbf{v}$$", color=PURE_GREEN).next_to(av, UR)

        v_copy = v.copy().set_color(GRAY)

        self.add(v_copy)
        self.play(Write(T_W),Transform(T_V,aT_V),Transform(newnp, anewnp),Transform(EI, aEI), Transform(EJ, aEJ),
                  Transform(I_label, aI_label),
                  Transform(J_label, aJ_label), Transform(v, av), Transform(v_label, av_label))
        self.wait(1)

        T_W_INV = Tex(r"$$\mathbf{W}^{-1}$$",color=PURE_RED)
        T_eq = Tex(r"$$=$$",color=BLACK)
        T_res = Tex(r"$$\mathbf{v}$$",color=PURE_RED)
        aT_V.set_color(PURE_RED)
        aT_W = T_W.copy().set_color(PURE_RED)
        vg = VGroup(T_W_INV,aT_W, aT_V,T_eq,T_res).arrange(RIGHT).to_corner(UL)

        aEI = Vector([1, 0], color=RED)
        aEJ = Vector([0, 1], color=BLUE)
        aI_label = Tex(r"$$\hat{i}$$", color=RED).next_to(aEI, UR)
        aJ_label = Tex(r"$$\hat{j}$$", color=BLUE).next_to(aEJ, UR)
        av = Vector([1, 1], color=PURE_GREEN)
        av_label = Tex(r"$$\mathbf{v}$$", color=PURE_GREEN).next_to(av, UR)
        self.play(Write(T_W_INV),FadeIn(T_eq,T_res),Transform(T_V,aT_V),Transform(T_W,aT_W),
                  Transform(newnp, numberplane), Transform(numberplane, bnewnp), Transform(EI, aEI), Transform(EJ, aEJ),
                  Transform(I_label, aI_label),
                  Transform(J_label, aJ_label), Transform(v, av), Transform(v_label, av_label)
                  )
        self.wait(1)

        aT_W_INV = T_W_INV.copy()
        vg = VGroup(aT_W_INV, aT_W).arrange(RIGHT).to_corner(UL)
        self.play(FadeOut(numberplane,T_eq,T_res,T_V),Transform(T_W_INV,aT_W_INV),Transform(T_W,aT_W))
        self.wait(1)


        numberplane = NumberPlane(axis_config={"color":BLACK})

        aEI = Vector([2, 1], color=RED)
        aEJ = Vector([0.5, 2.5], color=BLUE)
        aI_label = Tex(r"$$\hat{i}$$", color=RED).next_to(aEI, UR)
        aJ_label = Tex(r"$$\hat{j}$$", color=BLUE).next_to(aEJ, UR)
        av = Vector([2.5, 3.5], color=PURE_GREEN)
        av_label = Tex(r"$$\mathbf{v}$$", color=PURE_GREEN).next_to(av, UR)

        self.add(numberplane)
        self.play(Transform(newnp, anewnp), Transform(EI, aEI), Transform(EJ, aEJ),
                  Transform(I_label, aI_label),
                  Transform(J_label, aJ_label), Transform(v, av), Transform(v_label, av_label))

        aEI = Vector([1, 0], color=RED)
        aEJ = Vector([0, 1], color=BLUE)
        aI_label = Tex(r"$$\hat{i}$$", color=RED).next_to(aEI, UR)
        aJ_label = Tex(r"$$\hat{j}$$", color=BLUE).next_to(aEJ, UR)
        av = Vector([1, 1], color=PURE_GREEN)
        av_label = Tex(r"$$\mathbf{v}$$", color=PURE_GREEN).next_to(av, UR)

        T_eq2 = Tex(r"$$=$$",color=BLACK)
        T_res2 = Tex(r"$$\mathbf{\text{E}}$$",color=BLACK)

        vg = VGroup(aT_W_INV, aT_W,T_eq2,T_res2).arrange(RIGHT).to_corner(UL)

        self.play(Transform(newnp, numberplane.copy()), Transform(EI, aEI), Transform(EJ, aEJ),
                  Transform(I_label, aI_label),
                  Transform(J_label, aJ_label), Transform(v, av), Transform(v_label, av_label),
                  Transform(T_W_INV,aT_W_INV),Transform(T_W,aT_W),Write(T_eq2),Write(T_res2))
        self.wait(1)

        T_eq3 = T_eq2.copy()
        T_res3 = Tex(r"$$\begin{bmatrix}  1&  0&0  & ...\\  0&  1&  0& \\  0& 0 & 1 & \\  \vdots &  &  &\ddots \end{bmatrix}$$",color=BLACK)
        aT_eq2 = T_eq2.copy()
        aT_res2 = T_res2.copy()
        vg = VGroup(aT_W_INV, aT_W, aT_eq2, aT_res2,T_eq3,T_res3).arrange(RIGHT).to_corner(UL)
        t_notice = Text("注明：此处图示以二阶矩阵为例，但其实指任意方阵的变换，所以E的阶数不定",color=GRAY,font_size=25).to_corner(DR)
        self.play(Transform(T_eq2,aT_eq2),Transform(T_res2,aT_res2),Transform(T_W_INV,aT_W_INV),Transform(T_W,aT_W),FadeIn(T_eq3,T_res3),Write(t_notice))
        self.wait(1)

class s3_part3(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60*DEGREES,theta=30*DEGREES)
        ex = Vector([3,0,0],color=PURE_RED)
        ey = Vector([0, 3, 0], color=PURE_BLUE)
        ez = Vector([0, 0, 3], color=PURE_GREEN)
        x_lb = Tex(r"$$x$$",color=PURE_RED).move_to([3,0,-0.25])
        y_lb = Tex(r"$$y$$", color=PURE_BLUE).move_to([0,3,-0.25])
        z_lb = Tex(r"$$z$$", color=PURE_GREEN).move_to([0,0,3+0.25])
        self.add_fixed_orientation_mobjects(x_lb,y_lb,z_lb)
        self.add(ex,ey,ez)
        self.wait(1)
        exc = Vector([3, 0, 0], color=RED)
        eyc = Vector([0, 3, 0], color=BLUE)
        ezc = Vector([0, 0, 3], color=GREEN)
        _x_lb = Tex(r"$$x'$$", color=PURE_RED).move_to([3, 0, -0.25])
        _y_lb = Tex(r"$$y'$$", color=PURE_BLUE).move_to([0, 3, -0.25])
        _z_lb = Tex(r"$$z'$$", color=PURE_GREEN).move_to([0, 0, 3 + 0.25])
        RZT = ValueTracker(0)
        RXT = ValueTracker(0)
        RYT = ValueTracker(0)
        isable = True
        exc.add_updater(lambda m:m.put_start_and_end_on([0,0,0],[3*((sin(RYT.get_value())*sin(RXT.get_value())*sin(RZT.get_value())) + (cos(RYT.get_value())*cos(RZT.get_value()))),
                                                                   3*(cos(RXT.get_value())*sin(RZT.get_value())),
                                                                   3*((cos(RYT.get_value())*sin(RXT.get_value())*sin(RZT.get_value())) - (sin(RYT.get_value())*cos(RZT.get_value())))]) if isable else m)
        eyc.add_updater(lambda m: m.put_start_and_end_on([0, 0, 0],[3*((sin(RYT.get_value())*sin(RXT.get_value())*cos(RZT.get_value())) - (cos(RYT.get_value())*sin(RZT.get_value()))),
                                                                      3*(cos(RXT.get_value())*cos(RZT.get_value())),
                                                                      3*((cos(RYT.get_value())*sin(RXT.get_value())*cos(RZT.get_value())) + (sin(RYT.get_value())*sin(RZT.get_value())))]) if isable else m)
        ezc.add_updater(lambda m:m.put_start_and_end_on([0,0,0],[3*(sin(RYT.get_value())*cos(RXT.get_value())),
                                                                   3*(-sin(RXT.get_value())),
                                                                   3*(cos(RYT.get_value())*cos(RXT.get_value()))]) if isable else m)

        _x_lb.add_updater(lambda m:m.move_to([3*(sin(RYT.get_value())*sin(RXT.get_value())*sin(RZT.get_value()) + cos(RYT.get_value())*cos(RZT.get_value())),
                                                                   3*(cos(RXT.get_value())*sin(RZT.get_value())),
                                                                   3*(cos(RYT.get_value())*sin(RXT.get_value())*sin(RZT.get_value()) - sin(RYT.get_value())*cos(RZT.get_value()))-0.25]) if isable else m)
        _y_lb.add_updater(lambda m:m.move_to([3*(sin(RYT.get_value())*sin(RXT.get_value())*cos(RZT.get_value()) - cos(RYT.get_value())*sin(RZT.get_value())),
                                                                      3*(cos(RXT.get_value())*cos(RZT.get_value())),
                                                                      3*(cos(RYT.get_value())*sin(RXT.get_value())*cos(RZT.get_value()) + sin(RYT.get_value())*sin(RZT.get_value()))-0.25]) if isable else m)
        _z_lb.add_updater(lambda m:m.move_to([3*(sin(RYT.get_value())*cos(RXT.get_value())),
                                                                   3*(-sin(RXT.get_value())),
                                                                   3*(cos(RYT.get_value())*cos(RXT.get_value()))+0.25]) if isable else m)

        self.add_fixed_orientation_mobjects(_x_lb,_y_lb,_z_lb)
        self.add(exc,eyc,ezc)
        self.play(RZT.animate.set_value(30*DEGREES),RXT.animate.set_value(30*DEGREES),RYT.animate.set_value(30*DEGREES))
        self.wait(1)

        t1 = Tex(r"$$\mathbf{A}\mathbf{p}'=\mathbf{p}$$",color=BLACK).to_corner(UL)
        t2 = Tex(r"$$\mathbf{A}^{-1}\mathbf{p}=\mathbf{p}'$$", color=BLACK).next_to(t1,DOWN,aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(t1)
        self.play(Write(t1))
        self.wait(1)
        self.add_fixed_in_frame_mobjects(t2)
        self.play(Write(t2))
        self.wait(1)

        RZT.set_value(0)
        RXT.set_value(0)
        RYT.set_value(0)

        self.play(RZT.animate.set_value(30*DEGREES),RXT.animate.set_value(45*DEGREES),RYT.animate.set_value(60*DEGREES))
        self.wait(1)

        arcZ = Arc(radius=0.5,start_angle=0,angle=TAU,arc_center=[0,0,2],stroke_width=10,color=PURE_GREEN)
        arrZ = SVGMobject("arrow.svg").scale(0.25).move_to([0.5*cos(30*DEGREES),0.5*sin(30*DEGREES),2])
        arcX = Arc(radius=0.5, start_angle=0, angle=TAU, arc_center=[2, 0, 0], stroke_width=10,
                   color=PURE_RED)
        arcX.rotate(90*DEGREES,UP)
        arrX = SVGMobject("arrow.svg").rotate(90*DEGREES,IN).scale(0.25).move_to([2, 0.5 * sin(30 * DEGREES), 0.5 * cos(30 * DEGREES)])
        arcY = Arc(radius=0.5, start_angle=0, angle=TAU, arc_center=[0, 2, 0], stroke_width=10,
                   color=PURE_BLUE)
        arcY.rotate(90*DEGREES,LEFT)
        arrY = SVGMobject("arrow.svg").rotate(90 * DEGREES, IN).scale(0.25).move_to(
            [0.5, 2,0])

        RZT.set_value(0)
        RXT.set_value(0)
        RYT.set_value(0)
        self.add_fixed_orientation_mobjects(arrZ)
        self.play(RZT.animate.set_value(30*DEGREES),Create(arcZ),FadeIn(arrZ))
        self.play(RXT.animate.set_value(45*DEGREES),Create(arcX),FadeIn(arrX))
        self.add_fixed_orientation_mobjects(arrY)
        self.play(RYT.animate.set_value(60*DEGREES),Create(arcY),FadeIn(arrY))
        self.wait(1)
        isable = False
        exc.add_updater(lambda m:m.put_start_and_end_on([0,0,0],[3*cos(RYT.get_value())*cos(RZT.get_value()),
                                                                 3*cos(RYT.get_value())*sin(RZT.get_value()),
                                                                 3*(-sin(RYT.get_value()))]) if (not isable) else m)
        eyc.add_updater(lambda m: m.put_start_and_end_on([0, 0, 0], [3 * (sin(RXT.get_value())*sin(RYT.get_value())*cos(RZT.get_value()) - cos(RXT.get_value())*sin(RZT.get_value())),
                                                                     3 * (sin(RXT.get_value())*sin(RYT.get_value())*cos(RZT.get_value()) + cos(RXT.get_value())*cos(RZT.get_value())),
                                                                     3 * sin(RXT.get_value())*cos(RYT.get_value())]) if (not isable) else m)
        ezc.add_updater(lambda m: m.put_start_and_end_on([0, 0, 0], [3 * (cos(RXT.get_value())*sin(RYT.get_value())*cos(RZT.get_value()) + sin(RXT.get_value())*sin(RZT.get_value())),
                                                                     3 * (cos(RXT.get_value())*sin(RYT.get_value())*sin(RZT.get_value()) - sin(RXT.get_value())*cos(RZT.get_value())),
                                                                     3 * (cos(RXT.get_value())*cos(RYT.get_value()))]) if (not isable) else m)
        _x_lb.add_updater(lambda m:m.move_to([3*cos(RYT.get_value())*cos(RZT.get_value()),
                                                                 3*cos(RYT.get_value())*sin(RZT.get_value()),
                                                                 3*(-sin(RYT.get_value()))]) if (not isable) else m)
        _y_lb.add_updater(lambda m:m.move_to([3 * (sin(RXT.get_value())*sin(RYT.get_value())*cos(RZT.get_value()) - cos(RXT.get_value())*sin(RZT.get_value())),
                                                                     3 * (sin(RXT.get_value())*sin(RYT.get_value())*cos(RZT.get_value()) + cos(RXT.get_value())*cos(RZT.get_value())),
                                                                     3 * sin(RXT.get_value())*cos(RYT.get_value())]) if (not isable) else m)
        _z_lb.add_updater(lambda m:m.move_to([3 * (cos(RXT.get_value())*sin(RYT.get_value())*cos(RZT.get_value()) + sin(RXT.get_value())*sin(RZT.get_value())),
                                                                     3 * (cos(RXT.get_value())*sin(RYT.get_value())*sin(RZT.get_value()) - sin(RXT.get_value())*cos(RZT.get_value())),
                                                                     3 * (cos(RXT.get_value())*cos(RYT.get_value()))]) if (not isable) else m)

        RXT.set_value(0)
        RYT.set_value(0)
        RZT.set_value(0)
        self.remove(arcX,arcY,arcZ,arrX,arrY,arrZ)
        self.play(RXT.animate.set_value(45*DEGREES),Create(arcX),FadeIn(arrX))
        self.add_fixed_orientation_mobjects(arrY)
        self.play(RYT.animate.set_value(60 * DEGREES), Create(arcY), FadeIn(arrY))
        self.add_fixed_orientation_mobjects(arrZ)
        self.play(RZT.animate.set_value(30 * DEGREES), Create(arcZ), FadeIn(arrZ))
        self.wait(1)
        isable = True
        RXT.set_value(0)
        RYT.set_value(0)
        RZT.set_value(0)
        self.remove(arcX, arcY, arcZ, arrX, arrY, arrZ)
        self.add_fixed_orientation_mobjects(arrZ)
        self.play(RZT.animate.set_value(30 * DEGREES), Create(arcZ), FadeIn(arrZ))
        self.play(RXT.animate.set_value(45 * DEGREES), Create(arcX), FadeIn(arrX))
        self.add_fixed_orientation_mobjects(arrY)
        self.play(RYT.animate.set_value(60 * DEGREES), Create(arcY), FadeIn(arrY))
        self.wait(1)

        vec = Vector([3,3,3],color=ORANGE)
        vec_l = Tex(r"$$\mathbf{v}'$$",color=ORANGE).move_to([3,3,3.25])
        veccopy = vec.copy().set_color(GRAY)
        veccopy_l = Tex(r"$$\mathbf{v}$$",color=GRAY).move_to([3,3,3.25])

        vec.add_updater(lambda m:m.put_start_and_end_on([0,0,0],[3*(sin(RYT.get_value())*sin(RXT.get_value())*sin(RZT.get_value()) + sin(RYT.get_value())*sin(RXT.get_value())*cos(RZT.get_value()) + sin(RYT.get_value())*cos(RXT.get_value()) + cos(RYT.get_value())*cos(RZT.get_value()) - cos(RYT.get_value())*sin(RZT.get_value())),
                                                                 3*(cos(RXT.get_value())*cos(RZT.get_value()) + cos(RXT.get_value())*sin(RZT.get_value()) - sin(RXT.get_value())),
                                                                 3*(cos(RYT.get_value())*sin(RXT.get_value())*cos(RZT.get_value()) + cos(RYT.get_value())*sin(RXT.get_value())*sin(RZT.get_value()) + cos(RYT.get_value())*cos(RXT.get_value()) + sin(RYT.get_value())*sin(RZT.get_value()) - sin(RYT.get_value())*cos(RZT.get_value()))]))
        vec_l.add_updater(lambda m: m.move_to([
            3*(sin(RYT.get_value()) * sin(RXT.get_value()) * sin(RZT.get_value()) + sin(RYT.get_value()) * sin(
                RXT.get_value()) * cos(RZT.get_value()) + sin(RYT.get_value()) * cos(RXT.get_value()) + cos(
                RYT.get_value()) * cos(RZT.get_value()) - cos(RYT.get_value()) * sin(RZT.get_value())),
            3*(cos(RXT.get_value()) * cos(RZT.get_value()) + cos(RXT.get_value()) * sin(RZT.get_value()) - sin(
                RXT.get_value())),
            3*(cos(RYT.get_value()) * sin(RXT.get_value()) * cos(RZT.get_value()) + cos(RYT.get_value()) * sin(
                RXT.get_value()) * sin(RZT.get_value()) + cos(RYT.get_value()) * cos(RXT.get_value()) + sin(
                RYT.get_value()) * sin(RZT.get_value()) - sin(RYT.get_value()) * cos(RZT.get_value()))+0.25]))

        RXT.set_value(0)
        RYT.set_value(0)
        RZT.set_value(0)
        self.remove(arcX, arcY, arcZ, arrX, arrY, arrZ,t1,t2)
        TTTT = Tex(r"$$\mathbf{v}'=\mathbf{R}_z(\theta)\mathbf{v}$$",color=BLACK).to_corner(UL)
        TTTT2 = Tex(r"$$\mathbf{v}'=\mathbf{R}_x(\phi)\mathbf{R}_z(\theta)\mathbf{v}$$",color=BLACK).to_corner(UL)
        TTTT3 = Tex(r"$$\mathbf{v}'=\mathbf{R}_z(\psi)\mathbf{R}_x(\phi)\mathbf{R}_z(\theta)\mathbf{v}=\mathbf{R}(\theta,\phi,\psi)v$$",color=BLACK).to_corner(UL)
        self.add_fixed_in_frame_mobjects(TTTT)
        self.add_fixed_orientation_mobjects(arrZ,vec_l,veccopy_l)
        self.add(veccopy,vec)
        self.play(RZT.animate.set_value(30 * DEGREES), Create(arcZ), FadeIn(arrZ),FadeIn(vec_l),Write(TTTT))
        self.add_fixed_in_frame_mobjects(TTTT2)
        self.play(RXT.animate.set_value(45 * DEGREES), Create(arcX), FadeIn(arrX),FadeIn(TTTT2),FadeOut(TTTT))
        self.add_fixed_orientation_mobjects(arrY)
        self.add_fixed_in_frame_mobjects(TTTT3)
        self.play(RYT.animate.set_value(60 * DEGREES), Create(arcY), FadeIn(arrY),FadeIn(TTTT3),FadeOut(TTTT2))
        self.wait(1)

        TRZ = Tex(r"$$\mathbf{R}_z(\theta)$$",color=BLACK).to_corner(UL)
        self.add_fixed_in_frame_mobjects(TRZ)
        self.play(RXT.animate.set_value(0),RYT.animate.set_value(0),RZT.animate.set_value(0),FadeOut(vec,veccopy,vec_l,veccopy_l,TTTT3,arcX, arcY, arcZ, arrX, arrY, arrZ),FadeIn(TRZ))
        self.wait(1)
        self.play(FadeIn(arrZ),Create(arcZ))
        self.wait(1)
        self.move_camera(theta=-90*DEGREES,phi=0,added_anims=[FadeOut(arrZ,_x_lb,_y_lb,_z_lb),Create(arcZ)])
        self.play(Create(arcZ))
        self.wait(1)

        ARR = Arc(radius=0.5,start_angle=0,angle=TAU,stroke_width=10,color=GRAY)
        self.add_fixed_in_frame_mobjects(ARR)
        self.move_camera(theta=0,added_anims=[Create(ARR)])
        self.move_camera(phi= 90*DEGREES,added_anims=[Create(arcX)])
        self.play(Create(arcX))
        self.wait(1)

        self.move_camera(theta=90*DEGREES,added_anims=[Create(ARR),Create(arcY)])
        self.play(Create(arcY))
        self.wait(1)
        self.move_camera(phi=60*DEGREES,theta=30*DEGREES,added_anims=[FadeOut(ARR),Create(arcX),Create(arcY),Create(arcZ)])
        self.play(Create(arcX),Create(arcY),Create(arcZ),FadeIn(arrY,arrX,arrZ))
        self.wait(1)
        self.play(FadeOut(arcX,arcY,arcZ,arrX,arrY,arrZ))
        self.wait(1)

        aTRZ = Tex(r"$$\mathbf{R}_z(\theta)=\begin{bmatrix}  ?&  ?& ?\\ ? &?  &? \\  ?& ? &?\end{bmatrix}$$",color=BLACK).to_corner(UL)
        arcTheta1 = Arc(radius=0.5,start_angle=0,angle=30*DEGREES,color=BLACK)
        arcTheta2 = Arc(radius=0.5, start_angle=90*DEGREES, angle=30 * DEGREES, color=BLACK)
        theta_l1 = Tex(r"$$\theta$$",color=BLACK).move_to([1,0.25,0])
        theta_l2 = Tex(r"$$\theta$$", color=BLACK).move_to([-0.25, 1, 0])
        self.add_fixed_in_frame_mobjects(aTRZ)
        self.play(RZT.animate.set_value(30*DEGREES),FadeIn(_x_lb,_y_lb,aTRZ,theta_l1,theta_l2),FadeOut(TRZ),Create(arcTheta1),Create(arcTheta2))
        self.wait(1)
        TRZ = Tex(r"$$\mathbf{R}_z(\theta)=\begin{bmatrix}  ?&  ?& 0\\ ? &?  &0 \\  ?& ? &1\end{bmatrix}$$",color=BLACK).to_corner(UL)
        self.add_fixed_in_frame_mobjects(TRZ)
        self.play(FadeOut(aTRZ),FadeIn(TRZ))
        self.wait(1)

        OPX = DashedLine([0,0,0],[3*cos(30*DEGREES),0,0],color=RED_A,stroke_width=10)
        XPX = DashedLine([3*cos(30 * DEGREES), 3*sin(30 * DEGREES), 0], [3*cos(30 * DEGREES), 0, 0], color=BLUE_A, stroke_width=10)
        OPY = DashedLine([0,0,0],[0,3*cos(30*DEGREES),0],color=BLUE_A,stroke_width=10)
        YPY = DashedLine([-3*sin(30*DEGREES), 3*cos(30 * DEGREES), 0], [0, 3*cos(30 * DEGREES), 0], color=RED_A, stroke_width=10)
        ZR1 = Tex(r"$$\cos \theta$$",color=RED).move_to([1.5*cos(30*DEGREES),-0.25,0])
        ZR2 = Tex(r"$$\sin \theta$$", color=BLUE).move_to([3*cos(30 * DEGREES)+0.25, 1.5*sin(30 * DEGREES), 0])
        ZR3 = Tex(r"$$\cos \theta$$", color=BLUE).move_to([0.25, 1.5*cos(30 * DEGREES), 0])
        ZR4 = Tex(r"$$-\sin \theta$$", color=RED).move_to([-1.5*sin(30*DEGREES), 3*cos(30 * DEGREES)+0.5, 0])

        T_XP = Tex(r"$$x'=\begin{bmatrix} \cos \theta\\ \sin \theta \\0\end{bmatrix}$$",color=RED).next_to(TRZ,DOWN,aligned_edge=LEFT)
        T_YP = Tex(r"$$y'=\begin{bmatrix} -\sin\theta\\ \cos\theta \\0\end{bmatrix}$$",color=BLUE).next_to(T_XP,DOWN,aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(T_XP,T_YP)
        self.add_fixed_orientation_mobjects(ZR1,ZR2,ZR3,ZR4)
        self.play(FadeIn(ZR1,ZR2,ZR3,ZR4,OPX,XPX,OPY,YPY,T_XP,T_YP))
        self.wait(1)
        aTRZ = Tex(r"$$\mathbf{R}_z(\theta)=\begin{bmatrix}  \cos \theta&-\sin \theta& 0\\ \sin \theta  &\cos \theta &0 \\  0& 0 &1\end{bmatrix}$$",color=BLACK).to_corner(UL)
        self.add_fixed_in_frame_mobjects(aTRZ)
        self.play(FadeOut(TRZ),FadeIn(aTRZ))
        self.wait(1)

        self.play(FadeOut(_x_lb,_y_lb,theta_l1,theta_l2,arcTheta1,arcTheta2,T_XP,T_YP,OPX,XPX,OPY,YPY,ZR1,ZR2,ZR3,ZR4),RZT.animate.set_value(0))
        self.wait(1)

        self.play(RXT.animate.set_value(30*DEGREES),FadeIn(_y_lb,_z_lb))
        self.wait(1)
        TRX = Tex(r"$$\mathbf{R}_x(\phi)=\begin{bmatrix}  1& 0 & 0\\ 0 &  \cos \phi& -\sin \phi\\  0& \sin \phi & \cos \phi\end{bmatrix}$$",color=BLACK).next_to(aTRZ,DOWN,aligned_edge=LEFT)
        t_el = Tex(r"$$y'=\begin{bmatrix} 0\\ \cos \phi  \\ \sin \phi \end{bmatrix}$$$$z'=\begin{bmatrix} 0\\ -\sin\phi  \\ \cos \phi \end{bmatrix}$$",color=BLACK).next_to(TRX,DOWN,aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(TRX,t_el)
        self.play(Write(TRX),Write(t_el))
        self.wait(1)
        self.play(FadeOut(t_el,_z_lb,_y_lb), RXT.animate.set_value(0))
        self.wait(1)
        self.play(RYT.animate.set_value(30*DEGREES),FadeIn(_x_lb,_z_lb))
        self.wait(1)
        TRY = Tex(r"$$\mathbf{R}_y(\psi) = \begin{bmatrix} \cos \psi & 0 & \sin \psi \\  0& 1 & 0\\-\sin \psi  & 0 & \cos \psi\end{bmatrix}$$",color=BLACK).to_corner(UR)
        t_ell = Tex(r"$$x'=\begin{bmatrix} \cos \psi\\ 0\\-\sin \psi\end{bmatrix}$$ $$z'=\begin{bmatrix} \sin \psi\\ 0\\\cos \psi\end{bmatrix}$$",color=BLACK).next_to(TRY,DOWN,aligned_edge=RIGHT)
        self.add_fixed_in_frame_mobjects(TRY,t_ell)
        self.play(Write(TRY),Write(t_ell))
        self.wait(1)
        self.play(FadeOut(t_ell,_x_lb,_z_lb),TRY.animate.set_value(0))
        self.wait(1)

        RXT.set_value(0)
        RYT.set_value(0)
        RZT.set_value(0)
        t_all = Tex(r"$$\mathbf{R}(\theta,\phi,\psi)=\mathbf{R}_z(\theta)$$",color=BLACK).to_corner(DR)
        self.add_fixed_in_frame_mobjects(t_all)
        self.play(FadeIn(t_all,_x_lb,_y_lb),RZT.animate.set_value(30*DEGREES))
        at_all = Tex(r"$$\mathbf{R}(\theta,\phi,\psi)=\mathbf{R}_x(\phi)\mathbf{R}_z(\theta)$$",color=BLACK).next_to(TRY,DOWN,aligned_edge=LEFT).to_corner(DR)
        self.add_fixed_in_frame_mobjects(at_all)
        self.play(FadeIn(at_all,_z_lb),FadeOut(t_all),RXT.animate.set_value(45*DEGREES))
        t_all = Tex(r"$$\mathbf{R}(\theta,\phi,\psi)=\mathbf{R}_y(\psi)\mathbf{R}_x(\phi)\mathbf{R}_z(\theta)$$", color=PURE_RED).next_to(TRY, DOWN, aligned_edge=LEFT).to_corner(DR)
        self.add_fixed_in_frame_mobjects(t_all)
        self.play(FadeIn(t_all),FadeOut(at_all),RYT.animate.set_value(60*DEGREES))
        self.wait(1)
        self.play(FadeOut(_x_lb,_y_lb,_z_lb,x_lb,y_lb,z_lb,ex,ey,ez,exc,eyc,ezc),TRY.animate.next_to(TRX,DOWN,aligned_edge=LEFT),t_all.animate.center().to_edge(RIGHT))
        self.wait(1)
        t_inv = Tex(r"$$\mathbf{R}^{-1}=???$$",color=BLACK).next_to(t_all.copy().to_corner(UR),DOWN,aligned_edge=RIGHT)
        self.add_fixed_in_frame_mobjects(t_inv)
        self.play(t_all.animate.to_corner(UR),Write(t_inv))
        self.wait(1)
        at_inv = Tex(r"$$\mathbf{R}^{-1} \mathbf{R}=\mathbf{\text{E}}$$",color=BLACK).next_to(t_all,DOWN,aligned_edge=RIGHT)
        t_horrible = Text("\"It's horrible, just horrible!\"",color=PURE_RED,font_size=25).to_corner(DR)
        self.add_fixed_in_frame_mobjects(at_inv,t_horrible)
        self.play(FadeOut(t_inv),FadeIn(at_inv),Write(t_horrible))
        self.wait(1)
        self.play(FadeOut(t_horrible,TRX,TRY,aTRZ,t_all),at_inv.animate.center())
        self.wait(1)
        t_ggg = Tex(r"$$ax^2+bx+c=0$$$$x ={-b \pm \sqrt{b^2-4ac}\over 2a} $$",color=BLACK)
        self.add_fixed_in_frame_mobjects(t_ggg)
        self.play(at_inv.animate.to_edge(UP),Write(t_ggg))
        self.wait(1)
        at_ggg = Tex(r"$$x^2=c$$$$x=\sqrt[]{c}$$",color=BLACK)
        self.add_fixed_in_frame_mobjects(at_ggg)
        self.play(FadeOut(t_ggg),FadeIn(at_ggg))
        self.wait(1)
        t_inv = Tex(r"$$\mathbf{R}$$",color=BLACK)
        self.add_fixed_in_frame_mobjects(t_inv)
        self.play(FadeOut(at_ggg,at_inv),FadeIn(t_inv))
        self.wait(1)

class s4(Scene):
    def construct(self):
        nbp = NumberPlane(axis_config={"color":BLACK})
        ex = Vector([1,0],color=PURE_RED)
        ey = Vector([0,1],color=PURE_BLUE)
        x_label = Tex(r"$$\hat{i}$$",color=PURE_RED).move_to([1.25,0,0])
        y_label = Tex(r"$$\hat{j}$$", color=PURE_BLUE).move_to([0, 1.25,0])
        self.wait(1)
        self.play(Create(nbp),Create(ex),Create(ey),Write(x_label),Write(y_label))
        self.wait(1)

        nnn = nbp.copy()
        anbp = NumberPlane(axis_config={"color": GRAY}, background_line_style={"stroke_color": YELLOW_D},
                            x_axis_config={"rotation":30*DEGREES},
                            y_axis_config={"rotation":120*DEGREES})
        t_R = Tex(r"$$\mathbf{R}$$",color=BLACK).to_corner(UL)
        aex = Vector([cos(30*DEGREES),sin(30*DEGREES)],color=PURE_RED)
        aey = Vector([-sin(30 * DEGREES),cos(30 * DEGREES)], color=PURE_BLUE)
        ax_label = Tex(r"$$\hat{i}$$", color=PURE_RED).move_to([cos(30*DEGREES)+0.25, sin(30*DEGREES), 0])
        ay_label = Tex(r"$$\hat{j}$$", color=PURE_BLUE).move_to([-sin(30 * DEGREES), cos(30 * DEGREES)+0.25, 0])
        self.play(Transform(nnn,anbp),Write(t_R),Transform(ex,aex),Transform(ey,aey),Transform(x_label,ax_label),Transform(y_label,ay_label))
        self.wait(1)
        t2 = Tex(r"$$=\begin{bmatrix} \hat{i} &\hat{j}\end{bmatrix}$$",color=BLACK).next_to(t_R,DOWN,aligned_edge=LEFT)
        t3 = Tex(r"$$\left \| \hat{i}  \right \| = \left \| \hat{j}  \right \| =1$$",color=BLACK).next_to(t2,DOWN,aligned_edge=LEFT)
        t3_ = Tex(r"$$\hat{i}\cdot \hat{j}=0$$",color=BLACK).next_to(t3,DOWN,aligned_edge=LEFT)
        self.play(Write(t2),Write(t3),Write(t3_))
        self.wait(1)
        tdarr1 = Tex(r"$$\Downarrow $$",color=BLACK).next_to(t3_,DOWN)
        t4 = Tex(r"$$\mathbf{R}^{\top}\mathbf{R}=\mathbf{\text{E}} $$",color=PURE_RED).next_to(tdarr1,DOWN).to_edge(LEFT)
        self.play(Write(t4),Write(tdarr1))
        self.wait(1)
        tdarr2 = Tex(r"$$\Downarrow $$",color=BLACK).next_to(t4,DOWN)
        t5 = Tex(r"$$\mathbf{R}^{-1}=\mathbf{R}^{\top}$$",color=PURE_RED).next_to(tdarr2,DOWN).to_edge(LEFT)
        self.play(Write(tdarr2),Write(t5))
        self.wait(1)
        t6 = Tex(r"$$\begin{bmatrix}  a& b & c\\ d & e & f\\ g & h &i\end{bmatrix}^{\top}=\begin{bmatrix} a & d & g\\  b& e & h\\  c&  f&i\end{bmatrix}$$",color=BLACK).to_corner(UR)
        t7 = Tex(r"$$\begin{bmatrix}  a& b & c\\ d & e &f\end{bmatrix}^{\top}=\begin{bmatrix}  a& d\\  b& e\\  c&f\end{bmatrix}$$",color=BLACK).next_to(t6,DOWN,aligned_edge=RIGHT)
        self.play(Write(t6),Write(t7))
        self.wait(1)

class s4_part2(Scene):
    def construct(self):
        t1 = Tex(r"$$\hat{i}\cdot\hat{i}=1$$",color=BLACK).to_corner(UL)
        self.wait(1)
        self.play(Write(t1))
        self.wait(1)
        t2 = Tex(r"$$\hat{i}\cdot\hat{j}=0$$",color=BLACK).next_to(t1,DOWN,aligned_edge=LEFT)
        self.play(Write(t2))
        self.wait(1)
        t3 = Tex(r"$$\begin{bmatrix}  \mathbf{a}_{1,1}&\mathbf{a}_{1,2} &\cdots\\  \mathbf{a}_{2,1}&\mathbf{a}_{1,2} & \\ \vdots& &\ddots\end{bmatrix}\begin{bmatrix}\mathbf{b}_{1} \\ \mathbf{b}_{2} \\\vdots \end{bmatrix}$$",
                 color=BLACK).to_corner(UR)
        t4 = Tex(r"$$=\mathbf{b}_1\begin{bmatrix}\mathbf{a}_{1,1} \\ \mathbf{a}_{2,1}\\\vdots \end{bmatrix} +\mathbf{b}_2\begin{bmatrix}\mathbf{a}_{1,2} \\ \mathbf{a}_{2,2}\\\vdots \end{bmatrix} + \cdots$$",color=BLACK).next_to(t3,DOWN,aligned_edge=RIGHT)
        t5 = Tex(r"$$=\begin{bmatrix}\mathbf{b}_1 \mathbf{a}_{1,1}+\mathbf{b}_2 \mathbf{a}_{1,2}+\cdots  \\\mathbf{b}_1 \mathbf{a}_{2,1}+\mathbf{b}_2 \mathbf{a}_{2,2}+\cdots   \\\vdots\end{bmatrix}$$",
                 color=BLACK).next_to(t4,DOWN,aligned_edge=RIGHT)
        self.play(Write(t3),Write(t4),Write(t5))
        self.wait(1)
        t6 = Tex(r"$$=\begin{bmatrix}\mathbf{b}\cdot \mathbf{a}_1 \\\mathbf{b}\cdot \mathbf{a}_2 \\\vdots \end{bmatrix}$$",color=BLACK).next_to(t3,DOWN,aligned_edge=RIGHT)
        self.play(Write(t6),FadeOut(t4,t5))
        self.wait(1)
        self.play(FadeOut(t3,t6))
        T1 = Tex(r"$$\mathbf{A}=\begin{bmatrix} \hat{i}  &\hat{j} \\\end{bmatrix}=\begin{bmatrix} \hat{i}_x  &\hat{j}_x \\ \hat{i}_y  &\hat{j}_y\end{bmatrix}$$",color=BLACK).next_to(t2,DOWN,aligned_edge=LEFT)
        self.play(Write(T1))
        self.wait(1)
        T2 = Tex(r"$$\mathbf{A}^{\top}=\begin{bmatrix} \hat{i}_x &\hat{i}_y  \\ \hat{j}_x  &\hat{j}_y \end{bmatrix}=\begin{bmatrix}\hat{i}^{\top} \\\hat{j}^{\top} \end{bmatrix}$$",
                 color=BLACK).next_to(T1,DOWN,aligned_edge=LEFT)
        self.play(Write(T2))
        self.wait(1)
        T3 = Tex(r"$$\mathbf{A}^{\top}\mathbf{A}=\begin{bmatrix}\hat{i}^{\top}  \\\hat{j}^{\top}\end{bmatrix}\begin{bmatrix} \hat{i}  & \hat{j} \end{bmatrix}$$",color=BLACK).next_to(T2,DOWN,aligned_edge=LEFT)
        self.play(Write(T3))
        self.wait(1)
        T4 = Tex(r"$$=\begin{bmatrix}\begin{bmatrix} \hat{i}^{\top} \\\hat{j}^{\top}\end{bmatrix}\hat{i}  &  \begin{bmatrix}\hat{i}^{\top} \\\hat{j}^{\top}\end{bmatrix}\hat{j} \end{bmatrix}$$",
                 color=BLACK).next_to(T3,DOWN,aligned_edge=LEFT)
        self.play(Write(T4))
        self.wait(1)
        T5 = Tex(r"$$\begin{bmatrix} \hat{i}^{\top} \\ \hat{j}^{\top}\end{bmatrix}\hat{i}=\begin{bmatrix}\hat{i}\cdot \hat{i}   \\\hat{j}\cdot \hat{i}\end{bmatrix} =\begin{bmatrix}1 \\0\end{bmatrix}$$",
                 color=BLACK).to_corner(UR)
        self.play(Write(T5))
        self.wait(1)
        aT5 = Tex(r"$$\begin{bmatrix} \hat{i}^{\top} \\ \hat{j}^{\top}\end{bmatrix}\hat{j}=\begin{bmatrix}\hat{i}\cdot \hat{j}   \\\hat{j}\cdot \hat{j}\end{bmatrix} =\begin{bmatrix}0 \\1\end{bmatrix}$$",
                 color=BLACK).to_corner(UR)
        self.play(Transform(T5,aT5))
        self.wait(1)
        T6 = Tex(r"$$=\begin{bmatrix}1  & 0\\0  &1\end{bmatrix}=\mathbf{\text{E}}$$",color=PURE_RED).next_to(T4,RIGHT)
        self.play(Write(T6))
        self.wait(1)
        self.play(FadeOut(t1,t2,T1,T2,T3,T4,T5,T6))
        self.wait(1)
        TT1 = Tex(r"$$\mathbf{\text{O} }(n)=\left \{ \mathbf{A}\in  \mathbb{R}^{n\times n}\mid \mathbf{A}^{\top}\mathbf{A}=\mathbf{\text{E} }  \right \}  $$",color=BLACK)
        t_ntc = Text("注明：群和集合虽然不完全一样，但是包含了集合的所有特性\n考虑到本期视频不会用到群区别于集合的地方，就把它当作集合吧！",color=GRAY,font_size=20).to_corner(DR)
        self.play(Write(TT1),Write(t_ntc))
        self.wait(1)
        TT2 = Tex(r"$$\not \forall \mathbf{A}\in\mathbf{\text{O} }=\mathbf{R} $$",color=BLACK)
        aTT1 = TT1.copy()
        v = VGroup(aTT1,TT2).arrange(DOWN)
        self.play(Transform(TT1,aTT1),Write(TT2),FadeOut(t_ntc))
        self.wait(1)
        TT3 = Tex(r"$$\mathbf{\text{SO}}(n)=\left \{ \mathbf{A}\in \mathbb{R}^{n\times n}\mid \mathbf{A}^{\top}\mathbf{A}=\mathbf{\text{E}},\text{det}(\mathbf{A})=1   \right \} $$",color=BLACK)
        self.play(FadeOut(TT2),Transform(TT1,TT3))
        self.wait(1)

class s4_part3(Scene):
    def construct(self):
        nbp = NumberPlane(axis_config={"color":BLACK})
        ei = Vector([1,0],color=PURE_RED)
        ej = Vector([0, 1], color=PURE_BLUE)
        self.add(nbp,ei,ej)
        self.wait(1)
        cnbp = nbp.copy()
        anbp = NumberPlane(axis_config={"color": GRAY}, background_line_style={"stroke_color": YELLOW_D},
                           x_axis_config={"rotation": 15 * DEGREES,"unit_size":2},
                           y_axis_config={"rotation": 75 * DEGREES})
        po = Polygon([0,0,0],[1,0,0],[1,1,0],[0,1,0],color=BLACK,stroke_width=0)
        self.play(Create(po))
        self.wait(1)
        det = Polygon([0, 0, 0], [2 * cos(15 * DEGREES), 2 * sin(15 * DEGREES), 0],
                      [2 * cos(15 * DEGREES) + cos(75 * DEGREES), 2 * sin(15 * DEGREES) + sin(75 * DEGREES), 0],
                      [cos(75 * DEGREES), sin(75 * DEGREES), 0], color=RED,fill_opacity=0.75,stroke_width=0)
        aei = Vector([2 * cos(15 * DEGREES), 2 * sin(15 * DEGREES)], color=PURE_RED)
        aej = Vector([cos(75 * DEGREES), sin(75 * DEGREES)], color=PURE_BLUE)
        self.play(Transform(cnbp,anbp),Transform(po,det),Transform(ei,aei),Transform(ej,aej))
        self.wait(1)
        T1 = Tex(r"$$\text{AREA}=\left | \text{det}(\mathbf{A})  \right | $$",color=PURE_RED).to_edge(DOWN)
        self.play(Write(T1))
        self.wait(1)
        anbp = NumberPlane(axis_config={"color": GRAY}, background_line_style={"stroke_color": YELLOW_D},
                           x_axis_config={"rotation": 30 * DEGREES},
                           y_axis_config={"rotation": 120 * DEGREES})
        det = Polygon([0, 0, 0], [cos(30 * DEGREES), sin(30 * DEGREES), 0],
                      [cos(30 * DEGREES) + cos(120 * DEGREES), sin(30 * DEGREES) + sin(120 * DEGREES), 0],
                      [cos(120 * DEGREES), sin(120 * DEGREES), 0], color=RED, fill_opacity=0.75, stroke_width=0)
        aei = Vector([cos(30 * DEGREES), sin(30 * DEGREES)], color=PURE_RED)
        aej = Vector([cos(120 * DEGREES), sin(120 * DEGREES)], color=PURE_BLUE)
        self.play(Transform(cnbp,anbp),Transform(po,det),Transform(ei,aei),Transform(ej,aej))
        anbp = NumberPlane(axis_config={"color": GRAY}, background_line_style={"stroke_color": YELLOW_D},
                           x_axis_config={"rotation": 60 * DEGREES},
                           y_axis_config={"rotation": 150 * DEGREES})
        det = Polygon([0, 0, 0], [cos(60 * DEGREES), sin(60 * DEGREES), 0],
                      [cos(60 * DEGREES) + cos(150 * DEGREES), sin(60 * DEGREES) + sin(150 * DEGREES), 0],
                      [cos(150 * DEGREES), sin(150 * DEGREES), 0], color=RED, fill_opacity=0.75, stroke_width=0)
        aei = Vector([cos(60 * DEGREES), sin(60 * DEGREES)], color=PURE_RED)
        aej = Vector([cos(150 * DEGREES), sin(150 * DEGREES)], color=PURE_BLUE)
        aT1 = Tex(r"$$\left | \text{det}(\mathbf{\text{O}}) \right | =\text{AREA}=1$$",color=PURE_RED).to_edge(DOWN)
        self.play(Transform(cnbp, anbp), Transform(po, det), Transform(ei, aei), Transform(ej, aej),Transform(T1,aT1))
        self.wait(1)
        aT1 = Tex(r"$$\text{det}(\mathbf{\text{O}})  =\pm 1$$", color=PURE_RED).to_edge(DOWN)
        self.play(Transform(T1,aT1))
        self.wait(1)
        T2 = Tex(r"$$\text{det}(\mathbf{\text{A}})>0$$", color=BLACK).to_corner(UL)
        self.play(Write(T2))
        self.wait(1)
        anbp = NumberPlane(axis_config={"color": GRAY}, background_line_style={"stroke_color": YELLOW_D},
                           x_axis_config={"rotation": 240 * DEGREES},
                           y_axis_config={"rotation": 150 * DEGREES})
        det = Polygon([0, 0, 0], [cos(240 * DEGREES), sin(240 * DEGREES), 0],
                      [cos(240 * DEGREES) + cos(150 * DEGREES), sin(240 * DEGREES) + sin(150 * DEGREES), 0],
                      [cos(150 * DEGREES), sin(150 * DEGREES), 0], color=GREEN, fill_opacity=0.75, stroke_width=0)
        aei = Vector([cos(240 * DEGREES), sin(240 * DEGREES)], color=PURE_RED)
        aej = Vector([cos(150 * DEGREES), sin(150 * DEGREES)], color=PURE_BLUE)
        aT2 = Tex(r"$$\text{det}(\mathbf{\text{A}})<0$$", color=BLACK).to_corner(UL)
        self.play(Transform(cnbp, anbp), Transform(po, det), Transform(ei, aei), Transform(ej, aej), Transform(T2, aT2))
        self.wait(1)
        anbp = NumberPlane(axis_config={"color": GRAY}, background_line_style={"stroke_color": YELLOW_D},
                           x_axis_config={"rotation": 60 * DEGREES},
                           y_axis_config={"rotation": 150 * DEGREES})
        det = Polygon([0, 0, 0], [cos(60 * DEGREES), sin(60 * DEGREES), 0],
                      [cos(60 * DEGREES) + cos(150 * DEGREES), sin(60 * DEGREES) + sin(150 * DEGREES), 0],
                      [cos(150 * DEGREES), sin(150 * DEGREES), 0], color=RED, fill_opacity=0.75, stroke_width=0)
        aei = Vector([cos(60 * DEGREES), sin(60 * DEGREES)], color=PURE_RED)
        aej = Vector([cos(150 * DEGREES), sin(150 * DEGREES)], color=PURE_BLUE)
        aT1 = Tex(r"$$\text{det}(\mathbf{\text{SO}})=1$$", color=PURE_RED).to_edge(DOWN)
        self.play(Transform(cnbp, anbp), Transform(po, det), Transform(ei, aei), Transform(ej, aej),FadeOut(T2))# Transform(T1, aT1),
        anbp = NumberPlane(axis_config={"color": GRAY}, background_line_style={"stroke_color": YELLOW_D},
                           x_axis_config={"rotation": 120 * DEGREES},
                           y_axis_config={"rotation": 210 * DEGREES})
        det = Polygon([0, 0, 0], [cos(120 * DEGREES), sin(120 * DEGREES), 0],
                      [cos(120 * DEGREES) + cos(210 * DEGREES), sin(120 * DEGREES) + sin(210 * DEGREES), 0],
                      [cos(210 * DEGREES), sin(210 * DEGREES), 0], color=RED, fill_opacity=0.75, stroke_width=0)
        aei = Vector([cos(120 * DEGREES), sin(120 * DEGREES)], color=PURE_RED)
        aej = Vector([cos(210 * DEGREES), sin(210 * DEGREES)], color=PURE_BLUE)
        self.play(Transform(cnbp, anbp), Transform(po, det), Transform(ei, aei), Transform(ej, aej),Transform(T1, aT1),
                  FadeOut(T2))
        self.wait(1)

class s4_part4(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=30 * DEGREES)
        ex = Vector([3, 0, 0], color=PURE_RED)
        ey = Vector([0, 3, 0], color=PURE_BLUE)
        ez = Vector([0, 0, 3], color=PURE_GREEN)
        x_lb = Tex(r"$$x$$", color=PURE_RED).move_to([3, 0, -0.25])
        y_lb = Tex(r"$$y$$", color=PURE_BLUE).move_to([0, 3, -0.25])
        z_lb = Tex(r"$$z$$", color=PURE_GREEN).move_to([0, 0, 3 + 0.25])
        self.add_fixed_orientation_mobjects(x_lb, y_lb, z_lb)
        self.add(ex, ey, ez)
        self.wait(1)
        exc = Vector([3, 0, 0], color=RED)
        eyc = Vector([0, 3, 0], color=BLUE)
        ezc = Vector([0, 0, 3], color=GREEN)
        _x_lb = Tex(r"$$x'$$", color=PURE_RED).move_to([3, 0, -0.25])
        _y_lb = Tex(r"$$y'$$", color=PURE_BLUE).move_to([0, 3, -0.25])
        _z_lb = Tex(r"$$z'$$", color=PURE_GREEN).move_to([0, 0, 3 + 0.25])
        RZT = ValueTracker(0)
        RXT = ValueTracker(0)
        RYT = ValueTracker(0)
        isable = True
        exc.add_updater(lambda m: m.put_start_and_end_on([0, 0, 0], [3 * (
                    (sin(RYT.get_value()) * sin(RXT.get_value()) * sin(RZT.get_value())) + (
                        cos(RYT.get_value()) * cos(RZT.get_value()))),
                                                                     3 * (cos(RXT.get_value()) * sin(RZT.get_value())),
                                                                     3 * ((cos(RYT.get_value()) * sin(
                                                                         RXT.get_value()) * sin(RZT.get_value())) - (
                                                                                      sin(RYT.get_value()) * cos(
                                                                                  RZT.get_value())))]) if isable else m)
        eyc.add_updater(lambda m: m.put_start_and_end_on([0, 0, 0], [3 * (
                    (sin(RYT.get_value()) * sin(RXT.get_value()) * cos(RZT.get_value())) - (
                        cos(RYT.get_value()) * sin(RZT.get_value()))),
                                                                     3 * (cos(RXT.get_value()) * cos(RZT.get_value())),
                                                                     3 * ((cos(RYT.get_value()) * sin(
                                                                         RXT.get_value()) * cos(RZT.get_value())) + (
                                                                                      sin(RYT.get_value()) * sin(
                                                                                  RZT.get_value())))]) if isable else m)
        ezc.add_updater(lambda m: m.put_start_and_end_on([0, 0, 0], [3 * (sin(RYT.get_value()) * cos(RXT.get_value())),
                                                                     3 * (-sin(RXT.get_value())),
                                                                     3 * (cos(RYT.get_value()) * cos(
                                                                         RXT.get_value()))]) if isable else m)

        _x_lb.add_updater(lambda m: m.move_to([3 * (
                    sin(RYT.get_value()) * sin(RXT.get_value()) * sin(RZT.get_value()) + cos(RYT.get_value()) * cos(
                RZT.get_value())),
                                               3 * (cos(RXT.get_value()) * sin(RZT.get_value())),
                                               3 * (cos(RYT.get_value()) * sin(RXT.get_value()) * sin(
                                                   RZT.get_value()) - sin(RYT.get_value()) * cos(
                                                   RZT.get_value())) - 0.25]) if isable else m)
        _y_lb.add_updater(lambda m: m.move_to([3 * (
                    sin(RYT.get_value()) * sin(RXT.get_value()) * cos(RZT.get_value()) - cos(RYT.get_value()) * sin(
                RZT.get_value())),
                                               3 * (cos(RXT.get_value()) * cos(RZT.get_value())),
                                               3 * (cos(RYT.get_value()) * sin(RXT.get_value()) * cos(
                                                   RZT.get_value()) + sin(RYT.get_value()) * sin(
                                                   RZT.get_value())) - 0.25]) if isable else m)
        _z_lb.add_updater(lambda m: m.move_to([3 * (sin(RYT.get_value()) * cos(RXT.get_value())),
                                               3 * (-sin(RXT.get_value())),
                                               3 * (cos(RYT.get_value()) * cos(
                                                   RXT.get_value())) + 0.25]) if isable else m)

        self.add_fixed_orientation_mobjects(_x_lb, _y_lb, _z_lb)
        self.add(exc, eyc, ezc)
        self.play(RZT.animate.set_value(30 * DEGREES), RXT.animate.set_value(30 * DEGREES),
                  RYT.animate.set_value(30 * DEGREES))
        self.wait(1)
        isable = False
        vm = [-2,3,1]
        DotP = Dot3D([2,-1,2],color=PURE_RED)
        P_ = Arrow([0,0,0],[2,-1,2],color=GREEN,buff=0)
        P = Arrow(vm,[2,-1,2],color=ORANGE,buff=0)
        M = Arrow([0,0,0],vm,color=BLACK,buff=0)
        T_P_ = Tex(r"$$\mathbf{p}'$$",color=GREEN)
        T_EQ = Tex(r"$$=$$",color=BLACK)
        T_R = Tex(r"$$\mathbf{R}$$",color=BLACK)
        T_P = Tex(r"$$\mathbf{p}$$",color=ORANGE)
        T_ADD = Tex(r"$$+$$",color=BLACK)
        T_M = Tex(r"$$\mathbf{m}$$",color=BLACK)
        TTTT = VGroup(T_P_,T_EQ,T_R,T_P,T_ADD,T_M).arrange(RIGHT).to_corner(UL)
        self.add_fixed_in_frame_mobjects(T_P_,T_EQ,T_R,T_P,T_ADD,T_M)
        self.play(_x_lb.animate.shift(vm),_y_lb.animate.shift(vm),_z_lb.animate.shift(vm),
                  exc.animate.shift(vm),eyc.animate.shift(vm),ezc.animate.shift(vm),FadeIn(P_,P,M,DotP,T_P_,T_EQ,T_R,T_P,T_ADD,T_M))
        self.wait(1)
        aT_P_ = Tex(r"$$\mathbf{p}'$$", color=GREEN)
        aT_EQ = Tex(r"$$=$$", color=BLACK)
        aT_RI = Tex(r"$$\mathbf{R}^{-1}$$", color=BLACK)
        aT_P = Tex(r"$$\mathbf{p}$$", color=ORANGE)
        aT_MINUS = Tex(r"$$-$$", color=BLACK)
        aT_M = Tex(r"$$\mathbf{m}$$", color=BLACK)
        aT_L = Tex(r"$$($$",color=BLACK)
        aT_RC = Tex(r"$$)$$",color=BLACK)
        TTTT2 = VGroup(aT_P,aT_EQ,aT_RI,aT_L,aT_P_,aT_MINUS,aT_M,aT_RC).arrange(RIGHT).next_to(TTTT,DOWN,aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(aT_P,aT_EQ,aT_RI,aT_L,aT_P_,aT_MINUS,aT_M,aT_RC)
        self.play(FadeIn(aT_P,aT_EQ,aT_RI,aT_L,aT_P_,aT_MINUS,aT_M,aT_RC))
        self.wait(1)

        aaT_P_ = Tex(r"$$\mathbf{p}'$$", color=GREEN)
        aaT_EQ = Tex(r"$$=$$", color=BLACK)
        aaT_RI = Tex(r"$$\mathbf{R}^{\top}$$", color=BLACK)
        aaT_P = Tex(r"$$\mathbf{p}$$", color=ORANGE)
        aaT_MINUS = Tex(r"$$-$$", color=BLACK)
        aaT_M = Tex(r"$$\mathbf{m}$$", color=BLACK)
        aaT_L = Tex(r"$$($$", color=BLACK)
        aaT_RC = Tex(r"$$)$$", color=BLACK)
        TTTT2 = VGroup(aaT_P, aaT_EQ, aaT_RI, aaT_L, aaT_P_, aaT_MINUS, aaT_M, aaT_RC).arrange(RIGHT).next_to(TTTT, DOWN,
                                                                                                      aligned_edge=LEFT)
        self.play(Transform(aT_RI,aaT_RI),Transform(aT_P,aaT_P),Transform(aT_EQ,aaT_EQ),Transform(aT_L,aaT_L),
                  Transform(aT_P_,aaT_P_),Transform(aT_MINUS,aaT_MINUS),Transform(aT_M,aaT_M),Transform(aT_RC,aaT_RC))

        self.wait(1)
        self.play(FadeOut(T_P_,T_EQ,T_R,T_P,T_ADD,T_M,aT_P,aT_EQ,aT_RI,aT_L,aT_P_,aT_MINUS,aT_M,aT_RC))
        T_W = Tex(r"$$\mathbf{W}$$",color=BLACK)
        TTTT = VGroup(T_P_,T_EQ,T_W,T_P).arrange(RIGHT).to_corner(UL)
        T_WI = Tex(r"$$\mathbf{W}^{-1}$$", color=BLACK)
        TTTT2 = VGroup(aT_P,aT_EQ,T_WI,aT_P_).arrange(RIGHT).next_to(TTTT,DOWN,aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(T_W,T_WI)
        self.play(FadeIn(T_P_,T_EQ,T_W,T_P,aT_P,aT_EQ,T_WI,aT_P_))
        self.wait(1)
        self.play(FadeOut(T_P_,T_EQ,T_W,T_P,aT_P,aT_EQ,T_WI,aT_P_))
        T_P_ = Tex(r"$$\mathbf{p}'$$", color=GREEN)
        T_EQ = Tex(r"$$=$$", color=BLACK)
        T_R = Tex(r"$$\mathbf{R}$$", color=BLACK)
        T_P = Tex(r"$$\mathbf{p}$$", color=ORANGE)
        T_ADD = Tex(r"$$+$$", color=BLACK)
        T_M = Tex(r"$$\mathbf{m}$$", color=BLACK)
        TTTT = VGroup(T_P_, T_EQ, T_R, T_P, T_ADD, T_M).arrange(RIGHT).to_corner(UL)
        aT_P_ = Tex(r"$$\mathbf{p}'$$", color=GREEN)
        aT_EQ = Tex(r"$$=$$", color=BLACK)
        aT_RI = Tex(r"$$\mathbf{R}^{-1}$$", color=BLACK)
        aT_P = Tex(r"$$\mathbf{p}$$", color=ORANGE)
        aT_MINUS = Tex(r"$$-$$", color=BLACK)
        aT_M = Tex(r"$$\mathbf{m}$$", color=BLACK)
        aT_L = Tex(r"$$($$", color=BLACK)
        aT_RC = Tex(r"$$)$$", color=BLACK)
        TTTT2 = VGroup(aT_P, aT_EQ, aT_RI, aT_L, aT_P_, aT_MINUS, aT_M, aT_RC).arrange(RIGHT).next_to(TTTT, DOWN,
                                                                                                      aligned_edge=LEFT)
        self.add_fixed_in_frame_mobjects(aT_P, aT_EQ, aT_RI, aT_L, aT_P_, aT_MINUS, aT_M, aT_RC,T_P_,T_EQ,T_R,T_P,T_ADD,T_M)
        self.play(FadeIn(T_P_,T_EQ,T_R,T_P,T_ADD,T_M,aT_P,aT_EQ,aT_RI,aT_L,aT_P_,aT_MINUS,aT_M,aT_RC))
        self.wait(1)

class s4_part5(Scene):
    def construct(self):
        T1 = Tex(r"$$\mathbf{p}'=\mathbf{R}\mathbf{p}+\mathbf{m}$$",color=BLACK).to_corner(UL)
        T2 = Tex(r"$$\mathbf{p}=\mathbf{R}^{-1}(\mathbf{p}'-\mathbf{m})$$",color=BLACK).next_to(T1,DOWN,aligned_edge=LEFT)
        self.add(T1,T2)
        self.wait(1)
        T1_2 = Tex(r"$$=\begin{bmatrix} \mathbf{R}_{1,1} &\mathbf{R}_{1,2}  &\mathbf{R}_{1,3} \\\mathbf{R}_{2,1} &\mathbf{R}_{2,2}  &\mathbf{R}_{2,3} \\\mathbf{R}_{3,1} &\mathbf{R}_{3,2}  &\mathbf{R}_{3,3}\end{bmatrix}\begin{bmatrix}\mathbf{p}_{1} \\ \mathbf{p}_{2} \\\mathbf{p}_{3} \end{bmatrix}+\begin{bmatrix}\mathbf{m}_{1} \\\mathbf{m}_{2} \\\mathbf{m}_{3}\end{bmatrix}$$",
                  color=BLACK).next_to(T1,DOWN,aligned_edge=LEFT)
        aT2 = T2.copy().next_to(T1_2,DOWN,aligned_edge=LEFT)
        self.play(Write(T1_2),Transform(T2,aT2))
        T1_3 = Tex(r"$$=\mathbf{p}_{1}\begin{bmatrix}\mathbf{R}_{1,1} \\ \mathbf{R}_{2,1}\\\mathbf{R}_{3,1}\end{bmatrix}+\mathbf{p}_{2}\begin{bmatrix}\mathbf{R}_{1,2} \\ \mathbf{R}_{2,2}\\\mathbf{R}_{3,2}\end{bmatrix}+\mathbf{p}_{3}\begin{bmatrix}\mathbf{R}_{1,3} \\\mathbf{R}_{2,3}\\\mathbf{R}_{3,3}\end{bmatrix}+1\cdot\begin{bmatrix}\mathbf{m}_{1} \\\mathbf{m}_{2} \\\mathbf{m}_{3}\end{bmatrix}$$",
                   color=BLACK).next_to(T1_2,DOWN,aligned_edge=LEFT)
        aT2 = T2.copy().next_to(T1_3,DOWN,aligned_edge=LEFT)
        self.play(Write(T1_3),Transform(T2,aT2))
        self.wait(1)
        t1 = Tex(r"$$\mathbf{p}_{1}\begin{bmatrix}\mathbf{R}_{1,1} \\ \mathbf{R}_{2,1}\\\mathbf{R}_{3,1}\\0\end{bmatrix}+\mathbf{p}_{2}\begin{bmatrix}\mathbf{R}_{1,2} \\\mathbf{R}_{2,2}\\\mathbf{R}_{3,2}\\0\end{bmatrix}+\mathbf{p}_{3}\begin{bmatrix}\mathbf{R}_{1,3} \\ \mathbf{R}_{2,3}\\\mathbf{R}_{3,3}\\0\end{bmatrix}+1\cdot\begin{bmatrix}\mathbf{m}_{1} \\\mathbf{m}_{2} \\\mathbf{m}_{3}\\1\end{bmatrix}$$",
                   color=BLACK).next_to(T1,DOWN,aligned_edge=LEFT)
        aT2.next_to(t1,DOWN,aligned_edge=LEFT)
        self.play(Write(t1),FadeOut(T1_2,T1_3),Transform(T2,aT2))
        self.wait(1)
        t1_2 = Tex(r"$$=\begin{bmatrix} \mathbf{R}_{1,1} & \mathbf{R}_{1,2} & \mathbf{R}_{1,3} & \mathbf{m}_{1}\\  \mathbf{R}_{2,1} & \mathbf{R}_{2,2} & \mathbf{R}_{2,3} & \mathbf{m}_{2} \\  \mathbf{R}_{3,1} & \mathbf{R}_{3,2} & \mathbf{R}_{3,3} & \mathbf{m}_{3} \\  0& 0 &0  &1\end{bmatrix}\begin{bmatrix} \mathbf{p}_{1}\\\mathbf{p}_{2}\\ \mathbf{p}_{3}\\1 \\\end{bmatrix}=\begin{bmatrix}\mathbf{p}'_{1} \\\mathbf{p}'_{2} \\\mathbf{p}'_{3} \\1\end{bmatrix}$$",
                   color=BLACK).next_to(t1,DOWN,aligned_edge=LEFT)
        aT2.next_to(t1_2,DOWN,aligned_edge=LEFT)
        self.play(Write(t1_2),Transform(T2,aT2))
        self.wait(1)
        at1_2 = Tex(r"$$=\begin{bmatrix} \mathbf{R}_{1,1} & \mathbf{R}_{1,2} & \mathbf{R}_{1,3} & \mathbf{m}_{1}\\  \mathbf{R}_{2,1} & \mathbf{R}_{2,2} & \mathbf{R}_{2,3} & \mathbf{m}_{2} \\  \mathbf{R}_{3,1} & \mathbf{R}_{3,2} & \mathbf{R}_{3,3} & \mathbf{m}_{3} \\  0& 0 &0  &1\end{bmatrix}\mathbf{p}=\mathbf{p}'$$",
                    color=BLACK).next_to(t1,DOWN,aligned_edge=LEFT)
        self.play(Transform(t1_2,at1_2))
        self.wait(1)
        at1_2 = Tex(r"$$\mathbf{p}'=\begin{bmatrix} \mathbf{R} & \mathbf{m}\\  \mathbf{0}^{\top}&1\end{bmatrix}\mathbf{p}$$",color=BLACK).to_corner(UL)
        aT2.next_to(at1_2, DOWN, aligned_edge=LEFT)
        self.play(Transform(t1_2, at1_2),Transform(T2,aT2),FadeOut(t1,T1))
        self.wait(1)
        at1_2 = Tex(r"$$\mathbf{p}'=\mathbf{T}\mathbf{p}$$",color=BLACK).to_corner(UL)
        tT = Tex(r"$$\mathbf{T}\in\mathbf{\text{SE}}(3)$$",color=BLACK).next_to(at1_2,DOWN,aligned_edge=LEFT)
        tSE = Tex(r"$$\mathbf{\text{SE}}(n)=\left \{ \begin{bmatrix} \mathbf{R} & \mathbf{m}\\ \mathbf{0}^{\top} & 1\end{bmatrix} \in \mathbb{R}^{(n+1)\times (n+1)} \mid \mathbf{R}\in \mathbf{\text{SO}}(n), \mathbf{m}\in \mathbb{R}^{n} \right \} $$",color=BLACK).next_to(tT,DOWN,aligned_edge=LEFT)
        aT2.next_to(tSE,DOWN,aligned_edge=LEFT)
        self.play(Transform(t1_2,at1_2),Transform(T2,aT2),Write(tT),Write(tSE))
        self.wait(1)
        wT = Tex(r"$$=\mathbf{R}^{-1}\mathbf{p}'-\mathbf{R}^{-1}\mathbf{m}$$",color=BLACK).next_to(aT2,DOWN,aligned_edge=LEFT)
        self.play(Write(wT))
        self.wait(1)
        wT2 = Tex(r"$$=\begin{bmatrix} \mathbf{R}^{\top} & -\mathbf{R}^{\top}\mathbf{m} \\ \mathbf{0}^{\top} &1\end{bmatrix}\mathbf{p}'$$",color=BLACK).next_to(wT,DOWN,aligned_edge=LEFT)
        self.play(Write(wT2))
        self.wait(1)

class templateAnimation1(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=30 * DEGREES)
        ex = Vector([3, 0, 0], color=PURE_RED)
        ey = Vector([0, 3, 0], color=PURE_BLUE)
        ez = Vector([0, 0, 3], color=PURE_GREEN)
        x_lb = Tex(r"$$x$$", color=PURE_RED).move_to([3, 0, -0.25])
        y_lb = Tex(r"$$y$$", color=PURE_BLUE).move_to([0, 3, -0.25])
        z_lb = Tex(r"$$z$$", color=PURE_GREEN).move_to([0, 0, 3 + 0.25])
        self.add_fixed_orientation_mobjects(x_lb, y_lb, z_lb)
        self.add(ex, ey, ez)
        self.wait(1)
        exc = Vector([3, 0, 0], color=RED)
        eyc = Vector([0, 3, 0], color=BLUE)
        ezc = Vector([0, 0, 3], color=GREEN)
        _x_lb = Tex(r"$$x'$$", color=PURE_RED).move_to([3, 0, -0.25])
        _y_lb = Tex(r"$$y'$$", color=PURE_BLUE).move_to([0, 3, -0.25])
        _z_lb = Tex(r"$$z'$$", color=PURE_GREEN).move_to([0, 0, 3 + 0.25])
        RZT = ValueTracker(0)
        RXT = ValueTracker(0)
        RYT = ValueTracker(0)
        isable = True
        exc.add_updater(lambda m: m.put_start_and_end_on([0, 0, 0], [3 * (
                (sin(RYT.get_value()) * sin(RXT.get_value()) * sin(RZT.get_value())) + (
                cos(RYT.get_value()) * cos(RZT.get_value()))),
                                                                     3 * (cos(RXT.get_value()) * sin(RZT.get_value())),
                                                                     3 * ((cos(RYT.get_value()) * sin(
                                                                         RXT.get_value()) * sin(RZT.get_value())) - (
                                                                                  sin(RYT.get_value()) * cos(
                                                                              RZT.get_value())))]) if isable else m)
        eyc.add_updater(lambda m: m.put_start_and_end_on([0, 0, 0], [3 * (
                (sin(RYT.get_value()) * sin(RXT.get_value()) * cos(RZT.get_value())) - (
                cos(RYT.get_value()) * sin(RZT.get_value()))),
                                                                     3 * (cos(RXT.get_value()) * cos(RZT.get_value())),
                                                                     3 * ((cos(RYT.get_value()) * sin(
                                                                         RXT.get_value()) * cos(RZT.get_value())) + (
                                                                                  sin(RYT.get_value()) * sin(
                                                                              RZT.get_value())))]) if isable else m)
        ezc.add_updater(lambda m: m.put_start_and_end_on([0, 0, 0], [3 * (sin(RYT.get_value()) * cos(RXT.get_value())),
                                                                     3 * (-sin(RXT.get_value())),
                                                                     3 * (cos(RYT.get_value()) * cos(
                                                                         RXT.get_value()))]) if isable else m)

        _x_lb.add_updater(lambda m: m.move_to([3 * (
                sin(RYT.get_value()) * sin(RXT.get_value()) * sin(RZT.get_value()) + cos(RYT.get_value()) * cos(
            RZT.get_value())),
                                               3 * (cos(RXT.get_value()) * sin(RZT.get_value())),
                                               3 * (cos(RYT.get_value()) * sin(RXT.get_value()) * sin(
                                                   RZT.get_value()) - sin(RYT.get_value()) * cos(
                                                   RZT.get_value())) - 0.25]) if isable else m)
        _y_lb.add_updater(lambda m: m.move_to([3 * (
                sin(RYT.get_value()) * sin(RXT.get_value()) * cos(RZT.get_value()) - cos(RYT.get_value()) * sin(
            RZT.get_value())),
                                               3 * (cos(RXT.get_value()) * cos(RZT.get_value())),
                                               3 * (cos(RYT.get_value()) * sin(RXT.get_value()) * cos(
                                                   RZT.get_value()) + sin(RYT.get_value()) * sin(
                                                   RZT.get_value())) - 0.25]) if isable else m)
        _z_lb.add_updater(lambda m: m.move_to([3 * (sin(RYT.get_value()) * cos(RXT.get_value())),
                                               3 * (-sin(RXT.get_value())),
                                               3 * (cos(RYT.get_value()) * cos(
                                                   RXT.get_value())) + 0.25]) if isable else m)

        self.add_fixed_orientation_mobjects(_x_lb, _y_lb, _z_lb)
        self.add(exc, eyc, ezc)
        self.play(RZT.animate.set_value(30 * DEGREES), RXT.animate.set_value(30 * DEGREES),
                  RYT.animate.set_value(30 * DEGREES))
        self.wait(1)
        isable = False
        vm = [-2, 3, 1]
        DotP = Dot3D([2, -1, 2], color=PURE_RED)
        P_ = Arrow([0, 0, 0], [2, -1, 2], color=GREEN, buff=0)
        P = Arrow(vm, [2, -1, 2], color=ORANGE, buff=0)
        M = Arrow([0, 0, 0], vm, color=BLACK, buff=0)
        T_P_ = Tex(r"$$\mathbf{p}$$", color=ORANGE)
        T_EQ = Tex(r"$$=$$", color=BLACK)
        T_R = Tex(r"$$\mathbf{SE(3,\mathbf{R},\mathbf{m})^{-1}}$$", color=BLACK)
        T_P = Tex(r"$$\mathbf{p}'$$", color=GREEN)
        TTTT = VGroup(T_P_, T_EQ, T_R, T_P).arrange(RIGHT).to_corner(UL)
        self.add_fixed_in_frame_mobjects(T_P_, T_EQ, T_R, T_P)
        self.play(_x_lb.animate.shift(vm), _y_lb.animate.shift(vm), _z_lb.animate.shift(vm),
                  exc.animate.shift(vm), eyc.animate.shift(vm), ezc.animate.shift(vm),
                  FadeIn(P_, P, M, DotP, T_P_, T_EQ, T_R, T_P))
        self.wait(1)

class s5(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=30 * DEGREES)
        e_camera = VGroup(Vector([-1,0,0],color=RED),Vector([0,0,1],color=BLUE),Vector([0,1,0],color=GREEN))
        label_x = Tex(r"$$x$$", color=RED).move_to([-1, 0, 0])
        label_y = Tex(r"$$y$$", color=BLUE).move_to([0, 0, 1])
        label_z = Tex(r"$$z$$", color=GREEN).move_to([0, 1, 0])
        dot_p = Dot3D([1,-4,-1],color=BLUE)
        label_p = Tex(r"$$\text{P}$$",color=BLUE).move_to([1,-4,-1.25])
        dot_q = Dot3D([0,0,0],color=DARK_BLUE)
        label_q = Tex(r"$$\text{Q}$$",color=DARK_BLUE).move_to([0,0,-0.25])
        line_op = Arrow([0,0,0],[1,-4,-1],color=BLACK,buff=0)
        frame = Square(side_length=3,color=GRAY,fill_opacity=0.25)
        frame.rotate(90*DEGREES,RIGHT)

        tracker = ValueTracker(0)
        y1 = True
        dot_q.add_updater(lambda m: m.move_to([1*tracker.get_value()/4,-tracker.get_value(),-1*tracker.get_value()/4] if y1 else m))
        label_q.add_updater(lambda m: m.move_to(
            [1 * tracker.get_value()/4, -tracker.get_value(), -1 * tracker.get_value()/4 -0.25] if y1 else m))
        frame.add_updater(lambda m: m.move_to(
            [0, -tracker.get_value(), 0] if y1 else m))

        self.add_fixed_orientation_mobjects(label_z,label_x,label_y,label_q,label_p)
        self.add(e_camera,label_z,label_y,label_x,frame,label_p,label_q,line_op,dot_q,dot_p)
        self.wait(1)
        self.play(tracker.animate.set_value(2))
        self.wait(1)
        line_l = Line3D([1,-4,-1],[-1,-4,0],color=PURE_RED)
        y1 = False
        y2 = False
        tracker2 = ValueTracker(0)
        dot_p.add_updater(lambda m:m.move_to([1-(2*tracker2.get_value()),-4,-1+tracker2.get_value()]) if y2 else m)
        line_op.add_updater(lambda m:m.put_start_and_end_on([0,0,0],[1-(2*tracker2.get_value()),-4,-1+tracker2.get_value()]) if y2 else m)
        dot_q.add_updater(lambda m:m.move_to([(1-(2*tracker2.get_value()))/2,-2,(-1+tracker2.get_value())/2]) if y2 else m)
        label_p.add_updater(lambda m:m.move_to([1-(2*tracker2.get_value()),-4,-1+tracker2.get_value()-0.25]) if y2 else m)
        label_q.add_updater(lambda m: m.move_to([(1-(2*tracker2.get_value()))/2,-2,(-1+tracker2.get_value())/2-0.25]) if y2 else m)
        lineqq = Line3D([(1-(2*0))/2,-2,(-1+0)/2],[(1-(2*1))/2,-2,(-1+1)/2],color=DARK_GRAY)
        self.play(Write(line_l))
        self.wait(1)
        y2 = True
        self.play(tracker2.animate.set_value(1),line_op.animate.get_center(),Write(lineqq))
        self.wait(1)
        self.play(tracker2.animate.set_value(0))
        triangle = Polygon([0,0,0],[1-(2*0),-4,-1+0],[1-(2*0),-4,-1+0],color=RED,fill_opacity=0.25)
        self.play(tracker2.animate.set_value(1),Transform(triangle,Polygon([0,0,0],[1-(2*0),-4,-1+0],[1-(2*1),-4,-1+1],color=RED,fill_opacity=0.25)))
        self.wait(1)
        self.play(FadeOut(triangle))
        self.wait(1)
        trueTriangle = Polygon([1-(2*0),-4,-1+0],[1-(2*1),-4,-1+1],[2,-4,2],color=BLUE)
        self.play(FadeIn(trueTriangle),FadeOut(line_l,lineqq),tracker2.animate.set_value(0))
        self.wait(1)
        twoTriangles = VGroup(Polygon([0,0,0],[1-(2*1),-4,-1+1],[2,-4,2],color=RED,fill_opacity=0.25),Polygon([0,0,0],[1-(2*0),-4,-1+0],[2,-4,2],color=RED,fill_opacity=0.25))
        importantTriangle = Polygon([0,0,0],[1-(2*0),-4,-1+0],[1-(2*0),-4,-1+0],color=RED,fill_opacity=0.25)
        oneTriangle = Polygon([(1-(2*0))/2,-2,(-1+0)/2],[(1-(2*1))/2,-2,(-1+1)/2],[2/2,-2,2/2],color=BLACK)
        y2 = True
        self.move_camera(theta=-30*DEGREES,added_anims=[tracker2.animate.set_value(1),dot_p.animate.get_center(),line_op.animate.get_center(),dot_q.animate.get_center(),
                                                        Transform(importantTriangle,Polygon([0,0,0],[1-(2*0),-4,-1+0],[1-(2*1),-4,-1+1],color=RED,fill_opacity=0.25)),
                                                        FadeIn(twoTriangles,oneTriangle)])
        self.wait(1)
        self.move_camera(theta=60*DEGREES)
        self.wait(1)
        self.play(FadeOut(importantTriangle,twoTriangles,oneTriangle,trueTriangle,lineqq))
        self.wait(1)

        cone = Cone(height=sqrt(16+(1/4)),direction=0.5*X_AXIS+4*Y_AXIS,base_radius=0.5,checkerboard_colors=False,background_stroke_opacity=0.25)
        self.move_camera(theta=195*DEGREES,added_anims=[Create(cone)])
        self.wait(1)