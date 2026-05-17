from NTools import *

class s1(NScene):
    def construct(self):
        self.say(["在《几何原本》中，",
                  "「所有直角都彼此相等」作为一条公设而存在；",])
        self.say(["但实际上，希尔伯特在《几何基础》将它作为一条定理而推出，",
                  "因此称欧几里得「错误地」将它作为了一条公理."])
        self.say(["而本期视频将在《几何原本》的框架内推出第四公设——",
                  "即，使用那些除了第四公设以外的公设和公理以及欧几里得自己使用过的隐含条件，",
                  "从而说明，即使在《几何原本》假定的背景下，第四公设依然是不必要的."])
        self.ending(' ')

class s2(NScene):
    def construct(self):
        t=["引理1[《几何原本》I.4]：",
           "若一个三角形的两条边分别与另外一个三角形的两条边相等，",
           "且这些边夹的角也相等，",
           "那么这两个三角形全等，即，对应边等于对应边，对应角等于对应角."]
        self.say(t)
        self.wait(3)

        t=["假设三角形ABC、DEF是给定的两个三角形，",
           "且AB、AC分别等于DE、DF，A处的角等于D处的角."]
        A = Dot([0,0,0],color=BLACK)
        B = Dot([-1,-2,0],color=BLACK)
        C = Dot([1.5,-2,0],color=BLACK)
        VGroup(A,B,C).shift(5*LEFT+1*UP)
        t_A = MathTex("A", color=BLACK).next_to(A, UP)
        t_B = MathTex("B", color=BLACK).next_to(B, LEFT)
        t_C = MathTex("C", color=BLACK).next_to(C, RIGHT)

        D,E,F=A.copy(),B.copy(),C.copy()
        VGroup(D,E,F).shift(5*RIGHT)
        t_D,t_E,t_F=MathTex("D", color=BLACK).next_to(D, UP),MathTex("E",color=BLACK).next_to(E,LEFT),MathTex("F",color=BLACK).next_to(F,RIGHT)

        ABC = falling_maple(A,B,C)
        DEF = withered_leaf(D,E,F)

        AB = line_via_dot(A,B)
        DE = line_via_dot(D,E)
        BC = line_via_dot(B,C)
        EF = line_via_dot(E,F)
        AC = line_via_dot(A,C)
        DF = line_via_dot(D,F)

        eqs = VGroup(equal_lines_notes_group(AB,DE),equal_line_notes(AC,DF),
                     equal_lines_notes_group(BC,EF))

        self.say(t,Create(ABC),Create(DEF),FadeIn(A,B,C,D,E,F,t_A,t_B,t_C,t_D,t_E,t_F),Create(eqs))

        t=["将三角形DEF叠合在ABC上，",
           "使AB和DE重合，",
           "这一点是可以做到的，因为相等的量彼此重合.",
           "[公理4(Common Notion IV)，注意不是将要证明的「公设4」(Postulate IV)]"]
        self.say(t,FadeOut(eqs),DEF.animate.shift(5*LEFT),FadeOut(t_D,t_E,t_F),
                 Transform(t_A,MathTex("A(D)", color=BLACK).next_to(A, UP)),
                 Transform(t_B,MathTex("B(E)", color=BLACK).next_to(B, LEFT)),
                 Transform(t_C,MathTex("C(F)", color=BLACK).next_to(C, RIGHT)),
                 VGroup(D,E,F).animate.shift(5*LEFT))
        self.wait(3)

        t=["而角BAC等于角EDF；",
           "因此DF在AC上[公理4]"]
        self.say(t)

        t=["但是DF也等于AC，因此F与C重合；",
           "因此，EF与BC重合；",
           "因此，它们相等[公理4]"]
        self.say(t)

        self.say(["用类似的方法，可以证明这两个三角形全等；",
           "这个证明在今天的主题下是可以被接受的，因为这正是《几何原本》中的证明方法."])
        self.say(["需要提到的是，这个方法用到了「叠合」，",
                  "而这其实暗中引用了一个欧几里得没有说明的公理；",
           "这个公理在希尔伯特的几何公理体系中被归入了合同公理的第六个."])
        self.say(["事实上，不难用反证法由此推出，",
                  "若一个三角形的三条边都与另外一个三角形的三条边分别相等，",
                  "那么这两个三角形全等.[I.8]"])

        GH = VGroup(Line([-1,-1,0],[8,-1,0],color=BLACK),Dot([-1,-1,0],color=BLACK))
        GK = VGroup(line_via_dot(B,C),B.copy(),C.copy())
        a = VGroup(line_via_dot(B,A),B.copy(),A.copy())
        b = VGroup(line_via_dot(C, A), C.copy(), A.copy())
        c_a = Circle(radius=distance(B,A),color=BLACK).move_to([-1,-1,0])
        c_b = Circle(radius=distance(C,A),color=BLACK).move_to([1.5,-1,0])
        Ls = VGroup(*[Dot(i,color=BLACK)for i in cross_c(c_a,c_b)])
        ls = VGroup(*[Line([-1,-1,0],i,color=BLACK)for i in cross_c(c_a,c_b)])

        self.say(["因此，结合显然不需要公设4就可以证明的命题I.2，",
                  "我们可以给出复制角的方法，即，在给定边的给定侧构造全等三角形."],
            FadeIn(GH),FadeIn(GK),GK.animate.shift(5*RIGHT),Create(a),a.animate.shift(5*RIGHT),FadeOut(a),Create(c_a),
                 Create(b),b.animate.shift(5*RIGHT),Create(c_b),FadeOut(b),FadeIn(Ls),
                 Create(ls),
                 is_sequencing=True)
        self.say(["事实上，《几何原本》第一卷直到命题14才首次使用了公设4；",
                  "因此，使用在此之前的命题来证明公设4是被允许的；",
                  "此外，在命题14之后的一些命题，比如角的复制[I.23]，",
                  "也可以像刚才那样，不使用公设4来推出."])
        self.wait(3)
        self.ending(' ')

class s3(NScene):
    def construct(self):
        t = ["引理2[《几何基础》定理12]：",
             "若两角彼此相等，则它们的补角也彼此相等."]
        self.say(t)
        t=["设角ABC、A'B'C'彼此相等；",
           "且在它们各自的边上取BA等于B'A'、BC等于B'C'[I.2]"]
        C = Dot([0, 0, 0], color=BLACK)
        A = Dot([-1, -2, 0], color=BLACK)
        B = Dot([1.5, -2, 0], color=BLACK)
        VGroup(A, B, C).shift(5 * LEFT + 1 * UP)
        A_, B_, C_ = A.copy(), B.copy(), C.copy()
        VGroup(A_, B_, C_).shift(7*RIGHT)
        ABC = withered_leaf(A, B, C)
        A_B_C_ = withered_leaf(A_, B_, C_)
        t_A = MathTex("A", color=BLACK).next_to(A, DOWN)
        t_B = MathTex("B", color=BLACK).next_to(B, DOWN)
        t_C = MathTex("C", color=BLACK).next_to(C, UP)
        t_A_, t_B_, t_C_ = MathTex("A\'", color=BLACK).next_to(A_, DOWN), MathTex("B\'", color=BLACK).next_to(B_, DOWN), MathTex(
            "C\'", color=BLACK).next_to(C_, UP)

        BA = line_via_dot(B,A)
        BC = line_via_dot(B,C)
        B_A_ = line_via_dot(B_,A_)
        B_C_ = line_via_dot(B_,C_)

        eqs1 = VGroup(equal_lines_notes_group(BA,B_A_),equal_lines_notes_group(BC,B_C_,n=2))

        self.say(t,Create(BA),Create(BC),Create(B_A_),Create(B_C_),Create(eqs1),FadeIn(B,A,C,B_,A_,C_,t_B,t_C,t_A,t_B_,t_C_,t_A_,t_B_))

        t=["于是，由于角ABC、A'B'C'彼此相等，三角形ABC、A'B'C'全等[引理1，即I.4]；",
                  "因此，AC等于A'C'，角BAC等于角B'A'C'."]
        AC = line_via_dot(A,C)
        A_C_ = line_via_dot(A_,C_)
        eqs2 = equal_lines_notes_group(AC,A_C_,n=3)

        self.say(t,Create(AC),Create(A_C_),Create(eqs2),Create(ABC),Create(A_B_C_))

        t = ["延长AB至D；再延长A'B'至D'，使BD等于B'D'[I.2]."]
        D = Dot(B.copy().shift(2*RIGHT).get_center(),color=BLACK)
        BD = line_via_dot(B,D)
        D_ = D.copy().shift(7*RIGHT)
        B_D_ = line_via_dot(B_,D_)
        t_D = MathTex("D", color=BLACK).next_to(D, DOWN)
        t_D_ = MathTex("D\'", color=BLACK).next_to(D_, DOWN)
        eq4 = equal_lines_notes_group(BD,B_D_,n=4)
        self.say(t,FadeIn(D,D_,t_D,t_D_),Create(eq4),Create(BD),Create(B_D_))

        t=["但是AB也等于A'B'；",
           "因此，整个AD等于整个A'D'[公理2]."]
        self.say(t)

        t=["且已经证明AC等于A'C'，角BAC等于角B'A'C'；",
           "因此，三角形ACD全等于三角形A'C'D'[引理1]."]

        ACD = withered_leaf(A,D,C)
        A_C_D_ = withered_leaf(A_,D_,C_)
        self.say(t,ReplacementTransform(ABC,ACD),ReplacementTransform(A_B_C_,A_C_D_))

        t=["因此，CD等于C'D'，且角ADC等于角A'D'C'."]
        CD = line_via_dot(C,D)
        C_D_ = line_via_dot(C_,D_)
        eqs5 = equal_lines_notes_group(CD,C_D_,n=5)
        self.say(t,Create(CD),Create(C_D_),Create(eqs5))

        t=["但DB也等于D'B'；",
           "因此，三角形BDC全等于三角形B'D'C'[引理1]；",
           "因此，补角DBC等于补角D'B'C'."]
        BDC = falling_maple(B,D,C)
        B_D_C_ = falling_maple(B_,D_,C_)

        self.say(t,ReplacementTransform(ACD,BDC),ReplacementTransform(A_C_D_,B_D_C_))
        self.wait(3)
        self.ending(' ')

class s4(NScene):
    def construct(self):
        self.say(["现在正式开始证明：","所有直角都彼此相等[「公设」4]"])

        t=["给定任意的两个直角ABC、DEF；",
           "假设它们并不相等."]
        A = Dot([-1, -1, 0], color=BLACK)
        B = Dot([1.5,-1,0], color=BLACK)
        C = Dot([1.5,1.5,0], color=BLACK)
        VGroup(A,B,C).shift(5*LEFT)
        D,E,F = A.copy(),B.copy(),C.copy()
        VGroup(D,E,F).shift(7*RIGHT)
        t_A = MathTex("A", color=BLACK).next_to(A, DOWN)
        t_B = MathTex("B", color=BLACK).next_to(B, DOWN)
        t_C = MathTex("C", color=BLACK).next_to(C, UP)
        t_D = MathTex("D", color=BLACK).next_to(D, DOWN)
        t_E = MathTex("E", color=BLACK).next_to(E, DOWN)
        t_F = MathTex("F", color=BLACK).next_to(F, UP)

        AB = line_via_dot(B,A)
        BC = line_via_dot(B,C)
        DE = line_via_dot(E,D)
        EF = line_via_dot(E,F)

        self.say(t,FadeIn(A,B,C,D,E,F,t_A,t_B,t_C,t_D,t_E,t_F),Create(AB),Create(BC),Create(DE),Create(EF))

        t=["分别延长AB、DE至G、H；",
           "则由于它们都是直角，角ABC、DEF分别等于角CBG、FEH."]
        G = B.copy().shift(2.5*RIGHT)
        H = E.copy().shift(2.5*RIGHT)
        t_G = MathTex("G", color=BLACK).next_to(G, DOWN)
        t_H = MathTex("H", color=BLACK).next_to(H, DOWN)
        BG = line_via_dot(B,G)
        EH = line_via_dot(E,H)
        eqangles = VGroup(equal_angle_notes_group(angles=[[C, B, A], [G, B, C]],is_change_color=True),
                          equal_angle_notes_group(angles=[[F, E, D], [H, E, F]], n=2,is_change_color=True))
        self.say(t,FadeIn(G,H,t_G,t_H),Create(BG),Create(EH),Create(eqangles))

        t=["在C所在的那一侧，在BA上作角ABK等于角DEF[引理1，推论]."]
        K = Dot(AB.copy().rotate(-60*DEGREES,about_point=B.get_center()).get_end(),color=BLACK)
        t_K = MathTex("K", color=BLACK).next_to(K, UP)
        BK = line_via_dot(B,K)
        eq_ABK = equal_angle_note(K,B,A,n=2,color=LEAF_RED)
        self.say(t,FadeOut(eqangles[0]),Create(eq_ABK),Create(BK),FadeIn(K,t_K))

        t=["因为已经假设角ABC、DEF互不相等；",
           "因此，角ABC也不等于角ABK；",
           "因此，BC与BK不重合；假设它相对于BC的、在A所在的一侧.",
           "（如果不在A这侧，那么它在另一侧，","事实上两种情况下都是类似的证法，因此这里只讨论在A一侧的情况）"]
        self.say(t)
        self.wait(3)

        t=["因为角ABK等于角DEF，它们的补角KBG、FEH也彼此相等[引理2]；",
           "但已经证明，由于角DEF是直角，角KBG即角FEH等于角DEF、从而等于角ABK；",
           "因此，KBG也等于角ABK."]
        eq_K = equal_angle_note(G,B,K,n=2,color=LEAF_YELLOW)
        self.say(t,Create(eq_K))

        t=["在BC的另一侧作角BCL等于角BCK[引理1，推论]；",
           "由于角ABC等于角CBG，余下的角KBA、GBL也彼此相等[公理3]."]
        BL = BK.copy().rotate(-60*DEGREES,about_point=B.get_center())
        L = Dot(BL.get_end(),color=BLACK)
        t_L = MathTex("L", color=BLACK).next_to(L, UP)
        eqsL = equal_angle_notes_solid(L,B,C,size=1,color=LEAF_YELLOW)
        eqsK = equal_angle_notes_solid(C,B,K,size=1,color=LEAF_RED)
        eq2r = equal_angle_note(G,B,L,n=2,color=LEAF_RED)
        self.say(t,Create(eqsL),Create(eqsK),Create(eq2r),Create(BL),FadeIn(L,t_L))

        t=["但是已经证明，角KBA也等于角KBG；",
           "因此，角GBL也等于角GBK：",
           "小的等于大的，这是荒谬的[公理5]."]
        eqfinal = equal_angle_note(G,B,K,n=2,size=1,color=LEAF_RED)
        self.say(t,Create(eqfinal),Indicate(eqfinal),Indicate(eq2r),is_sequencing=True)

        t=["类似的可以证明，即使K在另一侧，也能推出这样的矛盾；",
           "因此，直角ABC并非不等于直角DEF；",
           "因此，所有直角都彼此相等."]
        self.say(t)
        self.ending("这就是所要证明的.")

class s5(NScene):
    def construct(self):
        t=["事实上，上述证明与《几何原本》中的诸多证明一样，",
           "都用到了一些隐含的公理，比如「一直线把平面分为两侧」，以及「叠合」的意义；",
           "因此，欧几里得几何空间事实上需要的公理比《几何原本》中所罗列的要更多.",
           "希尔伯特在《几何基础》中描述了五组共20条公理，从而完成了几何的公理化，",
           "本期视频的命题就是从中所汲取的."]
        self.say(t)
        self.ending(" ")