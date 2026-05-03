from NTools import *

class s1(NScene):
    def construct(self):
        A = Dot([-4,-2,0],color=BLACK)
        B = Dot([4,-2,0],color=BLACK)
        C = Dot([-2,2,0],color=BLACK)
        l_A = MathTex("A",color=BLACK).next_to(A,DOWN)
        l_B = MathTex("B",color=BLACK).next_to(B,DOWN)
        l_C = MathTex("C",color=BLACK).next_to(C,UP)
        ABC = Polygon(A.get_center(),B.get_center(),C.get_center(),color=BLACK,fill_color=0)
        D = Dot([-2,-1,0],color=BLACK)
        l_D = MathTex("D", color=BLACK).next_to(D, UL)
        self.play(FadeIn(A,B,C,l_A,l_B,l_C,l_D,D),Create(ABC))
        self.say("设给定的任意三角形为三角形ABC\n且D为其内部任一点",VGroup(A,B,C,l_A,l_B,l_C,l_D,D,ABC).animate.shift(LEFT*2))
        DA = Line(D.get_center(),A.get_center(),color=BLACK)
        DB = Line(D.get_center(),B.get_center(),color=BLACK)
        DC = Line(D.get_center(),C.get_center(),color=BLACK)
        self.say("连接DA、DB、DC",FadeIn(DA,DB,DC))
        E = Dot(2*D.get_center()-A.get_center(),color=BLACK)
        l_E = MathTex("E",color=BLACK).next_to(E,UR)
        DE = Line(D.get_center(),E.get_center(),color=BLACK)
        DEeqDA = VGroup(equal_line_notes(DA),equal_line_notes(DE))
        self.say("延长AD至E，使得AD等于DE",Succession(AnimationGroup(FadeIn(E,l_E),Create(DE)),Create(DEeqDA)))
        EF = parallel_line_cross_point_meet_line(DC,E,DB,color=BLACK)
        F = Dot(EF.get_end(),color=BLACK)
        l_F = MathTex("F",color=BLACK).next_to(F,LEFT)
        EFparaDC = VGroup(parallel_line_notes(EF),parallel_line_notes(DC.copy().reverse_direction()))
        self.say("过E作DC的平行线EF，使之交DB于F",Succession(AnimationGroup(Create(EF),FadeIn(F,l_F)),Create(EFparaDC)))
        CE = Line(C.get_center(),E.get_center(),color=BLACK)
        CF = Line(C.get_center(),F.get_center(),color=BLACK)
        self.say("连接CE、CF",Create(CE),Create(CF))
        CDB = Polygon(C.get_center(),D.get_center(),B.get_center(),color=LIGHT_GRAY,fill_opacity=0.37)
        CDB_ = CDB.copy()
        CDF = Polygon(C.get_center(),D.get_center(),F.get_center(),color=RED,fill_opacity=0.37)
        t1 = MathTex(r"DB:DF=S_{\triangle BDC}:S_{\triangle FDC}",color=BLACK).to_corner(UR)
        self.say("于是，DB与DF之比\n就如同三角形BDC与三角形FDC[面积]之比\n[《几何原本》VI.1]",
                 Write(t1),Succession(AnimationGroup(Create(CDB),Create(CDB_)),CDB_.animate.become(CDF)))
        CDE = Polygon(C.get_center(),D.get_center(),E.get_center(),color=RED,fill_opacity=0.37)
        t2 = MathTex(r"=S_{\triangle BDC}:S_{\triangle EDC}",color=BLACK).next_to(t1,DOWN,aligned_edge=RIGHT)
        self.say("但是，由于EF平行于DC\n三角形FDC也等于三角形EDC\n[I.37]",
                 Write(t2),CDB_.animate.become(CDE))
        CDA = Polygon(C.get_center(),D.get_center(),A.get_center(),color=RED, fill_opacity=0.37)
        t3 = MathTex(r"=S_{\triangle BDC}:S_{\triangle ADC}",color=BLACK).next_to(t2,DOWN,aligned_edge=RIGHT)
        self.say("而DE等于DA\n因此，三角形EDC也等于三角形CDA\n[I.38]",
                 Write(t3),CDB_.animate.become(CDA))
        t4 = MathTex(r"DB:DF=S_{\triangle BDC}:S_{\triangle CDA}",color=RED).to_corner(UR)
        self.say("于是，我们得到了这个比例式",
                 FadeOut(t1,t2,t3),Write(t4))

        EG = parallel_line_cross_point_meet_line(DB,E,DC,color=BLACK)
        G = Dot(EG.get_end(),color=BLACK)
        l_G = MathTex("G",color=BLACK).next_to(G,RIGHT)
        EGparaDB = VGroup(parallel_line_notes(EG,2),parallel_line_notes(DB.reverse_direction(),2))
        t5 = MathTex(r"DC:DG=S_{\triangle BDC}:S_{\triangle ADB}",color=BLUE).next_to(t4,DOWN,aligned_edge=RIGHT)

        GB = Line(G.get_center(),B.get_center(),color=BLACK)
        EB = Line(E.get_center(),B.get_center(),color=BLACK)

        CDB__ = CDB.copy()
        GDB = Polygon(G.get_center(),D.get_center(),B.get_center(),color=BLUE,fill_opacity=0.37)
        EDB = Polygon(E.get_center(),D.get_center(),B.get_center(),color=BLUE,fill_opacity=0.37)
        ADB = Polygon(A.get_center(),D.get_center(),B.get_center(),color=BLUE,fill_opacity=0.37)
        self.say("同理，过E作DB的平行线EG，使之交DC于G\n并连接GB、EB\n就类似地可以得到另一个比例式",
                 Succession(AnimationGroup(Create(EG),FadeIn(G,l_G)),Create(EGparaDB),
                            AnimationGroup(Create(GB),Create(EB))))
        self.play(FadeIn(CDB__))
        self.play(CDB__.animate.become(GDB))
        self.play(CDB__.animate.become(EDB))
        self.play(CDB__.animate.become(ADB))
        self.play(Write(t5))
        self.wait(self.space)

        t6 = MathTex(r"DE:DA=1",color=BLACK).next_to(t5,DOWN,aligned_edge=RIGHT)
        self.say("而显然，因为DE等于DA\n所以它们的比为1",Write(t6))
        t7 = MathTex(r"\frac{DE}{DA}:\frac{DB}{DF}:\frac{DC}{DG}=1:\frac{S_{\triangle BDC}}{S_{\triangle CDA}}:\frac{S_{\triangle BDC}}{S_{\triangle ADB}}"
                     ,color=BLACK).next_to(t6,DOWN,aligned_edge=RIGHT)
        t8 = MathTex(r"=\frac{1}{S_{\triangle{BDC}}}:\frac{1}{S_{\triangle CDA}}:\frac{1}{S_{\triangle ADB}}",color=BLACK).next_to(t7,DOWN,aligned_edge=RIGHT)
        self.say("于是立即得到\nDE、DF、DG与DA、DB、DC的比的关系\n就是它们所对的三角形之间的关系",
                 Succession(Write(t7),Write(t8)))
        t9 = MathTex(r"\frac{DE}{DA}:\frac{DF}{DB}:\frac{DG}{DC}=S_{\triangle BDC}:S_{\triangle CDA}:S_{\triangle ADB}",
                     color=PURE_RED).to_corner(UR)
        self.play(FadeOut(t7,t8,t4,t5,t6),Write(t9))
        self.play(Indicate(t9))
        self.wait(self.space)

        EGDF = Polygon(E.get_center(),G.get_center(),D.get_center(),F.get_center(),color=GREEN,fill_opacity=0.37)
        t10 = MathTex(r"\overrightarrow{DE}=\overrightarrow{DF}+\overrightarrow{DG}",color=BLACK).next_to(t9,DOWN,aligned_edge=RIGHT)
        self.say("由于EGDF显然是一个平行四边形\n根据平行四边形法则\n向量DE就是向量DG、DF的和",
                 Create(EGDF),Write(t10))
        t11 = MathTex(r"\overrightarrow{DA}=-\overrightarrow{DE}",color=BLACK).next_to(t10,DOWN,aligned_edge=RIGHT)
        t12 = MathTex(r"\overrightarrow{DA}+\overrightarrow{DF}+\overrightarrow{DG}=\overrightarrow{0}",color=BLACK).next_to(t11,DOWN,aligned_edge=RIGHT)
        self.say("但向量DA显然与向量DE相反\n因此，向量DA、DG、DF之和为零向量",
                 Succession(Write(t11),Write(t12)))
        t13 = MathTex(r"S_{\triangle BDC}\overrightarrow{DA}+S_{\triangle CDA}\overrightarrow{DB}+S_{\triangle ADB}\overrightarrow{DC}=\overrightarrow{0}"
                      ,color=PURE_RED).next_to(t12.copy().next_to(t9,DOWN,aligned_edge=RIGHT),DOWN,aligned_edge=RIGHT)
        self.say("于是立即得到\n向量DA、DB、DC分别乘以与它们所对的三角形成比例的实数后\n它们的和就是零向量",
                 Write(t13),t12.animate.next_to(t9,DOWN,aligned_edge=RIGHT),
                 FadeOut(t10,t11))
        self.ending("这就是所要证明的.")
class bkg(Scene):
    def construct(self):
        pass
class s2(Scene):
    def construct(self):
        t = Text("实际上，上述证明并不需要E、F、G在三角形内部\n甚至不需要D在三角形内部\n因为，显然，在任何时候，\nDB与DF之比都如同三角形BDC与三角形CDF之比\n也就等同三角形BDC与三角形CDA之比\n这就能够用和上述证明一样的方法证明那个结论了"
                 ,color=BLACK,font_size=DEFAULT_FONT_SIZE/2).to_corner(UR)
        self.play(Write(t))
        self.wait(2)
